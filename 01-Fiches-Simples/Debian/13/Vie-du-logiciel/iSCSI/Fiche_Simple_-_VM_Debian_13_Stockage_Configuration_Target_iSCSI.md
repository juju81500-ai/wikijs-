# 📄 VM_Debian_13_Stockage_Configuration-Target-iSCSI-LIO.md

- **Environnement** : VM / Serveur Stockage (Debian 13)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Stockage / SAN iSCSI Target
- **Tags** : `[debian13]`, `[iscsi]`, `[targetcli]`, `[storage]`, `[san]`, `[hardening]`

## 🎯 Problème précis à résoudre
Configurer un serveur de stockage iSCSI Target (SAN) sous Debian 13 à l'aide du sous-système LIO et `targetcli-fb`, créer un LUN et sécuriser l'accès par authentification CHAP.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du gestionnaire iSCSI Target LIO :
   `apt-get update && apt-get install -y targetcli-fb`
   👉 Explication : Installe l'interface d'administration en ligne de commande pour le module kernel iSCSI.

2. Création d'un stockage basé sur un fichier image temporaire :
   `targetcli /backstores/fileio create name=file1 image_file=/tmp/iscsi.img size=1G`
   👉 Explication : Instancie un volume de stockage virtuel de 1 Go pour les essais.

3. Initialisation d'un Target IQN de test :
   `targetcli /iscsi create iqn.2026-10.local.lab:target0`
   👉 Explication : Génère le nom d'identifiant iSCSI unique pour le serveur cible.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier qu'un LV dédié existe, qu'il ne contient pas de système de fichiers monté en écriture et qu'une sauvegarde est disponible avant de le présenter :
   `sudo lvs -a -o +devices`
   👉 Explication : La présentation iSCSI expose des blocs bruts au client ; n'exporter jamais le volume racine ni un LV déjà utilisé.
2. Créer le backstore uniquement avec le périphérique vérifié :
   `targetcli /backstores/block create name=lun_prod dev=/dev/vg_storage/lv_iscsi`

2. Configuration du Target iSCSI et de l'IP d'écoute réseau :
   `targetcli /iscsi/iqn.2026-10.local.lab:target-prod/tpg1/portals create 192.168.1.50 3260`
   👉 Explication : Lie le service iSCSI à l'adresse IP dédiée du réseau de stockage SAN.

4. Déclaration de l'initiateur client autorisé :
   `targetcli /iscsi/iqn.2026-10.local.lab:target-prod/tpg1/acls create iqn.2026-10.local.lab:initiator01`
   👉 Explication : Autorise uniquement la machine possédant cet IQN à se connecter au volume.

5. Sauvegarde de la configuration :
   `targetcli saveconfig`
   👉 Explication : Enregistre de manière permanente les paramètres de configuration.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Activer CHAP pour l'ACL de l'initiateur via une session d'administration restreinte. Saisir un secret unique conservé dans le coffre, sans le mettre dans l'historique shell ni dans la fiche :
   ```text
   targetcli
   /iscsi/iqn.2026-10.local.lab:target-prod/tpg1/acls/iqn.2026-10.local.lab:initiator01 set auth userid=iscsi_user password=<SECRET_CHAP>
   saveconfig
   ```
   👉 Explication : Remplacer le placeholder dans la session sécurisée et configurer le même secret côté initiateur. La commande seule ne configure pas l'authentification mutuelle.

2. Autoriser TCP/3260 uniquement depuis les initiateurs prévus dans le pare-feu persistant géré par le serveur. Valider et appliquer la règle par ce gestionnaire ; une règle `nft add rule` ajoutée à chaud n'est pas persistante.

3. Vérifier le nom du service fourni par le paquet puis l'activer :
   ```bash
   systemctl list-unit-files '*target*'
   systemctl status target
   ```
   Le nom exact dépend du paquet installé. Vérifier après redémarrage planifié que la configuration restaurée et les LUN sont toujours présents.
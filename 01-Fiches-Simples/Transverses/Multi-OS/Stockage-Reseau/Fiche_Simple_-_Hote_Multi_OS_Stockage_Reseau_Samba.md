# Fiche_Simple_-_Hote_Multi_OS_Stockage_Reseau_Samba.md

- **Environnement** : Serveur de stockage Linux dédié (Debian) pour Samba, NFSv4 et iSCSI
- **OS / Version** : Multi-OS (serveur Linux Debian); paquets de la distribution
- **Catégorie** : stockage réseau
- **Tags** : `stockage`, `samba`, `smb`

---

## Problème précis à résoudre

Publier un partage SMB limité à un groupe.

## 1. Hors-Production (Lab / Test / POC)

1. Installer Samba :
   ```bash
   sudo apt install samba
   ```
   👉 Explication : le paquet fournit le serveur SMB `smbd`.

2. Créer un groupe d'accès (exemple `partage`) et appliquer les permissions du répertoire :
   ```bash
   sudo groupadd partage
   sudo chgrp partage /srv/partage
   sudo chmod 2770 /srv/partage
   ```
   👉 Explication : seuls les membres du groupe accèdent au dossier, et les nouveaux fichiers héritent du groupe.

3. Déclarer un partage nommé dans `/etc/samba/smb.conf` avec `valid users = @partage`, sans `guest ok = yes`.
   👉 Explication : le partage est limité aux groupes nécessaires et jamais anonyme.

4. Valider la configuration :
   ```bash
   sudo testparm -s
   ```
   👉 Explication : la commande signale toute erreur de syntaxe.

5. Activer et contrôler le service :
   ```bash
   sudo systemctl enable --now smbd
   sudo systemctl --no-pager status smbd
   ```
   👉 Explication : le serveur démarre au boot.

6. Ouvrir TCP/445 uniquement aux sous-réseaux clients prévus, puis tester depuis un client avec un compte non administrateur.
   👉 Explication : on valide l'accès réel et on limite l'exposition.

## 2. Production — Contrôles

Définir le modèle d'identité (comptes locaux ou annuaire) et documenter les groupes.

## 3. Production — Sécurité

- Ne pas utiliser `guest ok = yes` en production.
- Ouvrir TCP/445 uniquement aux sous-réseaux prévus.

## Validation et retour arrière

- **Validation** : `testparm -s` sans erreur et accès réussi avec un compte non administrateur.
- **Retour arrière** : Retirer le partage de `smb.conf` puis `sudo systemctl restart smbd`.

## Si le problème n'est pas résolu

- [Samba — documentation](https://www.samba.org/samba/docs/)
- [Linux NFS — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html)
- [Guide complet — déployer Samba](../../../../02-Fiches-Completes/Transverses/Multi-OS/Installation-Deploiement/07_Stockage_Reseau_NAS_SAN_Samba_NFSv4_iSCSI.md#2-deployer-samba)

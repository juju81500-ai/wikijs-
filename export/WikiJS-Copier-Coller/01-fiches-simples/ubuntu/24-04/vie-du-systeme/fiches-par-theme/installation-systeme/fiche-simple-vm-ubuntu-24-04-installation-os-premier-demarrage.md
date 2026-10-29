# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Installation_OS_Premier_Demarrage.md

- **Environnement** : VM Ubuntu Server sur Proxmox VE, KVM ou VMware
- **OS / Version** : Ubuntu Server 24.04 LTS
- **Catégorie** : Installation / Système

## 🎯 Problème précis à résoudre
Installer Ubuntu Server 24.04 LTS sur une nouvelle VM, configurer stockage et réseau initial, et identifier si cloud-init restera propriétaire des paramètres réseau.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Télécharger l'ISO depuis une source officielle Canonical et contrôler l'empreinte publiée.
2. Créer une VM avec disque, firmware, CPU, mémoire et interface réseau conformes au lab; monter l'ISO.
3. Dans l'installateur, choisir langue, clavier, profil Ubuntu Server, stockage et réseau; créer un compte nominatif. Installer OpenSSH si requis.
4. Au premier démarrage, vérifier :
   ```bash
   lsb_release -a
   hostnamectl
   lsblk -f
   ip -br address
   cloud-init status --long
   ```
   👉 *Explication : une configuration Netplan créée par cloud-init peut être régénérée; identifier la source avant toute modification persistante.*

## ⚡ 2. Production — Façon Simplifiée
1. Valider ISO, ressources, stockage, réseau virtuel, hostname, plan IP et procédure de sauvegarde.
2. Installer selon le plan de stockage du rôle; garder une console hyperviseur pendant la configuration réseau.
3. Appliquer les fiches existantes pour mises à jour, compte d'administration, SSH par clé, Netplan, DNS, UFW et cloud-init.
4. Installer uniquement les paquets nécessaires, appliquer les mises à jour et effectuer un redémarrage de validation.

## 🔒 3. Production — Façon Sécurisée
1. Vérifier l'image et ses sources de téléchargement; ne pas réutiliser un média inconnu.
2. Maintenir un accès console, une clé SSH de secours contrôlée et un retour arrière réseau.
3. Ne pas désactiver cloud-init globalement si d'autres mécanismes de provisionnement en dépendent.

## ✅ Validation et retour arrière
- Confirmer version, hostname, interfaces, routes, DNS, SSH, état des mises à jour et services systemd.
- Tester une restauration en VM isolée avant d'y déployer des données importantes.
- En cas de défaut, restaurer le fichier Netplan/configuration cloud-init sauvegardé depuis la console ou reconstruire la VM.
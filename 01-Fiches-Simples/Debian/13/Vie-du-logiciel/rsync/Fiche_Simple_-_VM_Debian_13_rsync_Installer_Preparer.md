# Fiche_Simple_-_VM_Debian_13_rsync_Installer_Preparer.md

- **Environnement** : Debian 13 Trixie; source et destination locales ou SSH
- **OS / Version** : Debian 13; paquet rsync du dépôt Debian
- **Catégorie** : sauvegarde de fichiers / préparation
- **Tags** : `debian13`, `rsync`, `apt`, `ssh`, `installation`

---

## Problème précis à résoudre

Installer rsync et préparer la connexion et les chemins sans risque de confusion entre source et destination.

## 1. Hors-Production (Lab / Test / POC)

1. Installer rsync et contrôler la version :
   ```bash
   sudo apt update
   sudo apt install rsync
   rsync --version | head -1
   ```
   👉 Explication : la version est consignée avec la procédure.

2. Créer une clé SSH dédiée (destination distante) :
   ```bash
   ssh-keygen -t ed25519 -f ~/.ssh/id_rsync_backup -C "rsync-backup"
   ssh-copy-id -i ~/.ssh/id_rsync_backup.pub utilisateur@sauvegarde.example.net
   ```
   👉 Explication : limiter ensuite la clé à la destination (options `command=`/`from=` dans `authorized_keys`).

3. Tester la connexion avant la première synchronisation :
   ```bash
   ssh -i ~/.ssh/id_rsync_backup utilisateur@sauvegarde.example.net 'hostname; df -h /srv/backup'
   ```
   👉 Explication : on valide l'authentification et l'espace disponible.

4. Définir les variables sans ambiguïté :
   ```bash
   SRC=/srv/data/
   DST=utilisateur@sauvegarde.example.net:/srv/backup/data/
   echo "$SRC -> $DST"
   ```
   👉 Explication : `/srv/data/` copie le contenu; `/srv/data` copie le répertoire lui-même. Vérifier chaque chemin avant exécution.

## 2. Production — Contrôles

Documenter paquets, versions, comptes de service, chemins, accès, propriétaire des données et procédure de rotation des clés.

## 3. Production — Sécurité

- Ne pas déposer de clé privée dans un dépôt ou une fiche.
- Limiter la clé au répertoire et aux opérations indispensables.
- Vérifier l'empreinte SSH par un canal fiable; ne pas accepter une identité inconnue à l'aveugle.
- Ne pas lancer rsync avant d'avoir confirmé le sens source → destination.

## Validation et retour arrière

- **Validation** : version, connexion, compte distant et chemins vérifiés avec données de test.
- **Retour arrière** : retirer uniquement la configuration de test créée; ne pas supprimer des clés partagées ou des données existantes sans validation.

## Si le problème n'est pas résolu

- [Debian — paquet rsync](https://packages.debian.org/trixie/rsync)
- [rsync — page de manuel officielle](https://download.samba.org/pub/rsync/rsync.1.html)
- [Guide complet rsync Debian 13](../../../../../02-Fiches-Completes/Debian/13/Autres/92_Sauvegarde_Fichiers_rsync_Debian_13.md#2-installer-et-preparer)

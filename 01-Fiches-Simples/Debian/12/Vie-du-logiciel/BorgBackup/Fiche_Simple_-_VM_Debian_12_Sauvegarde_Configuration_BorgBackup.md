# 📄 VM_Debian_12_Sauvegarde_Configuration-BorgBackup.md

- **Environnement** : VM (Debian 12 Bookworm)
- **OS / Version** : Debian 12 - Famille Debian
- **Catégorie** : Sauvegarde & Archivage / BorgBackup
- **Tags** : `[debian12]`, `[borgbackup]`, `[sauvegarde]`, `[chiffrement]`, `[deduplication]`, `[hardening]`

## 🎯 Problème précis à résoudre
Mettre en place une stratégie de sauvegarde chiffrée, dédupliquée et compressée avec BorgBackup sur Debian 12, et automatiser l'archivage quotidien des répertoires critiques.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet BorgBackup :
   `apt-get update && apt-get install -y borgbackup`
   👉 Explication : Installe l'outil de sauvegarde en ligne de commande.
2. Initialisation d'un dépôt local sans chiffrement :
   `borg init --encryption=none /var/backups/borg-repo`
   👉 Explication : Prépare la structure de dépôt Borg pour des sauvegardes locales de test.
3. Création d'une première archive de test :
   `borg create /var/backups/borg-repo::archive-01 /etc /var/log`
   👉 Explication : Compresse et stocke les répertoires de configuration et de journaux.

---

## ⚡ 2. Production — Façon Simplifiée
1. Initialisation d'un dépôt chiffré par clé principale :
   `borg init --encryption=repokey-blake2 /mnt/backup-disk/borg-prod`
   👉 Explication : Initialise un dépôt chiffré en AES-256 avec authentification forte des blocs.
2. Exécution d'une sauvegarde complète avec compression ZSTD :
   `borg create --stats --progress --compression zstd,3 /mnt/backup-disk/borg-prod::{hostname}-{now:%Y-%m-%d_%H:%M} /etc /var/www /home`
   👉 Explication : Sauvegarde les répertoires de données avec horodatage dynamique et compression rapide.
3. Contrôle des archives existantes dans le dépôt :
   `borg list /mnt/backup-disk/borg-prod`
   👉 Explication : Affiche la liste et l'empreinte de toutes les sauvegardes enregistrées.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Exporter la clé du dépôt et la stocker hors site dans un coffre chiffré, avec accès limité et procédure de récupération testée :
   ```bash
   sudo borg key export /mnt/backup-disk/borg-prod /root/borg-key-backup.txt
   sudo chmod 600 /root/borg-key-backup.txt
   ```
   👉 Explication : La perte de la clé ou de la phrase de passe peut rendre le dépôt irrécupérable. Une copie non chiffrée de la clé doit être protégée comme un secret de production.
2. Simuler la rétention avant toute suppression :
   `sudo borg prune --dry-run --list --keep-daily=7 --keep-weekly=4 --keep-monthly=12 /mnt/backup-disk/borg-prod`
   👉 Explication : Examiner les archives qui seraient supprimées, valider la politique et vérifier qu'une copie indépendante existe avant d'exécuter sans `--dry-run`.
3. Automatiser sous un compte dédié via un timer systemd ou un ordonnanceur documenté. Séparer la création d'archive de la purge, protéger le fichier d'environnement contenant les secrets, vérifier le code retour et envoyer une alerte en cas d'échec.
4. Tester régulièrement `borg check` et une restauration réelle dans un répertoire isolé. Une sauvegarde qui n'a jamais été restaurée n'est pas validée.
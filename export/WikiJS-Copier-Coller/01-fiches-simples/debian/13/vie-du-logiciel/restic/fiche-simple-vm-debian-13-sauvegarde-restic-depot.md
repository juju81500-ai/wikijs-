# 📄 Fiche_Simple_-_VM_Debian_13_Sauvegarde_Restic_Depot

- **Environnement** : VM ou serveur Debian 13 avec données applicatives à sauvegarder
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Sauvegarde / Dépôt chiffré Restic

## 🎯 Problème précis à résoudre
Créer un dépôt de sauvegarde Restic chiffré sur Debian 13, y sauvegarder des chemins précis avec une rétention définie, et contrôler l'intégrité du dépôt.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer Restic depuis les dépôts Debian 13 :
   ```bash
   sudo apt-get update
   sudo apt-get install -y restic
   restic version
   ```
   👉 Explication : Le paquet `restic` est disponible dans la section principale de Debian 13. Aucun dépôt tiers au format deb822 n'est nécessaire.

2. Créer un mot de passe de dépôt dans un fichier réservé à root, puis initialiser le dépôt local :
   ```bash
   sudo sh -c 'umask 077; openssl rand -base64 32 > /root/.restic-pass'
   sudo mkdir -p /srv/restic-repo
   sudo restic -r /srv/restic-repo --password-file /root/.restic-pass init
   ```
   👉 Explication : Le mot de passe est généré aléatoirement, avec des droits `0600`. Restic chiffre tout le dépôt avec ce secret : sa perte rend les sauvegardes inutilisables.

3. Sauvegarder un répertoire de test et lister les instantanés :
   ```bash
   sudo restic -r /srv/restic-repo --password-file /root/.restic-pass backup /etc
   sudo restic -r /srv/restic-repo --password-file /root/.restic-pass snapshots
   ```
   👉 Explication : `backup` crée un instantané chiffré et dédupliqué ; `snapshots` doit afficher une ligne avec l'identifiant et la date.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder les chemins de production définis par le rôle, en excluant les caches :
   ```bash
   sudo restic -r /srv/restic-repo --password-file /root/.restic-pass backup /etc /srv/<donnees_application> --exclude-caches
   ```
   👉 Explication : `--exclude-caches` ignore les répertoires marqués comme caches (fichier `CACHEDIR.TAG`). Remplacer `<donnees_application>` par le répertoire réel du service.

2. Appliquer la rétention et libérer l'espace des instantanés expirés :
   ```bash
   sudo restic -r /srv/restic-repo --password-file /root/.restic-pass forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune
   ```
   👉 Explication : Conserve 7 instantanés quotidiens, 4 hebdomadaires et 6 mensuels. `--prune` supprime réellement les données devenues inutiles ; sans lui, l'espace n'est pas libéré.

3. Planifier la sauvegarde avec une unité systemd (le timer Debian 13 remplace cron pour ce cas) et vérifier son prochain passage :
   ```bash
   sudo systemctl list-timers --all --no-pager | grep restic
   ```
   👉 Explication : Une unité `restic-backup.timer` doit être créée à partir de la fiche « Créer timer systemd » de Debian 13. Le contrôle ci-dessus confirme que le timer est actif et connaît sa prochaine exécution.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Contrôler l'intégrité du dépôt, y compris une partie des données réelles :
   ```bash
   sudo restic -r /srv/restic-repo --password-file /root/.restic-pass check
   sudo restic -r /srv/restic-repo --password-file /root/.restic-pass check --read-data-subset=1/10
   ```
   👉 Explication : Le premier contrôle vérifie la structure du dépôt. Le second relit un dixième des données pour détecter une corruption silencieuse du support.

2. Tester la restauration d'un fichier dans un répertoire temporaire isolé :
   ```bash
   sudo restic -r /srv/restic-repo --password-file /root/.restic-pass restore latest --target /tmp/restic-test --include /etc/hostname
   sudo diff /etc/hostname /tmp/restic-test/etc/hostname && echo "Restauration conforme"
   ```
   👉 Explication : Une sauvegarde n'est valide que si elle est restaurée. Supprimer `/tmp/restic-test` après le test.

3. Dupliquer le dépôt hors de la machine (copie chiffrée vers un second emplacement) et protéger le mot de passe :
   ```bash
   sudo ls -l /root/.restic-pass
   sudo restic -r /srv/restic-repo --password-file /root/.restic-pass copy --repo2 <autre_depot> --password-file2 /root/.restic-pass2
   ```
   👉 Explication : Le fichier de mot de passe doit être en `0600` et une copie doit être conservée dans le coffre-fort de l'entreprise. Le dépôt unique sur le même disque ne protège pas contre une panne matérielle.
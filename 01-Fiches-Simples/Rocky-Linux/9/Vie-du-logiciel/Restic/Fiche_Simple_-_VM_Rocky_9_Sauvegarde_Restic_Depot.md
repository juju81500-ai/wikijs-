# 📄 Fiche_Simple_-_VM_Rocky_9_Sauvegarde_Restic_Depot.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 (restic fourni par EPEL)
- **Catégorie** : Sauvegarde / Dépôt chiffré Restic
- **Tags** : `[rocky9]`, `[rhel9]`, `[restic]`, `[sauvegarde]`, `[epel]`, `[chiffrement]`

## 🎯 Problème précis à résoudre
Créer un dépôt Restic chiffré, lancer une sauvegarde des répertoires système et métier, appliquer une politique de rétention et programmer l'exécution sur Rocky Linux 9.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer EPEL puis Restic :
   ```bash
   sudo dnf install -y epel-release
   sudo dnf install -y restic
   restic version
   ```
   👉 Explication : Restic n'est pas dans les dépôts de base de Rocky Linux 9. La version affichée dépend du paquet publié dans EPEL.

2. Créer un dépôt local de test et son mot de passe :
   ```bash
   sudo sh -c 'umask 077; openssl rand -base64 32 > /root/.restic_pass'
   sudo mkdir -p /srv/restic/<nom_du_serveur>
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> init
   ```
   👉 Explication : Le mot de passe est généré aléatoirement avec des droits restrictifs. `init` crée le dépôt chiffré. La perte de ce mot de passe rend toutes les sauvegardes inutilisables.

3. Lancer une première sauvegarde de test :
   ```bash
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> backup /etc
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> snapshots
   ```
   👉 Explication : `backup` crée un instantané du répertoire `/etc`. `snapshots` doit afficher l'instantané créé.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder les répertoires utiles et appliquer la rétention :
   ```bash
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> backup /etc /home /srv --exclude-caches
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune
   ```
   👉 Explication : `--exclude-caches` ignore les répertoires marqués comme caches. `forget --prune` supprime les anciens instantanés et libère l'espace. Adapter les chemins aux données réelles.

2. Programmer la sauvegarde quotidienne avec cron, dans `/etc/cron.d/` :
   ```text
   30 2 * * * root env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> backup /etc /home /srv --exclude-caches --quiet
   ```
   👉 Explication : Exécution tous les jours à 02h30 sous `root`. Le format `/etc/cron.d/` exige le nom de l'utilisateur après les champs horaires.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Déporter le dépôt sur un serveur de sauvegarde distant via SFTP, avec un compte dédié :
   ```bash
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r sftp:<utilisateur_sauvegarde>@<serveur_sauvegarde>:/srv/restic/<nom_du_serveur> init
   ```
   👉 Explication : Une copie hors du serveur protège contre la perte matérielle ou le chiffrement par un rançongiciel. Le compte SFTP doit être sans droits d'administration sur le serveur de sauvegarde.

2. Contrôler les droits du fichier de mot de passe :
   ```bash
   sudo ls -l /root/.restic_pass
   ```
   👉 Explication : Le fichier doit être en `-rw-------`, propriété de `root`.

3. Vérifier périodiquement l'intégrité du dépôt, avec lecture d'un dixième des données :
   ```bash
   sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> check --read-data-subset=1/10
   ```
   👉 Explication : `check` valide la structure du dépôt. Le sous-ensemble `1/10` lit une partie des données à chaque exécution, ce qui couvre tout le dépôt sur dix passages.

---

## ✅ Contrôle
```bash
sudo env RESTIC_PASSWORD_FILE=/root/.restic_pass restic -r /srv/restic/<nom_du_serveur> snapshots --latest 1
```
👉 Explication : Affiche le dernier instantané. Sa date doit correspondre à la dernière exécution programmée.

# 📄 PostgreSQL

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : PostgreSQL 15.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données
- **Tags** : `[debian-12]`, `[postgresql]`, `[base-de-donnees]`, `[sauvegarde]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer PostgreSQL sur Debian 12, créer une base et un rôle de test, puis le préparer pour la production : écoute limitée, accès réservé à l'application cliente avec authentification chiffrée, sauvegarde testée. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du serveur :
```bash
sudo apt update
sudo apt install -y postgresql postgresql-contrib
psql --version
pg_lsclusters
systemctl status postgresql --no-pager
```
👉 Explication : Installe PostgreSQL 15 depuis les dépôts Debian 12 et crée un cluster `15/main`. `pg_lsclusters` doit afficher l'état `online`.

2. Création d'un compte système et d'une base de test liée au rôle `labuser` :
```bash
sudo useradd -m labuser
sudo -u postgres psql -c "CREATE ROLE labuser LOGIN;"
sudo -u postgres createdb -O labuser essai_lab
```
👉 Explication : Le rôle `labuser` est propriétaire de la base `essai_lab`. Par défaut, l'authentification locale `peer` relie le compte système au rôle de même nom, sans mot de passe : c'est acceptable en lab uniquement.

3. Test de connexion :
```bash
sudo -u labuser psql -d essai_lab -c "SELECT current_user, current_database();"
```
👉 Explication : Doit afficher `labuser` et `essai_lab`. Une erreur `Peer authentication failed` signale un compte système absent ou différent du rôle.

---

## ⚡ 2. Production — Façon Simplifiée
1. Écoute réseau limitée à l'adresse du serveur de base :
```bash
sudo nano /etc/postgresql/15/main/postgresql.conf
sudo systemctl restart postgresql
sudo ss -ltnp | grep 5432
```
Dans le fichier, régler `listen_addresses = 'localhost,192.168.10.30'` (adresse du serveur de base, à adapter).
👉 Explication : Par défaut, PostgreSQL n'écoute que sur `localhost`. `ss` confirme le port 5432 et l'adresse d'écoute.

2. Autorisation d'un seul client dans `pg_hba.conf` avec authentification chiffrée :
```bash
sudo nano /etc/postgresql/15/main/pg_hba.conf
sudo systemctl reload postgresql
```
Ajouter cette ligne avant les règles générales :
```
host    base_appli    appli    192.168.10.21/32    scram-sha-256
```
👉 Explication : Seul le rôle `appli` peut se connecter à `base_appli`, depuis `192.168.10.21` (serveur applicatif, à adapter), avec la méthode `scram-sha-256`. Ne pas utiliser `trust` ni `md5` en production.

3. Création du rôle et de la base applicative, avec mot de passe généré :
```bash
APP_PASS=$(openssl rand -base64 24)
sudo -u postgres psql -c "CREATE ROLE appli LOGIN PASSWORD '$APP_PASS';"
sudo -u postgres createdb -O appli base_appli
echo "$APP_PASS"
```
👉 Explication : Le mot de passe s'affiche une seule fois : le copier dans le coffre-fort du pack. Le rôle `appli` devient propriétaire de `base_appli`.

4. Ouverture du pare-feu pour l'application et l'administration SSH :
```bash
sudo apt install -y ufw
sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow from 192.168.10.21 to any port 5432 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Le port 5432 n'est ouvert qu'au serveur applicatif. SSH est ouvert avant l'activation du pare-feu.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Recherche des règles d'authentification faibles :
```bash
sudo grep -nE "trust|md5|password" /etc/postgresql/15/main/pg_hba.conf
sudo -u postgres psql -c "SHOW password_encryption;"
```
👉 Explication : Toute ligne `trust` doit être supprimée. Les lignes `password` (en clair) et `md5` sont à remplacer par `scram-sha-256`. `password_encryption` doit afficher `scram-sha-256`.

2. Journalisation des connexions :
```bash
sudo -u postgres psql -c "ALTER SYSTEM SET log_connections = on;"
sudo -u postgres psql -c "ALTER SYSTEM SET log_disconnections = on;"
sudo systemctl reload postgresql
sudo tail -n 50 /var/log/postgresql/postgresql-15-main.log
```
👉 Explication : Enregistre chaque connexion et déconnexion. Les échecs `password authentication failed` répétés doivent être remontés au responsable sécurité.

3. Sauvegarde logique dans un dossier réservé à `postgres` :
```bash
sudo install -d -o postgres -g postgres -m 700 /var/backups/postgresql
sudo -u postgres pg_dump -Fc base_appli -f /var/backups/postgresql/base_appli-$(date +%F).dump
sudo -u postgres pg_dumpall --roles-only -f /var/backups/postgresql/roles-$(date +%F).sql
sudo ls -l /var/backups/postgresql
```
👉 Explication : `pg_dump -Fc` produit une sauvegarde compressée restaurable avec `pg_restore`. `pg_dumpall --roles-only` sauvegarde les rôles, y compris leurs hachages de mot de passe : le fichier doit être protégé comme un secret. Ces fichiers doivent être copiés hors du serveur.

4. Restauration de contrôle sur une base de test, jamais sur la production :
```bash
sudo -u postgres createdb base_test
sudo -u postgres pg_restore -d base_test /var/backups/postgresql/base_appli-$(date +%F).dump
sudo -u postgres psql -d base_test -c "\dt"
```
👉 Explication : Vérifie que la sauvegarde est exploitable. `\dt` liste les tables restaurées. Supprimer ensuite la base de test avec `sudo -u postgres dropdb base_test`.

---

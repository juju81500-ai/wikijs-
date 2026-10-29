# 📄 Fiche_Simple_-_VM_Debian_13_Database_Installation_PostgreSQL_17.md

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 (Trixie), PostgreSQL 17 des dépôts Debian
- **Catégorie** : Base de données / Installation / Sécurité

## 🎯 Problème précis à résoudre
Installer PostgreSQL 17 depuis les dépôts Debian 13, créer un rôle applicatif limité et n'autoriser les connexions distantes qu'avec TLS et `scram-sha-256`.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier la version candidate avant installation :
   ```bash
   cat /etc/debian_version
   apt-cache policy postgresql
   ```
2. Installer le serveur et les utilitaires; vérifier le cluster et sa version :
   ```bash
   sudo apt update
   sudo apt install postgresql-17 postgresql-client-17
   pg_lsclusters
   psql --version
   ```
3. Ouvrir une session locale et créer une base de test :
   ```bash
   sudo -u postgres psql
   ```
   ```sql
   CREATE ROLE lab_user LOGIN;
   \password lab_user
   CREATE DATABASE lab_db OWNER lab_user;
   ```
   👉 *Explication : saisir le mot de passe à l'invite `\password`; ne pas placer de secret en clair dans l'historique.*

## ⚡ 2. Production — Façon Simplifiée
1. Confirmer les chemins du cluster installé :
   ```bash
   pg_lsclusters
   sudo -u postgres psql -c 'SHOW config_file;'
   sudo -u postgres psql -c 'SHOW hba_file;'
   ```
2. Créer un rôle dédié, puis une base dont il est propriétaire :
   ```sql
   CREATE ROLE app_user LOGIN;
   \password app_user
   CREATE DATABASE app_prod OWNER app_user ENCODING 'UTF8';
   ```
3. Conserver `listen_addresses = 'localhost'` sauf besoin distant validé; si besoin, écouter seulement sur l'adresse privée du serveur DB.
   👉 *Explication : PostgreSQL 17 est la série fournie par Trixie; l'installation se fait par paquets versionnés `postgresql-17` et `postgresql-client-17`.*

## 🔒 3. Production — Façon Sécurisée
1. Dans le `pg_hba.conf` du cluster réel, ajouter la règle TLS avant les rejets :
   ```text
   hostssl app_prod app_user 192.0.2.20/32 scram-sha-256
   host    all      all      0.0.0.0/0     reject
   host    all      all      ::0/0         reject
   ```
2. Configurer `password_encryption = 'scram-sha-256'`, `ssl = on` et un certificat serveur valide; ouvrir TCP/5432 uniquement au réseau client prévu.
3. Valider puis recharger le cluster ciblé :
   ```bash
   sudo -u postgres psql -c 'SELECT pg_reload_conf();'
   sudo -u postgres psql -c 'SHOW ssl;'
   ```

## ✅ Validation et retour arrière
- Tester une connexion TLS depuis le client prévu et vérifier le journal PostgreSQL.
- Confirmer la version avec `pg_lsclusters` et `psql --version`; ne pas supposer que le nom de cluster est le même après migration majeure.
- Sauvegarder la base avant toute migration de données ou de cluster; ne pas copier un répertoire de données PostgreSQL 16 directement vers 17.
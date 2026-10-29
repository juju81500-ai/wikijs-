# Fiche_Simple_-_VM_Debian_13_NetBox_Installer_PostgreSQL_Redis.md

- **Environnement** : VM Debian 13 dédiée; PostgreSQL, Redis et NetBox locaux
- **OS / Version** : Debian 13; PostgreSQL 17, Redis depuis les dépôts Debian
- **Catégorie** : IPAM / DCIM / dépendances de base de données

---

## Problème précis à résoudre

Installer les dépendances requises et créer une base et un rôle dédiés sans exposer Redis ou PostgreSQL.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis :
   ```bash
   sudo apt update
   sudo apt install -y postgresql redis-server nginx python3 python3-pip python3-venv python3-dev build-essential libxml2-dev libxslt1-dev libffi-dev libpq-dev libssl-dev zlib1g-dev curl ca-certificates
   ```
   👉 Explication : installe la base, le cache, le serveur web et les outils de compilation Python.

2. Vérifier les versions :
   ```bash
   python3 --version
   psql --version
   redis-server --version
   ```
   👉 Explication : Python ≥ 3.12, PostgreSQL ≥ 15, Redis ≥ 6.

3. Démarrer et tester les services :
   ```bash
   sudo systemctl enable --now postgresql redis-server nginx
   sudo -u postgres psql -c 'SELECT version();'
   redis-cli ping
   ```
   👉 Explication : `redis-cli ping` doit répondre `PONG`.

4. Créer le rôle et la base (secret généré aléatoirement, saisi en console locale, conservé dans le coffre) :
   ```bash
   sudo -u postgres psql
   ```
   ```sql
   CREATE DATABASE netbox;
   CREATE USER netbox WITH PASSWORD 'REMPLACER_PAR_UN_SECRET_ALEATOIRE';
   ALTER DATABASE netbox OWNER TO netbox;
   \connect netbox
   GRANT CREATE ON SCHEMA public TO netbox;
   \q
   ```
   👉 Explication : remplacer le secret d'exemple; la base appartient au rôle dédié.

5. Vérifier que PostgreSQL et Redis n'écoutent que sur loopback :
   ```bash
   sudo ss -ltnp | grep -E ':(5432|6379)\b'
   ```
   👉 Explication : ne jamais publier 5432 ni 6379 sur le réseau.

## 2. Production — Contrôles

Définir capacité, sauvegarde PostgreSQL, rétention, supervision et responsables DB avant de charger des données d'autorité.

## 3. Production — Sécurité

- Utiliser un mot de passe aléatoire unique stocké dans un coffre approuvé; ne pas le conserver dans le shell ou le dépôt.
- Limiter les rôles et privilèges à la base NetBox.
- Ne pas exposer TCP/5432 ou TCP/6379 sur des interfaces externes.
- Ne pas réutiliser une base partagée sans plan de droits et de sauvegarde.

## Validation et retour arrière

- **Validation** : versions compatibles, services sains, base/rôle dédiés et écoute locale vérifiés.
- **Retour arrière** : conserver le plan de changement; ne pas supprimer une base préexistante en cas d'échec.

## Si le problème n'est pas résolu

- [NetBox — PostgreSQL](https://netbox.readthedocs.io/en/stable/installation/1-postgresql/)
- [NetBox — Redis](https://netbox.readthedocs.io/en/stable/installation/2-redis/)
- [Guide complet NetBox Debian 13](/02-fiches-completes/debian/13/installation-deploiement/73-deploiement-netbox-4-7-4-debian-13#2-installer-postgresql-et-redis)
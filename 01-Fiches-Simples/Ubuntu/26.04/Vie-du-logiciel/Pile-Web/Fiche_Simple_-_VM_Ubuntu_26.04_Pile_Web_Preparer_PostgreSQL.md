# Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Preparer_PostgreSQL.md

- **Environnement** : VM ou serveur dédié Ubuntu Server hébergeant une application PHP avec PostgreSQL local et TLS
- **OS / Version** : Ubuntu Server 26.04 LTS (Resolute); Nginx, PHP 8.5, PostgreSQL 18
- **Catégorie** : services web / base de données
- **Tags** : `ubuntu2604`, `nginx`, `php8.5`, `postgresql18`, `tls`

---

## Problème précis à résoudre

Créer un rôle et une base dédiés, secret saisi de façon interactive.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir psql :
   ```bash
   sudo -u postgres psql
   ```
   👉 Explication : Ouvre la console PostgreSQL.

2. Créer rôle et base :
   ```sql
   CREATE ROLE app_user LOGIN;
   \password app_user
   CREATE DATABASE appdb OWNER app_user ENCODING 'UTF8';
   ```
   👉 Explication : `\password` demande le secret au clavier (jamais en argument). `app_user` et `appdb` sont des exemples à remplacer.

## 2. Production — Contrôles

Garder l'écoute locale si la base ne sert qu'à l'application locale. Pour une base distante : adresse privée, TLS, `pg_hba.conf` limité et pare-feu.

## 3. Production — Sécurité

- Pas d'écoute sur toutes les interfaces.
- Secret stocké en coffre.

## Validation et retour arrière

- **Validation** : `sudo -u postgres psql -c "\l"` liste `appdb`.
- **Retour arrière** : `DROP DATABASE appdb; DROP ROLE app_user;` dans psql.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [PostgreSQL 18 — documentation](https://www.postgresql.org/docs/18/)
- [Guide complet — étape 3](../../../../../02-Fiches-Completes/Ubuntu/26.04/Installation-Deploiement/21_Pile_Web_Ubuntu_Server_26.04_Nginx_PHP85_PostgreSQL18.md#3-preparer-postgresql)

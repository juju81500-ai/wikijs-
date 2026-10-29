# Fiche_Simple_-_VM_Rocky_9_Pile_Web_Securiser_MariaDB.md

- **Environnement** : VM ou serveur Rocky Linux 9 hébergeant une application PHP avec MariaDB locale
- **OS / Version** : Rocky Linux 9 / RHEL 9; Nginx, PHP-FPM et MariaDB des dépôts actifs
- **Catégorie** : services web / base de données

---

## Problème précis à résoudre

Durcir MariaDB et créer une base et un compte applicatif dédiés.

## 1. Hors-Production (Lab / Test / POC)

1. Durcir MariaDB :
   ```bash
   sudo mariadb-secure-installation
   ```
   👉 Explication : Assistant interactif de durcissement (mot de passe root, comptes anonymes, base de test).

2. Ouvrir la console :
   ```bash
   sudo mariadb
   ```
   👉 Explication : Ouvre la console SQL.

3. Créer base et compte :
   ```sql
   CREATE DATABASE appdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'REMPLACER_PAR_UN_SECRET_UNIQUE';
   GRANT SELECT, INSERT, UPDATE, DELETE ON appdb.* TO 'appuser'@'localhost';
   EXIT;
   ```
   👉 Explication : Crée base et compte à droits minimaux; `appdb`, `appuser` et le secret sont des exemples à remplacer, le secret venant du coffre.

## 2. Production — Contrôles

Garder MariaDB en écoute locale si l'application est sur le même serveur.

## 3. Production — Sécurité

- Ne pas ouvrir 3306 sur le réseau.
- Ne jamais passer le secret en argument de commande.

## Validation et retour arrière

- **Validation** : connexion avec `appuser` possible en local et rien d'autre n'écoute en 3306 à distance.
- **Retour arrière** : `DROP USER 'appuser'@'localhost'; DROP DATABASE appdb;` dans la console.

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet — étape 3](/02-fiches-completes/rocky-linux/9/installation-deploiement/23-pile-web-rocky-linux-9-nginx-php-mariadb#3-securiser-mariadb)
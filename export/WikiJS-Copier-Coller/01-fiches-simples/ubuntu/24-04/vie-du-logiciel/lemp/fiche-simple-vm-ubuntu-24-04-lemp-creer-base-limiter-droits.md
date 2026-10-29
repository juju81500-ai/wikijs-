# Fiche_Simple_-_VM_Ubuntu_24.04_LEMP_Creer_Base_Limiter_Droits.md

- **Environnement** : VM Ubuntu Server 24.04 dédiée à une application Web PHP
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble); Nginx, PHP 8.3, MariaDB 10.11
- **Catégorie** : web / base de données

---

## Problème précis à résoudre

Créer la base applicative avec un compte aux droits minimaux.

## 1. Hors-Production (Lab / Test / POC)

1. Durcir l'installation MariaDB :
   ```bash
   sudo mariadb-secure-installation
   ```
   👉 Explication : assistant interactif: définit la politique des comptes et supprime les éléments de test.

2. Ouvrir la console SQL :
   ```bash
   sudo mariadb
   ```
   👉 Explication : connexion locale administrateur.

3. Dans la console, créer base et compte (remplacer `appdb`, `appuser` et le secret d'exemple par vos valeurs; le secret vient du coffre) :
   ```sql
   CREATE DATABASE appdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'REMPLACER_PAR_UN_SECRET_UNIQUE';
   GRANT SELECT, INSERT, UPDATE, DELETE ON appdb.* TO 'appuser'@'localhost';
   EXIT;
   ```
   👉 Explication : limite le compte aux droits nécessaires à l'exécution.

## 2. Production — Contrôles

Accorder des droits de migration seulement pendant une procédure approuvée.

## 3. Production — Sécurité

- MariaDB reste local: ne pas publier TCP/3306 si la pile est sur une seule VM.
- Ne jamais mettre le mot de passe réel dans un wiki ou dans l'historique.

## Validation et retour arrière

- **Validation** : le compte applicatif se connecte à `appdb` avec les seuls droits accordés.
- **Retour arrière** : dans la console SQL: `DROP USER 'appuser'@'localhost';` puis `DROP DATABASE appdb;` (uniquement s'il s'agit d'une base de test).

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [Ubuntu 24.04 — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet LEMP Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/20-pile-lemp-ubuntu-server-24-04-nginx-php83-mariadb#3-creer-et-limiter-la-base-applicative)
# Fiche_Simple_-_VM_Debian_13_LEMP_Securiser_MariaDB.md

- **Environnement** : MariaDB local sur Debian 13; compte applicatif limité à sa base
- **OS / Version** : Debian 13 Trixie; MariaDB des dépôts Debian
- **Catégorie** : pile Web LEMP / base de données

---

## Problème précis à résoudre

Initialiser MariaDB de façon sécurisée et créer une base ainsi qu'un compte limité pour l'application.

## 1. Hors-Production (Lab / Test / POC)

1. Sécuriser l'installation :
   ```bash
   sudo mariadb-secure-installation
   ```
   👉 Explication : conserver l'authentification `unix_socket` pour root; supprimer comptes anonymes et base `test`; interdire root à distance.

2. Créer base et compte applicatif (mot de passe saisi, non écrit en clair) :
   ```bash
   read -rsp "Mot de passe appuser : " APW; echo
   sudo mariadb -e "CREATE DATABASE appdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; CREATE USER 'appuser'@'localhost' IDENTIFIED BY '${APW}';"
   ```
   👉 Explication : compte local distinct, limité à `localhost`.

3. Accorder le minimum :
   ```bash
   sudo mariadb -e "GRANT SELECT, INSERT, UPDATE, DELETE ON appdb.* TO 'appuser'@'localhost';"
   ```
   👉 Explication : ajouter `CREATE, ALTER, INDEX` seulement si les migrations l'exigent.

4. Vérifier l'écoute :
   ```bash
   sudo ss -lntp | grep 3306
   ```
   👉 Explication : `127.0.0.1:3306` attendu; pas d'écoute sur les réseaux non prévus.

5. Tester la connexion applicative :
   ```bash
   mariadb -u appuser -p appdb -e 'SELECT 1;'
   unset APW
   ```
   👉 Explication : saisir le mot de passe à l'invite; on n'utilise pas le compte administrateur.

## 2. Production — Contrôles

Valider nom de base, propriétaire, privilèges, procédure de rotation des secrets, sauvegarde cohérente et test de restauration.

## 3. Production — Sécurité

- Remplacer tout secret d'exemple par une valeur unique issue du gestionnaire de secrets.
- Ne pas créer un compte applicatif accessible depuis `%`.
- Ne pas accorder `GRANT ALL` par commodité.
- Ne pas écouter sur toutes les interfaces; si accès distant requis, le concevoir sur réseau privé filtré avec TLS.

## Validation et retour arrière

- **Validation** : connexion locale et droits applicatifs conformes; écoute réseau limitée à la conception.
- **Retour arrière** : conserver export et configuration avant changement; révoquer seulement le compte/base créés après validation de leurs données.

## Si le problème n'est pas résolu

- [MariaDB — sécuriser l'installation](https://mariadb.com/kb/en/mysql_secure_installation/)
- [MariaDB — gestion des comptes](https://mariadb.com/kb/en/account-management-sql-commands/)
- [Guide complet LEMP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb#2-securiser-mariadb-et-creer-la-base)
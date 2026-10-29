# Fiche_Simple_-_VM_Debian_13_phpIPAM_Base.md

- **Environnement** : VM Debian 13, phpIPAM avec MariaDB locale, PHP-FPM et Nginx
- **OS / Version** : Debian 13 Trixie x86-64; phpIPAM 1.8.3; PHP 8.4
- **Catégorie** : IPAM / base de données

---

## Problème précis à résoudre

Créer une base UTF-8 et un utilisateur limité à cette base.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   read -rsp 'Mot de passe SQL phpipam : ' DBPW; echo
   sudo mariadb <<SQL
   CREATE DATABASE phpipam CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'phpipam'@'127.0.0.1' IDENTIFIED BY '${DBPW}';
   GRANT ALL PRIVILEGES ON phpipam.* TO 'phpipam'@'127.0.0.1';
   FLUSH PRIVILEGES;
   SQL
   unset DBPW
   ```
   👉 Explication : saisit le secret sans l'afficher (valeur aléatoire conservée dans un coffre), crée la base et l'utilisateur limité au schéma `phpipam`, puis efface la variable.

## 2. Production — Contrôles

Garder MariaDB sur localhost et ne pas publier le port 3306.

## 3. Production — Sécurité

- Ne jamais utiliser le compte root MariaDB depuis le site web.
- Secret aléatoire et unique, stocké dans un coffre.
- Ne pas mettre le secret dans l'historique du shell.

## Validation et retour arrière

- **Validation** : `sudo mariadb -e "SHOW DATABASES LIKE 'phpipam';"` affiche la base.
- **Retour arrière** : `sudo mariadb -e "DROP DATABASE phpipam; DROP USER 'phpipam'@'127.0.0.1';"` (uniquement avant mise en service).

## Si le problème n'est pas résolu

- [phpIPAM — installation](https://phpipam.net/documents/installation/)
- [phpIPAM — releases officielles](https://github.com/phpipam/phpipam/releases)
- [Guide complet Déployer phpIPAM 1.8.3 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/74-deploiement-phpipam-1-8-3-debian-13#3-creer-la-base-dediee)
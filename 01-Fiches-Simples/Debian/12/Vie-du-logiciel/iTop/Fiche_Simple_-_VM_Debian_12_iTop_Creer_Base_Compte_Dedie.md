# Fiche_Simple_-_VM_Debian_12_iTop_Creer_Base_Compte_Dedie.md

- **Environnement** : VM Linux dédiée avec Apache, PHP 8.2 ou 8.3 et MariaDB 10.11 (serveur ITSM/CMDB)
- **OS / Version** : Debian 12 Bookworm (ou Ubuntu Server 24.04 LTS); iTop Community 3.3.0
- **Catégorie** : ITSM / CMDB / helpdesk
- **Tags** : `debian12`, `itop`, `itsm`, `cmdb`, `apache`, `mariadb`

---

## Problème précis à résoudre

Créer une base UTF-8 et un compte réservé à iTop.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir le client MariaDB en local :
   ```bash
   sudo mariadb
   ```
   👉 Explication : connexion par le socket système, sans mot de passe en argument.

2. Créer la base :
   ```sql
   CREATE DATABASE itop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
   👉 Explication : jeu de caractères UTF-8 attendu par iTop.

3. Créer l'utilisateur (remplacer SECRET_LONG_ET_UNIQUE par un secret aléatoire tiré du coffre) :
   ```sql
   CREATE USER 'itop'@'localhost' IDENTIFIED BY 'SECRET_LONG_ET_UNIQUE';
   ```
   👉 Explication : compte réservé à iTop, accessible seulement en local.

4. Accorder les droits sur cette seule base :
   ```sql
   GRANT ALL PRIVILEGES ON itop.* TO 'itop'@'localhost';
   ```
   👉 Explication : limite les droits à la base `itop`; ne jamais utiliser root depuis l'application.

## 2. Production — Contrôles

Stocker le secret dans un coffre et documenter propriétaire et rotation.

## 3. Production — Sécurité

- Ne pas utiliser le compte root de la base depuis l'application.
- Ne pas laisser le secret dans l'historique shell.

## Validation et retour arrière

- **Validation** : la connexion avec le compte `itop` fonctionne et la base existe (`SHOW DATABASES;`).
- **Retour arrière** : en lab, supprimer base et utilisateur seulement s'ils sont vides: `DROP DATABASE itop;` puis `DROP USER 'itop'@'localhost';`.

## Si le problème n'est pas résolu

- [MariaDB — CREATE USER](https://mariadb.com/kb/en/create-user/)
- [iTop — installation et mise à niveau](https://www.itophub.io/wiki/page?id=latest:install:start)
- [Guide complet](../../../../../02-Fiches-Completes/Transverses/Multi-OS/Installation-Deploiement/40_Deploiement_iTop_3.3_Debian12_Ubuntu2404.md#3-creer-une-base-et-un-compte-dedies)

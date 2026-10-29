---
title: "Fiche Simple - VM Ubuntu 26.04 LibreNMS Configurer MariaDB"
description: "Régler MariaDB et créer une base et un compte dédiés à LibreNMS."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2604", "librenms", "snmpv3", "nginx", "mariadb"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Configurer_MariaDB.md

- **Environnement** : VM Ubuntu Server 26.04 dédiée à LibreNMS (Nginx, PHP-FPM, MariaDB, SNMP)
- **OS / Version** : Ubuntu Server 26.04 LTS; LibreNMS 26.10.2; PHP 8.5
- **Catégorie** : supervision / base de données
- **Tags** : `ubuntu2604`, `librenms`, `snmpv3`, `nginx`, `mariadb`

---

## Problème précis à résoudre

Régler MariaDB et créer une base et un compte dédiés à LibreNMS.

## 1. Hors-Production (Lab / Test / POC)

1. Éditer `/etc/mysql/mariadb.conf.d/50-server.cnf` et ajouter sous `[mariadbd]` :
   ```ini
   innodb_file_per_table=1
   lower_case_table_names=0
   ```
   👉 Explication : active une table InnoDB par fichier et la sensibilité à la casse requise par LibreNMS.

2. Redémarrer MariaDB :
   ```bash
   sudo systemctl enable --now mariadb
   sudo systemctl restart mariadb
   ```
   👉 Explication : Démarre MariaDB au boot et applique la configuration.

3. Ouvrir la console :
   ```bash
   sudo mariadb
   ```
   👉 Explication : Ouvre la console SQL en root local.

4. Créer base et utilisateur :
   ```sql
   CREATE DATABASE librenms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'librenms'@'localhost' IDENTIFIED BY 'REMPLACER_PAR_UN_SECRET_LONG';
   GRANT ALL PRIVILEGES ON librenms.* TO 'librenms'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```
   👉 Explication : Crée base et compte dédiés. `REMPLACER_PAR_UN_SECRET_LONG` est à remplacer par une valeur aléatoire tirée du coffre.

## 2. Production — Contrôles

Stocker le mot de passe en coffre; vérifier que MariaDB n'écoute qu'en local.

## 3. Production — Sécurité

- Aucun accès MariaDB distant pour LibreNMS.
- Ne pas laisser le secret dans l'historique shell ni dans un ticket.

## Validation et retour arrière

- **Validation** : `sudo mariadb -e "SHOW DATABASES;"` liste `librenms`.
- **Retour arrière** : `DROP DATABASE librenms; DROP USER 'librenms'@'localhost';` dans la console MariaDB, ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [LibreNMS — Installation](https://docs.librenms.org/Installation/Install-LibreNMS/)
- [Guide complet — étape 4](/02-fiches-completes/ubuntu/26-04/installation-deploiement/46-deploiement-librenms-26-10-2-ubuntu-26-04#4-configurer-mariadb)
---
title: "VM_Debian_13_Database_Installation-MariaDB-11"
description: "Installer le SGBD MariaDB 11 sur Debian 13, initialiser la sécurité d'accès, créer une base et un utilisateur applicatif restreint, et chiffrer les flux réseau."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[debian13]", "[mariadb]", "[database]", "[sql]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 VM_Debian_13_Database_Installation-MariaDB-11.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Bases de données / MariaDB
- **Tags** : `[debian13]`, `[mariadb]`, `[database]`, `[sql]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer le SGBD MariaDB 11 sur Debian 13, initialiser la sécurité d'accès, créer une base et un utilisateur applicatif restreint, et chiffrer les flux réseau.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide du serveur MariaDB :
   `apt-get update && apt-get install -y mariadb-server`
   👉 Explication : Télécharge et installe le paquet MariaDB serveur de base depuis les dépôts Debian 13.

2. Exécution de l'assistant de sécurisation interactif :
   `mariadb-secure-installation`
   👉 Explication : Supprime l'accès root sans mot de passe, les utilisateurs anonymes et la base de données de test.

3. Créer une base et un utilisateur local depuis la console MariaDB :
   ```bash
   sudo mariadb
   ```
   ```sql
   CREATE DATABASE db_test;
   CREATE USER 'usr_test'@'localhost' IDENTIFIED BY '<SECRET_UNIQUE>';
   GRANT SELECT, INSERT, UPDATE, DELETE ON db_test.* TO 'usr_test'@'localhost';
   EXIT;
   ```
   👉 Explication : Remplacer le placeholder dans la console, utiliser un secret unique et ne jamais créer un compte test accessible depuis `%`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installation des composants serveur et client MariaDB :
   `apt-get install -y mariadb-server mariadb-client`
   👉 Explication : Installe l'ensemble des paquets nécessaires à la gestion de la base de données.

2. Initialisation de la base de données applicative en UTF-8 :
   `mariadb -e "CREATE DATABASE app_prod CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"`
   👉 Explication : Prépare la base de production avec l'encodage de caractères complet recommandé.

3. Créer un compte applicatif limité à l'adresse exacte du serveur applicatif depuis la console MariaDB :
   ```sql
   CREATE USER 'app_user'@'192.0.2.20' IDENTIFIED BY '<SECRET_UNIQUE>';
   GRANT SELECT, INSERT, UPDATE, DELETE ON app_prod.* TO 'app_user'@'192.0.2.20';
   ```
   👉 Explication : Remplacer l'adresse et le secret. N'utiliser ni `%` ni un mot de passe d'exemple ; ajouter des privilèges de migration uniquement pendant les migrations.

4. Si l'application est sur un autre hôte, sauvegarder et modifier la directive `bind-address` dans `/etc/mysql/mariadb.conf.d/50-server.cnf` pour écouter sur l'IP privée du serveur DB. Vérifier que cette IP est assignée avant le redémarrage.
   ```bash
   sudo mariadb -e "SHOW VARIABLES LIKE 'bind_address';"
   sudo systemctl restart mariadb
   sudo ss -lntp | grep 3306
   ```
   👉 Explication : Ne pas écouter sur toutes les interfaces. Confirmer l'accès local avant d'ouvrir le port aux seuls hôtes applicatifs.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Après installation des certificats émis par l'autorité approuvée, sauvegarder puis configurer dans un fichier dédié :
   ```ini
   [mariadb]
   ssl-ca=/etc/mysql/ssl/ca-cert.pem
   ssl-cert=/etc/mysql/ssl/server-cert.pem
   ssl-key=/etc/mysql/ssl/server-key.pem
   require_secure_transport=ON
   local-infile=0
   ```
   👉 Explication : Tester d'abord les clients TLS ; exiger le transport sécurisé peut refuser les clients non configurés.

2. Restreindre la clé privée au compte du service et conserver la chaîne publique lisible :
   `sudo chown mysql:mysql /etc/mysql/ssl/server-key.pem && sudo chmod 600 /etc/mysql/ssl/server-key.pem`
   👉 Explication : Ne pas appliquer récursivement des permissions aux certificats, et vérifier que MariaDB peut lire la clé avant redémarrage.

3. Autoriser TCP/3306 uniquement depuis l'adresse du serveur applicatif dans le pare-feu persistant géré par l'hôte. Valider et appliquer la règle par ce gestionnaire ; une commande `nft add rule` seule n'est pas persistante.
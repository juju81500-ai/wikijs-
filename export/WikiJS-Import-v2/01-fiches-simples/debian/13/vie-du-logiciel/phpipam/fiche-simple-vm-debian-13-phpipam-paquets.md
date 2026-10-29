---
title: "Fiche Simple - VM Debian 13 phpIPAM Paquets"
description: "Installer Nginx, MariaDB, PHP-FPM et les extensions PHP requises."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "phpipam", "ipam", "nginx", "mariadb", "apt", "php"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_phpIPAM_Paquets.md

- **Environnement** : VM Debian 13, phpIPAM avec MariaDB locale, PHP-FPM et Nginx
- **OS / Version** : Debian 13 Trixie x86-64; phpIPAM 1.8.3; PHP 8.4
- **Catégorie** : IPAM / installation
- **Tags** : `debian13`, `phpipam`, `ipam`, `nginx`, `mariadb`, `apt`, `php`

---

## Problème précis à résoudre

Installer Nginx, MariaDB, PHP-FPM et les extensions PHP requises.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   sudo apt update
   sudo apt install -y nginx mariadb-server mariadb-client git ca-certificates curl php-fpm php-cli php-mysql php-gmp php-common php-mbstring php-gd php-curl php-xml php-pear php-zip php-ldap
   ```
   👉 Explication : installe serveur web, base de données, PHP-FPM et extensions de phpIPAM.

2. Exécuter :
   ```bash
   php -v
   php -m
   ```
   👉 Explication : affiche la version PHP et les modules; vérifier `pdo_mysql`, `gmp`, `mbstring`, `curl`, `xml`.

3. Exécuter :
   ```bash
   sudo systemctl enable --now nginx mariadb
   ```
   👉 Explication : active et démarre Nginx et MariaDB.

4. Exécuter :
   ```bash
   systemctl list-units 'php*-fpm.service'
   ```
   👉 Explication : retrouve le nom exact de l'unité PHP-FPM installée.

## 2. Production — Contrôles

Valider les versions des paquets en préproduction.

## 3. Production — Sécurité

- Garder MariaDB sur localhost.
- Installer uniquement les paquets listés.

## Validation et retour arrière

- **Validation** : les modules PHP requis sont présents et nginx et mariadb sont actifs.
- **Retour arrière** : `sudo systemctl disable --now nginx mariadb` puis `sudo apt remove` des paquets si besoin (VM de test).

## Si le problème n'est pas résolu

- [phpIPAM — installation](https://phpipam.net/documents/installation/)
- [phpIPAM — releases officielles](https://github.com/phpipam/phpipam/releases)
- [Guide complet Déployer phpIPAM 1.8.3 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/74-deploiement-phpipam-1-8-3-debian-13#2-installer-les-paquets)
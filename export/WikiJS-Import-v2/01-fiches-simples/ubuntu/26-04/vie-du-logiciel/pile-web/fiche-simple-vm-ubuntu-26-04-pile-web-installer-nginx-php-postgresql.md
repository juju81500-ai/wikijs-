---
title: "Fiche Simple - VM Ubuntu 26.04 Pile Web Installer Nginx PHP PostgreSQL"
description: "Installer les paquets et démarrer les services."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2604", "nginx", "php8.5", "postgresql18", "tls"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Installer_Nginx_PHP_PostgreSQL.md

- **Environnement** : VM ou serveur dédié Ubuntu Server hébergeant une application PHP avec PostgreSQL local et TLS
- **OS / Version** : Ubuntu Server 26.04 LTS (Resolute); Nginx, PHP 8.5, PostgreSQL 18
- **Catégorie** : services web / installation
- **Tags** : `ubuntu2604`, `nginx`, `php8.5`, `postgresql18`, `tls`

---

## Problème précis à résoudre

Installer les paquets et démarrer les services.

## 1. Hors-Production (Lab / Test / POC)

1. Installer :
   ```bash
   sudo apt install nginx php8.5-fpm php8.5-cli php8.5-pgsql \
     php8.5-curl php8.5-gd php8.5-mbstring php8.5-xml php8.5-zip postgresql-18
   ```
   👉 Explication : Installe la pile depuis les dépôts Ubuntu.

2. Démarrer :
   ```bash
   sudo systemctl enable --now nginx php8.5-fpm postgresql
   ```
   👉 Explication : Active et démarre les services.

3. Contrôler :
   ```bash
   nginx -v
   php8.5 -v
   pg_lsclusters
   ls -l /run/php/
   systemctl --failed
   ```
   👉 Explication : Vérifie versions, cluster PostgreSQL, socket FPM et absence d'unité en échec.

## 2. Production — Contrôles

Noter les versions installées.

## 3. Production — Sécurité

- Ne pas publier les services avant la configuration TLS et pare-feu.

## Validation et retour arrière

- **Validation** : services actifs, cluster `online`, socket présent.
- **Retour arrière** : `sudo systemctl disable --now nginx php8.5-fpm postgresql` puis `sudo apt remove` des paquets, ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [PostgreSQL 18 — documentation](https://www.postgresql.org/docs/18/)
- [Guide complet — étape 2](/02-fiches-completes/ubuntu/26-04/installation-deploiement/21-pile-web-ubuntu-server-26-04-nginx-php85-postgresql18#2-installer-nginx-php-fpm-et-postgresql)
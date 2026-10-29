---
title: "Fiche Simple - VM Ubuntu 24.04 LEMP Configurer Nginx PHPFPM"
description: "Créer un server block Nginx qui transmet les fichiers PHP au socket FPM."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu24.04", "nginx", "php8.3", "mariadb", "lemp", "server-block", "php-fpm"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_LEMP_Configurer_Nginx_PHPFPM.md

- **Environnement** : VM Ubuntu Server 24.04 dédiée à une application Web PHP
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble); Nginx, PHP 8.3, MariaDB 10.11
- **Catégorie** : web / configuration
- **Tags** : `ubuntu24.04`, `nginx`, `php8.3`, `mariadb`, `lemp`, `server-block`, `php-fpm`

---

## Problème précis à résoudre

Créer un server block Nginx qui transmet les fichiers PHP au socket FPM.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire applicatif :
   ```bash
   sudo install -d -o root -g www-data -m 0755 /var/www/app/public
   ```
   👉 Explication : la racine est lisible par le groupe Web.

2. Créer `/etc/nginx/sites-available/app` avec ce contenu (`app.example.net` est à remplacer par votre FQDN) :
   ```nginx
   server {
       listen 80;
       listen [::]:80;
       server_name app.example.net;
       root /var/www/app/public;
       index index.php;

       location / { try_files $uri $uri/ =404; }
       location ~ \.php$ {
           try_files $uri =404;
           include snippets/fastcgi-php.conf;
           fastcgi_pass unix:/run/php/php8.3-fpm.sock;
       }
       location ~ /\. { deny all; }
   }
   ```
   👉 Explication : définit FQDN, racine, `try_files`, refus des fichiers cachés et socket FPM.

3. Activer le site, tester puis recharger :
   ```bash
   sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app
   sudo nginx -t
   sudo systemctl reload nginx
   ```
   👉 Explication : `nginx -t` doit réussir avant tout rechargement.

## 2. Production — Contrôles

Donner l'écriture au groupe Web uniquement sur cache et uploads réellement requis.

## 3. Production — Sécurité

- Ne pas recharger Nginx si `nginx -t` échoue.

## Validation et retour arrière

- **Validation** : `nginx -t` OK et le site répond.
- **Retour arrière** : `sudo rm /etc/nginx/sites-enabled/app`, `sudo nginx -t`, puis `sudo systemctl reload nginx`.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [Ubuntu 24.04 — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet LEMP Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/20-pile-lemp-ubuntu-server-24-04-nginx-php83-mariadb#4-configurer-nginx-et-php-fpm)
---
title: "Fiche Simple - VM Debian 13 phpIPAM Nginx PHP"
description: "Publier phpIPAM en HTTPS via Nginx et PHP-FPM."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "phpipam", "ipam", "nginx", "mariadb", "php-fpm", "tls"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_phpIPAM_Nginx_PHP.md

- **Environnement** : VM Debian 13, phpIPAM avec MariaDB locale, PHP-FPM et Nginx
- **OS / Version** : Debian 13 Trixie x86-64; phpIPAM 1.8.3; PHP 8.4
- **Catégorie** : IPAM / serveur web
- **Tags** : `debian13`, `phpipam`, `ipam`, `nginx`, `mariadb`, `nginx`, `php-fpm`, `tls`

---

## Problème précis à résoudre

Publier phpIPAM en HTTPS via Nginx et PHP-FPM.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   sudoedit /etc/nginx/sites-available/phpipam
   ```
   👉 Explication : créer le site : un serveur 80 qui redirige vers HTTPS, et un serveur 443 avec `root /var/www/phpipam`, `ssl_certificate`/`ssl_certificate_key`, `location /api`, `location ~ \.php$` (`include snippets/fastcgi-php.conf;` et `fastcgi_pass unix:/run/php/php8.4-fpm.sock;`) et `location ~ /\. { deny all; }`. `ipam.example.net` et les chemins de certificats sont à remplacer.

2. Exécuter :
   ```bash
   ls -l /run/php/php8.4-fpm.sock
   ```
   👉 Explication : vérifie l'existence du socket PHP-FPM avant activation (et celle des certificats déclarés).

3. Exécuter :
   ```bash
   sudo ln -s /etc/nginx/sites-available/phpipam /etc/nginx/sites-enabled/phpipam
   sudo nginx -t
   sudo systemctl reload nginx
   ```
   👉 Explication : active le site, teste la syntaxe, puis recharge Nginx.

## 2. Production — Contrôles

Limiter le port HTTPS au réseau d'administration.

## 3. Production — Sécurité

- Ne pas publier le port 3306.
- Ne faire confiance aux en-têtes `X-Forwarded-*` que si le proxy les remplace systématiquement et que l'accès direct au backend est bloqué.

## Validation et retour arrière

- **Validation** : `sudo nginx -t` est valide et le site répond en HTTPS depuis le réseau d'administration.
- **Retour arrière** : supprimer le lien dans `sites-enabled`, puis `sudo nginx -t` et `sudo systemctl reload nginx`.

## Si le problème n'est pas résolu

- [phpIPAM — installation](https://phpipam.net/documents/installation/)
- [phpIPAM — releases officielles](https://github.com/phpipam/phpipam/releases)
- [Guide complet Déployer phpIPAM 1.8.3 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/74-deploiement-phpipam-1-8-3-debian-13#5-configurer-nginx-et-php-fpm)
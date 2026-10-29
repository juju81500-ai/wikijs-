---
title: "Fiche Simple - VM Debian 12 GLPI Installer Application"
description: "Déployer l'archive GLPI officielle dans un répertoire versionné et configurer le serveur Web sans rendre toute l'installation modifiable."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "glpi", "php", "nginx", "deployment"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_GLPI_Installer_Application.md

- **Environnement** : VM Debian dédiée avec serveur Web et PHP-FPM installés
- **OS / Version** : Debian 12 ou 13; version GLPI validée
- **Catégorie** : GLPI / déploiement applicatif
- **Tags** : `debian12`, `glpi`, `php`, `nginx`, `deployment`

---

## Problème précis à résoudre

Déployer l'archive GLPI officielle dans un répertoire versionné et configurer le serveur Web sans rendre toute l'installation modifiable.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire des versions :
   ```bash
   sudo install -d -o root -g www-data -m 0750 /var/www/glpi/releases
   ```
   👉 Explication : propriété root; le serveur Web n'écrit pas dans le code.

2. Télécharger l'archive officielle de la version validée et vérifier l'empreinte publiée :
   ```bash
   cd /tmp
   curl -fsSLO URL_OFFICIELLE_ARCHIVE_GLPI
   sha256sum glpi-X.Y.Z.tgz
   ```
   👉 Explication : remplacer URL et version; comparer avec l'empreinte ou la signature de la release GitHub officielle.

3. Extraire dans un répertoire de version et créer le lien `current` :
   ```bash
   sudo tar xzf glpi-X.Y.Z.tgz -C /var/www/glpi/releases
   sudo mv /var/www/glpi/releases/glpi /var/www/glpi/releases/X.Y.Z
   sudo ln -sfn /var/www/glpi/releases/X.Y.Z /var/www/glpi/current
   ```
   👉 Explication : le lien permet un retour arrière rapide.

4. Donner l'écriture aux seuls chemins nécessaires (`config`, `files`, `marketplace`) :
   ```bash
   sudo install -d -o www-data -g www-data -m 0750 /var/lib/glpi /etc/glpi /var/log/glpi
   ```
   👉 Explication : déplacer ces répertoires hors de la racine Web selon la documentation de la version.

5. Créer l'hôte virtuel Nginx (nom DNS, socket PHP réel, racine publique `public/`) :
   ```bash
   ls /run/php/
   sudo tee /etc/nginx/sites-available/glpi >/dev/null <<'EOF'
   server {
       listen 80;
       server_name glpi.example.net;
       root /var/www/glpi/current/public;
       index index.php;
       location / { try_files $uri /index.php$is_args$args; }
       location ~ \.php$ {
           include snippets/fastcgi-php.conf;
           fastcgi_pass unix:/run/php/php8.2-fpm.sock;
       }
       location ~ /\. { deny all; }
   }
   EOF
   sudo ln -s /etc/nginx/sites-available/glpi /etc/nginx/sites-enabled/glpi
   sudo nginx -t && sudo systemctl reload nginx
   ```
   👉 Explication : adapter le socket (Debian 12 : `php8.2-fpm.sock`); ne recharger que si `nginx -t` réussit.

## 2. Production — Contrôles

Faire relire source, empreinte, version, chemins, propriétaire, permissions, socket FPM et configuration du virtual host.

## 3. Production — Sécurité

- Ne pas déployer une archive dont la provenance ou l'intégrité ne peut pas être vérifiée.
- Ne pas rendre toute l'installation modifiable par l'utilisateur du serveur Web.
- Refuser l'accès Web aux fichiers cachés, données et configurations.
- Ne pas basculer le lien `current` avant validation de la configuration.

## Validation et retour arrière

- **Validation** : version vérifiée, chemins et droits minimaux, virtual host accepté par le test de configuration.
- **Retour arrière** : restaurer la configuration et le lien vers la version précédente connue comme valide.

## Si le problème n'est pas résolu

- [GLPI — documentation d'installation](https://glpi-install.readthedocs.io/en/latest/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet GLPI Debian](/02-fiches-completes/debian/12/installation-deploiement/03-helpdesk-itsm-glpi-11-12-debian-12-13)
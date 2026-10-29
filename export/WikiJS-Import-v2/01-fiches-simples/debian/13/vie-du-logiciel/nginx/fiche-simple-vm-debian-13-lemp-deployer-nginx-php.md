---
title: "Fiche Simple - VM Debian 13 LEMP Deployer Nginx PHP"
description: "Configurer un hôte Nginx et le relier au socket PHP-FPM réellement installé, avec un test temporaire non sensible."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "lemp", "nginx", "php-fpm", "virtual-host"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_LEMP_Deployer_Nginx_PHP.md

- **Environnement** : Debian 13; Nginx et PHP-FPM 8.4 depuis les dépôts Debian
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : pile Web LEMP / virtual host
- **Tags** : `debian13`, `lemp`, `nginx`, `php-fpm`, `virtual-host`

---

## Problème précis à résoudre

Configurer un hôte Nginx et le relier au socket PHP-FPM réellement installé, avec un test temporaire non sensible.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire public :
   ```bash
   sudo install -d -o root -g www-data -m 0755 /var/www/app/public
   ```
   👉 Explication : propriétaire root, lecture pour le serveur Web.

2. Déposer un endpoint de test neutre (jamais `phpinfo()`) :
   ```bash
   sudo tee /var/www/app/public/index.php >/dev/null <<'PHP'
   <?php
   header('Content-Type: text/plain; charset=utf-8');
   echo "PHP-FPM fonctionne\n";
   PHP
   sudo chmod 0644 /var/www/app/public/index.php
   ```
   👉 Explication : message neutre, à supprimer après le test.

3. Repérer le socket PHP-FPM réel :
   ```bash
   ls -l /run/php/
   ```
   👉 Explication : utiliser ce nom exact dans `fastcgi_pass` (ex. `php8.4-fpm.sock`).

4. Créer le server block :
   ```bash
   sudo tee /etc/nginx/sites-available/app >/dev/null <<'EOF'
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
           fastcgi_pass unix:/run/php/php8.4-fpm.sock;
       }
       location ~ /\. { deny all; }
   }
   EOF
   ```
   👉 Explication : remplacer `server_name` et le socket; `try_files $uri =404` évite d'exécuter un fichier inexistant.

5. Activer, tester, démarrer, recharger :
   ```bash
   sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app
   sudo nginx -t
   sudo systemctl enable --now nginx mariadb php8.4-fpm
   sudo systemctl reload nginx
   ```
   👉 Explication : ne recharger que si `nginx -t` réussit.

## 2. Production — Contrôles

Vérifier chemins, nom DNS, socket FPM, droits du code, modules PHP nécessaires et validation de configuration avant tout rechargement.

## 3. Production — Sécurité

- Ne pas rendre le code applicatif modifiable par le processus Web hors répertoires nécessaires.
- Refuser l'accès aux fichiers cachés et ne pas publier de page de diagnostic PHP.
- Ne pas activer un site si `nginx -t` échoue.
- Supprimer le fichier de test dès que son résultat est confirmé.

## Validation et retour arrière

- **Validation** : endpoint local répond, socket FPM est actif et les journaux ne signalent pas d'erreur.
- **Retour arrière** : restaurer le server block précédent, vérifier `nginx -t`, recharger Nginx et retirer le site de test.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [PHP — configuration FPM](https://www.php.net/manual/en/install.fpm.php)
- [Guide complet LEMP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb#3-deployer-un-hote-nginx-et-php-fpm)
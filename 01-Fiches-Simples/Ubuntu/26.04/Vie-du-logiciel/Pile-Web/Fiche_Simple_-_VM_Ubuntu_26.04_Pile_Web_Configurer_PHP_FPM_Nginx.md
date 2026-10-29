# Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Configurer_PHP_FPM_Nginx.md

- **Environnement** : VM ou serveur dédié Ubuntu Server hébergeant une application PHP avec PostgreSQL local et TLS
- **OS / Version** : Ubuntu Server 26.04 LTS (Resolute); Nginx, PHP 8.5, PostgreSQL 18
- **Catégorie** : services web / configuration
- **Tags** : `ubuntu2604`, `nginx`, `php8.5`, `postgresql18`, `tls`

---

## Problème précis à résoudre

Créer le server block Nginx et l'activer après validation.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire :
   ```bash
   sudo mkdir -p /var/www/app/public
   sudo chown -R root:www-data /var/www/app
   sudo chmod -R 750 /var/www/app
   ```
   👉 Explication : Répertoire non modifiable par l'utilisateur web (chemin à adapter).

2. Créer `/etc/nginx/sites-available/app` (remplacer `app.example.net`) :
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
           fastcgi_pass unix:/run/php/php8.5-fpm.sock;
       }
       location ~ /\. { deny all; }
   }
   ```
   👉 Explication : vhost minimal; le socket doit exister dans `/run/php/`.

3. Activer et valider :
   ```bash
   sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app
   sudo nginx -t
   sudo systemctl reload nginx
   ```
   👉 Explication : Active le site, teste la syntaxe puis recharge.

## 2. Production — Contrôles

Confirmer le socket dans `/run/php/` avant le rechargement.

## 3. Production — Sécurité

- Interdire les fichiers cachés; droits minimaux.

## Validation et retour arrière

- **Validation** : `nginx -t` OK et rechargement sans erreur.
- **Retour arrière** : `sudo rm /etc/nginx/sites-enabled/app && sudo nginx -t && sudo systemctl reload nginx`.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [PostgreSQL 18 — documentation](https://www.postgresql.org/docs/18/)
- [Guide complet — étape 4](../../../../../02-Fiches-Completes/Ubuntu/26.04/Installation-Deploiement/21_Pile_Web_Ubuntu_Server_26.04_Nginx_PHP85_PostgreSQL18.md#4-configurer-php-fpm-et-nginx)

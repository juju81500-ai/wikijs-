# Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Configurer_PHP_FPM_Nginx.md

- **Environnement** : VM Ubuntu Server 26.04 dédiée à LibreNMS (Nginx, PHP-FPM, MariaDB, SNMP)
- **OS / Version** : Ubuntu Server 26.04 LTS; LibreNMS 26.10.2; PHP 8.5
- **Catégorie** : supervision / serveur web

---

## Problème précis à résoudre

Créer un pool PHP-FPM dédié et un vhost Nginx pour LibreNMS.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le pool :
   ```bash
   sudo cp /etc/php/8.5/fpm/pool.d/www.conf /etc/php/8.5/fpm/pool.d/librenms.conf
   sudoedit /etc/php/8.5/fpm/pool.d/librenms.conf
   ```
   👉 Explication : Crée le pool dédié à partir du pool par défaut puis l'édite.

2. Dans ce fichier, renommer la section `[www]` en `[librenms]` et définir (supprimer toute valeur dupliquée) :
   ```ini
   user = librenms
   group = librenms
   listen = /run/php-fpm-librenms.sock
   listen.owner = www-data
   listen.group = www-data
   listen.mode = 0660
   ```
   👉 Explication : le pool tourne sous le compte de service et expose un socket lisible par Nginx.

3. Définir la timezone dans `/etc/php/8.5/fpm/php.ini` et `/etc/php/8.5/cli/php.ini`.
   👉 Explication : garde un fuseau cohérent entre web et tâches.

4. Créer `/etc/nginx/conf.d/librenms.conf` (remplacer `librenms.example.net` par le vrai nom DNS) :
   ```nginx
   server {
     listen 80;
     server_name librenms.example.net;
     root /opt/librenms/html;
     index index.php;
     charset utf-8;
   
     location / {
       try_files $uri $uri/ /index.php?$query_string;
     }
   
     location ~ [^/]\.php(/|$) {
       fastcgi_pass unix:/run/php-fpm-librenms.sock;
       fastcgi_split_path_info ^(.+\.php)(/.+)$;
       include fastcgi.conf;
     }
   
     location ~ /\. {
       deny all;
     }
   }
   ```
   👉 Explication : HTTP seulement pour le contrôle initial; ne pas exposer ainsi.

5. Tester et redémarrer :
   ```bash
   sudo nginx -t
   sudo systemctl restart php8.5-fpm nginx
   ```
   👉 Explication : Teste la syntaxe puis redémarre les services.

## 2. Production — Contrôles

Mettre le TLS au reverse proxy ou configurer un vhost HTTPS approuvé avant tout accès utilisateur; restreindre l'administration au réseau de gestion.

## 3. Production — Sécurité

- Ne pas ouvrir le port HTTP public avant HTTPS via un certificat approuvé.

## Validation et retour arrière

- **Validation** : `nginx -t` est OK et `php8.5-fpm` et `nginx` sont actifs.
- **Retour arrière** : supprimer `/etc/nginx/conf.d/librenms.conf` et le pool `librenms.conf`, puis `sudo systemctl restart php8.5-fpm nginx`.

## Si le problème n'est pas résolu

- [LibreNMS — Installation](https://docs.librenms.org/Installation/Install-LibreNMS/)
- [Guide complet — étape 5](/02-fiches-completes/ubuntu/26-04/installation-deploiement/46-deploiement-librenms-26-10-2-ubuntu-26-04#5-configurer-php-fpm-et-nginx)
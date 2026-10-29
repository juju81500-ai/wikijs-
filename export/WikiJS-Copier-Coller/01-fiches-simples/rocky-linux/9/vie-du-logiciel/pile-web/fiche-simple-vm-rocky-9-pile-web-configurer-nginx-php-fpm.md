# Fiche_Simple_-_VM_Rocky_9_Pile_Web_Configurer_Nginx_PHP_FPM.md

- **Environnement** : VM ou serveur Rocky Linux 9 hébergeant une application PHP avec MariaDB locale
- **OS / Version** : Rocky Linux 9 / RHEL 9; Nginx, PHP-FPM et MariaDB des dépôts actifs
- **Catégorie** : services web / configuration

---

## Problème précis à résoudre

Créer le répertoire applicatif et le server block Nginx relié à PHP-FPM.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire :
   ```bash
   sudo mkdir -p /var/www/app/public
   sudo chown -R root:nginx /var/www/app
   sudo chmod -R 750 /var/www/app
   ```
   👉 Explication : Crée le répertoire applicatif avec des droits minimaux (chemin et groupe à adapter).

2. Créer `/etc/nginx/conf.d/app.conf` (remplacer `app.example.net` par le vrai nom) :
   ```nginx
   server {
       listen 80;
       server_name app.example.net;
       root /var/www/app/public;
       index index.php;
   
       location / { try_files $uri $uri/ =404; }
       location ~ \.php$ {
           try_files $uri =404;
           include fastcgi_params;
           fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
           fastcgi_pass unix:/run/php-fpm/www.sock;
       }
       location ~ /\. { deny all; }
   }
   ```
   👉 Explication : vhost minimal; vérifier que le socket correspond au pool PHP-FPM installé.

3. Tester puis recharger :
   ```bash
   sudo nginx -t
   sudo systemctl reload nginx
   ```
   👉 Explication : Teste la syntaxe avant de recharger.

## 2. Production — Contrôles

Vérifier la valeur du socket et du pool PHP-FPM.

## 3. Production — Sécurité

- Interdire l'accès aux fichiers cachés (`location ~ /\.`).
- Droits applicatifs minimaux.

## Validation et retour arrière

- **Validation** : `nginx -t` OK et la page de test répond.
- **Retour arrière** : supprimer `/etc/nginx/conf.d/app.conf` puis `sudo systemctl reload nginx`.

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet — étape 4](/02-fiches-completes/rocky-linux/9/installation-deploiement/23-pile-web-rocky-linux-9-nginx-php-mariadb#4-configurer-nginx-et-php-fpm)
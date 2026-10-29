# 📄 Fiche_Simple_-_VM_Debian_13_Web_Installation_Nginx_PHP8.4_FPM.md

- **Environnement** : VM ou serveur Debian 13
- **OS / Version** : Debian 13 (Trixie), Nginx et PHP-FPM 8.4 des dépôts Debian
- **Catégorie** : Web / Installation / Configuration
- **Tags** : `[debian13]`, `[trixie]`, `[nginx]`, `[php8.4]`, `[php-fpm]`, `[web]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer Nginx et PHP-FPM 8.4 sur Debian 13, relier le serveur au socket FPM de Trixie et vérifier les paquets disponibles avant l'installation.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier la version Debian et la série PHP candidate :
   ```bash
   cat /etc/debian_version
   apt-cache policy php8.4-fpm
   ```
2. Installer Nginx et les paquets PHP 8.4 requis par le lab :
   ```bash
   sudo apt update
   sudo apt install nginx php8.4-fpm php8.4-cli php8.4-mysql php8.4-xml php8.4-mbstring php8.4-curl
   ```
3. Vérifier les versions, services et socket réellement installés :
   ```bash
   nginx -v
   php8.4 -v
   systemctl status nginx php8.4-fpm --no-pager
   ls -l /run/php/
   ```
   👉 *Explication : Trixie fournit PHP 8.4 dans sa base; les révisions de sécurité évoluent. N'ajouter aucun dépôt tiers pour obtenir une version déjà fournie par Debian.*

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder la configuration Nginx et installer uniquement les modules PHP nécessaires à l'application.
2. Créer le server block dans `/etc/nginx/sites-available/app.conf`; définir `server_name`, `root`, `try_files` et le socket réellement présent, généralement `/run/php/php8.4-fpm.sock`.
3. Activer le site et valider avant rechargement :
   ```bash
   sudo ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf
   sudo nginx -t
   sudo systemctl reload nginx
   sudo systemctl status php8.4-fpm --no-pager
   ```
4. Tester le site avec un endpoint temporaire affichant uniquement `OK`, puis le supprimer immédiatement; ne pas publier `phpinfo()`.

## 🔒 3. Production — Façon Sécurisée
1. Vérifier la version active avec `apt-cache policy` et `php8.4 -v`; éviter de mélanger les modules de versions PHP ou des dépôts externes.
2. Configurer `expose_php = Off` et `display_errors = Off` dans le `php.ini` réellement chargé par FPM; confirmer avec `php8.4 --ini`.
3. Garder le code non modifiable par le processus Web et limiter l'écriture aux répertoires applicatifs nécessaires.

## ✅ Validation et retour arrière
- Confirmer `nginx -t`, l'état des services, le socket PHP-FPM, le code HTTP attendu et les journaux.
- En cas d'échec, restaurer le server block sauvegardé, exécuter `nginx -t`, puis recharger Nginx.
- Vérifier que le site ne référence pas un ancien socket PHP après mise à jour.
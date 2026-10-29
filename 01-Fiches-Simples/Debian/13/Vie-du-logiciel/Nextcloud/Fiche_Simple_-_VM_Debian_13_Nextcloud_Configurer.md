# Fiche_Simple_-_VM_Debian_13_Nextcloud_Configurer

- **Environnement** : VM Debian 13; Nextcloud (archive officielle), Apache, PHP 8.4 et MariaDB
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Nextcloud — Configurer
- **Tags** : `debian13`, `nextcloud`, `cloud`, `apache`, `php`, `configurer`

---

## Problème précis à résoudre

Configurer Apache, le domaine de confiance, le cache et les tâches de fond de Nextcloud.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le virtual host Apache :
   ```bash
   sudo tee /etc/apache2/sites-available/nextcloud.conf >/dev/null <<'EOF'
   <VirtualHost *:80>
     ServerName CLOUD.EXAMPLE.NET
     DocumentRoot /var/www/nextcloud
     <Directory /var/www/nextcloud/>
       Require all granted
       AllowOverride All
       Options FollowSymLinks MultiViews
       <IfModule mod_dav.c>
         Dav off
       </IfModule>
     </Directory>
   </VirtualHost>
   EOF
   ```
   👉 Explication : `CLOUD.EXAMPLE.NET` est à remplacer ; `AllowOverride All` autorise le `.htaccess` fourni par Nextcloud.

2. Activer le site et les modules :
   ```bash
   sudo a2enmod rewrite headers env dir mime setenvif
   sudo a2dissite 000-default
   sudo a2ensite nextcloud
   sudo apache2ctl configtest && sudo systemctl reload apache2
   ```
   👉 Explication : le rechargement n'a lieu que si `configtest` répond `Syntax OK`.

3. Déclarer le domaine de confiance et l'URL :
   ```bash
   cd /var/www/nextcloud
   sudo -u www-data php occ config:system:set trusted_domains 1 --value=CLOUD.EXAMPLE.NET
   sudo -u www-data php occ config:system:set overwrite.cli.url --value=https://CLOUD.EXAMPLE.NET
   ```
   👉 Explication : évite les erreurs « domaine non fiable » ; l'URL sera en HTTPS après la fiche Sécuriser.

4. Activer le cache local APCu et la région téléphonique :
   ```bash
   sudo -u www-data php occ config:system:set memcache.local --value='\OC\Memcache\APCu'
   sudo -u www-data php occ config:system:set default_phone_region --value=FR
   ```
   👉 Explication : à adapter au pays. Redis est recommandé pour le verrouillage de fichiers en production.

5. Passer les tâches de fond en cron système :
   ```bash
   sudo -u www-data php occ background:cron
   echo '*/5 * * * * www-data php -f /var/www/nextcloud/cron.php' | sudo tee /etc/cron.d/nextcloud
   ```
   👉 Explication : la tâche toutes les 5 minutes est la méthode recommandée par la documentation ; la limite de mémoire PHP (≥ 512 Mo recommandé) se règle dans `/etc/php/8.4/apache2/php.ini`.

## 2. Production — Contrôles

Relire `config/config.php` (sans le diffuser, il contient des secrets), contrôler `memory_limit`, `upload_max_filesize`, OPcache et la page Administration > Vue d'ensemble.

## 3. Production — Sécurité

- Ne jamais publier `config.php`.
- `trusted_domains` limité aux noms réellement utilisés.

## Validation et retour arrière

- **Validation** : `sudo apache2ctl configtest` renvoie `Syntax OK` et `occ status` fonctionne.
- **Retour arrière** : `sudo a2dissite nextcloud && sudo systemctl reload apache2` et restauration de `config/config.php` depuis la sauvegarde.

## Si le problème n'est pas résolu

- [Nextcloud — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Nextcloud_Prerequis_Limites.md)
- [Nextcloud — Installer](Fiche_Simple_-_VM_Debian_13_Nextcloud_Installer.md)
- [Nextcloud — manuel d'administration](https://docs.nextcloud.com/server/latest/admin_manual/)
- [Nextcloud — prérequis système](https://docs.nextcloud.com/server/latest/admin_manual/installation/system_requirements.html)

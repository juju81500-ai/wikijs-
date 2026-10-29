# Fiche_Simple_-_VM_Debian_13_LEMP_Depanner.md

- **Environnement** : pile LEMP Debian 13; diagnostic local et accès administrateur contrôlé
- **OS / Version** : Debian 13 Trixie; Nginx, MariaDB, PHP-FPM 8.4
- **Catégorie** : pile Web LEMP / dépannage
- **Tags** : `debian13`, `lemp`, `nginx`, `mariadb`, `php-fpm`, `diagnostic`

---

## Problème précis à résoudre

Diagnostiquer un défaut Nginx, PHP-FPM ou MariaDB sans exposer d'informations de configuration ou modifier les données à l'aveugle.

## 1. Hors-Production (Lab / Test / POC)

1. Tester la configuration Nginx :
   ```bash
   sudo nginx -t
   ```
   👉 Explication : indique la ligne en erreur.

2. Lire les journaux :
   ```bash
   sudo journalctl -u nginx -u mariadb -u php8.4-fpm --since '-30 minutes' --no-pager
   ```
   👉 Explication : un service arrêté ou une erreur de socket y apparaît.

3. Vérifier les ports et sockets :
   ```bash
   sudo ss -lntp
   ls -l /run/php/
   ```
   👉 Explication : `502 Bad Gateway` = PHP-FPM arrêté ou socket `fastcgi_pass` incorrect.

4. Tester MariaDB :
   ```bash
   sudo mariadb -e 'SHOW DATABASES;'
   ```
   👉 Explication : un `404` vient plutôt de `root` ou `server_name`; ne pas exposer les erreurs PHP détaillées aux visiteurs.

## 2. Production — Contrôles

Consigner symptômes, heure, changements récents, code HTTP, services, journaux et hypothèse vérifiée avant appliquer une correction.

## 3. Production — Sécurité

- Ne pas activer l'affichage public des erreurs PHP ou `phpinfo()`.
- Ne pas envoyer de secrets, contenu de base ou journaux complets dans un ticket public.
- Ne pas redémarrer ou supprimer des données avant sauvegarde et analyse d'impact.
- Restreindre les requêtes de diagnostic aux hôtes autorisés.

## Validation et retour arrière

- **Validation** : cause reproduite ou isolée, correction testée, service contrôlé et journaux sans nouvelle erreur.
- **Retour arrière** : restaurer le fichier précédent, exécuter `nginx -t`, puis recharger; ne pas supprimer base ni volume.

## Si le problème n'est pas résolu

- [Nginx — documentation de dépannage](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)
- [PHP-FPM — manuel PHP](https://www.php.net/manual/en/install.fpm.php)
- [Guide complet LEMP Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/02_Pile_LEMP_Debian_13_Nginx_PHP_MariaDB.md#7-depannage)

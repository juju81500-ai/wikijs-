# Fiche_Simple_-_VM_Rocky_9_Pile_Web_Sauvegarder_Retour.md

- **Environnement** : VM ou serveur Rocky Linux 9 hébergeant une application PHP avec MariaDB locale
- **OS / Version** : Rocky Linux 9 / RHEL 9; Nginx, PHP-FPM et MariaDB des dépôts actifs
- **Catégorie** : services web / sauvegarde
- **Tags** : `rocky9`, `nginx`, `php-fpm`, `mariadb`, `selinux`

---

## Problème précis à résoudre

Sauvegarder code, configuration et base, puis savoir revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Dump de la base :
   ```bash
   sudo mariadb-dump --single-transaction appdb > appdb.sql
   ```
   👉 Explication : Dump cohérent de la base (`appdb` est un exemple); à copier vers une cible indépendante.

2. Archiver code et config :
   ```bash
   sudo tar czf app-config.tar.gz /var/www/app /etc/nginx /etc/php-fpm.d
   ```
   👉 Explication : Archive code et configuration (chemins à adapter).

3. Tester la restauration dans un environnement isolé.
   👉 Explication : une sauvegarde non testée n'est pas fiable.

## 2. Production — Contrôles

Si une mise à jour échoue, restaurer configuration et base compatibles.

## 3. Production — Sécurité

- Dump et archives contiennent des secrets : chiffrer et restreindre l'accès.
- Ne pas rétrograder le serveur SQL avec des fichiers de données modifiés par une version plus récente.

## Validation et retour arrière

- **Validation** : sauvegarde indépendante créée et restauration testée.
- **Retour arrière** : restaurer config et base compatibles depuis la sauvegarde.

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet — étape 7](../../../../../02-Fiches-Completes/Rocky-Linux/9/Installation-Deploiement/23_Pile_Web_Rocky_Linux_9_Nginx_PHP_MariaDB.md#7-sauvegarder-et-revenir-en-arriere)

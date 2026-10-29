# Fiche_Simple_-_VM_Debian_13_LEMP_Preparer.md

- **Environnement** : VM ou serveur dédié Debian 13 Trixie pour une application Web PHP
- **OS / Version** : Debian 13; Nginx, PHP-FPM et MariaDB depuis les dépôts Debian
- **Catégorie** : pile Web LEMP / préparation
- **Tags** : `debian13`, `lemp`, `nginx`, `php-fpm`, `mariadb`, `preparation`

---

## Problème précis à résoudre

Préparer l'hébergement d'une application PHP sans exposer de service ni démarrer une migration non sauvegardée.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le DNS, l'IP et l'accès de secours :
   ```bash
   ip -br a
   getent hosts app.example.net
   ```
   👉 Explication : remplacer `app.example.net`; garder une console ou un SSH de secours avant tout changement.

2. Installer la pile :
   ```bash
   sudo apt update
   sudo apt install --yes nginx mariadb-server php-fpm php-mysql php-curl php-gd php-mbstring php-xml php-zip
   ```
   👉 Explication : Nginx, MariaDB et PHP-FPM avec les extensions courantes.

3. Vérifier les versions candidates :
   ```bash
   sudo apt-cache policy php-fpm mariadb-server
   ```
   👉 Explication : Debian 13 fournit PHP 8.4; ne pas lancer de `full-upgrade` à l'aveugle en production.

4. Vérifier que MariaDB n'est pas exposé :
   ```bash
   sudo ss -lntp | grep ':3306'
   ```
   👉 Explication : l'écoute doit être sur `127.0.0.1`.

## 2. Production — Contrôles

Faire approuver le nom DNS, les ressources, les responsables applicatifs, les fenêtres de maintenance, les paquets et la stratégie de sauvegarde/restauration.

## 3. Production — Sécurité

- Ne pas publier MariaDB sur Internet; limiter l'accès à l'hôte local par défaut.
- N'ouvrir que les ports nécessaires au service Web et à l'administration contrôlée.
- Ne pas installer les extensions PHP inutiles à l'application.
- Ne pas réaliser de `full-upgrade` en production sans sauvegarde vérifiée et plan de changement.

## Validation et retour arrière

- **Validation** : prérequis, paquets candidats, accès de secours et plan de sauvegarde sont documentés.
- **Arrêt** : ne pas exposer le service si le DNS, le filtrage ou la restauration ne sont pas définis.

## Si le problème n'est pas résolu

- [Debian — documentation](https://www.debian.org/doc/)
- [Guide complet LEMP Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/02_Pile_LEMP_Debian_13_Nginx_PHP_MariaDB.md#1-prerequis-et-preparation)

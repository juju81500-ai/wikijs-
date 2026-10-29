# Fiche_Simple_-_VM_Ubuntu_24.04_LEMP_Installer_Pile.md

- **Environnement** : VM Ubuntu Server 24.04 dédiée à une application Web PHP
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble); Nginx, PHP 8.3, MariaDB 10.11
- **Catégorie** : web / installation

---

## Problème précis à résoudre

Installer Nginx, MariaDB et PHP-FPM 8.3 et les activer.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo apt install nginx mariadb-server php8.3-fpm php8.3-cli \
     php8.3-mysql php8.3-curl php8.3-gd php8.3-mbstring php8.3-xml php8.3-zip
   ```
   👉 Explication : installe serveur Web, base et extensions PHP courantes.

2. Activer et démarrer les services :
   ```bash
   sudo systemctl enable --now nginx mariadb php8.3-fpm
   ```
   👉 Explication : ils démarreront aussi au boot.

3. Vérifier version, état et socket :
   ```bash
   php8.3 -v
   systemctl --no-pager status nginx mariadb php8.3-fpm
   ls -l /run/php/
   ```
   👉 Explication : le socket FPM doit exister dans `/run/php/`.

## 2. Production — Contrôles

Planifier les mises à jour de sécurité de la pile.

## 3. Production — Sécurité

- Installer uniquement les extensions PHP nécessaires à l'application.

## Validation et retour arrière

- **Validation** : trois services actifs et socket `php8.3-fpm.sock` présent.
- **Retour arrière** : `sudo systemctl disable --now nginx mariadb php8.3-fpm` puis `sudo apt remove` des paquets installés si la VM doit revenir à l'état initial.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [Ubuntu 24.04 — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet LEMP Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/20-pile-lemp-ubuntu-server-24-04-nginx-php83-mariadb#2-installer-la-pile)
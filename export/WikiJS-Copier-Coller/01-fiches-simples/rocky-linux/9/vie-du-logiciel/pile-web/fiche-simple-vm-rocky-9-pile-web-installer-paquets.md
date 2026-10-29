# Fiche_Simple_-_VM_Rocky_9_Pile_Web_Installer_Paquets.md

- **Environnement** : VM ou serveur Rocky Linux 9 hébergeant une application PHP avec MariaDB locale
- **OS / Version** : Rocky Linux 9 / RHEL 9; Nginx, PHP-FPM et MariaDB des dépôts actifs
- **Catégorie** : services web / installation

---

## Problème précis à résoudre

Installer Nginx, PHP-FPM et MariaDB puis activer les services.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo dnf install nginx php-fpm php-cli php-mysqlnd php-curl php-gd php-mbstring php-xml mariadb-server
   ```
   👉 Explication : Installe la pile depuis les dépôts Rocky approuvés.

2. Démarrer les services :
   ```bash
   sudo systemctl enable --now nginx mariadb php-fpm
   ```
   👉 Explication : Active et démarre les trois services.

3. Contrôler :
   ```bash
   systemctl --no-pager status nginx mariadb php-fpm
   php -v
   ls -l /run/php-fpm/
   ```
   👉 Explication : Contrôle l'état, la version PHP et le socket PHP-FPM (le chemin réel dépend de la configuration installée).

## 2. Production — Contrôles

Vérifier le chemin du socket PHP-FPM réellement fourni.

## 3. Production — Sécurité

- Aucun service ne doit être publié avant la configuration TLS et pare-feu.

## Validation et retour arrière

- **Validation** : les trois services sont actifs et le socket PHP-FPM existe.
- **Retour arrière** : `sudo systemctl disable --now nginx mariadb php-fpm` puis `sudo dnf remove` des paquets, ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet — étape 2](/02-fiches-completes/rocky-linux/9/installation-deploiement/23-pile-web-rocky-linux-9-nginx-php-mariadb#2-installer-les-paquets)
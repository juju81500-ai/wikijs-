# Fiche_Simple_-_VM_Rocky_9_Pile_Web_Prerequis_Versions.md

- **Environnement** : VM ou serveur Rocky Linux 9 hébergeant une application PHP avec MariaDB locale
- **OS / Version** : Rocky Linux 9 / RHEL 9; Nginx, PHP-FPM et MariaDB des dépôts actifs
- **Catégorie** : services web / prérequis
- **Tags** : `rocky9`, `nginx`, `php-fpm`, `mariadb`, `selinux`

---

## Problème précis à résoudre

Choisir les versions PHP, Nginx et MariaDB avant d'installer, sans les supposer.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les versions disponibles :
   ```bash
   cat /etc/rocky-release
   sudo dnf module list php
   sudo dnf info nginx php-fpm mariadb-server
   ```
   👉 Explication : Affiche la version de Rocky, les streams PHP proposés et les versions candidates des paquets.

2. Noter hostname/FQDN, IP stable, stockage, ports, sauvegardes et accès console.
   👉 Explication : ces éléments sont à figer avant l'installation.

## 2. Production — Contrôles

Valider le stream PHP par rapport à l'application à héberger.

## 3. Production — Sécurité

- N'utiliser que les dépôts Rocky approuvés.

## Validation et retour arrière

- **Validation** : versions candidates relevées et compatibles avec l'application.
- **Retour arrière** : aucun changement n'a été fait.

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet — étape 1](../../../../../02-Fiches-Completes/Rocky-Linux/9/Installation-Deploiement/23_Pile_Web_Rocky_Linux_9_Nginx_PHP_MariaDB.md#1-prerequis-et-choix-des-versions)

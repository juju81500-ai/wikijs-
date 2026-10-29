# Fiche_Simple_-_VM_Debian_12_iTop_Installer_Apache_PHP_MariaDB.md

- **Environnement** : VM Linux dédiée avec Apache, PHP 8.2 ou 8.3 et MariaDB 10.11 (serveur ITSM/CMDB)
- **OS / Version** : Debian 12 Bookworm (ou Ubuntu Server 24.04 LTS); iTop Community 3.3.0
- **Catégorie** : ITSM / CMDB / helpdesk
- **Tags** : `debian12`, `itop`, `itsm`, `cmdb`, `apache`, `mariadb`

---

## Problème précis à résoudre

Installer la pile web et base de données requise par iTop.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour l'index et contrôler les versions proposées :
   ```bash
   sudo apt update
   apt-cache policy apache2 mariadb-server php
   ```
   👉 Explication : vérifie que PHP est entre 8.2 et 8.4 avant installation.

2. Installer les paquets :
   ```bash
   sudo apt install apache2 mariadb-server graphviz \
     php libapache2-mod-php php-cli php-mysql php-json php-xml php-gd \
     php-zip php-curl php-soap php-mbstring php-apcu php-ldap php-imap
   ```
   👉 Explication : installe Apache, MariaDB et les extensions PHP demandées par iTop.

3. Activer le module de réécriture :
   ```bash
   sudo a2enmod rewrite
   ```
   👉 Explication : requis par l'application.

4. Démarrer et activer les services :
   ```bash
   sudo systemctl enable --now apache2 mariadb
   ```
   👉 Explication : les services démarrent au boot.

5. Vérifier PHP et ses modules :
   ```bash
   php -v
   php -m | grep -Ei 'mysqli|xml|gd|zip|curl|soap|mbstring|apcu|ldap|imap'
   ```
   👉 Explication : toutes les extensions requises doivent apparaître.

6. Configurer TLS et un VirtualHost Apache avec le nom DNS réel avant d'ouvrir l'application.
   👉 Explication : le HTTPS doit être actif pour les utilisateurs.

## 2. Production — Contrôles

Verrouiller les versions, planifier les mises à jour de sécurité d'Apache, PHP et MariaDB.

## 3. Production — Sécurité

- Exposer uniquement HTTPS; ne pas laisser la base accessible depuis le réseau.

## Validation et retour arrière

- **Validation** : Apache et MariaDB sont actifs et PHP charge les extensions.
- **Retour arrière** : en lab, désinstaller avec `sudo apt remove` les paquets ajoutés, uniquement si aucune donnée n'est présente.

## Si le problème n'est pas résolu

- [iTop — compatibilité](https://www.itophub.io/wiki/page?id=latest:install:requirements)
- [iTop — installation et mise à niveau](https://www.itophub.io/wiki/page?id=latest:install:start)
- [Guide complet](../../../../../02-Fiches-Completes/Transverses/Multi-OS/Installation-Deploiement/40_Deploiement_iTop_3.3_Debian12_Ubuntu2404.md#2-installer-apache-php-et-mariadb)

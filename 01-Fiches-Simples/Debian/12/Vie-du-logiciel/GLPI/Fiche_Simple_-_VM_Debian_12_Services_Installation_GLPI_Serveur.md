# 📄 VM_Debian_12_Services_Installation-GLPI-Serveur.md

- **Environnement** : VM (Debian 12 Bookworm)
- **OS / Version** : Debian 12 - Famille Debian
- **Catégorie** : Gestion de Parc & Helpdesk / GLPI
- **Tags** : `[debian12]`, `[glpi]`, `[apache2]`, `[mariadb]`, `[php8.2]`, `[helpdesk]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer la plateforme de gestion de parc et helpdesk GLPI sur Debian 12 avec la pile LAMP, configurer la base de données et sécuriser le répertoire d'installation web.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide de la pile LAMP minimale :
   `apt-get update && apt-get install -y apache2 mariadb-server php php-mysql libapache2-mod-php wget tar`
   👉 Explication : Télécharge et installe les composants Web et base de données de base.

2. Extraction de l'archive GLPI :
   `tar -xzf glpi-10.0.12.tgz -C /var/www/html/`
   👉 Explication : Extrait le code source officiel de GLPI directement dans la racine du serveur web.

3. Attribution globale des droits à l'utilisateur web :
   `chown -R www-data:www-data /var/www/html/glpi`
   👉 Explication : Accorde la propriété de tous les fichiers à Apache pour permettre l'assistant d'installation web.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installation complète de toutes les extensions PHP requises :
   `apt-get install -y apache2 mariadb-server php8.2 php8.2-curl php8.2-gd php8.2-mbstring php8.2-xml php8.2-intl php8.2-ldap php8.2-mysqli php8.2-xmlrpc php8.2-zip php8.2-bz2 php8.2-gmp`
   👉 Explication : Installe l'ensemble des modules PHP nécessaires au fonctionnement des fonctionnalités avancées.

2. Création et sécurisation de la base de données MariaDB :
   `mysql -e "CREATE DATABASE glpidb CHARACTER SET utf8mb4;"`
   👉 Explication : Prépare la base de données glpidb pour le service.

3. Exécution de l'assistant d'installation GLPI en ligne de commande :
   `php /var/www/html/glpi/bin/console db:install --db-name=glpidb --no-interaction`
   👉 Explication : Initialise le schéma de base de données GLPI sans passer par l'interface graphique.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Relocalisation des dossiers sensibles (files, config, log) HORS du VirtualHost web racine :
   `mkdir -p /var/glpi/{config,files,log} && mv /var/www/html/glpi/config/* /var/glpi/config/`
   👉 Explication : Sort les données de configuration et fichiers joints du chemin d'accès HTTP direct.

2. Configuration du fichier de redirection interne :
   `echo "<?php define('GLPI_CONFIG_DIR', '/var/glpi/config');" > /var/www/html/glpi/inc/downstream.php`
   👉 Explication : Indique au système l'emplacement sécurisé des dossiers déplacés.

3. Restauration des permissions système strictes sur l'arborescence :
   `chown -R root:root /var/www/html/glpi && chown -R www-data:www-data /var/glpi`
   👉 Explication : Empêche le serveur web d'écrire ou de modifier les fichiers de code source.
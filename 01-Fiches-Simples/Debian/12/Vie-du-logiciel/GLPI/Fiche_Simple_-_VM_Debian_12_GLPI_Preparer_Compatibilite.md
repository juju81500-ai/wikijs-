# Fiche_Simple_-_VM_Debian_12_GLPI_Preparer_Compatibilite.md

- **Environnement** : VM Debian dédiée pour GLPI avec serveur Web, PHP-FPM et MariaDB
- **OS / Version** : Debian 12 ou 13; version GLPI maintenue à confirmer
- **Catégorie** : GLPI / préparation et compatibilité
- **Tags** : `debian12`, `debian13`, `glpi`, `itsm`, `compatibilite`

---

## Problème précis à résoudre

Préparer le déploiement GLPI en validant les versions supportées, le stockage, le réseau et la stratégie de reprise avant installation.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter la matrice officielle de la version GLPI retenue (PHP, extensions, bases supportées), puis installer la pile :
   ```bash
   sudo apt update
   sudo apt install --yes nginx mariadb-server php-fpm php-mysql php-curl php-gd php-intl php-mbstring php-xml php-zip
   ```
   👉 Explication : installe Nginx, MariaDB et PHP-FPM avec les extensions courantes.

2. Vérifier la version de PHP et les extensions :
   ```bash
   php -v
   php -m | grep -Ei 'curl|gd|intl|mbstring|mysqli|xml|zip|bz2|ldap|opcache'
   ```
   👉 Explication : installer les extensions supplémentaires exigées par la version de GLPI retenue.

3. Contrôler DNS, espace disque et préparer la sauvegarde :
   ```bash
   getent hosts glpi.example.net
   df -h /var/www
   ```
   👉 Explication : prévoir TLS, stockage des documents, fenêtre de maintenance; ne jamais exposer le répertoire de données ni la configuration au Web.

## 2. Production — Contrôles

Faire approuver versions, ressources, stockage persistant, DNS/TLS, dépendances, sauvegardes, responsabilités et fenêtre de déploiement.

## 3. Production — Sécurité

- Ne pas installer une version future ou non confirmée.
- Ne pas exposer répertoire de données ou fichiers de configuration au serveur Web.
- Ne pas publier MariaDB sur Internet.
- Ne pas commencer avant d'avoir défini la restauration conjointe de la base et des fichiers.

## Validation et retour arrière

- **Validation** : version supportée confirmée, compatibilité documentée et plan de restauration prêt.
- **Arrêt** : reporter si la version ou ses dépendances ne sont pas explicitement supportées.

## Si le problème n'est pas résolu

- [GLPI — documentation](https://glpi-install.readthedocs.io/en/latest/)
- [GLPI — prérequis](https://glpi-install.readthedocs.io/en/latest/prerequisites.html)
- [Guide complet GLPI Debian](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/03_Helpdesk_ITSM_GLPI_11_12_Debian_12_13.md)

# Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Preparer_Serveur.md

- **Environnement** : VM Ubuntu Server 26.04 dédiée à LibreNMS (Nginx, PHP-FPM, MariaDB, SNMP)
- **OS / Version** : Ubuntu Server 26.04 LTS; LibreNMS 26.10.2; PHP 8.5
- **Catégorie** : supervision / préparation
- **Tags** : `ubuntu2604`, `librenms`, `snmpv3`, `nginx`, `mariadb`

---

## Problème précis à résoudre

Vérifier que le serveur et les versions PHP disponibles conviennent avant d'installer LibreNMS.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les versions disponibles :
   ```bash
   cat /etc/os-release
   apt-cache policy php-fpm mariadb-server
   ```
   👉 Explication : Contrôle la version d'Ubuntu et les versions PHP/MariaDB proposées par les dépôts approuvés (PHP 8.5 recommandé, 8.4 minimum).

2. Contrôler l'heure :
   ```bash
   timedatectl
   ```
   👉 Explication : Affiche fuseau et synchronisation de l'heure; le fuseau du système et de PHP doivent être cohérents.

3. Lister par écrit DNS, TLS, NTP, disque dédié RRD/logs, sauvegardes et appareils autorisés à superviser.
   👉 Explication : évite de superviser des équipements hors périmètre.

## 2. Production — Contrôles

Valider le nom DNS, le certificat TLS, le stockage et la liste des équipements avec les responsables réseau.

## 3. Production — Sécurité

- L'interface LibreNMS n'est pas sécurisée pour une exposition Internet par défaut : prévoir reverse proxy HTTPS/SSO ou accès limité au réseau de supervision.
- Ne pas ajouter de dépôt PHP tiers non validé.

## Validation et retour arrière

- **Validation** : PHP 8.4 ou 8.5 disponible depuis les dépôts approuvés et prérequis écrits.
- **Retour arrière** : aucun changement n'a été fait.

## Si le problème n'est pas résolu

- [LibreNMS — Installation](https://docs.librenms.org/Installation/Install-LibreNMS/)
- [Guide complet — étape 1](../../../../../02-Fiches-Completes/Ubuntu/26.04/Installation-Deploiement/46_Deploiement_LibreNMS_26.10.2_Ubuntu_26.04.md#1-preparer-le-serveur)

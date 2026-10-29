# Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Installer_Paquets.md

- **Environnement** : VM Ubuntu Server 26.04 dédiée à LibreNMS (Nginx, PHP-FPM, MariaDB, SNMP)
- **OS / Version** : Ubuntu Server 26.04 LTS; LibreNMS 26.10.2; PHP 8.5
- **Catégorie** : supervision / paquets
- **Tags** : `ubuntu2604`, `librenms`, `snmpv3`, `nginx`, `mariadb`

---

## Problème précis à résoudre

Installer les paquets système, PHP, MariaDB, Nginx et SNMP requis par LibreNMS.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour l'index :
   ```bash
   sudo apt update
   ```
   👉 Explication : Rafraîchit l'index des paquets.

2. Installer les dépendances :
   ```bash
   sudo apt install acl curl fping git mariadb-client mariadb-server mtr-tiny \
     nginx-full nmap php-cli php-curl php-fpm php-gd php-gmp php-mbstring \
     php-mysql php-snmp php-xml php-zip python3-command-runner python3-dotenv \
     python3-pip python3-psutil python3-pymysql python3-redis python3-setuptools \
     python3-systemd rrdtool snmp snmpd traceroute unzip whois
   ```
   👉 Explication : Installe la liste officielle des dépendances reprise du guide.

3. Vérifier PHP et ses modules :
   ```bash
   php -v
   php -m | grep -Ei "curl|gd|gmp|mbstring|mysql|snmp|xml|zip"
   ```
   👉 Explication : `php -v` doit afficher 8.4 ou 8.5 et les modules requis doivent être listés.

## 2. Production — Contrôles

Définir la timezone du système et de PHP de façon cohérente.

## 3. Production — Sécurité

- N'installer que des paquets des dépôts Ubuntu approuvés.

## Validation et retour arrière

- **Validation** : les paquets sont installés et PHP 8.4/8.5 expose les modules requis.
- **Retour arrière** : `sudo apt remove` des paquets ajoutés si le serveur est abandonné; sinon restaurer le snapshot.

## Si le problème n'est pas résolu

- [LibreNMS — Installation](https://docs.librenms.org/Installation/Install-LibreNMS/)
- [Guide complet — étape 2](../../../../../02-Fiches-Completes/Ubuntu/26.04/Installation-Deploiement/46_Deploiement_LibreNMS_26.10.2_Ubuntu_26.04.md#2-installer-les-paquets-requis)

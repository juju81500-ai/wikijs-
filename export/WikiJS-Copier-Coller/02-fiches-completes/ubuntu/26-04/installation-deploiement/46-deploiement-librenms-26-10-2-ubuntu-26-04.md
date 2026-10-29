# Déployer LibreNMS 26.10.2 sur Ubuntu Server 26.04

- **OS / Version** : Ubuntu Server 26.04 LTS; LibreNMS 26.10.2; PHP 8.5
- **Type de fiche** : Installation/Déploiement
- **Environnement** : VM Linux dédiée, Nginx, PHP-FPM, MariaDB et SNMP
- **Machine ciblée** : Serveur de supervision réseau
- **Catégorie** : Supervision / SNMP

## 1. Préparer le serveur

Fiche simple : [préparer le serveur LibreNMS](/01-fiches-simples/ubuntu/26-04/vie-du-logiciel/librenms/fiche-simple-vm-ubuntu-26-04-librenms-preparer-serveur).

LibreNMS recommande PHP 8.5 (minimum 8.4). Vérifier que la version est disponible depuis les dépôts Ubuntu approuvés avant installation; ne pas ajouter de dépôt tiers PHP non validé. Prévoir DNS, TLS, NTP, disque dédié aux RRD/logs, sauvegardes et liste des appareils que l'organisation est autorisée à superviser.

L'interface de LibreNMS n'est pas sécurisée pour exposition Internet par défaut. Prévoir un reverse proxy HTTPS/SSO ou un accès limité au réseau de supervision. Utiliser exclusivement des secrets SNMPv3 en lecture seule lorsque les équipements le permettent.

## 2. Installer les paquets requis

Fiche simple : [installer les paquets requis LibreNMS](/01-fiches-simples/ubuntu/26-04/vie-du-logiciel/librenms/fiche-simple-vm-ubuntu-26-04-librenms-installer-paquets).

```bash
sudo apt update
apt-cache policy php-fpm mariadb-server
sudo apt install acl curl fping git mariadb-client mariadb-server mtr-tiny \
  nginx-full nmap php-cli php-curl php-fpm php-gd php-gmp php-mbstring \
  php-mysql php-snmp php-xml php-zip python3-command-runner python3-dotenv \
  python3-pip python3-psutil python3-pymysql python3-redis python3-setuptools \
  python3-systemd rrdtool snmp snmpd traceroute unzip whois
```

Vérifier que `php -v` affiche 8.4 ou 8.5 et que les modules PHP requis sont actifs. Définir la timezone du système et de PHP de façon cohérente.

## 3. Créer le compte de service et installer le code

Fiche simple : [créer le compte de service et installer le code LibreNMS](/01-fiches-simples/ubuntu/26-04/vie-du-logiciel/librenms/fiche-simple-vm-ubuntu-26-04-librenms-compte-service-code).

```bash
sudo useradd librenms -d /opt/librenms -M -r -s "$(which bash)"
cd /opt
sudo git clone --branch 26.10.2 --depth 1 https://github.com/librenms/librenms.git
sudo chown -R librenms:librenms /opt/librenms
sudo chmod 771 /opt/librenms
sudo setfacl -d -m g::rwx /opt/librenms/rrd /opt/librenms/logs \
  /opt/librenms/bootstrap/cache /opt/librenms/storage
sudo setfacl -R -m g::rwx /opt/librenms/rrd /opt/librenms/logs \
  /opt/librenms/bootstrap/cache /opt/librenms/storage
```

Installer les dépendances PHP avec le compte LibreNMS non-root :

```bash
sudo -u librenms /opt/librenms/scripts/composer_wrapper.php install --no-dev
```

## 4. Configurer MariaDB

Fiche simple : [configurer MariaDB pour LibreNMS](/01-fiches-simples/ubuntu/26-04/vie-du-logiciel/librenms/fiche-simple-vm-ubuntu-26-04-librenms-configurer-mariadb).

Dans `/etc/mysql/mariadb.conf.d/50-server.cnf`, ajouter sous `[mariadbd]` :

```ini
innodb_file_per_table=1
lower_case_table_names=0
```

Redémarrer MariaDB, puis créer une base et un compte dédiés :

```bash
sudo systemctl enable --now mariadb
sudo systemctl restart mariadb
sudo mariadb
```

Dans MariaDB :

```sql
CREATE DATABASE librenms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'librenms'@'localhost' IDENTIFIED BY '<SECRET_LONG_ET_UNIQUE>';
GRANT ALL PRIVILEGES ON librenms.* TO 'librenms'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Remplacer le secret par une valeur aléatoire du coffre et ne pas accorder à LibreNMS d'accès MariaDB distant.

## 5. Configurer PHP-FPM et Nginx

Fiche simple : [configurer PHP-FPM et Nginx pour LibreNMS](/01-fiches-simples/ubuntu/26-04/vie-du-logiciel/librenms/fiche-simple-vm-ubuntu-26-04-librenms-configurer-php-fpm-nginx).

Créer un pool dédié à partir du pool par défaut :

```bash
sudo cp /etc/php/8.5/fpm/pool.d/www.conf /etc/php/8.5/fpm/pool.d/librenms.conf
sudoedit /etc/php/8.5/fpm/pool.d/librenms.conf
```

Dans ce fichier, renommer la section `[www]` en `[librenms]` et définir les paramètres suivants, en supprimant toute valeur conflictuelle dupliquée :

```ini
user = librenms
group = librenms
listen = /run/php-fpm-librenms.sock
listen.owner = www-data
listen.group = www-data
listen.mode = 0660
```

Configurer la timezone dans `/etc/php/8.5/fpm/php.ini` et `/etc/php/8.5/cli/php.ini`, puis redémarrer FPM.

Créer `/etc/nginx/conf.d/librenms.conf` en remplaçant le nom DNS :

```nginx
server {
  listen 80;
  server_name librenms.example.net;
  root /opt/librenms/html;
  index index.php;
  charset utf-8;

  location / {
    try_files $uri $uri/ /index.php?$query_string;
  }

  location ~ [^/]\.php(/|$) {
    fastcgi_pass unix:/run/php-fpm-librenms.sock;
    fastcgi_split_path_info ^(.+\.php)(/.+)$;
    include fastcgi.conf;
  }

  location ~ /\. {
    deny all;
  }
}
```

Cette configuration écoute en HTTP uniquement pour le contrôle initial; ne pas exposer l'application ainsi. Mettre ensuite le TLS au reverse proxy ou configurer un vhost HTTPS approuvé avant accès utilisateur. Tester puis redémarrer :

```bash
sudo nginx -t
sudo systemctl restart php8.5-fpm nginx

Ne pas ouvrir le port HTTP public avant de configurer HTTPS via le mécanisme de certificat approuvé. Restreindre l'administration au réseau de gestion ou au reverse proxy.

## 6. Programmer les tâches et le journal

Fiche simple : [programmer les tâches et le journal LibreNMS](../../../../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/LibreNMS/Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Taches_Journal.md).

```bash
sudo ln -s /opt/librenms/lnms /usr/bin/lnms
sudo cp /opt/librenms/misc/lnms-completion.bash /etc/bash_completion.d/
sudo cp /opt/librenms/dist/librenms.cron /etc/cron.d/librenms
sudo cp /opt/librenms/dist/librenms-scheduler.service \
  /opt/librenms/dist/librenms-scheduler.timer /etc/systemd/system/
sudo systemctl enable --now librenms-scheduler.timer
sudo cp /opt/librenms/misc/librenms.logrotate /etc/logrotate.d/librenms
```

## 7. Assistant, SNMP et recette

Fiche simple : [assistant, SNMP et recette LibreNMS](../../../../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/LibreNMS/Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Assistant_SNMP_Recette.md).

Ouvrir `https://librenms.example.net/install` depuis le réseau d'administration, terminer l'assistant avec la base dédiée puis vérifier le propriétaire de `config.php`. Ajouter `localhost`, puis un appareil de test explicitement autorisé.

Pour les équipements, préférer SNMPv3 `authPriv` lecture seule. Définir l'adresse du serveur LibreNMS comme source autorisée sur chaque appareil et n'ouvrir UDP/161 que depuis le poller. Éviter la communauté SNMPv2c `public` et ne pas activer les écritures SNMP.

Valider l'installation :

```bash
sudo -u librenms /opt/librenms/validate.php
sudo systemctl --no-pager status nginx php8.5-fpm mariadb librenms-scheduler.timer
```

Confirmer collecte, graphes, journaux, alertes de test et fuseau horaire avant d'ajouter d'autres cibles.

## 8. Sauvegarde et mises à jour

Fiche simple : [sauvegarde et mises à jour LibreNMS](../../../../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/LibreNMS/Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Sauvegarde_Mises_A_Jour.md).

Sauvegarder la base MariaDB, `/opt/librenms/.env` (il contient `APP_KEY`), configuration Nginx/PHP/SNMP et chemins RRD/logs requis. Chiffrer et tester une restauration hors production.

Avant mise à jour, lire les notes de version LibreNMS, sauvegarder et utiliser la procédure officielle. Après mise à niveau, exécuter `validate.php`, vérifier poller/scheduler et confirmer une collecte complète.

## Sources

- [LibreNMS — Installation](https://docs.librenms.org/Installation/Install-LibreNMS/)
- [LibreNMS — Release 26.10.2](https://github.com/librenms/librenms/releases/tag/26.10.2)
- [LibreNMS — SNMPv3](https://docs.librenms.org/Support/SNMP-Configuration-Examples/)
- [LibreNMS — Ajouter un appareil](https://docs.librenms.org/Support/Adding-a-Device/)
- [LibreNMS — Validation de l'installation](https://docs.librenms.org/Support/Install-Validation/)
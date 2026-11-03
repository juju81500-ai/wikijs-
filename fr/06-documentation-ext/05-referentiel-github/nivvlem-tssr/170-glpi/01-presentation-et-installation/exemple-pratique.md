---
title: "TP – Installation de l’environnement GLPI"
description: "+----------------+          +----------------+"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Installation de l’environnement GLPI
## 🧾 Prérequis

| Composant       | Version / Type                |
| --------------- | ----------------------------- |
| Hyperviseur     | VMware Workstation            |
| OS serveur GLPI | Debian 12 NetInstall 64 bits  |
| AD              | Windows Server 2019 graphique |
| Firewall        | pfSense                       |
| Client          | Windows 10 Sysprep            |
| Réseau          | 192.168.1.0/24 sur VMNet 18   |

---

## 🏗️ Architecture cible

```text
+----------------+          +----------------+
| srv-glpi      |          | srv-CD1 (ADDS) |
| 192.168.1.10   |          | 192.168.1.11    |
+----------------+          +----------------+
        |                         |
        +----------- pfSense (LAN 192.168.1.254 / WAN DHCP bridgé)
                                |
                            Internet
```

---

## 🔧 Étapes détaillées

### 1️⃣ Installation du serveur GLPI

#### Création de la VM

- Debian 12 64 bits NetInstall
- 4 Go RAM, 1 CPU, 40 Go HDD
- Installation en **bridge DHCP** temporairement
- Après install : passage en **VMNet 18** (LAN interne)
- DNS : `srv-CD1`
- Services installés : **SSH**, **environnement graphique léger**

### 2️⃣ Installation du domaine ADDS (srv-CD1)

- Déployer Windows Server 2019
- Créer le domaine `Olympus.gr`
- Configurer le DNS interne
- Ne pas créer d’OU ni d’utilisateurs pour le moment

### 3️⃣ Installation d’un client W10

- Déployer un client à partir de l’image Sysprep
- Ajouter le client au domaine `Olympus.gr`

### 4️⃣ Installation du firewall pfSense

#### Création de la VM

- OS type Other > FreeBSD 64-bit
- 512 Mo RAM, 1 CPU, 20 Go disque

#### Configuration réseau

- Carte 1 : bridge DHCP (WAN)
- Carte 2 : VMNet 18 (LAN)

#### Installation pfSense

- Interface em0 : WAN DHCP
- Interface em1 : LAN 192.168.1.254/24
- Accès web pfSense et configuration de base
- **Créer une règle de firewall permissive temporaire (any to any)** pour faciliter l’installation

#### Tests

```bash
# Depuis srv-CD01
nslookup ftp.fr.debian.org

# Depuis srv-glpi
ping ftp.fr.debian.org
```

---

## 🚀 Installation de GLPI

### Préparation du serveur Debian

#### Installation des paquets requis

```bash
apt update && apt upgrade -y

apt install task-web-server mariadb-server \
php7.3 php7.3-mysql php7.3-mbstring php7.3-curl php7.3-gd \
php7.3-xml php7.3-ldap php7.3-xmlrpc php7.3-imap php7.3-intl \
php7.3-zip php7.3-bz2 php-apcu-bc php-cas

systemctl restart apache2
```

### Configuration de MariaDB

```bash
mysql_secure_installation
# Réponses recommandées :
# Root password : n
# Remove anonymous users : Y
# Disallow root login remotely : Y
# Remove test database : Y
# Reload privilege tables : Y
```

#### Création de la base GLPI

```bash
mysql -u root -p
CREATE DATABASE glpidata;
GRANT ALL PRIVILEGES ON glpidata.* TO 'root'@'localhost' IDENTIFIED BY 'MotDePasseFort';
SHOW GRANTS FOR 'root'@'localhost';
```

### Téléchargement et déploiement de GLPI

#### Transfert de l’archive

- Transférer via **WinSCP** sur `/var/www/`

#### Installation

```bash
cd /var/www

# Exemple pour GLPI version 10.0.18
tar xvzf glpi-10.0.18.tar.gz
rm glpi-10.0.18.tar.gz

chown -R root:root glpi
```

---

## ⚙️ Configuration avancée (sécurisation)

### Déplacement des fichiers GLPI

```bash
mkdir /etc/glpi

# Créer le fichier /etc/glpi/local_define.php
# Exemple :
<?php
    define('GLPI_VAR_DIR', '/var/lib/glpi');
    define('GLPI_LOG_DIR', '/var/log/glpi');
?>
```

### Préparation des répertoires

```bash
mkdir /var/lib/glpi
cp -R /var/www/glpi/files/* /var/lib/glpi

mkdir /var/log/glpi

chown -R www-data /etc/glpi
chown -R www-data /var/lib/glpi
chown -R www-data /var/log/glpi

# Marketplace
chown -R www-data /var/www/glpi/marketplace
```

### Création de downstream.php

```bash
nano /var/www/glpi/inc/downstream.php

# Contenu :
<?php
    define('GLPI_CONFIG_DIR', '/etc/glpi/');
    if (file_exists(GLPI_CONFIG_DIR . '/local_define.php')) {
        require_once GLPI_CONFIG_DIR . '/local_define.php';
    }
?>
```

### Publication du site GLPI

```bash
nano /etc/apache2/sites-available/glpi.olympus.gr.conf

# Exemple :
<VirtualHost *:80>
    DocumentRoot /var/www/glpi
    ServerName glpi.olympus.gr

    <Directory /var/www/glpi>
        AllowOverride none
        Options Indexes FollowSymLinks MultiViews
        Require all granted
    </Directory>
</VirtualHost>

# Activation
a2ensite glpi.olympus.gr.conf
systemctl reload apache2.service
```

### Configuration DNS

```bash
# Changer le hostname de srv-glpi
hostnamectl set-hostname srv-glpi.olympus.gr

# Modifier /etc/hosts
127.0.1.1 srv-glpi srv-glpi.olympus.gr

# Sur srv-CD1 (AD)
# Créer un enregistrement A pour srv-glpi
# Créer un CNAME "glpi" pointant vers l’enregistrement A
```

### Test d’accès

- Depuis le client W10 :

```text
http://glpi.olympus.gr
```

---

## ✅ À retenir pour les révisions

- L’installation de GLPI repose sur une **infrastructure réseau propre** (pfSense + AD)
- **MariaDB** doit être correctement sécurisée
- Les fichiers GLPI doivent être déplacés et configurés selon les bonnes pratiques
- Il est essentiel de :
    - **Supprimer les droits inutiles**
    - **Restreindre les accès web**
    - Utiliser un **FQDN correctement configuré**

---

## 📌 Bonnes pratiques professionnelles

- Préparer un **document d’installation standardisé**
- Mettre en place une **supervision basique** (service Apache, MariaDB)
- Restreindre l’accès aux **ports ouverts sur pfSense**
- Protéger l’accès SSH au serveur GLPI
- Sauvegarder **régulièrement la base** et `/var/lib/glpi`
- Planifier les **mises à jour de GLPI** (versions stables uniquement)

---

## Commandes utiles

```bash
# MariaDB Secure Install
mysql_secure_installation

# Création DB GLPI
mysql -u root -p
CREATE DATABASE glpidata;
GRANT ALL PRIVILEGES ON glpidata.* TO 'root'@'localhost' IDENTIFIED BY 'MotDePasseFort';

# GLPI Directory permissions
chown -R www-data /etc/glpi
chown -R www-data /var/lib/glpi
chown -R www-data /var/log/glpi

# Apache reload
systemctl reload apache2.service
```
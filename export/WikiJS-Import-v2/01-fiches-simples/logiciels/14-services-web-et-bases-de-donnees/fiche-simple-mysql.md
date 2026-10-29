---
title: "MySQL"
description: "Installer MySQL 8.0 sur Debian 12 depuis le dépôt officiel, créer une base et un compte de test, puis le préparer pour la production : écoute limitée, compte applicatif restreint à son serveur, comptes nettoyés, sauvegarde testée. Les tests ne se font que sur votre propre serveur."
published: true
date: 2026-10-29T12:26:04Z
tags: ["[debian-12]", "[mysql]", "[base-de-donnees]", "[sauvegarde]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:26:04Z
dateModified: 2026-10-29T12:26:04Z
---

# 📄 MySQL

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : MySQL 8.0.x (dépôt APT officiel MySQL, Debian 12 ne fournit pas MySQL dans ses dépôts ; version à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données
- **Tags** : `[debian-12]`, `[mysql]`, `[base-de-donnees]`, `[sauvegarde]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer MySQL 8.0 sur Debian 12 depuis le dépôt officiel, créer une base et un compte de test, puis le préparer pour la production : écoute limitée, compte applicatif restreint à son serveur, comptes nettoyés, sauvegarde testée. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Ajout du dépôt officiel MySQL et installation du serveur :
```bash
sudo apt update
sudo apt install -y curl gnupg lsb-release
curl -LO https://dev.mysql.com/get/mysql-apt-config_0.8.33-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.33-1_all.deb
sudo apt update
sudo apt install -y mysql-server
mysql --version
systemctl status mysql --no-pager
```
👉 Explication : Le paquet `mysql-apt-config` ajoute le dépôt MySQL. Le numéro `0.8.33-1` est celui du paquet de configuration au moment de la rédaction : à vérifier sur la page de téléchargement MySQL. L'installation demande un mot de passe `root` : le conserver dans le coffre-fort du pack.

2. Sécurisation initiale de l'installation :
```bash
sudo mysql_secure_installation
```
👉 Explication : L'assistant propose de supprimer les comptes anonymes, la base de test et les connexions `root` distantes. En lab, répondre `Y` à chaque question.

3. Création d'une base et d'un compte de test :
```bash
LAB_PASS=$(openssl rand -base64 24)
sudo mysql -u root -p -e "CREATE DATABASE essai_lab CHARACTER SET utf8mb4; CREATE USER 'labuser'@'localhost' IDENTIFIED BY '$LAB_PASS'; GRANT ALL PRIVILEGES ON essai_lab.* TO 'labuser'@'localhost';"
echo "$LAB_PASS"
```
👉 Explication : Crée la base `essai_lab` et le compte `labuser` limité à cette base. Le mot de passe s'affiche une seule fois. `-p` demande le mot de passe `root` défini à l'installation.

4. Test de connexion :
```bash
mysql -u labuser -p essai_lab -e "SELECT CURRENT_USER(), VERSION();"
```
👉 Explication : Doit renvoyer `labuser@localhost` et la version 8.0.x.

---

## ⚡ 2. Production — Façon Simplifiée
1. Écoute réseau limitée à l'adresse du serveur de base :
```bash
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
sudo systemctl restart mysql
sudo ss -ltnp | grep 3306
```
Dans la section `[mysqld]`, régler `bind-address = 192.168.10.20` (adresse du serveur de base, à adapter).
👉 Explication : La directive `bind-address` limite l'écoute à l'interface réseau voulue. `ss` confirme le port 3306.

2. Création du compte applicatif, limité à son serveur et à sa base :
```bash
APP_PASS=$(openssl rand -base64 24)
sudo mysql -u root -p -e "CREATE DATABASE base_appli CHARACTER SET utf8mb4; CREATE USER 'appli'@'192.168.10.21' IDENTIFIED BY '$APP_PASS'; GRANT SELECT, INSERT, UPDATE, DELETE ON base_appli.* TO 'appli'@'192.168.10.21';"
echo "$APP_PASS"
```
👉 Explication : Le compte `appli` ne peut se connecter que depuis `192.168.10.21` (serveur applicatif, à adapter) et n'a que les droits de données sur `base_appli`. Copier le mot de passe dans le coffre-fort du pack.

3. Ouverture du pare-feu pour l'application et l'administration SSH :
```bash
sudo apt install -y ufw
sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow from 192.168.10.21 to any port 3306 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Le port 3306 n'est ouvert qu'au serveur applicatif. SSH est ouvert avant l'activation du pare-feu.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Liste des comptes et suppression des comptes anonymes :
```bash
sudo mysql -u root -p -e "SELECT user, host, plugin FROM mysql.user;"
sudo mysql -u root -p -e "DROP USER IF EXISTS ''@'localhost';"
```
👉 Explication : La première commande liste chaque compte avec son hôte et son plugin d'authentification. Tout compte `%` (accessible de partout) doit être justifié ou supprimé. La seconde supprime le compte anonyme local s'il existe.

2. Sauvegarde logique cohérente :
```bash
sudo install -d -m 700 /root/sauvegardes
sudo mysqldump -u root -p --single-transaction --routines --triggers --all-databases | gzip | sudo tee /root/sauvegardes/mysql-$(date +%F).sql.gz > /dev/null
sudo chmod 600 /root/sauvegardes/mysql-*.sql.gz
sudo ls -l /root/sauvegardes
```
👉 Explication : `--single-transaction` produit une copie cohérente des tables InnoDB sans les bloquer. Le fichier est compressé et réservé à `root`. Il doit être copié hors du serveur et restauré une fois sur une machine de test.

3. Restauration de contrôle sur une machine de test, jamais sur la production :
```bash
gunzip -c /root/sauvegardes/mysql-$(date +%F).sql.gz | sudo mysql -u root -p
sudo mysql -u root -p -e "SHOW DATABASES;"
```
👉 Explication : Vérifie que la sauvegarde est exploitable. Une sauvegarde non restaurée n'est pas une sauvegarde validée.

4. Contrôle des journaux de service :
```bash
sudo journalctl -u mysql -n 50 --no-pager
```
👉 Explication : Sous Debian, le journal de MySQL est consulté via `journalctl`. Les échecs d'authentification et les redémarrages inattendus doivent être remontés au responsable sécurité.

---
# 📄 MariaDB

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : MariaDB 10.11.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données

## 🎯 Problème précis à résoudre
Installer MariaDB sur Debian 12, créer une base et un compte de test, puis le préparer pour un usage en production : accès restreint à l'application cliente, comptes nettoyés, sauvegarde testée. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du serveur et du client :
```bash
sudo apt update
sudo apt install -y mariadb-server
mariadb --version
systemctl status mariadb --no-pager
```
👉 Explication : Installe MariaDB depuis les dépôts Debian 12. `systemctl status` doit afficher `Active: active (running)`, le service démarre seul avec le paquet.

2. Sécurisation initiale de l'installation (assistant Debian) :
```bash
sudo mysql_secure_installation
```
👉 Explication : L'assistant propose de supprimer les comptes anonymes, de désactiver la connexion `root` distante et de supprimer la base de test. Sur Debian, `root` s'authentifie par le socket Unix (compte système `root`) : aucun mot de passe `root` n'est donc à retenir pour l'administration locale. Répondre `Y` à toutes les questions en lab.

3. Création d'une base et d'un utilisateur de test lié au compte système `labuser` :
```bash
sudo useradd -m labuser
sudo mariadb -e "CREATE DATABASE essai_lab CHARACTER SET utf8mb4; CREATE USER 'labuser'@'localhost' IDENTIFIED VIA unix_socket; GRANT ALL PRIVILEGES ON essai_lab.* TO 'labuser'@'localhost'; FLUSH PRIVILEGES;"
```
👉 Explication : Crée la base `essai_lab` et un compte MariaDB `labuser` qui s'authentifie via le socket Unix : il faut être connecté au système sous l'utilisateur `labuser` pour s'y connecter, sans mot de passe.

4. Test de connexion :
```bash
sudo -u labuser mariadb essai_lab -e "SELECT CURRENT_USER(), VERSION();"
sudo mariadb -e "SHOW DATABASES;"
```
👉 Explication : La première commande doit renvoyer `labuser@localhost`. La seconde liste les bases, dont `essai_lab`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Écoute réseau limitée à l'adresse du serveur de base :
```bash
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
sudo systemctl restart mariadb
sudo ss -ltnp | grep 3306
```
Dans la section `[mysqld]`, régler `bind-address = 192.168.10.20` (adresse du serveur de base, à adapter) et ajouter la ligne `skip-name-resolve`.
👉 Explication : Par défaut, MariaDB écoute sur `127.0.0.1` uniquement. Ici l'écoute est limitée à l'interface réseau voulue. `ss` confirme le port 3306 et l'adresse d'écoute.

2. Création du compte applicatif, limité à son serveur et à sa base :
```bash
APP_PASS=$(openssl rand -base64 24)
sudo mariadb -e "CREATE DATABASE base_appli CHARACTER SET utf8mb4; CREATE USER 'appli'@'192.168.10.21' IDENTIFIED BY '$APP_PASS'; GRANT SELECT, INSERT, UPDATE, DELETE ON base_appli.* TO 'appli'@'192.168.10.21'; FLUSH PRIVILEGES;"
echo "$APP_PASS"
```
👉 Explication : Le mot de passe aléatoire s'affiche une seule fois : le copier dans le coffre-fort du pack. Le compte `appli` ne peut venir que de `192.168.10.21` (serveur applicatif, à adapter) et n'a que les droits de données sur `base_appli`.

3. Ouverture du pare-feu pour l'application et l'administration SSH :
```bash
sudo apt install -y ufw
sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow from 192.168.10.21 to any port 3306 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : SSH et MySQL ne sont autorisés que depuis les machines prévues. Ouvrir SSH avant d'activer le pare-feu évite de se couper l'accès.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Liste des comptes et suppression des comptes anonymes ou sans mot de passe :
```bash
sudo mariadb -e "SELECT User, Host, plugin FROM mysql.global_priv;"
sudo mariadb -e "DELETE FROM mysql.global_priv WHERE User='' ; FLUSH PRIVILEGES;"
```
👉 Explication : La première commande liste tous les comptes avec leur hôte autorisé et leur méthode d'authentification. La seconde supprime les comptes anonymes. Tout compte `%` (accessible de partout) doit être justifié ou supprimé. La table `mysql.global_priv` est celle de MariaDB 10.4 et plus (à vérifier sur la version déployée).

2. Sauvegarde logique testée :
```bash
sudo mkdir -p /root/sauvegardes
sudo mariadb-dump --single-transaction --routines --triggers --all-databases | gzip > /root/sauvegardes/mariadb-$(date +%F).sql.gz
sudo chmod 600 /root/sauvegardes/mariadb-*.sql.gz
sudo ls -l /root/sauvegardes
```
👉 Explication : `--single-transaction` produit une copie cohérente sans bloquer les tables InnoDB. La sauvegarde est compressée et réservée à `root`. Elle doit être copiée hors du serveur et restaurée sur une machine de test au moins une fois.

3. Restauration de contrôle sur une machine de test, jamais sur la production :
```bash
gunzip -c /root/sauvegardes/mariadb-$(date +%F).sql.gz | sudo mariadb
sudo mariadb -e "SHOW DATABASES;"
```
👉 Explication : Vérifie que la sauvegarde est exploitable. Une sauvegarde non restaurée n'est pas une sauvegarde validée.

4. Contrôle des journaux de service :
```bash
sudo journalctl -u mariadb -n 50 --no-pager
```
👉 Explication : Sous Debian, le journal d'erreurs de MariaDB est envoyé à `journalctl`. Les échecs d'authentification et les redémarrages inattendus doivent être remontés au responsable sécurité.

---
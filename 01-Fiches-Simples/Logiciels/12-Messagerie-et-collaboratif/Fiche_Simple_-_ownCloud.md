# 📄 ownCloud

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : ownCloud Classic 10.x (paquet du dépôt officiel ownCloud, à vérifier sur la version déployée)
- **Catégorie** : Messagerie et collaboratif
- **Tags** : `[debian-12]`, `[owncloud]`, `[cloud]`, `[php]`, `[hardening]`

## 🎯 Objectif
Installer ownCloud Classic sur Debian 12 avec Apache, MariaDB et PHP, vérifier sur ce même serveur que l'instance est installée et répond, puis la durcir (domaines de confiance, dossier de données hors racine web, HTTPS) avant de l'ouvrir aux utilisateurs. Les tests ne se font que sur votre propre serveur. Cette fiche concerne ownCloud Classic 10 sur Debian 12 uniquement. Elle ne décrit pas ownCloud Infinite Scale (oCIS) : des séries oCIS séparées couvrent Debian 13, Ubuntu Server 24.04 et Rocky Linux 9; les variantes ne sont pas interchangeables.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation des paquets serveur et des extensions PHP :
```bash
sudo apt update
sudo apt install -y apache2 mariadb-server php php-gd php-curl php-mbstring php-intl php-xml php-zip php-mysql php-bz2 php-ldap php-imagick php-apcu unzip wget
```
👉 Explication : Installe le serveur web, la base de données et les extensions PHP utilisées par ownCloud Classic. Les paquets proviennent des dépôts Debian 12.

2. Création de la base et de l'utilisateur de test :
```bash
sudo mysql -e "CREATE DATABASE owncloud CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
sudo mysql -e "CREATE USER 'oc_user'@'localhost' IDENTIFIED BY '<mot_de_passe_bdd_test>';"
sudo mysql -e "GRANT ALL PRIVILEGES ON owncloud.* TO 'oc_user'@'localhost';"
```
👉 Explication : Crée la base `owncloud` et un utilisateur dédié. `<mot_de_passe_bdd_test>` est un mot de passe de lab, jamais réutilisé.

3. Téléchargement de l'archive officielle et mise en place :
```bash
cd /tmp
wget https://download.owncloud.com/server/stable/owncloud-complete-latest.tar.bz2
sudo tar -xjf owncloud-complete-latest.tar.bz2 -C /var/www/
sudo chown -R www-data:www-data /var/www/owncloud
```
👉 Explication : Télécharge l'archive complète depuis le site officiel et la place dans `/var/www/owncloud`. L'URL exacte et la somme de contrôle sont à vérifier sur la version déployée.

4. Installation en ligne de commande via `occ` :
```bash
cd /var/www/owncloud
sudo -u www-data php occ maintenance:install --database "mysql" --database-name "owncloud" --database-user "oc_user" --database-pass "<mot_de_passe_bdd_test>" --admin-user "admin_test" --admin-pass "<mot_de_passe_admin_test>"
```
👉 Explication : `occ` est l'outil d'administration d'ownCloud. Cette commande crée les tables et le compte administrateur. Les options exactes sont à vérifier sur la version déployée.

5. Contrôle de l'état de l'instance :
```bash
sudo -u www-data php /var/www/owncloud/occ status
```
👉 Explication : Affiche la version, l'état d'installation (`installed: true`) et le mode maintenance (`maintenance: false`) attendu.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activation des modules Apache requis :
```bash
sudo a2enmod rewrite headers env dir mime setenvif
sudo systemctl reload apache2
```
👉 Explication : Active les modules Apache nécessaires à ownCloud. Le fichier de site (`/etc/apache2/sites-available/owncloud.conf`) pointe sur `/var/www/owncloud` et doit suivre la documentation officielle de la version déployée.

2. Déclaration du nom d'accès (domaines de confiance) :
```bash
cd /var/www/owncloud
sudo -u www-data php occ config:system:set trusted_domains 1 --value="<nom_serveur_cloud>"
sudo -u www-data php occ config:system:set overwrite.cli.url --value="https://<nom_serveur_cloud>/"
```
👉 Explication : Seul le nom déclaré est accepté dans l'en-tête `Host`. `<nom_serveur_cloud>` est le FQDN du service.

3. Contrôle de la configuration :
```bash
sudo -u www-data php /var/www/owncloud/occ status
sudo -u www-data php /var/www/owncloud/occ config:system:get trusted_domains
```
👉 Explication : Confirme que l'instance est installée et que le nom déclaré est bien enregistré.

4. Ouverture du pare-feu pour HTTPS et administration :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Ouvre SSH seulement pour `<adresse_ip_admin>` avant d'activer le pare-feu. Seul le port 443 est exposé aux utilisateurs.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Passage en mode maintenance pendant les modifications sensibles :
```bash
cd /var/www/owncloud
sudo -u www-data php occ maintenance:mode --on
sudo -u www-data php occ maintenance:mode --off
```
👉 Explication : Le mode maintenance bloque les accès pendant une mise à jour ou un changement de base. Le second appel le désactive une fois l'opération terminée.

2. Déplacement du dossier de données hors de la racine web :
```bash
sudo mkdir -p /srv/owncloud-data
sudo chown www-data:www-data /srv/owncloud-data
sudo chmod 750 /srv/owncloud-data
sudo -u www-data php occ config:system:set datadirectory --value="/srv/owncloud-data"
```
👉 Explication : Les fichiers des utilisateurs ne doivent jamais être accessibles par une URL. Le dossier reste lisible seulement par `www-data`. Le réglage `datadirectory` est à vérifier sur la version déployée, car il ne se modifie pas toujours après installation.

3. Contrôle des paramètres de sécurité :
```bash
sudo -u www-data php /var/www/owncloud/occ config:system:get datadirectory
sudo -u www-data php /var/www/owncloud/occ security:certificates
```
👉 Explication : Affiche le dossier de données utilisé, puis liste les certificats système reconnus par l'instance. Les avertissements de sécurité affichés dans l'interface d'administration doivent aussi être traités.

4. Sauvegarde de la configuration avant toute évolution :
```bash
sudo tar czf /root/owncloud-config-$(date +%F).tgz /var/www/owncloud/config
sudo ls -l /root/owncloud-config-*.tgz
```
👉 Explication : Crée une archive datée du fichier `config.php`, qui contient les identifiants de base de données. Le stocker hors du serveur, dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack).

---

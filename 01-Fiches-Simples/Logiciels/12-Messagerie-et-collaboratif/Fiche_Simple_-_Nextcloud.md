# 📄 Nextcloud

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Nextcloud 29.x (archive officielle, à vérifier sur la version déployée)
- **Catégorie** : Messagerie et collaboratif
- **Tags** : `[debian-12]`, `[nextcloud]`, `[cloud]`, `[php]`, `[hardening]`

## 🎯 Objectif
Installer Nextcloud sur Debian 12 avec Apache, MariaDB et PHP, vérifier sur ce même serveur que l'interface répond et que la commande d'état `occ` est saine, puis le durcir (domaines de confiance, HTTPS, dossier de données hors racine web) avant de l'ouvrir aux utilisateurs. Les tests ne se font que sur votre propre serveur. Le guide Docker du pack (fiche Nextcloud 29 dans `02-Fiches-Completes`) reste la référence pour un déploiement conteneurisé.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation des paquets serveur (Apache, MariaDB, PHP) :
```bash
sudo apt update
sudo apt install -y apache2 mariadb-server php php-gd php-curl php-mbstring php-intl php-xml php-zip php-mysql php-bz2 php-imagick php-gmp php-apcu unzip wget
```
👉 Explication : Installe le serveur web, la base de données et les extensions PHP requises par Nextcloud. Les paquets proviennent des dépôts Debian 12.

2. Création de la base et de l'utilisateur de test :
```bash
sudo mysql -e "CREATE DATABASE nextcloud CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;"
sudo mysql -e "CREATE USER 'nc_user'@'localhost' IDENTIFIED BY '<mot_de_passe_bdd_test>';"
sudo mysql -e "GRANT ALL PRIVILEGES ON nextcloud.* TO 'nc_user'@'localhost';"
```
👉 Explication : Crée la base `nextcloud` et un utilisateur dédié. `<mot_de_passe_bdd_test>` est un mot de passe de lab, jamais réutilisé. L'encodage `utf8mb4` est exigé par Nextcloud.

3. Téléchargement et extraction de l'archive officielle :
```bash
cd /tmp
wget https://download.nextcloud.com/server/releases/latest.tar.bz2
sudo tar -xjf latest.tar.bz2 -C /var/www/
sudo chown -R www-data:www-data /var/www/nextcloud
```
👉 Explication : Télécharge la dernière version stable depuis le site officiel de Nextcloud et place l'application dans `/var/www/nextcloud`, propriété de l'utilisateur du serveur web. Vérifier la somme de contrôle publiée par l'éditeur sur la version déployée.

4. Installation en ligne de commande via `occ` :
```bash
cd /var/www/nextcloud
sudo -u www-data php occ maintenance:install --database "mysql" --database-name "nextcloud" --database-user "nc_user" --database-pass "<mot_de_passe_bdd_test>" --admin-user "admin_test" --admin-pass "<mot_de_passe_admin_test>"
```
👉 Explication : `occ` est l'outil d'administration de Nextcloud. Cette commande crée les tables et le compte administrateur. Les options exactes peuvent varier selon la version, à vérifier sur la version déployée.

5. Contrôle de l'état de l'instance :
```bash
sudo -u www-data php /var/www/nextcloud/occ status
```
👉 Explication : Affiche la version installée, l'état d'installation (`installed: true`) et le mode maintenance (`maintenance: false`) attendu.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activation du site Apache et des modules nécessaires :
```bash
sudo a2enmod rewrite headers env dir mime
sudo systemctl reload apache2
```
👉 Explication : Active les modules Apache utilisés par Nextcloud. Le fichier de site (`/etc/apache2/sites-available/nextcloud.conf`) pointe sur `/var/www/nextcloud` et doit être créé à partir de la documentation officielle.

2. Déclaration du nom d'accès (domaines de confiance) :
```bash
cd /var/www/nextcloud
sudo -u www-data php occ config:system:set trusted_domains 1 --value="<nom_serveur_cloud>"
sudo -u www-data php occ config:system:set overwrite.cli.url --value="https://<nom_serveur_cloud>/"
```
👉 Explication : Seul le nom déclaré est accepté dans l'en-tête `Host`. `<nom_serveur_cloud>` est le FQDN du service. Sans cette étape, l'interface refuse les accès par nom.

3. Contrôle de l'état et de la configuration :
```bash
sudo -u www-data php /var/www/nextcloud/occ status
sudo -u www-data php /var/www/nextcloud/occ config:system:get trusted_domains
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
1. Passage en mode maintenance avant toute modification sensible :
```bash
cd /var/www/nextcloud
sudo -u www-data php occ maintenance:mode --on
sudo -u www-data php occ maintenance:mode --off
```
👉 Explication : Le mode maintenance bloque les accès pendant une modification (mise à jour, changement de base). Le second appel le désactive une fois l'opération terminée.

2. Déplacement du dossier de données hors de la racine web :
```bash
sudo mkdir -p /srv/nextcloud-data
sudo chown www-data:www-data /srv/nextcloud-data
sudo chmod 750 /srv/nextcloud-data
```
👉 Explication : Les fichiers des utilisateurs ne doivent jamais être accessibles par une URL. Le dossier `/srv/nextcloud-data` reste lisible seulement par `www-data`. Le réglage `datadirectory` se fait à l'installation ou dans `config/config.php`, à vérifier sur la version déployée.

3. Vérification des paramètres de sécurité :
```bash
sudo -u www-data php /var/www/nextcloud/occ config:system:get datadirectory
sudo -u www-data php /var/www/nextcloud/occ setupchecks
```
👉 Explication : Affiche le dossier de données utilisé, puis liste les avertissements de sécurité et de configuration détectés par Nextcloud (HTTPS, en-têtes, PHP). Chaque avertissement doit être traité ou justifié.

4. Sauvegarde de la configuration avant toute évolution :
```bash
sudo tar czf /root/nextcloud-config-$(date +%F).tgz /var/www/nextcloud/config
sudo ls -l /root/nextcloud-config-*.tgz
```
👉 Explication : Crée une archive datée du fichier `config.php`, qui contient les identifiants de base de données. Le stocker hors du serveur, dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack).

---

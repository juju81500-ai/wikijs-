# Déployer GLPI 11 sur Debian 12 ou 13

- **Environnement** : VM Linux dédiée, sauvegardée
- **Composants** : Nginx ou Apache, PHP-FPM, MariaDB, GLPI

## 1. Préparer et vérifier la compatibilité

Fiche simple : [préparer le déploiement et vérifier la compatibilité](/01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-preparer-compatibilite).

Utiliser une version maintenue de GLPI et consulter sa matrice officielle pour les versions PHP, extensions et bases supportées par le système choisi. GLPI 11.12 est une version future/indicative selon la source du pack : confirmer qu'elle existe et qu'elle est prise en charge avant installation.

Prévoir DNS, TLS, stockage des documents, compte de service, sauvegarde cohérente de la base et des fichiers, puis fenêtre de maintenance. Ne pas exposer le répertoire de données ou les fichiers de configuration au serveur Web.

```bash
sudo apt update
sudo apt install --yes nginx mariadb-server php-fpm php-mysql php-curl php-gd php-intl php-mbstring php-xml php-zip
php -v
```

Installer les extensions supplémentaires exigées par la version de GLPI effectivement retenue.

## 2. Créer une base dédiée

Fiche simple : [créer une base GLPI dédiée](/01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-creer-base).

```bash
sudo mariadb-secure-installation
sudo mariadb
```

Dans la console SQL, définir un secret unique conservé hors du dépôt :

```sql
CREATE DATABASE glpi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'glpi'@'localhost' IDENTIFIED BY 'REMPLACER_PAR_UN_SECRET_UNIQUE';
GRANT ALL PRIVILEGES ON glpi.* TO 'glpi'@'localhost';
EXIT;
```

## 3. Installer l'application

Fiche simple : [installer l'application GLPI](/01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-installer-application).

Télécharger l'archive depuis la source officielle de GLPI, vérifier son empreinte ou sa signature lorsqu'elle est publiée, puis la déployer en tant que root. Utiliser un répertoire de version et un lien `current` facilite le retour arrière.

```bash
sudo install -d -o root -g www-data -m 0750 /var/www/glpi/releases
```

Extraire la version validée sous `/var/www/glpi/releases/<version>`, configurer le serveur Web avec le répertoire public recommandé par cette version, et attribuer l'écriture uniquement aux chemins GLPI qui en ont besoin. Ne pas rendre toute l'installation modifiable par `www-data`.

Créer le virtual host avec le nom DNS choisi, le socket PHP-FPM réellement installé et le refus d'accès aux fichiers cachés. Valider la configuration du serveur Web avant rechargement.

## 4. Installer et vérifier

Fiche simple : [installer et recetter GLPI](/01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-installer-recetter).

Ouvrir l'URL HTTPS depuis un poste d'administration et suivre l'assistant GLPI avec le compte SQL dédié. Après installation, supprimer ou désactiver l'installateur selon la documentation officielle, remplacer le compte administrateur initial et activer les tâches planifiées recommandées.

```bash
sudo nginx -t
sudo systemctl --no-pager status nginx mariadb
sudo journalctl -u nginx --since '-15 minutes' --no-pager
```

Créer un ticket de test, vérifier les notifications, l'envoi de courriels et les tâches automatiques, puis supprimer les données de test.

## 5. Exploitation et retour arrière

Fiche simple : [maintenir et restaurer GLPI](/01-fiches-simples/debian/12/vie-du-logiciel/glpi/fiche-simple-vm-debian-12-glpi-maintenir-restaurer).

Avant toute mise à niveau, activer le mode maintenance, sauvegarder la base et les fichiers, puis vérifier leur restauration. Conserver l'ancienne version jusqu'à validation fonctionnelle. En cas d'échec, restaurer ensemble la base et les fichiers de la même sauvegarde ; ne pas restaurer l'un sans l'autre.
# Pile LEMP sur Debian 13 : Nginx, PHP-FPM et MariaDB

- **Environnement** : VM ou serveur dédié
- **OS** : Debian 13 (Trixie)
- **Rôle** : Héberger une application Web PHP avec une base MariaDB locale

> Debian 13 fournit PHP 8.4. Cette procédure utilise les paquets génériques de Trixie; vérifier les candidats avec `apt-cache policy php-fpm mariadb-server` avant installation. Les révisions mineures évoluent avec les mises à jour de sécurité.

## 1. Prérequis et préparation

Fiche simple : [préparer la pile LEMP](/01-fiches-simples/debian/13/vie-du-logiciel/lemp/fiche-simple-vm-debian-13-lemp-preparer).

- Prévoir un nom DNS, une adresse IP stable et un accès console ou SSH de secours.
- Remplacer `app.example.net` et les adresses d'exemple par les valeurs de l'environnement.
- N'exposer que les ports nécessaires. Ne pas publier MariaDB sur Internet.

```bash
sudo apt update
sudo apt install --yes nginx mariadb-server php-fpm php-mysql php-curl php-gd php-mbstring php-xml php-zip
sudo apt-cache policy php-fpm mariadb-server
```

Avant toute mise à niveau, planifier une fenêtre de maintenance et une sauvegarde vérifiée. Ne pas lancer un `full-upgrade` à l'aveugle sur un serveur en production.

## 2. Sécuriser MariaDB et créer la base

Fiche simple : [sécuriser MariaDB](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-lemp-securiser-mariadb).

```bash
sudo mariadb-secure-installation
sudo mariadb
```

Dans la console MariaDB, remplacer le mot de passe d'exemple par un secret unique conservé dans le gestionnaire de secrets, puis exécuter :

```sql
CREATE DATABASE appdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'REMPLACER_PAR_UN_SECRET_UNIQUE';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, INDEX ON appdb.* TO 'appuser'@'localhost';
EXIT;
```

Le compte applicatif est limité à la base de l'application. Ajouter d'autres privilèges seulement si l'installation ou les migrations en ont besoin.

```bash
sudo ss -lntp | grep ':3306' || true
```

MariaDB doit rester accessible uniquement localement, sauf architecture séparée nécessitant explicitement un réseau privé et des règles dédiées.

## 3. Déployer un hôte Nginx et PHP-FPM

Fiche simple : [déployer Nginx et PHP-FPM](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-lemp-deployer-nginx-php).

```bash
sudo install -d -o root -g www-data -m 0755 /var/www/app/public
sudo tee /var/www/app/public/index.php >/dev/null <<'PHP'
<?php
header('Content-Type: text/plain; charset=utf-8');
echo "PHP-FPM fonctionne\n";
PHP
sudo chmod 0644 /var/www/app/public/index.php
php-fpm8.4 -v
ls -l /run/php/
```

Créer `/etc/nginx/sites-available/app` et remplacer le socket FastCGI par celui réellement présent dans `/run/php/` :

```nginx
server {
	listen 80;
	listen [::]:80;
	server_name app.example.net;
	root /var/www/app/public;
	index index.php;

	location / {
		try_files $uri $uri/ =404;
	}

	location ~ \.php$ {
		try_files $uri =404;
		include snippets/fastcgi-php.conf;
		fastcgi_pass unix:/run/php/php8.4-fpm.sock;
	}

	location ~ /\. {
		deny all;
	}
}
```

Activer le site et valider avant rechargement :

```bash
sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app
sudo nginx -t
sudo systemctl enable --now nginx mariadb php8.4-fpm
sudo systemctl reload nginx
```

## 4. Contrôles fonctionnels

Fiche simple : [recetter les services](/01-fiches-simples/debian/13/vie-du-logiciel/lemp/fiche-simple-vm-debian-13-lemp-recetter-services).

```bash
curl -fsS -H 'Host: app.example.net' http://127.0.0.1/
sudo nginx -t
systemctl --no-pager --full status nginx mariadb php8.4-fpm
systemctl --no-pager --failed
sudo journalctl -u nginx -u mariadb -u php8.4-fpm --since '-15 minutes' --no-pager
```

La réponse attendue est `PHP-FPM fonctionne`. Supprimer immédiatement le fichier de test avant de déployer l'application :

```bash
sudo rm /var/www/app/public/index.php
```

## 5. TLS et filtrage réseau

Fiche simple : [configurer TLS et le filtrage](/01-fiches-simples/debian/13/vie-du-logiciel/lemp/fiche-simple-vm-debian-13-lemp-configurer-tls-filtrage).

- Publier le site uniquement après résolution DNS correcte et validation HTTP.
- Autoriser TCP/80 pour la validation du certificat et TCP/443 pour les utilisateurs; limiter SSH au réseau d'administration.
- Déployer le certificat avec l'outil ACME retenu par l'organisation, puis vérifier le renouvellement automatique.
- Ne pas ajouter de règle de pare-feu avant d'avoir identifié le gestionnaire actif et la méthode d'accès de secours.

## 6. Sauvegarde et retour arrière

Fiche simple : [sauvegarder et préparer le retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/lemp/fiche-simple-vm-debian-13-lemp-sauvegarder-retour-arriere).

Avant une modification, sauvegarder les fichiers Nginx et exporter la base avec un outil de sauvegarde approprié, puis vérifier qu'une restauration est possible. En cas d'échec de configuration, restaurer le fichier précédent, lancer `sudo nginx -t`, puis `sudo systemctl reload nginx`. Ne supprimer ni base ni volume pour dépanner un service.

## 7. Dépannage

Fiche simple : [diagnostiquer la pile LEMP](/01-fiches-simples/debian/13/vie-du-logiciel/lemp/fiche-simple-vm-debian-13-lemp-depanner).

```bash
sudo nginx -t
sudo journalctl -u nginx -u mariadb -u php8.4-fpm --since '-30 minutes' --no-pager
sudo ss -lntp
sudo mariadb -e 'SHOW DATABASES;'
```

Un `502 Bad Gateway` indique souvent un service PHP-FPM arrêté ou un socket incorrect. Un `404` peut venir du `root` ou du `server_name`. Ne pas exposer les erreurs PHP détaillées aux visiteurs en production.
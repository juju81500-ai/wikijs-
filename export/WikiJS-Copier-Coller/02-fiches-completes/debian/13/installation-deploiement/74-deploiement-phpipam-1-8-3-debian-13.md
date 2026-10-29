# Déployer phpIPAM 1.8.3 sur Debian 13

- **OS / Version** : Debian 13 Trixie x86-64; phpIPAM 1.8.3
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : application phpIPAM, MariaDB locale, PHP-FPM et Nginx; saisie IPAM manuelle
- **Catégorie** : IPAM

## 1. Périmètre et prérequis

Fiche simple : [cadrer le périmètre phpIPAM](/01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-perimetre).

Au 27 octobre 2026, la release GitHub stable la plus récente consultée est phpIPAM 1.8.3. L'archive officielle publie le SHA-256 `2fc737da5a04a842cda097f609c4db85c808270eaad5949c4ec03d10f874556d`. La branche 1.8.x déclare PHP 7.2 à 8.5; Debian 13 utilise PHP 8.4. La documentation d'installation détaillée vise Ubuntu, pas Debian 13: les noms de paquets et le socket PHP-FPM ci-dessous sont adaptés au système cible et doivent être validés en préproduction.

Cette fiche couvre l'inventaire IPAM tenu par les administrateurs. Les scans, pings automatiques, découverte d'hôtes, suppressions automatiques d'adresses inactives et exposition de la console hors réseau d'administration sont exclus. Préparer un FQDN, un certificat TLS, les administrateurs responsables et un plan d'adressage approuvé avant l'installation.

## 2. Installer les paquets

Fiche simple : [installer les paquets](/01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-paquets).

Installer Nginx, MariaDB, PHP-FPM et les extensions utilisées par phpIPAM :

```bash
sudo apt update
sudo apt install -y nginx mariadb-server mariadb-client git ca-certificates curl php-fpm php-cli php-mysql php-gmp php-common php-mbstring php-gd php-curl php-xml php-pear php-zip php-ldap
php -v
php -m
sudo systemctl enable --now nginx mariadb
```

Vérifier que PHP-FPM, `pdo_mysql`, `gmp`, `mbstring`, `curl` et `xml` sont disponibles. Le nom exact de l'unité PHP-FPM dépend du paquet installé; le retrouver avec `systemctl list-units 'php*-fpm.service'`.

## 3. Créer la base dédiée

Fiche simple : [créer la base dédiée](/01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-base).

Garder MariaDB sur localhost. Créer une base UTF-8 et un utilisateur limité à cette base; remplacer le secret d'exemple par une valeur aléatoire conservée dans un coffre :

```bash
sudo mariadb
```

Dans la console SQL :

```sql
CREATE DATABASE phpipam CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'phpipam'@'127.0.0.1' IDENTIFIED BY 'REMPLACER_PAR_UN_SECRET_ALEATOIRE';
GRANT ALL PRIVILEGES ON phpipam.* TO 'phpipam'@'127.0.0.1';
FLUSH PRIVILEGES;
EXIT;
```

La permission est limitée au schéma phpIPAM, nécessaire à l'assistant d'installation et aux migrations. Ne pas utiliser le compte root de MariaDB depuis le site web.

## 4. Télécharger la release et configurer l'application

Fiche simple : [télécharger la release et configurer l'application](/01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-release-config).

Télécharger l'archive de release, vérifier l'empreinte publiée et extraire le code dans un répertoire versionné :

```bash
cd /tmp
curl --fail --location --proto '=https' --tlsv1.2 -o phpipam-v1.8.3.tgz https://github.com/phpipam/phpipam/releases/download/v1.8.3/phpipam-v1.8.3.tgz
echo '2fc737da5a04a842cda097f609c4db85c808270eaad5949c4ec03d10f874556d  phpipam-v1.8.3.tgz' | sha256sum --check
tar -tzf phpipam-v1.8.3.tgz | head
sudo tar -xzf phpipam-v1.8.3.tgz -C /var/www
```

Vérifier le nom du dossier extrait, puis le lier vers `/var/www/phpipam`. Si un chemin d'installation existe déjà, arrêter et suivre la procédure de mise à niveau; ne pas écraser une instance.

```bash
sudo ln -s /var/www/phpipam-v1.8.3 /var/www/phpipam
sudo cp /var/www/phpipam/config.dist.php /var/www/phpipam/config.php
sudoedit /var/www/phpipam/config.php
```

Dans `config.php`, renseigner l'hôte `127.0.0.1`, l'utilisateur et le mot de passe dédiés, le nom `phpipam` et le port `3306`. Conserver `$debugging = false`, `$api_allow_unsafe = false` et les en-têtes proxy désactivés tant qu'aucun proxy de confiance n'est utilisé.

Protéger le fichier qui contient le secret SQL :

```bash
sudo chown root:www-data /var/www/phpipam/config.php
sudo chmod 0640 /var/www/phpipam/config.php
```

Le code applicatif reste non modifiable par `www-data`; ne pas appliquer un `chown -R www-data` au dépôt. Si un usage validé nécessite l'écriture d'un dossier de données, n'accorder l'accès qu'à ce dossier précis.

## 5. Configurer Nginx et PHP-FPM

Fiche simple : [configurer Nginx et PHP-FPM](/01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-nginx-php).

Créer `/etc/nginx/sites-available/phpipam` et adapter le nom DNS, les chemins de certificats et le socket FPM au serveur :

```nginx
server {
    listen 80;
    server_name ipam.example.net;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name ipam.example.net;
    root /var/www/phpipam;
    index index.php;

    ssl_certificate /etc/ssl/certs/ipam.example.net.pem;
    ssl_certificate_key /etc/ssl/private/ipam.example.net.key;

    location / {
        try_files $uri $uri/ /index.php;
    }

    location /api {
        try_files $uri $uri/ /api/index.php?$query_string;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.4-fpm.sock;
    }

    location ~ /\. {
        deny all;
    }
}
```

Valider l'existence des certificats et du socket avant activation. Activer le site et vérifier la configuration :

```bash
sudo ln -s /etc/nginx/sites-available/phpipam /etc/nginx/sites-enabled/phpipam
sudo nginx -t
sudo systemctl reload nginx
```

Limiter le port HTTPS au réseau d'administration. Garder MariaDB sur localhost; ne pas publier le port 3306. Si un reverse proxy TLS est ajouté, ne faire confiance à ses en-têtes `X-Forwarded-*` que si ce proxy les remplace systématiquement et que l'accès direct au backend est bloqué.

## 6. Initialiser et durcir phpIPAM

Fiche simple : [initialiser et durcir phpIPAM](/01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-initialiser-durcir).

Ouvrir `https://ipam.example.net/` depuis le réseau d'administration. Utiliser l'assistant d'installation de la release pour initialiser le schéma `phpipam`; fournir le compte SQL applicatif, jamais le compte root. Une fois la migration terminée :

1. Modifier immédiatement le mot de passe administrateur initial (les identifiants par défaut sont publiés dans le README officiel).
2. Dans `config.php`, passer `$disable_installer = true` pour désactiver les scripts `/app/install/`.
3. Vérifier de nouveau que `$debugging = false`, que le site est en HTTPS et que l'API ne permet pas le HTTP non sécurisé.
4. Créer des comptes nominatifs et groupes avec accès limité aux sections nécessaires; réserver le compte administrateur aux changements d'administration.
5. Si l'API est utilisée, créer un token minimal dédié à l'intégration, le protéger et tester ses droits avant toute synchronisation.

Saisir quelques prefixes et adresses fictifs ou réservés au lab. Vérifier que les sous-réseaux, VLAN et sections correspondent au plan approuvé. Ne pas activer les tâches de scan, ping, discovery ou suppression des adresses inactives dans cette procédure.

## 7. Sauvegarder et restaurer

Fiche simple : [sauvegarder et restaurer phpIPAM](/01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-sauvegarder).

Sauvegarder la base ainsi que `config.php`; protéger les deux, car le fichier de configuration permet l'accès SQL. Stocker les copies chiffrées hors de l'hôte :

```bash
sudo install -d -m 0700 /var/backups/phpipam
sudo mariadb-dump --single-transaction phpipam | gzip | sudo tee /var/backups/phpipam/phpipam-$(date +%F).sql.gz >/dev/null
sudo cp /var/www/phpipam/config.php /var/backups/phpipam/config.php
sudo chmod 0600 /var/backups/phpipam/*
```

Tester la restauration dans une base de laboratoire isolée avant de la considérer exploitable. Pour une restauration, arrêter l'écriture applicative, restaurer le code correspondant à la version et le dump, recopier la configuration appropriée, puis valider l'ouverture de session et la présence des objets. Ne pas restaurer une base de production par-dessus une instance active.

Avant toute mise à niveau, suivre l'ordre documenté : sauvegarder la base et `config.php`, remplacer le code en conservant la configuration, puis exécuter la migration de base de données par l'interface d'administration. Conserver le code précédent et son dump jusqu'à la validation.

## Sources

- [phpIPAM — releases officielles et empreintes](https://github.com/phpipam/phpipam/releases)
- [phpIPAM 1.8.3 — notes de version](https://github.com/phpipam/phpipam/releases/tag/v1.8.3)
- [phpIPAM 1.8.3 — README, versions PHP et bases compatibles](https://github.com/phpipam/phpipam/blob/v1.8.3/README.md)
- [phpIPAM — installation et prérequis](https://phpipam.net/documents/installation/)
- [phpIPAM — mise à niveau et restauration](https://phpipam.net/documents/upgrade/)
- [phpIPAM 1.8.3 — configuration de référence](https://github.com/phpipam/phpipam/blob/v1.8.3/config.dist.php)
- [phpIPAM — procédure Ubuntu amont, adaptée ici à Debian 13](https://phpipam.net/news/phpipam-installation-on-ubuntu-26-04-LTS/)
- [phpIPAM — politique de sécurité](https://github.com/phpipam/phpipam/blob/v1.8.3/SECURITY.md)

Les commandes Debian 13 et la configuration Nginx doivent être testées sur une VM de préproduction avant diffusion en production. Aucun déploiement ni test réel de restauration n'a été exécuté par cette fiche.
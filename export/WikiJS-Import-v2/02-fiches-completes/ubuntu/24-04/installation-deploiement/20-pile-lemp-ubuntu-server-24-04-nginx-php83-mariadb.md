---
title: "Pile LEMP sur Ubuntu Server 24.04 : Nginx, PHP-FPM et MariaDB"
description: "Fiche simple : [vérifier prérequis et versions](../../../../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/LEMP/FicheSimple-VMUbuntu24.04LEMPVerifierPrerequisVersions.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu24.04", "noble", "nginx", "php8.3", "mariadb", "lemp", "tls"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Pile LEMP sur Ubuntu Server 24.04 : Nginx, PHP-FPM et MariaDB

- **Type de fiche** : Installation / Déploiement
- **Environnement** : VM Ubuntu Server dédiée à une application Web
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble), Nginx, PHP 8.3, MariaDB 10.11
- **Rôle** : Déployer une application PHP avec base locale et TLS
- **Tags** : `ubuntu24.04`, `noble`, `nginx`, `php8.3`, `mariadb`, `lemp`, `tls`

## 1. Prérequis et versionnement

Fiche simple : [vérifier prérequis et versions](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-verifier-prerequis-versions).

Réserver hostname/FQDN, IP stable, volumes, accès SSH, sauvegarde et flux. Ubuntu 24.04 fournit PHP 8.3 et MariaDB 10.11 dans ses dépôts. Vérifier les candidats avant installation; les révisions de sécurité évoluent.

```bash
cat /etc/os-release
sudo apt update
apt-cache policy nginx php8.3-fpm mariadb-server
```

## 2. Installer la pile

Fiche simple : [installer la pile LEMP](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-installer-pile).

```bash
sudo apt install nginx mariadb-server php8.3-fpm php8.3-cli \
  php8.3-mysql php8.3-curl php8.3-gd php8.3-mbstring php8.3-xml php8.3-zip
sudo systemctl enable --now nginx mariadb php8.3-fpm
```

Vérifier séries, état des unités et socket :

```bash
php8.3 -v
systemctl --no-pager status nginx mariadb php8.3-fpm
ls -l /run/php/
```

## 3. Créer et limiter la base applicative

Fiche simple : [créer et limiter la base applicative](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-creer-base-limiter-droits).

```bash
sudo mariadb-secure-installation
sudo mariadb
```

Dans la console SQL, définir un secret par coffre et n'accorder que les droits nécessaires :

```sql
CREATE DATABASE appdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'REMPLACER_PAR_UN_SECRET_UNIQUE';
GRANT SELECT, INSERT, UPDATE, DELETE ON appdb.* TO 'appuser'@'localhost';
EXIT;
```

Ajouter des permissions de migration seulement pendant une procédure approuvée. MariaDB reste local; ne pas publier TCP/3306 si la pile est sur une seule VM.

## 4. Configurer Nginx et PHP-FPM

Fiche simple : [configurer Nginx et PHP-FPM](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-configurer-nginx-phpfpm).

Créer le répertoire applicatif et définir son propriétaire selon les besoins d'écriture réels :

```bash
sudo install -d -o root -g www-data -m 0755 /var/www/app/public
```

Créer un server block dans `/etc/nginx/sites-available/app`; définir FQDN, racine, index, `try_files`, refus des fichiers cachés et socket FPM :

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name app.example.net;
    root /var/www/app/public;
    index index.php;

    location / { try_files $uri $uri/ =404; }
    location ~ \.php$ {
        try_files $uri =404;
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.3-fpm.sock;
    }
    location ~ /\. { deny all; }
}
```

Activer et valider avant rechargement :

```bash
sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app
sudo nginx -t
sudo systemctl reload nginx
```

## 5. Déployer l'application et TLS

Fiche simple : [déployer l'application et TLS](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-deployer-application-tls).

Déployer une version applicative prise en charge, protéger le fichier de configuration et accorder au groupe Web une écriture uniquement sur cache/uploads requis. Configurer TLS avec l'autorité/outil ACME retenu et vérifier le renouvellement.

Pour un test FPM, créer temporairement un endpoint affichant uniquement `OK`, le tester via Nginx et le supprimer immédiatement; ne pas exposer `phpinfo()`.

## 6. Ouvrir les flux nécessaires

Fiche simple : [ouvrir les flux nécessaires](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-ouvrir-flux).

Autoriser TCP/80 pour ACME/redirect et TCP/443 pour les clients dans le pare-feu réellement géré. Restreindre SSH au réseau d'administration. Ne pas ajouter de règle `nft` runtime comme configuration finale ni désactiver UFW globalement.

## 7. Valider, sauvegarder et exploiter

Fiche simple : [valider, sauvegarder et exploiter](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-valider-sauvegarder-exploiter).

```bash
sudo nginx -t
systemctl --failed
curl -fsSI https://app.example.net/
sudo journalctl -u nginx -u mariadb -u php8.3-fpm --since today --no-pager
```

Sauvegarder configuration, fichiers applicatifs et base avec une procédure cohérente, cible indépendante et test de restauration. Surveiller certificats, espace disque, mises à jour et journaux.

## 8. Retour arrière

Fiche simple : [préparer le retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/lemp/fiche-simple-vm-ubuntu-24-04-lemp-retour-arriere).

Avant changement d'application ou de PHP, sauvegarder configuration et base. En cas d'échec, rétablir les fichiers de site précédents, exécuter `nginx -t`, puis recharger le service. Une migration de schéma de base exige aussi un plan de restauration cohérent; revenir uniquement à l'ancien code peut ne pas suffire.

## Sources

- [Ubuntu 24.04 — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [PHP 8.3 — documentation](https://www.php.net/manual/en/)
- [MariaDB — documentation Server](https://mariadb.com/docs/server/)
# Pile Web sur Ubuntu Server 26.04 : Nginx, PHP-FPM et PostgreSQL

- **Type de fiche** : Installation / Déploiement
- **Environnement** : VM ou serveur dédié Ubuntu Server
- **OS / Version** : Ubuntu Server 26.04 LTS (Resolute), Nginx, PHP 8.5 et PostgreSQL 18
- **Rôle** : Héberger une application PHP avec base PostgreSQL locale et TLS
- **Tags** : `ubuntu26.04`, `resolute`, `nginx`, `php8.5`, `postgresql18`, `web`, `tls`

## 1. Prérequis et versions

Fiche simple : [prérequis et versions de la pile web](../../../../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Prerequis_Versions.md).

Réserver hostname/FQDN, IP stable, volumes, accès SSH et méthode de sauvegarde. Ubuntu 26.04 fournit une base différente de Noble; vérifier les candidats avant installation :

```bash
cat /etc/os-release
sudo apt update
apt-cache policy nginx php8.5-fpm postgresql-18
```

Vérifier que l'application prend en charge PHP 8.5 et PostgreSQL 18 avant de déployer.

## 2. Installer Nginx, PHP-FPM et PostgreSQL

Fiche simple : [installer Nginx, PHP-FPM et PostgreSQL](../../../../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Installer_Nginx_PHP_PostgreSQL.md).

```bash
sudo apt install nginx php8.5-fpm php8.5-cli php8.5-pgsql \
  php8.5-curl php8.5-gd php8.5-mbstring php8.5-xml php8.5-zip postgresql-18
sudo systemctl enable --now nginx php8.5-fpm postgresql
```

Vérifier services, versions, cluster et socket :

```bash
nginx -v
php8.5 -v
pg_lsclusters
ls -l /run/php/
systemctl --failed
```

## 3. Préparer PostgreSQL

Fiche simple : [préparer PostgreSQL](../../../../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Preparer_PostgreSQL.md).

Créer un rôle avec secret saisi de façon interactive, puis une base limitée :

```bash
sudo -u postgres psql
```

```sql
CREATE ROLE app_user LOGIN;
\password app_user
CREATE DATABASE appdb OWNER app_user ENCODING 'UTF8';
```

Garder l'écoute locale si la base ne sert qu'à l'application locale. Pour un serveur DB distant, utiliser une adresse privée, TLS, `pg_hba.conf` limité et pare-feu adapté.

## 4. Configurer PHP-FPM et Nginx

Fiche simple : [configurer PHP-FPM et Nginx](../../../../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Configurer_PHP_FPM_Nginx.md).

Créer un répertoire non modifiable par l'utilisateur Web, puis un server block dans `/etc/nginx/sites-available/app` :

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
        fastcgi_pass unix:/run/php/php8.5-fpm.sock;
    }
    location ~ /\. { deny all; }
}
```

Confirmer le socket dans `/run/php/`, activer le site et valider avant rechargement :

```bash
sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled/app
sudo nginx -t
sudo systemctl reload nginx
```

## 5. Déployer l'application et TLS

Fiche simple : [déployer l'application et TLS](../../../../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Deployer_Application_TLS.md).

Déployer une version applicative compatible avec PHP 8.5, renseigner l'accès PostgreSQL via un secret protégé et limiter l'écriture aux seuls répertoires nécessaires. Configurer TLS avec l'outil ACME approuvé; tester le renouvellement.

Pour un essai FPM, créer un endpoint temporaire affichant `OK`, le tester via Nginx, puis le supprimer immédiatement; ne pas exposer `phpinfo()`.

## 6. Filtrer et surveiller

Fiche simple : [filtrer et surveiller la pile web](../../../../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Filtrer_Surveiller.md).

Autoriser uniquement les flux requis (généralement HTTPS et SSH depuis le réseau d'administration). Contrôler UFW/firewall effectivement actif, logs, espace disque, mises à jour et services.

## 7. Validation, sauvegarde et retour arrière

Fiche simple : [validation, sauvegarde et retour arrière de la pile web](../../../../01-Fiches-Simples/Ubuntu/26.04/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Validation_Sauvegarde_Retour.md).

Tester HTTPS, version PHP, connexion à la base, parcours de l'application et journaux. Sauvegarder fichiers et base dans une cible distincte, puis tester une restauration isolée. En cas d'échec, restaurer le server block précédent, valider avec `nginx -t`, puis recharger le service; restaurer aussi la base si son schéma a changé.

## Sources

- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/summary-for-lts-users/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [PHP 8.5 — documentation](https://www.php.net/manual/en/)
- [PostgreSQL 18 — documentation](https://www.postgresql.org/docs/18/)
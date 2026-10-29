# Pile Web sur Rocky Linux 9 : Nginx, PHP-FPM et MariaDB

- **Type de fiche** : Installation / Déploiement
- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9, Nginx, PHP-FPM et MariaDB fournis par les dépôts actifs
- **Rôle** : Héberger une application Web PHP avec base MariaDB locale
- **Tags** : `rocky9`, `rhel9`, `nginx`, `php-fpm`, `mariadb`, `lemp`, `selinux`

## 1. Prérequis et choix des versions

Fiche simple : [prérequis et choix des versions de la pile web](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_Prerequis_Versions.md).

Définir hostname/FQDN, IP stable, stockage, ports, sauvegardes et accès console. Rocky Linux 9 utilise DNF/AppStream et peut proposer différents streams PHP selon les dépôts activés; vérifier les candidats avant installation plutôt que supposer une version :

```bash
cat /etc/rocky-release
sudo dnf module list php
sudo dnf info nginx php-fpm mariadb-server
```

## 2. Installer les paquets

Fiche simple : [installer les paquets de la pile web](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_Installer_Paquets.md).

Après validation du stream PHP par rapport à l'application, installer les paquets depuis les dépôts Rocky approuvés :

```bash
sudo dnf install nginx php-fpm php-cli php-mysqlnd php-curl php-gd php-mbstring php-xml mariadb-server
sudo dnf info nginx php-fpm mariadb-server
```

Activer et contrôler les services :

```bash
sudo systemctl enable --now nginx mariadb php-fpm
systemctl --no-pager status nginx mariadb php-fpm
php -v
ls -l /run/php-fpm/
```

Le nom du socket PHP-FPM sur Rocky est souvent sous `/run/php-fpm/`; vérifier le chemin fourni par la configuration réellement installée.

## 3. Sécuriser MariaDB

Fiche simple : [sécuriser MariaDB](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_Securiser_MariaDB.md).

```bash
sudo mariadb-secure-installation
sudo mariadb
```

Créer une base et un compte dédié, et saisir le secret de manière interactive :

```sql
CREATE DATABASE appdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'appuser'@'localhost' IDENTIFIED BY 'REMPLACER_PAR_UN_SECRET_UNIQUE';
GRANT SELECT, INSERT, UPDATE, DELETE ON appdb.* TO 'appuser'@'localhost';
EXIT;
```

Garder MariaDB en écoute locale si l'application est sur le même serveur.

## 4. Configurer Nginx et PHP-FPM

Fiche simple : [configurer Nginx et PHP-FPM](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_Configurer_Nginx_PHP_FPM.md).

Créer le répertoire applicatif avec un propriétaire et des droits minimaux. Créer un server block dans `/etc/nginx/conf.d/app.conf` :

```nginx
server {
    listen 80;
    server_name app.example.net;
    root /var/www/app/public;
    index index.php;

    location / { try_files $uri $uri/ =404; }
    location ~ \.php$ {
        try_files $uri =404;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_pass unix:/run/php-fpm/www.sock;
    }
    location ~ /\. { deny all; }
}
```

Vérifier la valeur du socket et du pool PHP-FPM. Tester avant rechargement :

```bash
sudo nginx -t
sudo systemctl reload nginx
```

## 5. SELinux, firewalld et TLS

Fiche simple : [SELinux, firewalld et TLS de la pile web](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_SELinux_Firewalld_TLS.md).

Garder SELinux en `Enforcing`. Vérifier les contextes avec `restorecon`; si les fichiers web sont dans un chemin personnalisé, créer un contexte persistant et valider l'absence de refus AVC. Ouvrir seulement les services nécessaires dans la zone réellement active :

```bash
getenforce
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --zone=<ZONE_ACTIVE> --list-all
```

Configurer TLS avec une autorité/certificat approuvé et une procédure de renouvellement. Ne pas désactiver SELinux ou firewalld pour dépanner l'application.

## 6. Déployer et vérifier

Fiche simple : [déployer et vérifier la pile web](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_Deployer_Verifier.md).

Déployer une version applicative compatible avec la version PHP réellement installée. Tester l'application, la base, le socket FPM, HTTPS, logs, droits et services. Supprimer les pages de test avant d'ouvrir le service.

## 7. Sauvegarder et revenir en arrière

Fiche simple : [sauvegarder et revenir en arrière sur la pile web](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Pile-Web/Fiche_Simple_-_VM_Rocky_9_Pile_Web_Sauvegarder_Retour.md).

Sauvegarder code/configuration et effectuer un dump cohérent de MariaDB vers une cible indépendante. Tester la restauration dans un environnement isolé. Si la mise à jour échoue, restaurer config et base compatibles; ne pas rétrograder le serveur SQL en réutilisant des fichiers de données modifiés par une version plus récente.

## Sources

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [PHP — documentation](https://www.php.net/manual/en/)
- [MariaDB — documentation Server](https://mariadb.com/docs/server/)
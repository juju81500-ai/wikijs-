# Déployer Znuny 7.3.8 sur Debian 12

- **OS / Version** : Debian 12 Bookworm, Znuny 7.3.8
- **Type de fiche** : Installation/Déploiement
- **Environnement** : VM Linux dédiée, Apache/mod_perl et MariaDB 10.11
- **Machine ciblée** : Serveur helpdesk / ticketing
- **Catégorie** : ITSM / ticketing
- **Tags** : `znuny`, `debian12`, `itsm`, `ticketing`, `apache`, `mariadb`

## 1. Préparer l'installation

Fiche simple : [préparer l'installation](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Znuny/Fiche_Simple_-_VM_Debian_12_Znuny_Preparer.md).

Znuny 7.3.8 est une version de maintenance publiée le 14 octobre 2026. Vérifier les notes de version et le support applicatif avant mise en production. La documentation officielle teste notamment Debian 12 et Rocky Linux 9; ce guide cible Debian 12 et l'archive source officielle.

Prévoir DNS, TLS, SMTP, sauvegarde hors hôte et accès console/SSH de secours. Les prérequis officiels incluent Apache avec mod_perl, MariaDB 10.3+ ou un autre moteur supporté, Perl 5.16+ et plusieurs modules Perl. Utiliser un serveur dédié ou une VM de test avant production.

## 2. Installer les paquets système

Fiche simple : [installer les paquets système](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Znuny/Fiche_Simple_-_VM_Debian_12_Znuny_Paquets.md).

```bash
sudo apt update
sudo apt install apache2 mariadb-server mariadb-client \
  libapache2-mod-perl2 cpanminus gcc make tar gzip curl ca-certificates \
  libdbi-perl libdbd-mariadb-perl libxml-libxml-perl libxml-libxslt-perl \
  libjson-xs-perl libyaml-libyaml-perl libtext-csv-xs-perl \
  libtemplate-perl libtemplate-plugin-xml-perl libnet-ldap-perl \
  libnet-dns-perl libdatetime-perl libdatetime-timezone-perl \
  libmail-imapclient-perl libdata-uuid-perl libhash-merge-perl \
  libcrypt-eksblowfish-perl libspreadsheet-xlsx-perl libpackage-stash-perl
sudo systemctl enable --now apache2 mariadb
```

Comparer cette liste aux modules requis par la version et vérifier les modules Perl au contrôle d'installation. N'installer depuis CPAN que les dépendances manquantes, avec une procédure documentée.

## 3. Préparer MariaDB

Fiche simple : [préparer MariaDB](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Znuny/Fiche_Simple_-_VM_Debian_12_Znuny_MariaDB.md).

Créer une configuration de limites adaptée à Znuny :

```bash
sudo tee /etc/mysql/mariadb.conf.d/60-znuny.cnf >/dev/null <<'EOF'
[mysqld]
max_allowed_packet=256M
innodb_log_file_size=256M
EOF
sudo systemctl restart mariadb
```

Créer une base et un compte dédiés via le client local :

```bash
sudo mariadb
```

Dans le prompt MariaDB :

```sql
CREATE DATABASE znuny CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'znuny'@'localhost' IDENTIFIED BY '<SECRET_LONG_ET_UNIQUE>';
GRANT ALL PRIVILEGES ON znuny.* TO 'znuny'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

Remplacer le secret par une valeur aléatoire du coffre et ne pas utiliser l'utilisateur `root` dans l'application.

## 4. Télécharger et préparer Znuny

Fiche simple : [télécharger et préparer Znuny](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Znuny/Fiche_Simple_-_VM_Debian_12_Znuny_Telecharger.md).

Télécharger la version officielle puis vérifier son origine avant extraction :

```bash
cd /tmp
curl -fLO https://download.znuny.org/releases/znuny-7.3.8.tar.gz
tar -tzf znuny-7.3.8.tar.gz | head
sudo tar -xzf znuny-7.3.8.tar.gz -C /opt
sudo ln -sfn /opt/znuny-7.3.8 /opt/znuny
sudo useradd --system --home-dir /opt/znuny --shell /usr/sbin/nologin \
  --gid www-data znuny
```

Si le compte `znuny` ou le groupe `www-data` existe déjà, vérifier son UID, son groupe et son répertoire au lieu de le recréer.

## 5. Configurer Apache et les permissions

Fiche simple : [configurer Apache et les permissions](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Znuny/Fiche_Simple_-_VM_Debian_12_Znuny_Apache.md).

Activer mod_perl et le MPM compatible, puis installer le fichier de configuration officiel fourni par Znuny :

```bash
sudo a2dismod mpm_event mpm_worker
sudo a2enmod mpm_prefork perl
sudo ln -s /opt/znuny/scripts/apache2-httpd.include.conf \
  /etc/apache2/conf-available/zzz_znuny.conf
sudo a2enconf zzz_znuny
sudo /opt/znuny/bin/znuny.SetPermissions.pl
sudo apache2ctl configtest
sudo systemctl restart apache2
```

Si Apache héberge déjà d'autres applications, vérifier l'impact du passage à `mpm_prefork` avant application. Le nom DNS et TLS doivent être configurés dans un VirtualHost dédié, sans exposer la page installateur au-delà de la mise en service.

## 6. Exécuter l'assistant d'installation

Fiche simple : [exécuter l'assistant d'installation](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Znuny/Fiche_Simple_-_VM_Debian_12_Znuny_Assistant.md).

Ouvrir temporairement `https://support.example.net/znuny/installer.pl` depuis le réseau d'administration. Utiliser la base `znuny` et le compte dédié; renseigner l'adresse mail de support, le propriétaire du service et les premières données.

Terminer l'assistant, définir les identifiants initiaux, puis vérifier l'accès agent et client. Restreindre ou désactiver l'accès à l'installateur après réussite, conformément à la documentation Znuny.

## 7. Activer les tâches de fond

Fiche simple : [activer les tâches de fond](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Znuny/Fiche_Simple_-_VM_Debian_12_Znuny_Scheduler.md).

Znuny dépend du scheduler pour les tâches de traitement et de maintenance. Démarrer le script Cron de l'application avec le compte de service et vérifier les processus/logs :

```bash
sudo -u znuny /opt/znuny/bin/Cron.sh start
sudo -u znuny /opt/znuny/bin/znuny.Console.pl List
```

Rendre son démarrage persistant selon le mécanisme de service prévu par la version installée; ne pas lancer plusieurs schedulers concurrents.

## 8. Recette et exploitation

Fiche simple : [recette et exploitation](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Znuny/Fiche_Simple_-_VM_Debian_12_Znuny_Recette.md).

- Tester création, affectation, réponse par mail et accès selon rôles.
- Configurer SMTP, annuaire et filesystems de pièces jointes selon les politiques internes.
- Contrôler Apache, MariaDB, logs Znuny et scheduler après redémarrage.
- Sauvegarder la base, `/opt/znuny/Kernel/Config.pm`, les pièces jointes et toute configuration locale; restaurer dans un lab avant production.
- Planifier les mises à jour de sécurité et consulter les notes de version avant upgrade.

## Sources

- [Znuny — Installation officielle](https://doc.znuny.org/znuny/installation/index.html)
- [Znuny — Release 7.3.8](https://doc.znuny.org/znuny/releases/7_3_8/index.html)
- [Znuny — Opérations et maintenance](https://doc.znuny.org/znuny/standardoperations/index.html)
- [Znuny — CLI](https://doc.znuny.org/znuny/console/index.html)
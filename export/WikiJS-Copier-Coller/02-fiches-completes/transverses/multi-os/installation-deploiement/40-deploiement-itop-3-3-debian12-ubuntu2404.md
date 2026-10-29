# Déployer iTop 3.3 sur Debian 12 ou Ubuntu 24.04

- **OS / Version** : Debian 12 Bookworm ou Ubuntu Server 24.04 LTS; iTop Community 3.3.0
- **Type de fiche** : Installation/Déploiement
- **Environnement** : VM Linux avec Apache, PHP 8.2/8.3 et MariaDB 10.11
- **Machine ciblée** : Serveur ITSM/CMDB
- **Catégorie** : ITSM / CMDB / helpdesk

## 1. Dimensionner et préparer

Fiche simple : [dimensionner et préparer](/01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-dimensionner-preparer).

iTop 3.3 prend en charge PHP 8.2 à 8.4, MariaDB 10.6 à 11.8 et recommande Debian 12 ou Ubuntu 24.04. Adapter les ressources au volume : la recommandation constructeur pour moins de 5 000 tickets/mois, moins de 50 utilisateurs console et moins de 200 000 CI est 4 vCPU, 8 Go de RAM et 20 Go pour la base.

Préparer un nom DNS, TLS, IP fixe, SMTP, compte de service et sauvegarde testée. Installer l'application sur un hôte dédié; ne pas exposer directement le chemin `/setup` à Internet après l'assistant.

## 2. Installer Apache, PHP et MariaDB

Fiche simple : [installer Apache, PHP et MariaDB](/01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-installer-apache-php-mariadb).

Sur Debian 12 ou Ubuntu 24.04, vérifier les versions des dépôts avant installation :

```bash
sudo apt update
apt-cache policy apache2 mariadb-server php
sudo apt install apache2 mariadb-server graphviz \
  php libapache2-mod-php php-cli php-mysql php-json php-xml php-gd \
  php-zip php-curl php-soap php-mbstring php-apcu php-ldap php-imap
sudo a2enmod rewrite
sudo systemctl enable --now apache2 mariadb
```

Vérifier que `php` est entre 8.2 et 8.4 et que toutes les extensions requises sont chargées. Configurer TLS et un VirtualHost Apache avec le nom DNS réel avant d'ouvrir l'application aux utilisateurs.

## 3. Créer une base et un compte dédiés

Fiche simple : [créer une base et un compte dédiés](/01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-creer-base-compte-dedie).

Ouvrir le client MariaDB en local, puis créer une base UTF-8 et un utilisateur réservé à iTop. Remplacer le secret par une valeur aléatoire du coffre :

```sql
CREATE DATABASE itop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'itop'@'localhost' IDENTIFIED BY '<SECRET_LONG_ET_UNIQUE>';
GRANT ALL PRIVILEGES ON itop.* TO 'itop'@'localhost';
```

Ne pas utiliser le compte root de la base depuis l'application.

## 4. Installer le paquet officiel

Fiche simple : [installer le paquet officiel](/01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-installer-paquet-officiel).

Télécharger le paquet installable 3.3.0 (pas l'archive source GitHub) depuis la release officielle; vérifier une somme ou signature publiée avant de déployer :

```bash
curl -fL https://github.com/Combodo/iTop/releases/download/3.3.0/iTop-3.3.0-21411.zip -o /tmp/itop.zip
sudo install -d -o root -g www-data -m 0750 /var/www/itop
sudo unzip /tmp/itop.zip 'web/*' -d /var/www/itop
sudo mv /var/www/itop/web/* /var/www/itop/
sudo rmdir /var/www/itop/web
```

Créer les emplacements de données autorisés et leur attribuer seulement les droits nécessaires au compte Apache :

```bash
sudo install -d -o www-data -g www-data -m 0750 \
  /var/www/itop/data /var/www/itop/log /var/www/itop/conf \
  /var/www/itop/env-production /var/www/itop/env-production-build \
  /var/www/itop/env-test /var/www/itop/env-test-build
```

Ne pas appliquer de permissions globales `777` au répertoire Web.

## 5. Exécuter l'assistant initial

Fiche simple : [exécuter l'assistant initial](/01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-assistant-initial).

Vérifier Apache puis ouvrir `https://itsm.example.net/setup`. Sélectionner la base iTop dédiée, renseigner l'utilisateur et le secret, vérifier les contrôles PHP/Graphviz, choisir les modules réellement nécessaires, configurer le premier compte administrateur et terminer l'installation.

Après validation, appliquer la procédure officielle de protection de l'assistant setup et confirmer qu'il n'est plus accessible aux utilisateurs non autorisés. Configurer les notifications SMTP, l'annuaire LDAP/AD si requis, les profils et les premières données CMDB.

## 6. Activer les tâches planifiées

Fiche simple : [activer les tâches planifiées](/01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-activer-taches-planifiees).

Les SLA, notifications, sauvegardes automatiques et tâches asynchrones dépendent de `webservices/cron.php`. Créer son planificateur avec un compte d'administration iTop, stocker ses paramètres dans un fichier hors du DocumentRoot et suivre la fiche simple Debian dédiée.

## 7. Vérifier, sauvegarder et mettre à jour

Fiche simple : [vérifier, sauvegarder et mettre à jour](/01-fiches-simples/debian/12/vie-du-logiciel/itop/fiche-simple-vm-debian-12-itop-verifier-sauvegarder-maj).

- Tester connexion, création d'un ticket, d'une CI et les autorisations avec un compte non administrateur.
- Contrôler les journaux Apache/PHP et l'exécution des tâches planifiées.
- Sauvegarder la base, `conf/production/config-itop.php`, les extensions et les fichiers de données; tester une restauration isolée.
- Pour les sauvegardes volumineuses, préférer `mysqldump` cohérent et une solution de sauvegarde éprouvée; vérifier la limite iTop pour les archives internes dépassant 68 Go.
- Avant upgrade, sauvegarder et suivre le guide de migration de la version cible; ne pas mélanger code nouveau et schéma ancien sans exécuter le setup de migration.

## Sources

- [iTop — Installation et mise à niveau](https://www.itophub.io/wiki/page?id=latest:install:start)
- [iTop — Compatibilité et prérequis](https://www.itophub.io/wiki/page?id=latest:install:requirements)
- [iTop — Tâches planifiées](https://www.itophub.io/wiki/page?id=latest:admin:cron)
- [iTop — Sauvegarde des données](https://www.itophub.io/wiki/page?id=latest:admin:backup)
- [iTop — Release 3.3.0](https://github.com/Combodo/iTop/releases/tag/3.3.0)
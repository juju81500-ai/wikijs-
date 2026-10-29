# Fiche_Simple_-_VM_Debian_12_Znuny_Paquets.md

- **Environnement** : VM Debian 12 dédiée (Apache/mod_perl, MariaDB 10.11), Znuny 7.3.8
- **OS / Version** : Debian 12 Bookworm; Znuny 7.3.8
- **Catégorie** : ITSM / ticketing
- **Tags** : `debian12`, `znuny`, `apt`, `apache`, `mariadb`

---

## Problème précis à résoudre

Installer Apache, MariaDB et les modules Perl requis par Znuny.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour l'index des paquets :
   ```bash
   sudo apt update
   ```
   👉 Explication : on récupère les versions disponibles avant installation.

2. Installer Apache, MariaDB, mod_perl et les modules Perl :
   ```bash
   sudo apt install apache2 mariadb-server mariadb-client \
     libapache2-mod-perl2 cpanminus gcc make tar gzip curl ca-certificates \
     libdbi-perl libdbd-mariadb-perl libxml-libxml-perl libxml-libxslt-perl \
     libjson-xs-perl libyaml-libyaml-perl libtext-csv-xs-perl \
     libtemplate-perl libtemplate-plugin-xml-perl libnet-ldap-perl \
     libnet-dns-perl libdatetime-perl libdatetime-timezone-perl \
     libmail-imapclient-perl libdata-uuid-perl libhash-merge-perl \
     libcrypt-eksblowfish-perl libspreadsheet-xlsx-perl libpackage-stash-perl
   ```
   👉 Explication : ces paquets fournissent le serveur web, la base et les dépendances Perl de Znuny.

3. Activer et démarrer les services :
   ```bash
   sudo systemctl enable --now apache2 mariadb
   ```
   👉 Explication : les deux services démarrent maintenant et à chaque redémarrage.

4. Contrôler qu'ils sont actifs :
   ```bash
   systemctl is-active apache2 mariadb
   ```
   👉 Explication : la commande doit afficher `active` deux fois.

5. Comparer la liste aux modules requis par la version, puis n'installer depuis CPAN que les modules manquants avec une procédure documentée.
   👉 Explication : CPAN ne doit servir qu'en dernier recours, pour garder un système maintenable.

## 2. Production — Contrôles

Comparer la liste de paquets aux prérequis de la version installée et figer la procédure dans la documentation d'exploitation.

## 3. Production — Sécurité

- Ne pas installer de modules CPAN sans revue de provenance.
- Ne pas exposer MariaDB hors de la boucle locale.

## Validation et retour arrière

- **Validation** : `systemctl is-active apache2 mariadb` renvoie `active` pour les deux services.
- **Retour arrière** : `sudo apt remove` des paquets installés si rien d'autre ne les utilise; sur une VM de test, restaurer le snapshot.

## Si le problème n'est pas résolu

- [Znuny — Installation officielle](https://doc.znuny.org/znuny/installation/index.html)
- [Znuny — Release 7.3.8](https://doc.znuny.org/znuny/releases/7_3_8/index.html)
- [Guide complet — installer les paquets système](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/42_Deploiement_Znuny_7_3_8_Debian_12.md#2-installer-les-paquets-systeme)

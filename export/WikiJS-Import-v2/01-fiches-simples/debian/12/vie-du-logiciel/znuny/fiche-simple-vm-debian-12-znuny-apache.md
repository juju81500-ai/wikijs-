---
title: "Fiche Simple - VM Debian 12 Znuny Apache"
description: "Activer modperl, charger la configuration Znuny et appliquer les permissions."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "znuny", "apache", "mod_perl"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_Znuny_Apache.md

- **Environnement** : VM Debian 12 dédiée (Apache/mod_perl, MariaDB 10.11), Znuny 7.3.8
- **OS / Version** : Debian 12 Bookworm; Znuny 7.3.8
- **Catégorie** : ITSM / ticketing
- **Tags** : `debian12`, `znuny`, `apache`, `mod_perl`

---

## Problème précis à résoudre

Activer mod_perl, charger la configuration Znuny et appliquer les permissions.

## 1. Hors-Production (Lab / Test / POC)

1. Activer le MPM prefork et mod_perl :
   ```bash
   sudo a2dismod mpm_event mpm_worker
   sudo a2enmod mpm_prefork perl
   ```
   👉 Explication : mod_perl exige le MPM prefork.

2. Installer la configuration Apache fournie par Znuny :
   ```bash
   sudo ln -s /opt/znuny/scripts/apache2-httpd.include.conf \
     /etc/apache2/conf-available/zzz_znuny.conf
   sudo a2enconf zzz_znuny
   ```
   👉 Explication : on réutilise le fichier officiel via un lien symbolique.

3. Appliquer les permissions Znuny :
   ```bash
   sudo /opt/znuny/bin/znuny.SetPermissions.pl
   ```
   👉 Explication : le script officiel donne les bons droits aux fichiers de l'application.

4. Tester la syntaxe puis recharger Apache :
   ```bash
   sudo apache2ctl configtest
   sudo systemctl restart apache2
   ```
   👉 Explication : on valide la configuration avant de redémarrer le service.

## 2. Production — Contrôles

Configurer un VirtualHost dédié avec nom DNS et TLS; si Apache héberge d'autres sites, valider l'impact du passage à prefork.

## 3. Production — Sécurité

- Ne pas exposer la page installateur au-delà de la mise en service.
- Activer HTTPS avec un certificat valide avant d'ouvrir l'accès aux utilisateurs.

## Validation et retour arrière

- **Validation** : `apache2ctl configtest` renvoie `Syntax OK`.
- **Retour arrière** : `sudo a2disconf zzz_znuny`, rétablir `mpm_event` (`sudo a2dismod mpm_prefork perl; sudo a2enmod mpm_event`) puis `sudo systemctl restart apache2`.

## Si le problème n'est pas résolu

- [Znuny — Installation officielle](https://doc.znuny.org/znuny/installation/index.html)
- [Znuny — Release 7.3.8](https://doc.znuny.org/znuny/releases/7_3_8/index.html)
- [Guide complet — configurer Apache et les permissions](/02-fiches-completes/debian/12/installation-deploiement/42-deploiement-znuny-7-3-8-debian-12#5-configurer-apache-et-les-permissions)
---
title: "Fiche Simple - VM Debian 12 iTop Installer Paquet Officiel"
description: "Déployer l'archive officielle iTop 3.3.0 avec des droits stricts."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "itop", "itsm", "cmdb", "apache", "mariadb"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_iTop_Installer_Paquet_Officiel.md

- **Environnement** : VM Linux dédiée avec Apache, PHP 8.2 ou 8.3 et MariaDB 10.11 (serveur ITSM/CMDB)
- **OS / Version** : Debian 12 Bookworm (ou Ubuntu Server 24.04 LTS); iTop Community 3.3.0
- **Catégorie** : ITSM / CMDB / helpdesk
- **Tags** : `debian12`, `itop`, `itsm`, `cmdb`, `apache`, `mariadb`

---

## Problème précis à résoudre

Déployer l'archive officielle iTop 3.3.0 avec des droits stricts.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le paquet installable 3.3.0 (pas l'archive source GitHub) dans le répertoire personnel :
   ```bash
   curl -fL https://github.com/Combodo/iTop/releases/download/3.3.0/iTop-3.3.0-21411.zip -o ~/itop.zip
   ```
   👉 Explication : récupère l'archive officielle; vérifier une somme ou signature publiée avant déploiement.

2. Créer le répertoire de l'application :
   ```bash
   sudo install -d -o root -g www-data -m 0750 /var/www/itop
   ```
   👉 Explication : le répertoire appartient à root, lisible par Apache.

3. Décompresser et placer les fichiers :
   ```bash
   sudo unzip ~/itop.zip 'web/*' -d /var/www/itop
   sudo mv /var/www/itop/web/* /var/www/itop/
   sudo rmdir /var/www/itop/web
   ```
   👉 Explication : extrait uniquement le dossier `web` à la racine voulue.

4. Créer les répertoires de données inscriptibles :
   ```bash
   sudo install -d -o www-data -g www-data -m 0750 \
     /var/www/itop/data /var/www/itop/log /var/www/itop/conf \
     /var/www/itop/env-production /var/www/itop/env-production-build \
     /var/www/itop/env-test /var/www/itop/env-test-build
   ```
   👉 Explication : seul Apache écrit dans ces répertoires précis.

## 2. Production — Contrôles

Archiver la somme de l'archive contrôlée et la version déployée.

## 3. Production — Sécurité

- Ne jamais appliquer `777` au répertoire Web.
- Utiliser le paquet officiel, jamais l'archive de sources.

## Validation et retour arrière

- **Validation** : `/var/www/itop` contient les fichiers iTop avec les bons propriétaires (`ls -l /var/www/itop`).
- **Retour arrière** : supprimer `/var/www/itop` et `~/itop.zip` si l'assistant n'a pas encore été exécuté.

## Si le problème n'est pas résolu

- [iTop — release 3.3.0](https://github.com/Combodo/iTop/releases/tag/3.3.0)
- [iTop — installation et mise à niveau](https://www.itophub.io/wiki/page?id=latest:install:start)
- [Guide complet](/02-fiches-completes/transverses/multi-os/installation-deploiement/40-deploiement-itop-3-3-debian12-ubuntu2404#4-installer-le-paquet-officiel)
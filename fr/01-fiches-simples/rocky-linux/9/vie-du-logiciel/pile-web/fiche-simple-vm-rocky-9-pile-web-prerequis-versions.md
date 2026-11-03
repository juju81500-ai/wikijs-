---
title: "fiche-simple-vm-rocky-9-pile-web-prerequis-versions"
description: "Choisir les versions PHP, Nginx et MariaDB avant d'installer, sans les supposer."
published: true
date: 2026-11-03T14:22:28Z
tags: ["rocky9", "nginx", "php-fpm", "mariadb", "selinux"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# fiche-simple-vm-rocky-9-pile-web-prerequis-versions.md

- **Environnement** : [[Glossary:VM]] ou serveur Rocky Linux 9 hébergeant une application PHP avec MariaDB locale
- **OS / Version** : Rocky Linux 9 / [[Glossary:RHEL]] 9; Nginx, PHP-FPM et MariaDB des dépôts actifs
- **Catégorie** : services web / prérequis
- **Tags** : `rocky9`, `nginx`, `php-fpm`, `mariadb`, `selinux`

---

## Problème précis à résoudre

Choisir les versions PHP, Nginx et MariaDB avant d'installer, sans les supposer.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les versions disponibles :
   ```bash
   cat /etc/rocky-release
   sudo dnf module list php
   sudo dnf info nginx php-fpm mariadb-server
   ```
   👉 Explication : Affiche la version de Rocky, les streams PHP proposés et les versions candidates des paquets.

2. Noter hostname/FQDN, [[Glossary:IP]] stable, stockage, ports, sauvegardes et accès console.
   👉 Explication : ces éléments sont à figer avant l'installation.

## 2. Production — Contrôles

Valider le stream PHP par rapport à l'application à héberger.

## 3. Production — Sécurité

- N'utiliser que les dépôts Rocky approuvés.

## Validation et retour arrière

- **Validation** : versions candidates relevées et compatibles avec l'application.
- **Retour arrière** : aucun changement n'a été fait.

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet — étape 1](/fr/02-fiches-completes/rocky-linux/9/installation-deploiement/23-pile-web-rocky-linux-9-nginx-php-mariadb#1-prerequis-et-choix-des-versions)
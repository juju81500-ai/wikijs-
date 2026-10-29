---
title: "Fiche Simple - VM Debian 13 OCS Inventory PostgreSQL"
description: "Installer PostgreSQL 17 et créer un rôle et une base dédiés à OCS Inventory."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "ocs-inventory", "ocs3", "postgresql", "nginx", "base-de-donnees"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_OCS_Inventory_PostgreSQL.md

- **Environnement** : VM Debian 13 dédiée, OCS Inventory 3.0 (Nginx, uWSGI, PostgreSQL local)
- **OS / Version** : Debian 13 Trixie; OCS Inventory 3.0; PostgreSQL 17
- **Catégorie** : inventaire de parc / ITSM
- **Tags** : `debian13`, `ocs-inventory`, `ocs3`, `postgresql`, `nginx`, `base-de-donnees`

---

## Problème précis à résoudre

Installer PostgreSQL 17 et créer un rôle et une base dédiés à OCS Inventory.

## 1. Hors-Production (Lab / Test / POC)

1. Installer PostgreSQL depuis les dépôts Debian :
   ```bash
   sudo apt update
   apt-cache policy postgresql
   sudo apt install postgresql postgresql-contrib
   sudo systemctl enable --now postgresql
   psql --version
   ```
   👉 Explication : on contrôle la version candidate (17 sur Debian 13), on installe, on démarre et on active le service.

2. Ouvrir une session `psql` en tant que compte postgres :
   ```bash
   sudo -u postgres psql
   ```
   👉 Explication : le script SQL suivant se saisit dans cette invite interactive.

3. Dans `psql`, créer le rôle, saisir son mot de passe à l'invite, puis créer la base (`ocsuser` et `ocsdb` sont des noms d'exemple à adapter) :
   ```bash
   CREATE ROLE ocsuser LOGIN;
   \password ocsuser
   CREATE DATABASE ocsdb OWNER ocsuser ENCODING 'UTF8';
   \q
   ```
   👉 Explication : `\password` demande le mot de passe sans l'afficher : il n'apparaît ni dans un script ni dans l'historique.

4. Vérifier que PostgreSQL n'écoute que sur loopback :
   ```bash
   sudo ss -tlnp | grep 5432
   ```
   👉 Explication : avec backend et base sur la même VM, le port 5432 ne doit pas être ouvert au réseau.

## 2. Production — Contrôles

Prévoir la politique de mot de passe du rôle, la sauvegarde de la base et le dimensionnement du stockage.

## 3. Production — Sécurité

- Ne jamais passer le mot de passe en argument de commande.
- Ne pas ouvrir 5432 au réseau pour une architecture monohôte.

## Validation et retour arrière

- **Validation** : `psql --version` répond, la base `ocsdb` existe (`sudo -u postgres psql -l`) et 5432 est sur loopback.
- **Retour arrière** : Lab uniquement : `sudo -u postgres psql -c 'DROP DATABASE ocsdb;'` puis `DROP ROLE ocsuser;` après sauvegarde.

## Si le problème n'est pas résolu

- [OCS Inventory — Installation essentielle](https://documentation.ocsinventory-ng.org/quickstart-guides/for-administrators/installation-essentials.md)
- [PostgreSQL — documentation](https://www.postgresql.org/docs/17/)
- [Guide complet OCS Inventory 3 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/41-deploiement-ocs-inventory-3-debian-13#2-installer-postgresql-et-creer-la-base)
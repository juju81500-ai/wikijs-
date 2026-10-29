---
title: "Fiche Simple - VM Debian 13 OCS Inventory Sauvegarde"
description: "Sauvegarder base, configuration et clé d'encryption OCS, puis cadrer les mises à jour."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "ocs-inventory", "ocs3", "postgresql", "nginx", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_OCS_Inventory_Sauvegarde.md

- **Environnement** : VM Debian 13 dédiée, OCS Inventory 3.0 (Nginx, uWSGI, PostgreSQL local)
- **OS / Version** : Debian 13 Trixie; OCS Inventory 3.0; PostgreSQL 17
- **Catégorie** : inventaire de parc / ITSM
- **Tags** : `debian13`, `ocs-inventory`, `ocs3`, `postgresql`, `nginx`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder base, configuration et clé d'encryption OCS, puis cadrer les mises à jour.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter la base PostgreSQL (`ocsdb` est un nom d'exemple) vers un répertoire protégé :
   ```bash
   install -d -m 0700 "$HOME/sauvegardes-ocs"
   sudo -u postgres pg_dump -Fc ocsdb > "$HOME/sauvegardes-ocs/ocsdb.dump"
   ```
   👉 Explication : `pg_dump -Fc` produit une archive restaurable avec `pg_restore`.

2. Copier la configuration, les vhosts et les clés OCS, en particulier la clé d'encryption :
   ```bash
   sudo tar -czf "$HOME/sauvegardes-ocs/ocs-config.tar.gz" /etc/nginx/sites-available /etc/ocsinventory-backend
   ```
   👉 Explication : la clé d'encryption protège les valeurs sensibles stockées en base; sans elle la restauration est incomplète. Ajuster les chemins à votre installation.

3. Chiffrer les archives puis les copier hors VM.
   👉 Explication : une sauvegarde sur la même VM ne protège pas d'une perte de l'hôte.

4. Avant une mise à jour, sauvegarder, lire les notes de version, mettre à jour depuis les dépôts officiels et tester un agent pilote :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade ocsinventory-server
   ```
   👉 Explication : limite le risque de régression sur le parc.

## 2. Production — Contrôles

Planifier sauvegardes, durée de rétention, test de restauration trimestriel dans un environnement isolé.

## 3. Production — Sécurité

- Restaurer dans un environnement isolé sans reconnecter les agents de production.
- Chiffrer les archives qui contiennent la clé d'encryption.

## Validation et retour arrière

- **Validation** : Dump lisible par `pg_restore --list` et restauration testée en isolé.
- **Retour arrière** : Restaurer le dump et la configuration sauvegardés avant la mise à jour.

## Si le problème n'est pas résolu

- [OCS Inventory — Installation essentielle](https://documentation.ocsinventory-ng.org/quickstart-guides/for-administrators/installation-essentials.md)
- [PostgreSQL — pg_dump](https://www.postgresql.org/docs/17/app-pgdump.html)
- [Guide complet OCS Inventory 3 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/41-deploiement-ocs-inventory-3-debian-13#8-sauvegarde-et-exploitation)
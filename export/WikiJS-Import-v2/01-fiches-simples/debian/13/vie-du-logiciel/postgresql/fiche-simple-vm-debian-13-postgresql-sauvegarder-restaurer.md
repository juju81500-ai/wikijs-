---
title: "Fiche Simple - VM Debian 13 PostgreSQL Sauvegarder Restaurer"
description: "Sauvegarder une base et les objets globaux PostgreSQL et prouver la restauration."
published: true
date: 2026-10-29T20:35:13Z
tags: ["debian13", "postgresql", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:35:13Z
dateModified: 2026-10-29T20:35:13Z
---

# Fiche_Simple_-_VM_Debian_13_PostgreSQL_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; PostgreSQL 17 des dépôts Debian
- **Catégorie** : base de données / PostgreSQL / Sauvegarder et restaurer
- **Tags** : `debian13`, `postgresql`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder une base et les objets globaux PostgreSQL et prouver la restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder une base au format personnalisé :
   ```bash
   sudo install -d -o postgres -g postgres -m 0700 /var/backups/postgresql
   sudo -u postgres pg_dump -Fc APPDB -f /var/backups/postgresql/APPDB-$(date +%F).dump
   ```
   👉 Explication : remplacer `APPDB` (à remplacer) ; le format `-Fc` est compressé et restaurable avec `pg_restore`.

2. Sauvegarder les rôles et objets globaux :
   ```bash
   sudo -u postgres pg_dumpall --globals-only -f /var/backups/postgresql/globals-$(date +%F).sql
   ```
   👉 Explication : rôles et tablespaces ne sont pas inclus dans `pg_dump`.

3. Restaurer sur un serveur de test :
   ```bash
   sudo -u postgres createdb APPDB_TEST
   sudo -u postgres pg_restore -d APPDB_TEST /var/backups/postgresql/APPDB-DATE.dump
   ```
   👉 Explication : remplacer `DATE` (à remplacer) ; vérifier ensuite le nombre d'objets et de lignes.

4. Contrôler l'archive :
   ```bash
   sudo -u postgres pg_restore --list /var/backups/postgresql/APPDB-DATE.dump | head
   ```
   👉 Explication : si la liste s'affiche, l'archive est lisible.

## 2. Production — Contrôles

Sauvegarde planifiée et chiffrée, copie hors site, test de restauration régulier ; pour la restauration à un instant donné, étudier l'archivage WAL (`pg_basebackup`).

## 3. Production — Sécurité

- Chiffrer les copies.
- Dossier de sauvegarde en `0700`.
- Ne pas stocker sur le même disque.

## Validation et retour arrière

- **Validation** : restauration testée sur base distincte.
- **Retour arrière** : reprendre la sauvegarde précédente ; ne pas écraser la production sans copie préalable.

## Si le problème n'est pas résolu

- [PostgreSQL — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-prerequis-limites)
- [PostgreSQL — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-configurer)
- [PostgreSQL — Sécuriser (TLS, pg_hba, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-securiser)
- [PostgreSQL — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-valider)
- [PostgreSQL — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-mettre-a-jour)
- [Installation PostgreSQL 17 (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-database-installation-postgresql-17)
- [PostgreSQL — documentation officielle](https://www.postgresql.org/docs/)
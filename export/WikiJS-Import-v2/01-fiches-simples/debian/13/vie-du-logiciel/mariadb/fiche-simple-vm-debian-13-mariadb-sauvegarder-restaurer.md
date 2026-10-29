---
title: "Fiche Simple - VM Debian 13 MariaDB Sauvegarder Restaurer"
description: "Réaliser une sauvegarde logique cohérente de MariaDB et la restaurer sur un serveur de test."
published: true
date: 2026-10-29T20:35:13Z
tags: ["debian13", "mariadb", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:35:13Z
dateModified: 2026-10-29T20:35:13Z
---

# Fiche_Simple_-_VM_Debian_13_MariaDB_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MariaDB des dépôts Debian
- **Catégorie** : base de données / MariaDB / Sauvegarder et restaurer
- **Tags** : `debian13`, `mariadb`, `sauvegarde`

---

## Problème précis à résoudre

Réaliser une sauvegarde logique cohérente de MariaDB et la restaurer sur un serveur de test.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder toutes les bases :
   ```bash
   sudo install -d -m 0700 /var/backups/mariadb
   sudo sh -c 'mariadb-dump --single-transaction --routines --events --all-databases | gzip > /var/backups/mariadb/all-$(date +%F).sql.gz'
   ```
   👉 Explication : `--single-transaction` donne un instantané cohérent pour InnoDB sans verrouiller ; dossier en `0700`.

2. Contrôler l'archive :
   ```bash
   gzip -t /var/backups/mariadb/all-$(date +%F).sql.gz && echo OK
   ```
   👉 Explication : intégrité de la compression.

3. Restaurer sur un serveur de test :
   ```bash
   sudo sh -c 'gunzip -c /var/backups/mariadb/all-DATE.sql.gz | mariadb'
   ```
   👉 Explication : remplacer `DATE` (à remplacer) ; jamais sur la production sans validation préalable.

4. Vérifier les données restaurées :
   ```bash
   sudo mariadb -e 'SHOW DATABASES;'
   ```
   👉 Explication : les bases attendues sont présentes.

## 2. Production — Contrôles

Sauvegarde planifiée, chiffrée, copiée hors site, avec test de restauration régulier ; pour de gros volumes, évaluer `mariadb-backup` (sauvegarde physique, paquet `mariadb-backup`).

## 3. Production — Sécurité

- Chiffrer les copies (elles contiennent des données et des hachages de mots de passe).
- Droits `0700` sur le dossier.
- Ne pas stocker sur le même disque.

## Validation et retour arrière

- **Validation** : restauration testée sur un serveur distinct.
- **Retour arrière** : en cas d'échec, reprendre la sauvegarde précédente ; la production n'est jamais écrasée sans copie préalable.

## Si le problème n'est pas résolu

- [MariaDB — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-prerequis-limites)
- [MariaDB — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-configurer)
- [MariaDB — Sécuriser (TLS, comptes, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-securiser)
- [MariaDB — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-valider)
- [MariaDB — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-mettre-a-jour)
- [Guide complet LEMP Debian 13 (MariaDB)](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb)
- [Installation MariaDB 11 (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-database-installation-mariadb-11)
- [Durcissement MariaDB (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-lemp-securiser-mariadb)
- [MariaDB — documentation officielle](https://mariadb.com/kb/en/documentation/)
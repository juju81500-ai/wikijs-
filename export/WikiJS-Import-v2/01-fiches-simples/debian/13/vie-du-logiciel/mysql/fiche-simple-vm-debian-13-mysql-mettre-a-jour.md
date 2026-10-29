---
title: "Fiche Simple - VM Debian 13 MySQL Mettre A Jour"
description: "Mettre à jour MySQL avec un retour arrière fondé sur sauvegarde et instantané."
published: true
date: 2026-10-29T20:37:00Z
tags: ["debian13", "mysql", "mise-a-jour"]
editor: markdown
dateCreated: 2026-10-29T20:37:00Z
dateModified: 2026-10-29T20:37:00Z
---

# Fiche_Simple_-_VM_Debian_13_MySQL_Mettre_A_Jour

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MySQL Community (dépôt officiel Oracle)
- **Catégorie** : base de données / MySQL / Mise à jour et retour arrière
- **Tags** : `debian13`, `mysql`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour MySQL avec un retour arrière fondé sur sauvegarde et instantané.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder :
   ```bash
   sudo sh -c 'mysqldump --defaults-extra-file=/root/.my-backup.cnf --single-transaction --routines --events --all-databases | gzip > /var/backups/mysql/avant-maj-$(date +%F).sql.gz'
   sudo tar -czpf /var/backups/mysql/conf-$(date +%F).tar.gz /etc/mysql
   ```
   👉 Explication : données et configuration ; ajouter un instantané de VM.

2. Lister la mise à jour :
   ```bash
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -i mysql
   mysql --version
   ```
   👉 Explication : lire les notes de version ; une montée majeure se teste sur copie.

3. Appliquer :
   ```bash
   sudo apt install --only-upgrade mysql-server
   systemctl is-active mysql
   mysql -u root -p -e 'SELECT VERSION();'
   ```
   👉 Explication : depuis 8.0.16+, le serveur met à niveau le dictionnaire de données au démarrage.

4. Retour arrière :
   ```bash
   sudo systemctl stop mysql
   # restaurer l'instantané de VM, ou réinstaller la version précédente sur une VM saine puis :
   sudo sh -c 'gunzip -c /var/backups/mysql/avant-maj-DATE.sql.gz | mysql -u root -p'
   ```
   👉 Explication : le retour de version n'est pas supporté en place : instantané ou restauration logique. Remplacer `DATE` (à remplacer).

## 2. Production — Contrôles

Pilote d'abord, fenêtre approuvée, instantané préalable, surveillance ensuite.

## 3. Production — Sécurité

- Pas de montée majeure sans test sur copie.
- Garder les sauvegardes jusqu'à validation.
- Prévenir les applications.

## Validation et retour arrière

- **Validation** : `SELECT VERSION()` affiche la version cible et les applications fonctionnent.
- **Retour arrière** : restaurer l'instantané ou la sauvegarde logique.

## Si le problème n'est pas résolu

- [MySQL — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-prerequis-limites)
- [MySQL — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-installer)
- [MySQL — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-configurer)
- [MySQL — Sécuriser (TLS, comptes, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-securiser)
- [MySQL — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-valider)
- [MySQL — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-sauvegarder-restaurer)
- [MySQL — documentation officielle](https://dev.mysql.com/doc/)
- [Alternative MariaDB (fiches du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-prerequis-limites)
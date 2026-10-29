---
title: "Fiche Simple - VM Debian 13 MariaDB Valider"
description: "Prouver que MariaDB est opérationnel, sécurisé et supervisable."
published: true
date: 2026-10-29T20:35:13Z
tags: ["debian13", "mariadb", "recette"]
editor: markdown
dateCreated: 2026-10-29T20:35:13Z
dateModified: 2026-10-29T20:35:13Z
---

# Fiche_Simple_-_VM_Debian_13_MariaDB_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MariaDB des dépôts Debian
- **Catégorie** : base de données / MariaDB / Valider (recette)
- **Tags** : `debian13`, `mariadb`, `recette`

---

## Problème précis à résoudre

Prouver que MariaDB est opérationnel, sécurisé et supervisable.

## 1. Hors-Production (Lab / Test / POC)

1. État du service :
   ```bash
   systemctl is-active mariadb
   sudo mariadb -e 'SELECT VERSION(); SHOW DATABASES;'
   ```
   👉 Explication : service actif, version attendue.

2. Contrôler les comptes et l'écoute :
   ```bash
   sudo mariadb -e "SELECT user,host FROM mysql.user;"
   sudo ss -tlnp | grep -E 'mariadbd|mysqld'
   ```
   👉 Explication : pas de compte anonyme ni `root@%` ; seule l'adresse prévue écoute.

3. Tester une connexion applicative avec TLS :
   ```bash
   mariadb -h IP_SERVEUR -u APPUSER -p --ssl -e "SHOW STATUS LIKE 'Ssl_cipher';"
   ```
   👉 Explication : `Ssl_cipher` non vide prouve le chiffrement (option TLS du client à adapter à sa version).

4. Écrire et relire une donnée de test :
   ```bash
   sudo mariadb APPDB -e "CREATE TABLE recette(id INT); INSERT INTO recette VALUES (1); SELECT * FROM recette; DROP TABLE recette;"
   ```
   👉 Explication : vérifie lecture/écriture ; la table de test est supprimée.

## 2. Production — Contrôles

Consigner la recette et activer la supervision (disponibilité, connexions, espace disque, requêtes lentes).

## 3. Production — Sécurité

- Supprimer toute donnée ou table de test.
- Ne pas laisser de compte de recette.
- Surveiller `/var/log/mysql/` sans y exposer de secrets.

## Validation et retour arrière

- **Validation** : tous les contrôles réussis.
- **Retour arrière** : revenir à la configuration précédente et relancer la recette.

## Si le problème n'est pas résolu

- [MariaDB — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-prerequis-limites)
- [MariaDB — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-configurer)
- [MariaDB — Sécuriser (TLS, comptes, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-securiser)
- [MariaDB — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-sauvegarder-restaurer)
- [MariaDB — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-mettre-a-jour)
- [Guide complet LEMP Debian 13 (MariaDB)](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb)
- [Installation MariaDB 11 (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-database-installation-mariadb-11)
- [Durcissement MariaDB (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-lemp-securiser-mariadb)
- [MariaDB — documentation officielle](https://mariadb.com/kb/en/documentation/)
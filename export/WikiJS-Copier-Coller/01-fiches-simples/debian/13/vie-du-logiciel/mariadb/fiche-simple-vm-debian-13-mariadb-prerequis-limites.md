# Fiche_Simple_-_VM_Debian_13_MariaDB_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MariaDB des dépôts Debian
- **Catégorie** : base de données / MariaDB / Prérequis et limites

---

## Problème précis à résoudre

Cadrer l'exploitation de MariaDB sur Debian 13 avant de configurer, sécuriser et sauvegarder le serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'OS, la version candidate et l'espace disque :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   apt-cache policy mariadb-server
   df -h /var/lib/mysql /var/backups
   ```
   👉 Explication : la version de MariaDB est celle du dépôt Debian (à vérifier) ; prévoir 2 à 3 fois la taille des données pour sauvegardes et croissance.

2. Contrôler que le serveur est installé (sinon voir la fiche d'installation existante) :
   ```bash
   systemctl status mariadb --no-pager
   mariadb --version
   ```
   👉 Explication : l'installation est décrite dans la fiche `Database_Installation_MariaDB_11` du pack.

3. Lister les besoins applicatifs :
   👉 Explication : bases à créer, comptes applicatifs, adresses IP des clients, volumétrie, RPO/RTO attendus.

## 2. Production — Contrôles

Consigner version, volumétrie, clients autorisés, responsable, RPO/RTO et fenêtre de maintenance.

## 3. Production — Sécurité

- Pas d'exposition réseau avant la fiche Sécuriser.
- Prévoir un compte d'administration nominatif.
- Limites : serveur unique ; réplication et Galera hors périmètre de cette série.

## Validation et retour arrière

- **Validation** : périmètre et espace disque confirmés, service actif.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [MariaDB — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-configurer)
- [MariaDB — Sécuriser (TLS, comptes, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-securiser)
- [MariaDB — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-valider)
- [MariaDB — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-sauvegarder-restaurer)
- [MariaDB — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-mettre-a-jour)
- [Guide complet LEMP Debian 13 (MariaDB)](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb)
- [Installation MariaDB 11 (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-database-installation-mariadb-11)
- [Durcissement MariaDB (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-lemp-securiser-mariadb)
- [MariaDB — documentation officielle](https://mariadb.com/kb/en/documentation/)
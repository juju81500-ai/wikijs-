# Fiche_Simple_-_VM_Debian_13_MariaDB_Mettre_A_Jour

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MariaDB des dépôts Debian
- **Catégorie** : base de données / MariaDB / Mise à jour et retour arrière
- **Tags** : `debian13`, `mariadb`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour MariaDB (correctifs) avec un plan de retour arrière fondé sur la sauvegarde.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder avant la mise à jour :
   ```bash
   sudo sh -c 'mariadb-dump --single-transaction --routines --events --all-databases | gzip > /var/backups/mariadb/avant-maj-$(date +%F).sql.gz'
   sudo tar -czpf /var/backups/mariadb/conf-$(date +%F).tar.gz /etc/mysql
   ```
   👉 Explication : sauvegarde des données ET de la configuration ; faire aussi un instantané de la VM.

2. Lister la mise à jour disponible :
   ```bash
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -i mariadb
   mariadb --version
   ```
   👉 Explication : lire les notes de version ; une montée de version majeure se teste d'abord sur une copie.

3. Appliquer :
   ```bash
   sudo apt install --only-upgrade mariadb-server mariadb-client
   systemctl is-active mariadb
   sudo mariadb -e 'SELECT VERSION();'
   ```
   👉 Explication : les mises à jour mineures Debian exécutent la mise à niveau des tables ; en cas de doute lancer `sudo mariadb-upgrade`.

4. Revenir en arrière :
   ```bash
   sudo systemctl stop mariadb
   # restaurer l'instantané de la VM, ou réinstaller la version précédente sur une VM saine puis :
   sudo sh -c 'gunzip -c /var/backups/mariadb/avant-maj-DATE.sql.gz | mariadb'
   ```
   👉 Explication : le retour de version d'un serveur de base n'est pas supporté directement : l'instantané de VM ou la restauration logique est la voie de retour. Remplacer `DATE` (à remplacer).

## 2. Production — Contrôles

Pilote d'abord, fenêtre approuvée, instantané préalable, surveillance des journaux et des performances ensuite.

## 3. Production — Sécurité

- Pas de mise à jour majeure sans test sur copie.
- Sauvegardes conservées jusqu'à validation.
- Prévenir les applications avant l'arrêt.

## Validation et retour arrière

- **Validation** : `SELECT VERSION()` affiche la version cible, les applications fonctionnent.
- **Retour arrière** : restaurer l'instantané de VM ou la sauvegarde logique.

## Si le problème n'est pas résolu

- [MariaDB — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_MariaDB_Prerequis_Limites.md)
- [MariaDB — Configurer](Fiche_Simple_-_VM_Debian_13_MariaDB_Configurer.md)
- [MariaDB — Sécuriser (TLS, comptes, pare-feu)](Fiche_Simple_-_VM_Debian_13_MariaDB_Securiser.md)
- [MariaDB — Valider (recette)](Fiche_Simple_-_VM_Debian_13_MariaDB_Valider.md)
- [MariaDB — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_MariaDB_Sauvegarder_Restaurer.md)
- [Guide complet LEMP Debian 13 (MariaDB)](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/02_Pile_LEMP_Debian_13_Nginx_PHP_MariaDB.md)
- [Installation MariaDB 11 (fiche du pack)](Fiche_Simple_-_VM_Debian_13_Database_Installation_MariaDB_11.md)
- [Durcissement MariaDB (fiche du pack)](Fiche_Simple_-_VM_Debian_13_LEMP_Securiser_MariaDB.md)
- [MariaDB — documentation officielle](https://mariadb.com/kb/en/documentation/)

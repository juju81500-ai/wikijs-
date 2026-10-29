# Fiche_Simple_-_VM_Debian_13_PostgreSQL_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; PostgreSQL 17 des dépôts Debian
- **Catégorie** : base de données / PostgreSQL / Prérequis et limites

---

## Problème précis à résoudre

Cadrer l'exploitation de PostgreSQL sur Debian 13 avant configuration, sécurisation et sauvegarde.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'OS, la version et les clusters :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   apt-cache policy postgresql
   pg_lsclusters
   ```
   👉 Explication : Debian 13 fournit PostgreSQL 17 (à vérifier) ; `pg_lsclusters` liste les clusters, port et statut.

2. Contrôler l'espace disque :
   ```bash
   df -h /var/lib/postgresql /var/backups
   ```
   👉 Explication : prévoir de l'espace pour les sauvegardes et les journaux WAL.

3. Lister les besoins :
   👉 Explication : bases, rôles applicatifs, IP clientes, volumétrie, RPO/RTO.

## 2. Production — Contrôles

Consigner version, volumétrie, clients autorisés, responsable, RPO/RTO.

## 3. Production — Sécurité

- Pas d'exposition réseau avant la fiche Sécuriser.
- Limites : serveur unique ; réplication et haute disponibilité hors périmètre.
- Le compte `postgres` n'est utilisé que pour l'administration.

## Validation et retour arrière

- **Validation** : version, cluster et espace disque confirmés.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [PostgreSQL — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-configurer)
- [PostgreSQL — Sécuriser (TLS, pg_hba, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-securiser)
- [PostgreSQL — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-valider)
- [PostgreSQL — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-sauvegarder-restaurer)
- [PostgreSQL — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-mettre-a-jour)
- [Installation PostgreSQL 17 (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-database-installation-postgresql-17)
- [PostgreSQL — documentation officielle](https://www.postgresql.org/docs/)
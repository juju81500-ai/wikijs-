# Fiche_Simple_-_VM_Debian_13_PostgreSQL_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; PostgreSQL 17 des dépôts Debian
- **Catégorie** : base de données / PostgreSQL / Prérequis et limites
- **Tags** : `debian13`, `postgresql`, `prerequis`

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

- [PostgreSQL — Configurer](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Configurer.md)
- [PostgreSQL — Sécuriser (TLS, pg_hba, pare-feu)](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Securiser.md)
- [PostgreSQL — Valider (recette)](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Valider.md)
- [PostgreSQL — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Sauvegarder_Restaurer.md)
- [PostgreSQL — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Mettre_A_Jour.md)
- [Installation PostgreSQL 17 (fiche du pack)](Fiche_Simple_-_VM_Debian_13_Database_Installation_PostgreSQL_17.md)
- [PostgreSQL — documentation officielle](https://www.postgresql.org/docs/)

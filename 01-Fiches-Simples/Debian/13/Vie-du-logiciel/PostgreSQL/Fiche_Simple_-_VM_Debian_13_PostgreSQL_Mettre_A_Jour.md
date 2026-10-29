# Fiche_Simple_-_VM_Debian_13_PostgreSQL_Mettre_A_Jour

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; PostgreSQL 17 des dépôts Debian
- **Catégorie** : base de données / PostgreSQL / Mise à jour et retour arrière
- **Tags** : `debian13`, `postgresql`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour PostgreSQL (mineure ou majeure) avec un retour arrière fondé sur la sauvegarde.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder :
   ```bash
   sudo -u postgres pg_dumpall -f /var/backups/postgresql/avant-maj-$(date +%F).sql
   sudo tar -czpf /var/backups/postgresql/conf-$(date +%F).tar.gz /etc/postgresql
   ```
   👉 Explication : sauvegarde complète et configuration ; ajouter un instantané de VM.

2. Mise à jour mineure :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade postgresql postgresql-17
   pg_lsclusters
   ```
   👉 Explication : les versions mineures ne changent pas le format de données ; un redémarrage est nécessaire.

3. Mise à jour majeure (nouvelle version installée côte à côte) :
   ```bash
   sudo apt install postgresql-NOUVELLE_VERSION
   sudo pg_upgradecluster 17 main
   ```
   👉 Explication : remplacer `NOUVELLE_VERSION` (à remplacer, vérifier la disponibilité) ; l'ancien cluster est conservé arrêté jusqu'à validation.

4. Retour arrière :
   ```bash
   sudo pg_dropcluster NOUVELLE_VERSION main --stop
   sudo pg_ctlcluster 17 main start
   pg_lsclusters
   ```
   👉 Explication : tant que l'ancien cluster n'est pas supprimé, il reste la voie de retour ; sinon restaurer la sauvegarde ou l'instantané.

## 2. Production — Contrôles

Pilote d'abord, fenêtre approuvée, instantané préalable ; supprimer l'ancien cluster (`pg_dropcluster 17 main`) seulement après validation complète.

## 3. Production — Sécurité

- Pas de mise à jour majeure sans test sur copie.
- Conserver les sauvegardes jusqu'à validation.
- Relancer `ANALYZE` après une montée majeure.

## Validation et retour arrière

- **Validation** : `SELECT version()` renvoie la version cible et les applications fonctionnent.
- **Retour arrière** : relancer l'ancien cluster, ou restaurer l'instantané/la sauvegarde.

## Si le problème n'est pas résolu

- [PostgreSQL — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Prerequis_Limites.md)
- [PostgreSQL — Configurer](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Configurer.md)
- [PostgreSQL — Sécuriser (TLS, pg_hba, pare-feu)](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Securiser.md)
- [PostgreSQL — Valider (recette)](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Valider.md)
- [PostgreSQL — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Sauvegarder_Restaurer.md)
- [Installation PostgreSQL 17 (fiche du pack)](Fiche_Simple_-_VM_Debian_13_Database_Installation_PostgreSQL_17.md)
- [PostgreSQL — documentation officielle](https://www.postgresql.org/docs/)

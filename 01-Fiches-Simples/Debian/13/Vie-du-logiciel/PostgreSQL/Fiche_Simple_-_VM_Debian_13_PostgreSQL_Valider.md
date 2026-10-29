# Fiche_Simple_-_VM_Debian_13_PostgreSQL_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; PostgreSQL 17 des dépôts Debian
- **Catégorie** : base de données / PostgreSQL / Valider (recette)
- **Tags** : `debian13`, `postgresql`, `recette`

---

## Problème précis à résoudre

Prouver que PostgreSQL est opérationnel, chiffré et supervisable.

## 1. Hors-Production (Lab / Test / POC)

1. État du cluster et du service :
   ```bash
   pg_lsclusters
   sudo -u postgres psql -c 'SELECT version();'
   ```
   👉 Explication : cluster `online`.

2. Contrôler l'écoute et pg_hba :
   ```bash
   sudo ss -tlnp | grep 5432
   sudo -u postgres psql -c 'SELECT type,database,user_name,address,auth_method FROM pg_hba_file_rules;'
   ```
   👉 Explication : aucune règle `trust`.

3. Vérifier TLS :
   ```bash
   sudo -u postgres psql -c 'SHOW ssl;'
   psql 'host=IP_SERVEUR sslmode=require dbname=APPDB user=APPUSER' -c 'SELECT ssl, version FROM pg_stat_ssl WHERE pid = pg_backend_pid();'
   ```
   👉 Explication : `ssl = t` prouve le chiffrement de la session.

4. Écrire et relire une donnée de test :
   ```bash
   psql -h localhost -U APPUSER APPDB -c 'CREATE TABLE recette(id int); INSERT INTO recette VALUES (1); SELECT * FROM recette; DROP TABLE recette;'
   ```
   👉 Explication : vérifie droits et lecture/écriture.

## 2. Production — Contrôles

Consigner la recette, activer la supervision (disponibilité, connexions, espace disque, bloat).

## 3. Production — Sécurité

- Supprimer toute donnée de test.
- Pas de rôle de recette conservé.
- Surveiller `/var/log/postgresql/`.

## Validation et retour arrière

- **Validation** : tous les contrôles réussis.
- **Retour arrière** : revenir à la configuration précédente et relancer la recette.

## Si le problème n'est pas résolu

- [PostgreSQL — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Prerequis_Limites.md)
- [PostgreSQL — Configurer](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Configurer.md)
- [PostgreSQL — Sécuriser (TLS, pg_hba, pare-feu)](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Securiser.md)
- [PostgreSQL — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Sauvegarder_Restaurer.md)
- [PostgreSQL — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_PostgreSQL_Mettre_A_Jour.md)
- [Installation PostgreSQL 17 (fiche du pack)](Fiche_Simple_-_VM_Debian_13_Database_Installation_PostgreSQL_17.md)
- [PostgreSQL — documentation officielle](https://www.postgresql.org/docs/)

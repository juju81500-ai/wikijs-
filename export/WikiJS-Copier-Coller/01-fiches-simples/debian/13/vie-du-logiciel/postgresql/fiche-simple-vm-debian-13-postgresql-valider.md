# Fiche_Simple_-_VM_Debian_13_PostgreSQL_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; PostgreSQL 17 des dépôts Debian
- **Catégorie** : base de données / PostgreSQL / Valider (recette)

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

- [PostgreSQL — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-prerequis-limites)
- [PostgreSQL — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-configurer)
- [PostgreSQL — Sécuriser (TLS, pg_hba, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-securiser)
- [PostgreSQL — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-sauvegarder-restaurer)
- [PostgreSQL — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-mettre-a-jour)
- [Installation PostgreSQL 17 (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-database-installation-postgresql-17)
- [PostgreSQL — documentation officielle](https://www.postgresql.org/docs/)
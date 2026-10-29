# Fiche_Simple_-_VM_Debian_13_PostgreSQL_Configurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; PostgreSQL 17 des dépôts Debian
- **Catégorie** : base de données / PostgreSQL / Configurer

---

## Problème précis à résoudre

Configurer PostgreSQL (écoute, journalisation) et créer un rôle et une base applicatifs.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un fichier de configuration local :
   ```bash
   sudo tee /etc/postgresql/17/main/conf.d/60-local.conf >/dev/null <<'EOF'
   listen_addresses = 'localhost'
   log_connections = on
   log_disconnections = on
   log_min_duration_statement = 2000
   EOF
   sudo systemctl reload postgresql
   ```
   👉 Explication : adapter `17` à la version installée ; `conf.d` évite de modifier `postgresql.conf`.

2. Créer un rôle (mot de passe saisi) et une base :
   ```bash
   sudo -u postgres createuser --pwprompt APPUSER
   sudo -u postgres createdb --owner=APPUSER APPDB
   ```
   👉 Explication : remplacer `APPUSER` et `APPDB` (à remplacer) ; le mot de passe est demandé de façon interactive.

3. Révoquer les droits par défaut sur la base :
   ```bash
   sudo -u postgres psql -d APPDB -c 'REVOKE ALL ON SCHEMA public FROM PUBLIC; GRANT ALL ON SCHEMA public TO APPUSER;'
   ```
   👉 Explication : réduit les accès implicites du schéma `public`.

4. Contrôler :
   ```bash
   sudo -u postgres psql -c '\du' -c '\l'
   ```
   👉 Explication : un rôle par application, propriétaire de sa base.

## 2. Production — Contrôles

Configuration versionnée, un rôle par application, jamais d'application connectée en `postgres`.

## 3. Production — Sécurité

- Pas de rôle `SUPERUSER` pour une application.
- Ne pas passer de mot de passe en argument de ligne de commande.
- Journaliser connexions et requêtes lentes.

## Validation et retour arrière

- **Validation** : connexion applicative `psql -h localhost -U APPUSER APPDB` réussie.
- **Retour arrière** : supprimer `60-local.conf`, recharger, puis `DROP DATABASE`/`DROP ROLE` de test.

## Si le problème n'est pas résolu

- [PostgreSQL — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-prerequis-limites)
- [PostgreSQL — Sécuriser (TLS, pg_hba, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-securiser)
- [PostgreSQL — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-valider)
- [PostgreSQL — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-sauvegarder-restaurer)
- [PostgreSQL — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-postgresql-mettre-a-jour)
- [Installation PostgreSQL 17 (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-database-installation-postgresql-17)
- [PostgreSQL — documentation officielle](https://www.postgresql.org/docs/)
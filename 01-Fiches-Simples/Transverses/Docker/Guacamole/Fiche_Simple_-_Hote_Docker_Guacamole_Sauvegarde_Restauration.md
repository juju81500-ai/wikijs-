# Fiche_Simple_-_Hote_Docker_Guacamole_Sauvegarde_Restauration.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose (Guacamole, guacd, PostgreSQL, reverse proxy HTTPS)
- **OS / Version** : Docker Engine + Compose; images Apache Guacamole 1.6.0, PostgreSQL 16
- **Catégorie** : accès distant / sauvegarde
- **Tags** : `docker`, `apache-guacamole`, `compose`, `postgresql`, `pg_dump`, `restauration`

---

## Problème précis à résoudre

Sauvegarder la base et la configuration, et tester la restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter la base (adapter utilisateur et base) :
   ```bash
   docker compose exec -T db pg_dump -U guacamole -d guacamole_db > guacamole-sauvegarde.sql
   ```
   👉 Explication : `pg_dump` produit une sauvegarde cohérente.

2. Restreindre le fichier :
   ```bash
   chmod 0600 guacamole-sauvegarde.sql
   ```
   👉 Explication : il contient les définitions de connexion.

3. Restaurer dans un projet Compose isolé (autre dossier et autre nom de projet, à adapter) :
   ```bash
   docker compose -p guac-test up -d db
   docker compose -p guac-test exec -T db psql -U guacamole -d guacamole_db -f - < guacamole-sauvegarde.sql
   ```
   👉 Explication : ne jamais restaurer sur l'instance active sans fenêtre approuvée.

## 2. Production — Contrôles

Sauvegarder aussi Compose, `.env` via le coffre approuvé, proxy, certificats et inventaire des connexions; conserver une copie chiffrée hors hôte.

## 3. Production — Sécurité

- Exclure les secrets des dépôts.

## Validation et retour arrière

- **Validation** : un compte de test est retrouvé dans l'instance restaurée.
- **Retour arrière** : `docker compose -p guac-test down -v` supprime l'instance de test.

## Si le problème n'est pas résolu

- [Apache Guacamole — Docker](https://guacamole.apache.org/doc/gug/guacamole-docker.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet Apache Guacamole Docker](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/121_Deploiement_Apache_Guacamole_1.6_Docker.md#5-sauvegarde-et-restauration)

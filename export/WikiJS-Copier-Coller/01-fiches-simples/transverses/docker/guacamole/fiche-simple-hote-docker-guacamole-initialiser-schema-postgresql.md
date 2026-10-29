# Fiche_Simple_-_Hote_Docker_Guacamole_Initialiser_Schema_PostgreSQL.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose (Guacamole, guacd, PostgreSQL, reverse proxy HTTPS)
- **OS / Version** : Docker Engine + Compose; images Apache Guacamole 1.6.0, PostgreSQL 16
- **Catégorie** : accès distant / base de données

---

## Problème précis à résoudre

Créer le schéma Guacamole dans une base PostgreSQL vide.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer uniquement PostgreSQL et attendre qu'il soit sain :
   ```bash
   docker compose up -d db
   docker compose ps
   ```
   👉 Explication : le schéma s'importe dans une base prête.

2. Générer le schéma avec l'image Guacamole 1.6.0 :
   ```bash
   docker run --rm guacamole/guacamole:1.6.0 /opt/guacamole/bin/initdb.sh --postgresql > initdb.sql
   ```
   👉 Explication : l'outil `initdb.sh` fournit le SQL de la même version; le fichier ne contient aucun secret.

3. Importer dans la base neuve (adapter utilisateur et base si modifiés) :
   ```bash
   docker compose exec -T db psql -U guacamole -d guacamole_db -f - < initdb.sql
   ```
   👉 Explication : crée les tables Guacamole.

## 2. Production — Contrôles

Sauvegarder la base avant toute migration ou réinitialisation de schéma.

## 3. Production — Sécurité

- Ne jamais répéter cette initialisation sur une base en service.

## Validation et retour arrière

- **Validation** : l'import se termine sans erreur SQL.
- **Retour arrière** : `docker compose down -v` détruit la base de test vide (uniquement avant toute donnée utile).

## Si le problème n'est pas résolu

- [Apache Guacamole — Docker](https://guacamole.apache.org/doc/gug/guacamole-docker.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet Apache Guacamole Docker](/02-fiches-completes/transverses/docker/installation-deploiement/121-deploiement-apache-guacamole-1-6-docker#3-initialiser-le-schema-postgresql)
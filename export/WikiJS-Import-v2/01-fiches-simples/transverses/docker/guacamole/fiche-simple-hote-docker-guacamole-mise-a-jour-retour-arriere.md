---
title: "Fiche Simple - Hote Docker Guacamole Mise A Jour Retour Arriere"
description: "Mettre à jour sans perdre la possibilité de revenir en arrière."
published: true
date: 2026-10-29T19:41:12Z
tags: ["docker", "apache-guacamole", "compose", "postgresql", "mise-a-jour", "rollback"]
editor: markdown
dateCreated: 2026-10-29T19:41:12Z
dateModified: 2026-10-29T19:41:12Z
---

# Fiche_Simple_-_Hote_Docker_Guacamole_Mise_A_Jour_Retour_Arriere.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose (Guacamole, guacd, PostgreSQL, reverse proxy HTTPS)
- **OS / Version** : Docker Engine + Compose; images Apache Guacamole 1.6.0, PostgreSQL 16
- **Catégorie** : accès distant / maintenance
- **Tags** : `docker`, `apache-guacamole`, `compose`, `postgresql`, `mise-a-jour`, `rollback`

---

## Problème précis à résoudre

Mettre à jour sans perdre la possibilité de revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la base avant mise à jour (voir la fiche sauvegarde) :
   ```bash
   docker compose exec -T db pg_dump -U guacamole -d guacamole_db > avant-maj.sql
   ```
   👉 Explication : une migration de schéma peut empêcher le retour à l'ancien conteneur.

2. Après mise à jour de la version d'image dans `compose.yaml` (test sur clone), appliquer :
   ```bash
   docker compose pull
   docker compose up -d
   ```
   👉 Explication : récupère et relance les nouvelles images.

3. Pour revenir en arrière, remettre l'ancienne version d'image et restaurer la base compatible sur l'environnement de test :
   ```bash
   docker compose down
   docker compose up -d
   ```
   👉 Explication : versions d'images, configuration et base doivent rester cohérentes.

## 2. Production — Contrôles

Épingler les images par version (et digest après validation), lire les notes de version, un changement à la fois.

## 3. Production — Sécurité

- En incident, couper l'accès utilisateur, préserver les journaux et révoquer les comptes concernés.

## Validation et retour arrière

- **Validation** : authentification et connexion pilote fonctionnent après mise à jour.
- **Retour arrière** : restaurer ensemble images, configuration et base sauvegardées.

## Si le problème n'est pas résolu

- [Apache Guacamole — Docker](https://guacamole.apache.org/doc/gug/guacamole-docker.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet Apache Guacamole Docker](/02-fiches-completes/transverses/docker/installation-deploiement/121-deploiement-apache-guacamole-1-6-docker#7-mise-a-jour-et-retour-arriere)
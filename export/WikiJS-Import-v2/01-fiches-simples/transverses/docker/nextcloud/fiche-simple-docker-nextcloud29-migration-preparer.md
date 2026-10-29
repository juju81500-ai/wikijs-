---
title: "Fiche Simple - Docker Nextcloud29 Migration Preparer"
description: "Relever l'existant et le plan de migration avant de toucher à Nextcloud 29."
published: true
date: 2026-10-29T19:42:44Z
tags: ["nextcloud", "docker", "migration", "mariadb", "redis", "tls"]
editor: markdown
dateCreated: 2026-10-29T19:42:44Z
dateModified: 2026-10-29T19:42:44Z
---

# Fiche_Simple_-_Docker_Nextcloud29_Migration_Preparer.md

- **Environnement** : Hôte Linux avec Nextcloud 29, MariaDB, Redis et proxy TLS en conteneurs Docker Compose
- **OS / Version** : Linux serveur; Nextcloud 29 (branche ancienne) vers une version maintenue
- **Catégorie** : conteneurs / migration
- **Tags** : `nextcloud`, `docker`, `migration`, `mariadb`, `redis`, `tls`

---

## Problème précis à résoudre

Relever l'existant et le plan de migration avant de toucher à Nextcloud 29.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les versions et l'état de la stack (à lancer dans le répertoire du fichier Compose) :
   ```bash
   docker compose ps
   docker compose images
   docker compose config --quiet
   docker system df
   ```
   👉 Explication : on note images, moteur de base, Redis et l'espace Docker disponible.

2. Lire les notes de version et les chemins de mise à niveau supportés de Nextcloud; noter qu'un saut de version majeure peut être interdit.
   👉 Explication : on évite une migration non supportée.

3. Lister les volumes de configuration, données, base, Redis et certificats, et prévoir une fenêtre de maintenance avec un stockage de sauvegarde distinct de Docker.
   👉 Explication : rien ne doit être oublié dans la sauvegarde.

## 2. Production — Contrôles

Tester d'abord toute mise à jour d'image dans un environnement de test, jamais directement en production.

## 3. Production — Sécurité

- Nextcloud 29 est une branche ancienne : ne pas en faire une nouvelle installation exposée.
- Ne pas exposer l'instance pendant la préparation si des vulnérabilités connues existent.

## Validation et retour arrière

- **Validation** : Inventaire complet des versions, volumes et fenêtre de maintenance validé.
- **Retour arrière** : Aucune modification n'est faite; rien à annuler.

## Si le problème n'est pas résolu

- [Nextcloud — Admin manual : upgrade](https://docs.nextcloud.com/server/latest/admin_manual/maintenance/upgrade.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet migration Nextcloud 29 conteneurisé](/02-fiches-completes/transverses/docker/installation-deploiement/05-cloud-prive-nextcloud-29-docker-mariadb-redis#1-preparer-la-migration)
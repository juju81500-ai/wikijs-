---
title: "Réparation : un conteneur Docker redémarre en boucle"
description: "docker ps -a"
published: true
date: 2026-10-27T10:30:18Z
tags: ["reparation", "docker", "compose", "conteneur", "logs"]
editor: markdown
dateCreated: 2026-10-27T10:30:18Z
dateModified: 2026-10-27T10:30:18Z
---

# Réparation : un conteneur Docker redémarre en boucle

- **Périmètre** : Docker Engine et Docker Compose
- **Tags** : `reparation`, `docker`, `compose`, `conteneur`, `logs`

## 1. Observer avant d'agir

```bash
docker ps -a
docker inspect --format '{{.State.Status}} {{.State.ExitCode}} {{.State.Error}}' NOM_CONTENEUR
docker logs --tail 200 --timestamps NOM_CONTENEUR
docker events --since 15m
```

Identifier la cause de sortie, l'heure du premier redémarrage et les changements récents. Ne pas supprimer le conteneur, son volume ou l'image avant d'avoir préservé les données et relevé la configuration.

## 2. Vérifier la définition Compose

Dans le répertoire du projet :

```bash
docker compose ps -a
docker compose config --quiet
docker compose logs --tail 200 SERVICE
```

Vérifier les variables nécessaires, les ports, les montages, les droits sur les répertoires et la disponibilité des dépendances. Une erreur de configuration doit être corrigée dans le fichier Compose ou la source de configuration, pas dans le conteneur éphémère.

## 3. Appliquer une correction contrôlée

Sauvegarder les données persistantes et la définition Compose. Après validation, recréer uniquement le service concerné :

```bash
docker compose up -d --no-deps SERVICE
docker compose ps
docker compose logs --tail 100 SERVICE
```

Remplacer `SERVICE` par le nom du service Compose, pas le nom de l'image. Si l'état se dégrade, revenir au fichier de configuration versionné précédent et restaurer la sauvegarde uniquement si des données ont été altérées. Éviter `docker system prune`, `docker rm -f` et toute suppression de volume pendant le diagnostic.
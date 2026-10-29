---
title: "Fiche Simple - Hote Docker Stack Volumes Config"
description: "Archiver les volumes nommés et la configuration de la stack."
published: true
date: 2026-10-29T19:42:02Z
tags: ["docker", "compose", "sauvegarde", "volumes", "tar"]
editor: markdown
dateCreated: 2026-10-29T19:42:02Z
dateModified: 2026-10-29T19:42:02Z
---

# Fiche_Simple_-_Hote_Docker_Stack_Volumes_Config.md

- **Environnement** : Hôte Linux Docker avec stacks Compose et volumes persistants
- **OS / Version** : Distribution maintenue; Docker Engine et Compose v2
- **Catégorie** : conteneurs / sauvegarde-restauration
- **Tags** : `docker`, `compose`, `sauvegarde`, `volumes`, `tar`

---

## Problème précis à résoudre

Archiver les volumes nommés et la configuration de la stack.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter les services qui écrivent, sans supprimer les volumes :
   ```bash
   cd /opt/docker/mon-projet
   docker compose stop
   ```
   👉 Explication : on fige les données pour une copie cohérente.

2. Identifier le volume (`mon_volume` est un exemple à remplacer) :
   ```bash
   docker volume inspect mon_volume
   ```
   👉 Explication : on confirme son nom et son emplacement.

3. Archiver le volume vers un dossier de sauvegarde déjà monté :
   ```bash
   sudo install -d -m 0700 /mnt/backup/mon-projet
   sudo docker run --rm \
     --mount type=volume,src=mon_volume,dst=/source,readonly \
     --mount type=bind,src=/mnt/backup/mon-projet,dst=/backup \
     ubuntu:24.04 tar --numeric-owner -cpf /backup/mon_volume.tar -C /source .
   ```
   👉 Explication : le volume est monté en lecture seule et archivé en conservant propriétaires et droits.

4. Pour un bind mount, sauvegarder le chemin hôte correspondant avec l'outil retenu.
   👉 Explication : les bind mounts ne sont pas des volumes Docker.

5. Copier Compose, fichiers d'environnement et secrets dans une archive chiffrée aux permissions strictes.
   👉 Explication : ces fichiers contiennent des secrets.

6. Redémarrer puis vérifier la santé :
   ```bash
   docker compose up -d
   docker compose ps
   ```
   👉 Explication : le service reprend; on contrôle l'état.

## 2. Production — Contrôles

Redémarrer et vérifier la santé applicative après la sauvegarde.

## 3. Production — Sécurité

- Ne jamais utiliser `docker compose down -v` ni `docker volume prune`.
- Chiffrer l'archive de configuration.

## Validation et retour arrière

- **Validation** : L'archive `.tar` existe et les services sont revenus en bonne santé.
- **Retour arrière** : `docker compose up -d` redémarre la stack; supprimer l'archive incomplète.

## Si le problème n'est pas résolu

- [Docker — Volumes et sauvegarde/restauration](https://docs.docker.com/engine/storage/volumes/)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet — sauvegarder volumes et configuration](/02-fiches-completes/transverses/docker/autres/37-sauvegarde-restauration-stacks-docker#4-sauvegarder-volumes-et-configuration)
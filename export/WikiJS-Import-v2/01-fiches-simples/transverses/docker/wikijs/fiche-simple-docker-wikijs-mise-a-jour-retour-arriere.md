---
title: "Fiche Simple - Docker WikiJS Mise A Jour Retour Arriere"
description: "Mettre à jour Wiki.js en gardant la possibilité de revenir en arrière."
published: true
date: 2026-10-29T19:42:44Z
tags: ["wikijs", "docker", "compose", "postgresql", "traefik", "tls"]
editor: markdown
dateCreated: 2026-10-29T19:42:44Z
dateModified: 2026-10-29T19:42:44Z
---

# Fiche_Simple_-_Docker_WikiJS_Mise_A_Jour_Retour_Arriere.md

- **Environnement** : Hôte Linux avec Docker Engine, Compose v2 et Traefik déjà opérationnel
- **OS / Version** : Linux serveur; Wiki.js 2.x; PostgreSQL 17
- **Catégorie** : conteneurs / documentation
- **Tags** : `wikijs`, `docker`, `compose`, `postgresql`, `traefik`, `tls`

---

## Problème précis à résoudre

Mettre à jour Wiki.js en gardant la possibilité de revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Noter les images actuellement utilisées et vérifier la sauvegarde :
   ```bash
   cd /opt/docker/wikijs
   sudo docker compose images
   sudo ls -lh /var/backups/wikijs
   ```
   👉 Explication : ces références permettent de revenir en arrière.

2. Lire les notes de version Wiki.js avant de continuer.
   👉 Explication : on repère les changements incompatibles.

3. Mettre à jour et contrôler :
   ```bash
   cd /opt/docker/wikijs
   sudo docker compose pull
   sudo docker compose up -d
   sudo docker compose ps
   sudo docker compose logs --tail=100 wiki db
   ```
   👉 Explication : les nouvelles images sont tirées puis les services recréés; vérifier l'absence d'erreur.

## 2. Production — Contrôles

Ne jamais changer la version majeure de PostgreSQL en réutilisant le volume existant : une migration de données dédiée est nécessaire.

## 3. Production — Sécurité

- Sauvegarde restaurable vérifiée avant toute mise à jour.
- Ne pas utiliser `docker compose down -v`.

## Validation et retour arrière

- **Validation** : Services up, base healthy, wiki accessible et pages intactes.
- **Retour arrière** : Conserver les volumes, revenir aux images et à la configuration précédentes, puis restaurer la base uniquement si le schéma a été modifié.

## Si le problème n'est pas résolu

- [Wiki.js — Docker](https://docs.requarks.io/install/docker)
- [Wiki.js — Prérequis](https://docs.requarks.io/install/requirements)
- [Guide complet Wiki.js Docker PostgreSQL Traefik](/02-fiches-completes/transverses/docker/installation-deploiement/28-installation-wikijs-docker-postgresql-traefik#7-mise-a-jour-et-retour-arriere)
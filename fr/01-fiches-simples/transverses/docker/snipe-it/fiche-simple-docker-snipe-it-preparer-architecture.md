---
title: "fiche-simple-docker-snipe-it-preparer-architecture"
description: "Valider l'architecture avant de déployer Snipe-IT derrière Traefik."
published: true
date: 2026-11-03T14:22:28Z
tags: ["snipe-it", "docker", "mariadb", "traefik", "inventaire"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# fiche-simple-docker-snipe-it-preparer-architecture.md

- **Environnement** : Hôte Docker avec Docker Compose v2 et réseau Traefik existant
- **OS / Version** : Hôte Linux maintenu; Snipe-IT 8.8.3; MariaDB 11.4.7
- **Catégorie** : [[Glossary:ITSM]] / gestion des actifs
- **Tags** : `snipe-it`, `docker`, `mariadb`, `traefik`, `inventaire`

---

## Problème précis à résoudre

Valider l'architecture avant de déployer Snipe-IT derrière Traefik.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les prérequis :
   ```bash
   docker --version
   docker compose version
   docker network ls | grep traefik_proxy
   ```
   👉 Explication : Vérifie Docker, Compose v2 et la présence du réseau proxy Traefik existant.

2. Prévoir le [[Glossary:DNS]] (exemple `assets.example.net`, à remplacer), [[Glossary:TLS]] terminé par Traefik, volumes sauvegardés hors hôte et envoi [[Glossary:SMTP]].
   👉 Explication : ces éléments conditionnent la suite du déploiement.

3. Retenir l'image officielle `snipe/snipe-it` épinglée à `v8.8.3`; revalider la dernière version maintenue avant un nouveau déploiement.
   👉 Explication : garantit un déploiement reproductible.

## 2. Production — Contrôles

Garder la base dans un réseau privé et ne pas publier son port.

## 3. Production — Sécurité

- Utiliser uniquement l'image officielle.
- Ne pas exposer MariaDB.

## Validation et retour arrière

- **Validation** : Docker, Compose et réseau Traefik présents; DNS, TLS et SMTP prévus.
- **Retour arrière** : aucun changement n'a été fait.

## Si le problème n'est pas résolu

- [Snipe-IT — Docker Compose](https://snipe-it.readme.io/docs/docker)
- [Guide complet — étape 1](/fr/02-fiches-completes/transverses/docker/installation-deploiement/39-deploiement-snipe-it-8-docker-mariadb-traefik#1-preparer-larchitecture)
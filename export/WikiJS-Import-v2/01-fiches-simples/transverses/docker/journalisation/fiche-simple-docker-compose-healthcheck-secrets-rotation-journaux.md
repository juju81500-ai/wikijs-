---
title: "Fiche Simple - Docker Compose Healthcheck Secrets Rotation Journaux"
description: "Ajouter un contrôle de santé, une rotation des journaux Docker et un secret monté en fichier à un service Compose, sans inscrire de mot de passe dans le YAML."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[docker]", "[compose]", "[healthcheck]", "[secrets]", "[journaux]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_Docker_Compose_Healthcheck_Secrets_Rotation_Journaux.md

- **Environnement** : Hôte Docker Debian 12 ou Ubuntu 24.04
- **OS / Version** : Docker Compose v2
- **Catégorie** : Déploiement / Configuration / Sécurité
- **Tags** : `[docker]`, `[compose]`, `[healthcheck]`, `[secrets]`, `[journaux]`, `[hardening]`

## 🎯 Problème précis à résoudre
Ajouter un contrôle de santé, une rotation des journaux Docker et un secret monté en fichier à un service Compose, sans inscrire de mot de passe dans le YAML.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Ajouter au service une sonde correspondant à un outil réellement présent dans l'image :
   ```yaml
   services:
     app:
       image: exemple/app:version-fixee
       healthcheck:
         test: ["CMD", "/app/bin/healthcheck"]
         interval: 30s
         timeout: 5s
         retries: 3
         start_period: 20s
       logging:
         driver: json-file
         options:
           max-size: "10m"
           max-file: "3"
   ```
2. Valider le YAML rendu puis démarrer le service :
   ```bash
   docker compose config
   docker compose up -d
   docker compose ps
   ```
   👉 *Explication : remplacer l'image et le chemin de sonde par ceux du service; une commande absente rend le contrôle de santé inutilisable.*

## ⚡ 2. Production — Façon Simplifiée
1. Créer un fichier secret en dehors du dépôt et limiter ses permissions :
   ```bash
   install -d -m 0700 ./secrets
  SECRET_UID=10001
  SECRET_GID=10001
  sudo install -o "$SECRET_UID" -g "$SECRET_GID" -m 0400 /dev/null ./secrets/db_password
   ```
  Remplacer l'UID/GID d'exemple par ceux du processus dans l'image et tenir compte d'un éventuel user namespace. Ajouter le secret par un mécanisme sûr, sans le placer dans l'historique du shell; vérifier qu'il est lisible depuis le conteneur.
2. Déclarer le secret et l'autoriser uniquement au service qui en a besoin :
   ```yaml
   services:
     app:
       secrets:
         - db_password
   secrets:
     db_password:
       file: ./secrets/db_password
   ```
3. Vérifier le rendu et la santé après déploiement :
   ```bash
   docker compose config
   docker compose up -d
   docker compose ps
   docker inspect --format '{{.State.Health.Status}}' "$(docker compose ps -q app)"
   ```
   👉 *Explication : l'application doit lire le secret depuis `/run/secrets/db_password`; vérifier sa prise en charge avant le déploiement.*

## 🔒 3. Production — Façon Sécurisée
1. Ajouter `./secrets/` au `.gitignore`, limiter l'accès aux fichiers et préférer un coffre de secrets adapté aux environnements multi-hôtes.
2. Configurer `max-size` et `max-file` sur les services concernés afin d'éviter une saturation disque; vérifier l'espace après déploiement.
3. Ne pas utiliser `depends_on` comme garantie de disponibilité applicative; le service client doit gérer les erreurs et reconnexions.

## ✅ Validation et retour arrière
- Confirmer que `docker compose config` réussit, que la sonde passe et que les journaux sont bornés.
- Restaurer le YAML précédent en cas de régression et redéployer avec `docker compose up -d`.
- Retirer un secret seulement après avoir confirmé que l'application et ses dépendances ne l'utilisent plus.
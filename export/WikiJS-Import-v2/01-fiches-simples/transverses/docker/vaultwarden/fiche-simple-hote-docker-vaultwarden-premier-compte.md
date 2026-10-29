---
title: "Fiche Simple - Hote Docker Vaultwarden Premier Compte"
description: "Créer le compte administrateur puis interdire les inscriptions de tiers."
published: true
date: 2026-10-29T19:40:03Z
tags: ["docker", "vaultwarden", "comptes", "signups", "2fa"]
editor: markdown
dateCreated: 2026-10-29T19:40:03Z
dateModified: 2026-10-29T19:40:03Z
---

# Fiche_Simple_-_Hote_Docker_Vaultwarden_Premier_Compte.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose, Vaultwarden SQLite derrière un reverse proxy HTTPS
- **OS / Version** : Hôte Linux + Docker; image vaultwarden/server (tag à figer après validation)
- **Catégorie** : gestionnaire de mots de passe auto-hébergé
- **Tags** : `docker`, `vaultwarden`, `comptes`, `signups`, `2fa`

---

## Problème précis à résoudre

Créer le compte administrateur puis interdire les inscriptions de tiers.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir `https://vault.example.net` (remplacer par le vrai domaine) et créer le compte avec une phrase secrète forte.
   👉 Explication : le chiffrement est côté client; un mot de passe maître perdu ne peut pas être réinitialisé par l'administrateur.

2. Dans `compose.yaml`, passer `SIGNUPS_ALLOWED` à `"false"`.
   👉 Explication : le projet recommande de fermer les inscriptions après la création du compte.

3. Recréer le conteneur :
   ```bash
   docker compose up -d
   ```
   👉 Explication : Compose applique la nouvelle variable d'environnement.

4. Inviter les utilisateurs par les mécanismes documentés et activer l'authentification à deux facteurs.
   👉 Explication : seuls les invités accèdent au service, protégés par un second facteur.

## 2. Production — Contrôles

Conserver la procédure de récupération du compte administrateur et lister les utilisateurs invités.

## 3. Production — Sécurité

- Ne jamais laisser les inscriptions ouvertes en production.
- Ne jamais exposer `/admin` sans restriction d'accès.

## Validation et retour arrière

- **Validation** : Une tentative d'inscription est refusée et l'authentification à deux facteurs est active.
- **Retour arrière** : Repasser `SIGNUPS_ALLOWED` à `"true"` temporairement si besoin, puis `docker compose up -d`.

## Si le problème n'est pas résolu

- [Vaultwarden — Using Docker Compose](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Vaultwarden — Backing up your vault](https://github.com/dani-garcia/vaultwarden/wiki/Backing-up-your-vault)
- [Guide complet — créer le premier compte puis fermer les inscriptions](/02-fiches-completes/transverses/docker/installation-deploiement/94-deploiement-vaultwarden-docker-compose#4-creer-le-premier-compte-puis-fermer-les-inscriptions)
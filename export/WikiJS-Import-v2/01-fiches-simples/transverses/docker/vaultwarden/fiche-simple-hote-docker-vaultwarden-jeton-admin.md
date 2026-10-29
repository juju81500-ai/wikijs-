---
title: "Fiche Simple - Hote Docker Vaultwarden Jeton Admin"
description: "Générer un jeton d'administration haché (Argon2id) sans jamais le saisir en clair dans un fichier."
published: true
date: 2026-10-29T19:40:03Z
tags: ["docker", "vaultwarden", "admin-token", "argon2id"]
editor: markdown
dateCreated: 2026-10-29T19:40:03Z
dateModified: 2026-10-29T19:40:03Z
---

# Fiche_Simple_-_Hote_Docker_Vaultwarden_Jeton_Admin.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose, Vaultwarden SQLite derrière un reverse proxy HTTPS
- **OS / Version** : Hôte Linux + Docker; image vaultwarden/server (tag à figer après validation)
- **Catégorie** : gestionnaire de mots de passe auto-hébergé
- **Tags** : `docker`, `vaultwarden`, `admin-token`, `argon2id`

---

## Problème précis à résoudre

Générer un jeton d'administration haché (Argon2id) sans jamais le saisir en clair dans un fichier.

## 1. Hors-Production (Lab / Test / POC)

1. Décider si la page d'administration est vraiment nécessaire.
   👉 Explication : inutile pour une première installation; ne l'activer que si besoin.

2. Générer le hachage avec la commande intégrée :
   ```bash
   docker run --rm -it vaultwarden/server /vaultwarden hash
   ```
   👉 Explication : le mot de passe est saisi en interactif (deux fois), donc jamais en argument.

3. Saisir un mot de passe long et aléatoire, puis le ranger dans le gestionnaire de secrets avec la chaîne hachée.
   👉 Explication : seule la chaîne hachée ira dans le fichier Compose.

4. Dans le fichier Compose, doubler chaque `$` de la chaîne hachée (`$$`).
   👉 Explication : sinon Compose les interprète comme des variables.

## 2. Production — Contrôles

Conserver le mot de passe et le hachage dans le coffre; documenter qui peut ouvrir `/admin`.

## 3. Production — Sécurité

- Ne jamais stocker le jeton en clair dans `compose.yaml`.
- Ne jamais exposer `/admin` sans restriction d'accès.

## Validation et retour arrière

- **Validation** : La commande a produit une chaîne PHC commençant par `$argon2id$`.
- **Retour arrière** : Supprimer la ligne `ADMIN_TOKEN` du fichier Compose pour désactiver la page d'administration.

## Si le problème n'est pas résolu

- [Vaultwarden — Using Docker Compose](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Vaultwarden — Backing up your vault](https://github.com/dani-garcia/vaultwarden/wiki/Backing-up-your-vault)
- [Guide complet — préparer le jeton d'administration](/02-fiches-completes/transverses/docker/installation-deploiement/94-deploiement-vaultwarden-docker-compose#2-preparer-le-jeton-dadministration)
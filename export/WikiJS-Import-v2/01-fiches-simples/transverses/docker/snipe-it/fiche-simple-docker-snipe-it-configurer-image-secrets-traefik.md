---
title: "Fiche Simple - Docker Snipe-IT Configurer Image Secrets Traefik"
description: "Renseigner .env, générer APPKEY et relier le service à Traefik."
published: true
date: 2026-10-29T19:40:27Z
tags: ["snipe-it", "docker", "mariadb", "traefik", "inventaire"]
editor: markdown
dateCreated: 2026-10-29T19:40:27Z
dateModified: 2026-10-29T19:40:27Z
---

# Fiche_Simple_-_Docker_Snipe-IT_Configurer_Image_Secrets_Traefik.md

- **Environnement** : Hôte Docker avec Docker Compose v2 et réseau Traefik existant
- **OS / Version** : Hôte Linux maintenu; Snipe-IT 8.8.3; MariaDB 11.4.7
- **Catégorie** : ITSM / gestion des actifs
- **Tags** : `snipe-it`, `docker`, `mariadb`, `traefik`, `inventaire`

---

## Problème précis à résoudre

Renseigner `.env`, générer `APP_KEY` et relier le service à Traefik.

## 1. Hors-Production (Lab / Test / POC)

1. Dans `.env`, remplacer les valeurs d'exemple et définir au minimum :
   ```dotenv
   APP_VERSION=v8.8.3
   APP_ENV=production
   APP_DEBUG=false
   APP_URL=https://assets.example.net
   APP_TIMEZONE=Europe/Paris
   SECURE_COOKIES=true
   DB_DATABASE=snipeit
   DB_USERNAME=snipeit
   ```
   👉 Explication : `assets.example.net` est un exemple à remplacer par le vrai nom.

2. Générer des valeurs aléatoires distinctes pour `DB_PASSWORD` et `MYSQL_ROOT_PASSWORD` (générateur du coffre) et les saisir dans `.env`.
   👉 Explication : jamais de secret en argument de commande ni dans Git.

3. Générer la clé applicative :
   ```bash
   docker compose run --rm app php artisan key:generate --show
   ```
   👉 Explication : Commande officielle qui génère `APP_KEY`; copier le résultat dans `.env` avant la première initialisation.

4. Sauvegarder `APP_KEY` dans le coffre de secrets.
   👉 Explication : elle est nécessaire pour déchiffrer certains champs après restauration.

5. Utiliser les labels Traefik en vigueur pour router `app` vers le port 80, connecter `app` à `traefik_proxy`, retirer le port hôte 8000 et définir `APP_TRUSTED_PROXIES` avec le CIDR réel du réseau proxy.
   👉 Explication : Traefik publie l'application; la base n'est jamais exposée.

## 2. Production — Contrôles

Valider les labels Traefik avec le responsable du proxy.

## 3. Production — Sécurité

- Ne pas faire confiance à des réseaux proxy non maîtrisés.
- Ne pas publier MariaDB.

## Validation et retour arrière

- **Validation** : `.env` complet, `APP_KEY` en coffre, aucun port base publié.
- **Retour arrière** : restaurer `.env` depuis la copie des fichiers amont.

## Si le problème n'est pas résolu

- [Snipe-IT — Docker Compose](https://snipe-it.readme.io/docs/docker)
- [Guide complet — étape 3](/02-fiches-completes/transverses/docker/installation-deploiement/39-deploiement-snipe-it-8-docker-mariadb-traefik#3-configurer-limage-les-secrets-et-traefik)
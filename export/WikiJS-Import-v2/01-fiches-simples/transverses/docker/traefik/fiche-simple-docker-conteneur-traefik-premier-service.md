---
title: "Fiche Simple - Docker Conteneur Traefik Premier Service"
description: "Publier une application de test non sensible en HTTPS."
published: true
date: 2026-10-29T19:41:42Z
tags: ["traefik", "docker", "reverse-proxy", "acme", "tls"]
editor: markdown
dateCreated: 2026-10-29T19:41:42Z
dateModified: 2026-10-29T19:41:42Z
---

# Fiche_Simple_-_Docker_Conteneur_Traefik_Premier_Service.md

- **Environnement** : Hôte Docker Linux dédié ou contrôlé
- **OS / Version** : Linux avec Docker Engine et Compose; version Traefik maintenue (3.x)
- **Catégorie** : reverse proxy / déploiement
- **Tags** : `traefik`, `docker`, `reverse-proxy`, `acme`, `tls`

---

## Problème précis à résoudre

Publier une application de test non sensible en HTTPS.

## 1. Hors-Production (Lab / Test / POC)

1. Ajouter à l'application de test un routeur HTTPS, un service, un middleware de redirection HTTP vers HTTPS et le bon resolver (labels Compose).
   👉 Explication : Traefik construit ses routes depuis ces labels.

2. Démarrer la pile :
   ```bash
   docker compose up -d
   ```
   👉 Explication : lance Traefik et l'application.

3. Vérifier l'état :
   ```bash
   docker compose ps
   ```
   👉 Explication : tous les services doivent être `running`.

4. Lire les journaux Traefik :
   ```bash
   docker compose logs --tail 100 traefik
   ```
   👉 Explication : on cherche les erreurs ACME ou de routage.

## 2. Production — Contrôles

Commencer avec le serveur de staging ACME.

## 3. Production — Sécurité

- Appliquer une politique de sécurité (en-têtes, filtrage) adaptée au service.

## Validation et retour arrière

- **Validation** : L'application répond en HTTPS et HTTP redirige.
- **Retour arrière** : `docker compose down` arrête la pile sans effacer `acme.json`.

## Si le problème n'est pas résolu

- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Traefik — ACME / Let's Encrypt](https://doc.traefik.io/traefik/https/acme/)
- [Guide complet — 3. Déployer un premier service](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker#3-deployer-un-premier-service)
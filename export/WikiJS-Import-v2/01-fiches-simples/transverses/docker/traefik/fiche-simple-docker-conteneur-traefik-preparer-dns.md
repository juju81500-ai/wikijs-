---
title: "Fiche Simple - Docker Conteneur Traefik Preparer DNS"
description: "Vérifier que le DNS et les ports 80/443 pointent bien vers l'hôte."
published: true
date: 2026-10-29T19:41:42Z
tags: ["traefik", "docker", "reverse-proxy", "acme", "tls"]
editor: markdown
dateCreated: 2026-10-29T19:41:42Z
dateModified: 2026-10-29T19:41:42Z
---

# Fiche_Simple_-_Docker_Conteneur_Traefik_Preparer_DNS.md

- **Environnement** : Hôte Docker Linux dédié ou contrôlé
- **OS / Version** : Linux avec Docker Engine et Compose; version Traefik maintenue (3.x)
- **Catégorie** : reverse proxy / prérequis
- **Tags** : `traefik`, `docker`, `reverse-proxy`, `acme`, `tls`

---

## Problème précis à résoudre

Vérifier que le DNS et les ports 80/443 pointent bien vers l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les enregistrements (remplacer `app.example.test` par votre nom) :
   ```bash
   dig +short A app.example.test
   dig +short AAAA app.example.test
   ```
   👉 Explication : les adresses doivent correspondre à l'hôte.

2. Vérifier que 80 et 443 sont libres :
   ```bash
   sudo ss -lntp | grep -E ':(80|443)\b'
   ```
   👉 Explication : aucun autre service ne doit déjà les utiliser.

3. Créer le fichier de stockage ACME avec des droits stricts :
   ```bash
   touch acme.json
   chmod 600 acme.json
   ```
   👉 Explication : Traefik exige que seul son compte lise `acme.json`.

## 2. Production — Contrôles

Prévoir sauvegarde persistante de `acme.json` et mécanisme de renouvellement.

## 3. Production — Sécurité

- Ne pas exposer le tableau de bord sans authentification et filtrage.
- Ne pas monter le socket Docker brut : préférer un proxy de socket restreint.

## Validation et retour arrière

- **Validation** : DNS correct, ports libres et `acme.json` en `600`.
- **Retour arrière** : Aucun service n'est démarré; supprimer `acme.json` vide si besoin.

## Si le problème n'est pas résolu

- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Traefik — ACME / Let's Encrypt](https://doc.traefik.io/traefik/https/acme/)
- [Guide complet — 1. Préparer DNS et exposition](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker#1-preparer-dns-et-exposition)
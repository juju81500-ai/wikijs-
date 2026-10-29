---
title: "Fiche Simple - VM Debian 13 Caddy Valider Service"
description: "Vérifier la réponse HTTPS de Caddy, son certificat, son journal et l'absence d'exposition directe non désirée de l'amont."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "caddy", "https", "certificat", "validation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Caddy_Valider_Service.md

- **Environnement** : VM Debian 13, FQDN et client de test autorisés
- **OS / Version** : Debian 13; Caddy stable
- **Catégorie** : serveur Web / validation
- **Tags** : `debian13`, `caddy`, `https`, `certificat`, `validation`

---

## Problème précis à résoudre

Vérifier la réponse HTTPS de Caddy, son certificat, son journal et l'absence d'exposition directe non désirée de l'amont.

## 1. Hors-Production (Lab / Test / POC)

1. Tester HTTPS :
   ```bash
   curl -fsSI https://app.example.net/
   ```
   👉 Explication : code HTTP attendu et certificat valide (nom, expiration).

2. Lire les journaux :
   ```bash
   sudo journalctl -u caddy --since '15 minutes ago' --no-pager
   ```
   👉 Explication : repérer les erreurs ACME ou de connexion amont.

3. Vérifier les ports à l'écoute :
   ```bash
   sudo ss -ltnp
   ```
   👉 Explication : l'amont (8080) ne doit pas être accessible depuis des réseaux non prévus.

## 2. Production — Contrôles

Mettre en place sondes de disponibilité, alertes certificat, surveillance des journaux, espace disque et procédure d'incident avec propriétaire du service.

## 3. Production — Sécurité

- Ne pas utiliser `curl -k` pour faire passer un certificat invalide.
- Ne pas ouvrir de port de gestion ni exposer directement l'amont.
- Garder les journaux et informations de certificats selon les durées approuvées.
- Ne pas publier les sorties contenant secrets ou données utilisateur dans un ticket ouvert.

## Validation et retour arrière

- **Validation** : certificat valide, réponse et journaux conformes, ports limités aux flux prévus.
- **Retour arrière** : isoler le flux par le pare-feu approuvé si nécessaire et restaurer la configuration validée.

## Si le problème n'est pas résolu

- [Caddy — HTTPS automatique](https://caddyserver.com/docs/automatic-https)
- [Caddy — reverse_proxy](https://caddyserver.com/docs/caddyfile/directives/reverse_proxy)
- [Guide complet Caddy Debian 13](/02-fiches-completes/debian/13/installation-deploiement/91-deploiement-caddy-debian-13#4-verifier-le-service)
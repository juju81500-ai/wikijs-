---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 30 Protection Contre Le Brute"
description: "Limiter les tentatives de connexion."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-30"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

---

## Problème précis à résoudre

Limiter les tentatives de connexion.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Services > SSH > Options : limiter les tentatives et activer la journalisation.
   ```sh
   midclt call ssh.config
   ```
   👉 Explication : affiche la configuration.

2. Surveiller les échecs :
   ```sh
   grep -i 'failed' /var/log/auth.log | tail
   ```
   👉 Explication : repère les tentatives.

## 2. Production — Contrôles

Envoyer les journaux d'authentification vers un syslog central.

## 3. Production — Sécurité

Mots de passe longs ; accès SSH restreint par réseau.

## Validation et retour arrière

- **Validation** : Les échecs sont repérés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 19 Configuration Des Depots Logiciels"
description: "Choisir le canal de mises à jour."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-19"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-19`

---

## Problème précis à résoudre

Choisir le canal de mises à jour.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Mise à jour > Paramètres > Train de mise à jour (stable recommandé).
   ```bash
   sudo midclt call update.get_trains | python3 -m json.tool | head -30
   ```
   👉 Explication : liste les trains disponibles et le train courant.

2. Ne jamais modifier les dépôts Debian du système.
   👉 Explication : `apt` est désactivé ; le système se met à jour comme un ensemble.

## 2. Production — Contrôles

Utiliser uniquement le train stable en production.

## 3. Production — Sécurité

Les trains de test ne sont pas pour les données réelles.

## Validation et retour arrière

- **Validation** : Train stable sélectionné.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 43 Controle Des Services Et"
description: "Vérifier les services et ports ouverts."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-43"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier les services et ports ouverts.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Services (état et démarrage automatique).
   ```bash
   sudo midclt call service.query | python3 -m json.tool | grep -E '"service"|"state"'
   ```
   👉 Explication : état de chaque service.

2. Lister les ports :
   ```bash
   sudo ss -tulpn
   ```
   👉 Explication : comparer à la liste attendue.

## 2. Production — Contrôles

Comparer avec le runbook.

## 3. Production — Sécurité

Tout port non prévu est une anomalie.

## Validation et retour arrière

- **Validation** : Aucun service ni port imprévu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
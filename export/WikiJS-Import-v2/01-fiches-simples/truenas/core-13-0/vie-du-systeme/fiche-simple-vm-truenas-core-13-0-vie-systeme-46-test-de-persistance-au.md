---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 46 Test De Persistance Au"
description: "Vérifier que tout redémarre seul."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-46"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-46`

---

## Problème précis à résoudre

Vérifier que tout redémarre seul.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : icône Alimentation > Redémarrer.
   ```sh
   shutdown -r now
   ```
   👉 Explication : redémarre ; prévenir les utilisateurs.

2. Après redémarrage :
   ```sh
   zpool status -x
   service -e
   ifconfig | grep inet
   ```
   👉 Explication : pool sain, services démarrés, réseau actif.

## 2. Production — Contrôles

En fenêtre de maintenance.

## 3. Production — Sécurité

Pas de redémarrage pendant un resilver.

## Validation et retour arrière

- **Validation** : Pool en ligne et partages accessibles.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
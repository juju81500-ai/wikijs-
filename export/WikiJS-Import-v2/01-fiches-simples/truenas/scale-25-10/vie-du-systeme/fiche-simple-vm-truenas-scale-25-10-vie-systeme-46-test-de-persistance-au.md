---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 46 Test De Persistance Au"
description: "Vérifier que tout redémarre seul."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-46"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-46`

---

## Problème précis à résoudre

Vérifier que tout redémarre seul.

## 1. Hors-Production (Lab / Test / POC)

1. Redémarrer : GUI icône Alimentation > Redémarrer.
   ```bash
   sudo midclt call system.reboot
   ```
   👉 Explication : redémarre le NAS ; prévenir les utilisateurs.

2. Après redémarrage :
   ```bash
   sudo zpool status -x
   sudo midclt call service.query | grep -c RUNNING
   ip -br a
   ```
   👉 Explication : pool sain, services démarrés, réseau actif.

## 2. Production — Contrôles

Tester pendant une fenêtre de maintenance.

## 3. Production — Sécurité

Ne pas redémarrer un NAS en resilver ou en réplication.

## Validation et retour arrière

- **Validation** : Pool en ligne et partages accessibles.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
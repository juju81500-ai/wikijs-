---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 02 Recuperation De L Image"
description: "Obtenir l'ISO officielle de TrueNAS SCALE SCALE 25.10."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-02"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-02`

---

## Problème précis à résoudre

Obtenir l'ISO officielle de TrueNAS SCALE SCALE 25.10.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO depuis le site officiel :
   ```bash
   # GUI poste : https://www.truenas.com/download-truenas-community-edition/
   curl -LO https://download.truenas.com/TrueNAS-SCALE-Goldeye/VERSION/TrueNAS-SCALE-VERSION.iso
   ```
   👉 Explication : VERSION est la version exacte (ex. 25.10.0) affichée sur la page de téléchargement ; vérifier l'URL exacte sur le site avant de lancer.

2. Contrôler la taille du fichier :
   ```bash
   ls -lh TrueNAS-SCALE-*.iso
   ```
   👉 Explication : une taille anormalement petite indique un téléchargement interrompu.

3. Ranger l'ISO dans un dépôt interne avec sa version et sa date.
   👉 Explication : la même image sert à toutes les installations et reconstructions.

## 2. Production — Contrôles

Utiliser un dépôt d'images interne contrôlé.

## 3. Production — Sécurité

Ne télécharger que depuis `truenas.com`, en HTTPS.

## Validation et retour arrière

- **Validation** : ISO présente, taille cohérente, version notée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
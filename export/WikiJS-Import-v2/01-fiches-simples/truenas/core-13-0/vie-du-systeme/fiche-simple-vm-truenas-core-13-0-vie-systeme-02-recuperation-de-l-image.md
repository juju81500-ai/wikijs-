---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 02 Recuperation De L Image"
description: "Obtenir l'ISO officielle de TrueNAS CORE 13.0."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-02"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-02`

---

## Problème précis à résoudre

Obtenir l'ISO officielle de TrueNAS CORE 13.0.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO depuis le site officiel :
   ```sh
   fetch https://download.freenas.org/13.0/STABLE/RELEASE/x64/TrueNAS-13.0-RELEASE.iso
   ```
   👉 Explication : l'URL exacte et la révision (ex. 13.0-U6.x) sont à reprendre sur la page de téléchargement officielle ; sur Linux, utiliser `curl -LO` avec la même URL.

2. Contrôler la taille :
   ```sh
   ls -lh TrueNAS-13.0*.iso
   ```
   👉 Explication : une taille anormale indique un téléchargement interrompu.

3. Ranger l'ISO dans le dépôt interne avec sa version.
   👉 Explication : la même image sert pour toute reconstruction.

## 2. Production — Contrôles

Utiliser un dépôt d'images interne.

## 3. Production — Sécurité

Télécharger uniquement depuis `truenas.com` en HTTPS. CORE est en fin de vie : réserver aux systèmes existants.

## Validation et retour arrière

- **Validation** : ISO présente, taille cohérente.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
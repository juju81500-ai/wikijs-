---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 04 Preparation Du Support D"
description: "Créer la clé USB ou le média virtuel."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-04"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-04`

---

## Problème précis à résoudre

Créer la clé USB ou le média virtuel.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier la clé USB (poste FreeBSD) :
   ```sh
   geom disk list
   # ou sous Linux : lsblk -o NAME,SIZE,MODEL,TRAN
   ```
   👉 Explication : repérer la clé (jamais un disque de données).

2. Écrire l'ISO (remplacer da0 par la clé identifiée) :
   ```sh
   dd if=TrueNAS-13.0-RELEASE.iso of=/dev/da0 bs=1m conv=sync
   # Linux : sudo dd if=TrueNAS-13.0-RELEASE.iso of=/dev/sdX bs=4M status=progress conv=fsync
   ```
   👉 Explication : écrit l'image brute ; efface la clé.

3. Pour une VM ou un BMC, monter l'ISO en lecteur virtuel.
   👉 Explication : évite la clé physique.

## 2. Production — Contrôles

Utiliser le média virtuel du BMC.

## 3. Production — Sécurité

Retirer la clé après l'installation.

## Validation et retour arrière

- **Validation** : Le menu d'installation s'affiche.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 15 Chargeur D Amorcage"
description: "Vérifier l'amorçage du système installé."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-15"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-15`

---

## Problème précis à résoudre

Vérifier l'amorçage du système installé.

## 1. Hors-Production (Lab / Test / POC)

1. Retirer la clé d'installation et redémarrer ; vérifier le mode UEFI :
   ```bash
   [ -d /sys/firmware/efi ] && echo UEFI || echo BIOS
   ```
   👉 Explication : affiche UEFI ou BIOS.

2. Lister les environnements d'amorçage : GUI Système > Environnements d'amorçage.
   ```bash
   sudo midclt call bootenv.query | python3 -m json.tool | head -30
   ```
   👉 Explication : chaque mise à jour crée un environnement permettant le retour arrière.

## 2. Production — Contrôles

Garder au moins un environnement d'amorçage précédent.

## 3. Production — Sécurité

Protéger l'accès console et BMC.

## Validation et retour arrière

- **Validation** : Le NAS redémarre seul sur le disque système.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
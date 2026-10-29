---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 48 Test De Restauration Pra"
description: "Prouver la restauration."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-48"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-48`

---

## Problème précis à résoudre

Prouver la restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Restaurer un fichier depuis un snapshot :
   ```sh
   ls /mnt/POOL/DATASET/.zfs/snapshot/
   cp /mnt/POOL/DATASET/.zfs/snapshot/NOM_SNAP/FICHIER /mnt/POOL/DATASET/FICHIER_RESTAURE
   ```
   👉 Explication : NOM_SNAP est un snapshot existant ; GUI : Stockage > Snapshots > Cloner / Rollback.

2. Cloner un snapshot :
   ```sh
   zfs clone POOL/DATASET@NOM_SNAP POOL/TEST_RESTAURATION
   ```
   👉 Explication : copie de test sans toucher à l'original.

3. Restaurer la configuration : Système > Général > Charger la configuration.
   ```sh
   ls -l /data/freenas-v1.db
   ```
   👉 Explication : la base de configuration est ce fichier ; à tester sur un NAS de test.

## 2. Production — Contrôles

Tester chaque trimestre et mesurer.

## 3. Production — Sécurité

Détruire le clone ensuite : `zfs destroy POOL/TEST_RESTAURATION`.

## Validation et retour arrière

- **Validation** : Données et configuration restaurées.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
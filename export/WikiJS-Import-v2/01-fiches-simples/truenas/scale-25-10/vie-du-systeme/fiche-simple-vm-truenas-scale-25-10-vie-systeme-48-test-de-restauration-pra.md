---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 48 Test De Restauration Pra"
description: "Prouver que les données et la configuration sont récupérables."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-48"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-48`

---

## Problème précis à résoudre

Prouver que les données et la configuration sont récupérables.

## 1. Hors-Production (Lab / Test / POC)

1. Restaurer un fichier depuis un snapshot : GUI Jeux de données > dataset > `.zfs/snapshot` (SMB : Versions précédentes).
   ```bash
   ls /mnt/POOL/DATASET/.zfs/snapshot/
   cp /mnt/POOL/DATASET/.zfs/snapshot/NOM_SNAP/FICHIER /mnt/POOL/DATASET/FICHIER_RESTAURE
   ```
   👉 Explication : NOM_SNAP est un snapshot existant.

2. Cloner un snapshot pour tester : GUI Jeux de données > Cloner dans un nouveau jeu de données.
   ```bash
   sudo zfs clone POOL/DATASET@NOM_SNAP POOL/TEST_RESTAURATION
   ```
   👉 Explication : copie de test sans toucher à l'original.

3. Restaurer la configuration : Système > Général > Gérer la configuration > Charger le fichier.
   ```bash
   sudo midclt call config.upload
   ```
   👉 Explication : à tester sur un NAS de test (redémarre).

## 2. Production — Contrôles

Tester chaque trimestre et mesurer le temps de restauration.

## 3. Production — Sécurité

Détruire le clone de test ensuite : `sudo zfs destroy POOL/TEST_RESTAURATION`.

## Validation et retour arrière

- **Validation** : Données et configuration restaurées.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 40 Configuration Des Sauvegardes"
description: "Sauvegarder les données et la configuration."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-40"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_40_Configuration_Des_Sauvegardes

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 40 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-40`

---

## Problème précis à résoudre

Sauvegarder les données et la configuration.

## 1. Hors-Production (Lab / Test / POC)

1. Snapshots périodiques : GUI Protection des données > Tâches d'instantanés > Ajouter.
   ```bash
   sudo zfs snapshot POOL/DATASET@MANUEL
   sudo zfs list -t snapshot -r POOL/DATASET
   ```
   👉 Explication : crée et liste les snapshots ; la tâche automatique applique la rétention.

2. Réplication : GUI Protection des données > Tâches de réplication > Ajouter.
   ```bash
   sudo midclt call replication.query | python3 -m json.tool | head -30
   ```
   👉 Explication : envoie les snapshots vers un autre NAS (ZFS send/recv).

3. Configuration : GUI Système > Général > Gérer la configuration > Télécharger le fichier.
   ```bash
   sudo midclt call config.save '{"secretseed": true}'
   ```
   👉 Explication : exporte la configuration (à stocker chiffrée hors du NAS).

## 2. Production — Contrôles

Règle 3-2-1 : trois copies, deux supports, une hors site.

## 3. Production — Sécurité

Chiffrer les sauvegardes et protéger les clés.

## Validation et retour arrière

- **Validation** : Une copie récente existe sur un autre système.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
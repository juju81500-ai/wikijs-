---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 14 Selection Des Composants De"
description: "Choisir le mode d'installation."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-14"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-14`

---

## Problème précis à résoudre

Choisir le mode d'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir Fresh Install (nouvelle installation) ou Upgrade selon le cas, puis le mode d'amorçage UEFI.
   👉 Explication : un ajout de paquets Debian n'est pas supporté sur un NAS.

2. Lister les services actifs après installation : GUI Système > Services.
   ```bash
   sudo midclt call service.query | python3 -m json.tool | grep -E '"service"|"state"'
   ```
   👉 Explication : tous les services de partage sont arrêtés par défaut.

## 2. Production — Contrôles

N'activer que les services nécessaires (SMB, NFS, iSCSI, SSH).

## 3. Production — Sécurité

Ne pas utiliser `apt` sur le système : l'appliance est gérée par mises à jour officielles.

## Validation et retour arrière

- **Validation** : Liste des services documentée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 01 Definition Des Besoins Sizing"
description: "Dimensionner le NAS (capacité utile, RAM ECC, redondance) avant la création."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-01"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-01`

---

## Problème précis à résoudre

Dimensionner le NAS (capacité utile, RAM ECC, redondance) avant la création.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les ressources d'une machine ou d'un NAS existant :
   ```sh
   sysctl hw.ncpu hw.physmem
   geom disk list | grep -E 'Name|Mediasize'
   zpool list
   ```
   👉 Explication : CPU, RAM, disques et occupation des pools actuels.

2. Calculer la capacité utile selon la topologie :
   ```sh
   # MIRROR : 50 % ; RAIDZ1 : (N-1)/N ; RAIDZ2 : (N-2)/N ; RAIDZ3 : (N-3)/N
   # Exemple : 6 disques de 8 To en RAIDZ2 = 32 To bruts, environ 28 To utilisables
   ```
   👉 Explication : ne pas dépasser environ 80 % d'occupation du pool ZFS.

3. Dimensionner la RAM : 8 Go minimum, puis environ 1 Go par To, de préférence ECC.
   👉 Explication : la RAM alimente le cache ARC ; l'ECC évite la corruption en mémoire.

4. Choisir des disques CMR (pas SMR) et un disque de démarrage séparé (SSD ou clé fiable de 16 Go minimum, miroir conseillé).
   👉 Explication : le pool de données n'est jamais le disque système.

## 2. Production — Contrôles

Ajouter 20 à 30 % de marge de croissance et valider la topologie avec le propriétaire du service.

## 3. Production — Sécurité

La redondance ZFS n'est pas une sauvegarde : prévoir une seconde copie hors du NAS.

## Validation et retour arrière

- **Validation** : Tableau de sizing signé et conservé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
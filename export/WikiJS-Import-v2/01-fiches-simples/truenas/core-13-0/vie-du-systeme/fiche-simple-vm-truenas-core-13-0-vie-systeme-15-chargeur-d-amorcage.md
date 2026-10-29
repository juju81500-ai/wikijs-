---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 15 Chargeur D Amorcage"
description: "Vérifier l'amorçage du système installé."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-15"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-15`

---

## Problème précis à résoudre

Vérifier l'amorçage du système installé.

## 1. Hors-Production (Lab / Test / POC)

1. Retirer la clé, redémarrer, puis vérifier le mode :
   ```sh
   sysctl machdep.bootmethod
   ```
   👉 Explication : affiche UEFI ou BIOS.

2. Lister les environnements d'amorçage : GUI Système > Mises à jour de démarrage.
   ```sh
   beadm list
   ```
   👉 Explication : chaque mise à jour crée un environnement de retour.

## 2. Production — Contrôles

Garder un environnement précédent.

## 3. Production — Sécurité

Protéger console et BMC.

## Validation et retour arrière

- **Validation** : Le NAS démarre seul.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
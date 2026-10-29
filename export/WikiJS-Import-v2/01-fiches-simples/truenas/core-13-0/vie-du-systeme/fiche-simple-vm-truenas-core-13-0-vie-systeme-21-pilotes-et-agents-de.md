---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 21 Pilotes Et Agents De"
description: "Optimiser lorsque le NAS est une VM."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-21"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-21`

---

## Problème précis à résoudre

Optimiser lorsque le NAS est une VM.

## 1. Hors-Production (Lab / Test / POC)

1. Sur une VM, présenter le contrôleur HBA en passthrough PCI.
   ```sh
   pciconf -lv | grep -i -B3 -E 'sas|sata|nvme'
   ```
   👉 Explication : ZFS accède aux disques physiques.

2. Pilote invité si disponible (VMware : service open-vm-tools).
   ```sh
   service -e | grep -i vm
   ```
   👉 Explication : peut être absent ; documenter.

3. Contrôler les disques :
   ```sh
   camcontrol devlist
   dmesg | grep -i -E 'error|fail' | tail
   ```
   👉 Explication : disques et erreurs de pilotes.

## 2. Production — Contrôles

Préférer matériel dédié.

## 3. Production — Sécurité

Pas de pilotes tiers sur l'appliance.

## Validation et retour arrière

- **Validation** : Tous les disques sont visibles.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
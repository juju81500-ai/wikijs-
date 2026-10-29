---
title: "Fiche Simple - VM Ubuntu 24.04 Vie Systeme 13 Partitionnement Et Systemes De"
description: "Choisir une disposition disque saine."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2404", "vie-du-systeme", "cycle-de-vie", "etape-13"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-13`

---

## Problème précis à résoudre

Choisir une disposition disque saine.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la disposition obtenue (l'installateur crée par défaut un volume LVM `ubuntu-vg/ubuntu-lv`, souvent plus petit que le disque) :
   ```bash
   lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS
   df -hT
   sudo vgs
   sudo lvs
   ```
   👉 Explication : affiche partitions, types de système de fichiers et volumes LVM; `VFree` non nul dans `vgs` indique de l'espace non alloué.

2. Utiliser l'espace libre du groupe de volumes :
   ```bash
   sudo lvextend -r -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
   ```
   👉 Explication : agrandit le volume et son système de fichiers à chaud (adapter le nom du volume à la sortie de `lvs`).

## 2. Production — Contrôles

Séparer `/var` et `/home` quand le service écrit beaucoup; prévoir `/boot/efi` en UEFI.

## 3. Production — Sécurité

Options `nodev,nosuid,noexec` sur les montages de données (étape 33).

## Validation et retour arrière

- **Validation** : `df -hT` correspond au plan de partitionnement.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
---
title: "Fiche Simple - VM Debian 13 Vie Systeme 13 Partitionnement Et Systemes De"
description: "Choisir une disposition disque saine."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian13", "vie-du-systeme", "cycle-de-vie", "etape-13"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-13`

---

## Problème précis à résoudre

Choisir une disposition disque saine.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la disposition obtenue :
   ```bash
   lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS
   df -hT
   sudo vgs
   sudo lvs
   ```
   👉 Explication : affiche partitions, types de système de fichiers et volumes LVM.

2. Pour agrandir un volume plus tard, suivre la fiche LVM.
   👉 Explication : l'agrandissement se fait à chaud avec `lvextend -r`.

## 2. Production — Contrôles

Séparer `/var` et `/home` quand le service écrit beaucoup; prévoir `/boot/efi` en UEFI.

## 3. Production — Sécurité

Options `nodev,nosuid,noexec` sur les montages de données (étape 33).

## Validation et retour arrière

- **Validation** : `df -hT` correspond au plan de partitionnement.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)
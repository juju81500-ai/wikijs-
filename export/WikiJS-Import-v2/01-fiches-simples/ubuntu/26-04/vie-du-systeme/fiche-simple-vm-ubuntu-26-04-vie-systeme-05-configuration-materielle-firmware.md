---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 05 Configuration Materielle Firmware"
description: "Choisir UEFI/BIOS, Secure Boot et pilotes de stockage."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-05"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_05_Configuration_Materielle_Firmware

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 05 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-05`

---

## Problème précis à résoudre

Choisir UEFI/BIOS, Secure Boot et pilotes de stockage.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir UEFI (OVMF) pour une VM neuve (Proxmox : **VM > Hardware > BIOS > OVMF (UEFI)**), contrôleur **VirtIO SCSI single**, CPU de type `host` :
   ```bash
   qm set VMID --bios ovmf --machine q35 --scsihw virtio-scsi-single --cpu host
   qm set VMID --efidisk0 local-lvm:1,efitype=4m
   ```
   👉 Explication : règle le firmware, le type de machine et le contrôleur disque (remplacer `VMID` et le stockage).

2. Après installation, contrôler le mode de démarrage :
   ```bash
   [ -d /sys/firmware/efi ] && echo UEFI || echo BIOS
   mokutil --sb-state
   ```
   👉 Explication : indique UEFI/BIOS et l'état de Secure Boot (`mokutil` : `sudo apt install mokutil`).

## 2. Production — Contrôles

Activer la virtualisation imbriquée seulement si nécessaire.

## 3. Production — Sécurité

Garder Secure Boot actif quand les pilotes le permettent.

## Validation et retour arrière

- **Validation** : Le système démarre en UEFI avec le disque VirtIO.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
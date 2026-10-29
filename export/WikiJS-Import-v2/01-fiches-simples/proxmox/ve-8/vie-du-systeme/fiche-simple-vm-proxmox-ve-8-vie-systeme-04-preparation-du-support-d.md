---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 04 Preparation Du Support D"
description: "Rendre l'ISO démarrable sur un serveur physique, via clé USB ou iDRAC/iLO."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-04"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-04`

---

## Problème précis à résoudre

Rendre l'ISO démarrable sur un serveur physique, via clé USB ou iDRAC/iLO.

## 1. Hors-Production (Lab / Test / POC)

1. Clé USB : repérer la clé puis écrire l'image (remplacer `sdX` par la clé; **efface tout**) :
   ```bash
   lsblk -o NAME,SIZE,MODEL,TRAN
   sudo dd if=proxmox-ve_X.Y-Z.iso of=/dev/sdX bs=1M conv=fsync status=progress
   ```
   👉 Explication : écrit l'ISO en mode bloc; ne pas utiliser un simple copier-coller de fichier.

2. Alternative sans clé : monter l'ISO en média virtuel dans la console de gestion (iDRAC : **Console virtuelle > Connecter le média virtuel > Mapper CD/DVD**; iLO : **Remote Console > Virtual Media**).
   👉 Explication : évite le déplacement sur site; l'ISO doit rester accessible pendant toute l'installation.

3. Si l'hôte de test est lui-même une VM sous Proxmox (nested), attacher l'ISO (GUI : **VM > Hardware > Add > CD/DVD Drive**) :
   ```bash
   qm set VMID --ide2 local:iso/proxmox-ve_X.Y-Z.iso,media=cdrom
   ```
   👉 Explication : `VMID` = numéro de la VM de test; l'ISO doit avoir été téléversée dans le stockage (**Storage > ISO Images > Upload**).

## 2. Production — Contrôles

Utiliser le média virtuel de l'iDRAC pour les serveurs distants.

## 3. Production — Sécurité

Effacer ou ranger la clé après usage; protéger l'accès à la console de gestion.

## Validation et retour arrière

- **Validation** : Le serveur démarre sur le menu d'installation Proxmox.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
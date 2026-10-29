---
title: "Fiche Simple - VM Alpine 3.19 Vie Systeme 21 Pilotes Et Agents De"
description: "Installer l'agent de l'hyperviseur."
published: true
date: 2026-10-29T20:22:10Z
tags: ["alpine319", "vie-du-systeme", "cycle-de-vie", "etape-21"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-21`

---

## Problème précis à résoudre

Installer l'agent de l'hyperviseur.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier l'hyperviseur :
   ```sh
   grep -i -m1 hypervisor /proc/cpuinfo && dmesg | grep -i -m3 -E 'kvm|vmware|hyper-v'
   ```
   👉 Explication : indique si la machine est virtualisée et par quoi.

2. Sur Proxmox/KVM, installer l'agent invité :
   ```sh
   doas apk add qemu-guest-agent
   doas rc-update add qemu-guest-agent default
   doas rc-service qemu-guest-agent start
   ```
   👉 Explication : permet à l'hyperviseur d'arrêter proprement la VM et de lire son adresse IP (activer aussi l'option dans la VM). Sur VMware, installer `open-vm-tools` de la même manière.

3. Contrôler le service :
   ```sh
   rc-service qemu-guest-agent status
   ```
   👉 Explication : doit afficher `started`.

## 2. Production — Contrôles

Activer l'option « Agent QEMU » dans les paramètres de la VM.

## 3. Production — Sécurité

N'installer que l'agent correspondant à l'hyperviseur.

## Validation et retour arrière

- **Validation** : L'hyperviseur affiche l'adresse IP de la VM.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)
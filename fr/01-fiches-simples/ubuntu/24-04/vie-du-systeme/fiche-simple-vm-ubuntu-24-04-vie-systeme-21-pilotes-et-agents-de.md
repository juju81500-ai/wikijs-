---
title: "Fiche Simple - VM Ubuntu 24.04 Vie Systeme 21 Pilotes Et Agents De"
description: "Installer l'agent adapté à l'hyperviseur."
published: true
date: 2026-11-03T09:36:13Z
tags: ["ubuntu2404", "vie-du-systeme", "cycle-de-vie", "etape-21"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : [[Glossary:VM]] Ubuntu Server 24-04 [[Glossary:LTS]] « noble »
- **OS / Version** : Ubuntu 24-04; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-21`

---

## Problème précis à résoudre

Installer l'agent adapté à l'hyperviseur.

## 1. Hors-Production (Lab / Test / POC)

1. Proxmox/QEMU :
   ```bash
   sudo apt install qemu-guest-agent
   sudo systemctl enable --now qemu-guest-agent
   ```
   👉 Explication : permet à l'hyperviseur de lire l'[[Glossary:IP]] et d'arrêter proprement la VM (activer **Options > [[Glossary:QEMU]] Guest Agent** côté Proxmox); sur certaines images l'unité démarre seule : `enable` peut être refusé, vérifier `status`.

2. VMware ou Hyper-V (selon la plateforme) :
   ```bash
   sudo apt install open-vm-tools
   # ou : sudo apt install linux-tools-virtual linux-cloud-tools-virtual
   ```
   👉 Explication : agents équivalents pour ESXi et Hyper-V.

## 2. Production — Contrôles

Un seul agent, celui de l'hyperviseur réel.

## 3. Production — Sécurité

Mettre à jour l'agent avec le système.

## Validation et retour arrière

- **Validation** : `systemctl status qemu-guest-agent` actif.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Ubuntu 24-04 Systeme Qemu Guest Agent](/fr/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/qemu/fiche-simple-vm-ubuntu-24-04-systeme-qemu-guest-agent)
- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Ubuntu 24-04](/fr/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
---
title: "Fiche Simple - VM Ubuntu 24.04 Systeme Qemu Guest Agent"
description: "Installer et activer qemu-guest-agent sur une VM Ubuntu Server 24.04 LTS pour que l'hyperviseur puisse lire l'adresse IP, arrêter proprement la VM et figer le système de fichiers lors des sauvegardes."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[qemu]", "[guest-agent]", "[proxmox]", "[virtio]", "[kvm]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Systeme_Qemu_Guest_Agent

- **Environnement** : VM Ubuntu Server (KVM / QEMU / Proxmox VE)
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat)
- **Catégorie** : Système / Agent de virtualisation
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[qemu]`, `[guest-agent]`, `[proxmox]`, `[virtio]`, `[kvm]`

## 🎯 Problème précis à résoudre
Installer et activer `qemu-guest-agent` sur une VM Ubuntu Server 24.04 LTS pour que l'hyperviseur puisse lire l'adresse IP, arrêter proprement la VM et figer le système de fichiers lors des sauvegardes.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier la présence du canal virtio exposé par l'hyperviseur :
   ```bash
   ls -l /dev/virtio-ports/
   ```
   👉 *Explication : Le périphérique `org.qemu.guest_agent.0` doit apparaître. S'il est absent, activer l'agent dans la configuration de la VM côté hyperviseur avant de poursuivre.*
2. Installer et démarrer l'agent :
   ```bash
   sudo apt update
   sudo apt install -y qemu-guest-agent
   sudo systemctl enable --now qemu-guest-agent
   systemctl status qemu-guest-agent --no-pager
   ```
   👉 *Explication : Le paquet fournit l'unité `qemu-guest-agent.service`, qui communique avec l'hyperviseur via le canal virtio.*

## ⚡ 2. Production — Façon Simplifiée
1. Activer l'option « Agent QEMU » de la VM côté hyperviseur (Proxmox VE : Options > QEMU Guest Agent), puis redémarrer la VM.
2. Vérifier la remontée d'informations depuis l'hôte, par exemple avec `qm agent <vmid> ping` sur Proxmox VE.
   👉 *Explication : Un retour vide signifie que l'agent ne tourne pas dans la VM ou que l'option n'est pas active côté hyperviseur.*

## 🔒 3. Production — Façon Sécurisée
1. Contrôler que l'agent ne reste pas bloqué au démarrage et qu'il redémarre seul en cas d'échec :
   ```bash
   systemctl show qemu-guest-agent --property=Restart,UnitFileState
   sudo journalctl -u qemu-guest-agent --since today --no-pager
   ```
   👉 *Explication : Vérifie l'état d'activation de l'unité et l'absence d'erreurs de canal ; l'agent ne doit pas être exposé hors du lien virtio.*
2. Restreindre les commandes autorisées à l'agent côté hyperviseur (liste blanche des commandes) si la politique de sécurité l'exige, plutôt que de les laisser toutes actives.

## ✅ Validation et retour arrière
- Depuis l'hyperviseur, confirmer que l'adresse IP de la VM remonte dans l'interface.
- Lancer un arrêt propre depuis l'hyperviseur et vérifier qu'il aboutit sans délai d'expiration.
- Retour arrière : `sudo systemctl disable --now qemu-guest-agent` puis `sudo apt purge -y qemu-guest-agent`.
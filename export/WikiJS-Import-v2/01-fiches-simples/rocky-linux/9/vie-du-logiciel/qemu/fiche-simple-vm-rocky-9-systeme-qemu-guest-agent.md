---
title: "Fiche Simple - VM Rocky 9 Systeme Qemu Guest Agent"
description: "Installer l'agent invité QEMU sur Rocky Linux 9 pour remonter les adresses IP à l'hyperviseur, permettre l'arrêt propre de la VM et créer des snapshots cohérents."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[rocky9]", "[rhel9]", "[qemu]", "[kvm]", "[virtio]", "[proxmox]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Rocky_9_Systeme_Qemu_Guest_Agent.md

- **Environnement** : VM KVM / QEMU (Proxmox VE, libvirt)
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec systemd
- **Catégorie** : Système & Services / Agent de virtualisation
- **Tags** : `[rocky9]`, `[rhel9]`, `[qemu]`, `[kvm]`, `[virtio]`, `[proxmox]`

## 🎯 Problème précis à résoudre
Installer l'agent invité QEMU sur Rocky Linux 9 pour remonter les adresses IP à l'hyperviseur, permettre l'arrêt propre de la VM et créer des snapshots cohérents.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Confirmer que la machine est bien une VM KVM / QEMU :
   ```bash
   systemd-detect-virt
   ```
   👉 Explication : Retourne `kvm` ou `qemu` pour une VM de ce type, et `none` sur un serveur physique.

2. Installer et activer l'agent :
   ```bash
   sudo dnf install -y qemu-guest-agent
   sudo systemctl enable --now qemu-guest-agent
   systemctl status qemu-guest-agent --no-pager
   ```
   👉 Explication : Le service `qemu-guest-agent.service` communique avec l'hyperviseur via le canal virtio-serial. Le statut doit afficher `active (running)`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activer l'agent côté hyperviseur (Proxmox : onglet Options de la VM, ligne « QEMU Guest Agent »), puis vérifier le périphérique sur la VM :
   ```bash
   ls -l /dev/virtio-ports/
   ```
   👉 Explication : Le port `org.qemu.guest_agent.0` doit être présent. Sans lui, l'agent ne peut pas dialoguer avec l'hyperviseur, même si le service tourne.

2. Vérifier depuis l'hyperviseur Proxmox :
   ```bash
   sudo qm agent <vmid> ping
   sudo qm agent <vmid> network-get-interfaces
   ```
   👉 Explication : `qm agent ping` valide la liaison. `network-get-interfaces` doit lister les adresses IP de la VM. Remplacer `<vmid>` par l'identifiant numérique de la VM.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restreindre les commandes que l'hyperviseur peut demander à l'agent. Éditer le fichier de configuration :
   ```bash
   sudo vi /etc/sysconfig/qemu-ga
   sudo systemctl restart qemu-guest-agent
   ```
   👉 Explication : Renseigner `BLACKLIST_RPC` avec les commandes à bloquer, par exemple `guest-exec,guest-file-open`. Le nom exact des options dépend de la version du paquet; contrôler le contenu du fichier avant modification.

2. Vérifier les droits sur le port virtio :
   ```bash
   ls -l /dev/virtio-ports/org.qemu.guest_agent.0
   ```
   👉 Explication : Le périphérique doit appartenir à `root` ou au groupe prévu par le paquet, sans accès en écriture pour les utilisateurs ordinaires.

---

## ✅ Contrôle
```bash
systemctl is-active qemu-guest-agent
```
👉 Explication : Doit retourner `active`. L'hyperviseur affiche alors l'adresse IP de la VM dans son résumé.
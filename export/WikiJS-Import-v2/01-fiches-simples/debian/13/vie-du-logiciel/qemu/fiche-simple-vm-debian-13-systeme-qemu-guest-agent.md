---
title: "Fiche Simple - VM Debian 13 Systeme Qemu Guest Agent"
description: "Installer et activer l'agent invité QEMU (qemu-guest-agent) sur Debian 13 pour permettre à l'hyperviseur de lire les adresses IP de la VM, de geler les systèmes de fichiers lors des snapshots cohérents et de demander un arrêt propre."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[debian13]", "[debian]", "[qemu]", "[kvm]", "[virtio]", "[proxmox]", "[virtualisation]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Debian_13_Systeme_Qemu_Guest_Agent

- **Environnement** : VM Debian 13 sur KVM / QEMU, Proxmox VE ou hyperviseur compatible virtio
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Système & Services / Agent de virtualisation
- **Tags** : `[debian13]`, `[debian]`, `[qemu]`, `[kvm]`, `[virtio]`, `[proxmox]`, `[virtualisation]`

## 🎯 Problème précis à résoudre
Installer et activer l'agent invité QEMU (`qemu-guest-agent`) sur Debian 13 pour permettre à l'hyperviseur de lire les adresses IP de la VM, de geler les systèmes de fichiers lors des snapshots cohérents et de demander un arrêt propre.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier que la VM tourne bien sur un hyperviseur KVM / QEMU :
   ```bash
   systemd-detect-virt
   ```
   👉 Explication : La commande affiche `kvm` lorsque Debian 13 est exécuté dans une VM KVM / QEMU, ce qui correspond au cas traité ici.

2. Installer l'agent invité :
   ```bash
   sudo apt-get update
   sudo apt-get install -y qemu-guest-agent
   ```
   👉 Explication : Le paquet installe le service `qemu-guest-agent.service` et les règles udev qui détectent le port virtio `org.qemu.guest_agent.0`.

3. Activer et démarrer le service, puis contrôler son état :
   ```bash
   sudo systemctl enable --now qemu-guest-agent
   systemctl status qemu-guest-agent --no-pager
   ```
   👉 Explication : Le démon démarre immédiatement et à chaque boot. L'état attendu est `active (running)`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sur l'hôte Proxmox VE, activer l'agent pour la VM puis arrêter et redémarrer complètement la VM (un simple reboot de l'invité ne suffit pas à ajouter le périphérique) :
   ```bash
   qm set <vmid> --agent enabled=1
   qm config <vmid> | grep -i agent
   ```
   👉 Explication : `<vmid>` est l'identifiant numérique de la VM dans Proxmox. Le périphérique virtio est ajouté au prochain démarrage complet de la VM.

2. Sur la VM Debian 13, vérifier le canal de communication et le service :
   ```bash
   ls -l /dev/virtio-ports/org.qemu.guest_agent.0
   sudo systemctl is-active qemu-guest-agent
   ```
   👉 Explication : Le fichier de périphérique doit exister, et le service doit répondre `active`.

3. Depuis l'hôte Proxmox, tester la réponse de l'agent :
   ```bash
   qm agent <vmid> ping
   qm agent <vmid> network-get-interfaces
   ```
   👉 Explication : `ping` confirme la communication ; `network-get-interfaces` doit lister les adresses IP de la VM, ce qui prouve que l'agent est opérationnel.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier les options de l'agent disponibles et les RPC bloquables avant de durcir la configuration :
   ```bash
   /usr/bin/qemu-ga --help | grep -iE "block|blacklist"
   ```
   👉 Explication : L'agent peut exécuter des commandes côté invité (`guest-exec`) lorsqu'il est pleinement actif. Si l'hyperviseur n'a pas besoin de cette fonction, elle doit être bloquée.

2. Bloquer les RPC non nécessaires via le fichier de configuration du paquet (vérifier d'abord la variable `DAEMON_ARGS` présente dans le fichier) :
   ```bash
   sudo nano /etc/default/qemu-guest-agent
   sudo systemctl restart qemu-guest-agent
   ```
   Ajouter dans `DAEMON_ARGS` l'option `--block-rpcs=guest-exec,guest-exec-status` si l'option est acceptée par `qemu-ga --help`.
   👉 Explication : Ce réglage empêche l'exécution de commandes à distance depuis l'hyperviseur, sans désactiver la remontée d'adresses IP ni les snapshots cohérents.

3. Après toute mise à jour du noyau ou de l'agent, redémarrer le service et refaire le test de la section 2 (façon simplifiée) :
   ```bash
   sudo systemctl restart qemu-guest-agent
   qm agent <vmid> ping
   ```
   👉 Explication : Un agent qui ne répond plus fausse les sauvegardes en mode snapshot, car le gel des systèmes de fichiers ne peut plus être coordonné.
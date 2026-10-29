---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 34 Durcissement Du Noyau Et"
description: "Appliquer des paramètres noyau prudents."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-34"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_34_Durcissement_Du_Noyau_Et

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 34 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-34`

---

## Problème précis à résoudre

Appliquer des paramètres noyau prudents.

## 1. Hors-Production (Lab / Test / POC)

1. Créer `/etc/sysctl.d/99-durcissement.conf` :
   ```bash
   net.ipv4.conf.all.rp_filter = 1
   net.ipv4.conf.all.accept_redirects = 0
   net.ipv4.conf.all.send_redirects = 0
   net.ipv4.icmp_echo_ignore_broadcasts = 1
   kernel.dmesg_restrict = 1
   ```
   👉 Explication : protège contre l'usurpation d'adresses et les redirections ICMP.

2. Appliquer :
   ```bash
   sysctl --system
   ```
   👉 Explication : charge tous les fichiers sysctl.

3. Ne pas désactiver `net.ipv4.ip_forward` ni les ponts : Proxmox en a besoin pour les VM.
   👉 Explication : un durcissement trop strict coupe le réseau des VM.

## 2. Production — Contrôles

Tester sur un nœud avant généralisation.

## 3. Production — Sécurité

Documenter chaque paramètre et son motif.

## Validation et retour arrière

- **Validation** : `sysctl net.ipv4.conf.all.rp_filter` renvoie 1 et les VM gardent le réseau.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
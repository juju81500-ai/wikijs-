---
title: "Fiche Simple - VM Debian 13 GNS3 Deploiement Dependances"
description: "Installer les prérequis APT et vérifier KVM."
published: true
date: 2026-10-29T20:14:10Z
tags: ["gns3", "debian13", "qemu", "kvm"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_GNS3_Deploiement_Dependances.md

- **Environnement** : Poste Debian 13 amd64
- **OS / Version** : Debian 13 Trixie amd64; GNS3 2.2.61 stable
- **Catégorie** : simulation reseau / dependances
- **Tags** : `gns3`, `debian13`, `qemu`, `kvm`

---

## Problème précis à résoudre

Installer les prérequis APT et vérifier KVM.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis :
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip pipx python3-pyqt6 python3-pyqt6.qtwebsockets python3-pyqt6.qtsvg qemu-kvm qemu-utils libvirt-clients libvirt-daemon-system virtinst ubridge vpcs ca-certificates curl gnupg2
   ```
   👉 Explication : Dynamips est volontairement omis (optionnel, compilation séparée).

2. Vérifier les outils :
   ```bash
   python3 --version
   qemu-system-x86_64 --version
   ```
   👉 Explication : on contrôle Python et QEMU.

3. Activer libvirt et contrôler KVM :
   ```bash
   sudo systemctl enable --now libvirtd
   ls -l /dev/kvm
   ```
   👉 Explication : si `/dev/kvm` n'existe pas, arrêter et vérifier VT-x/AMD-V, le noyau et la virtualisation imbriquée.

## 2. Production — Contrôles

Documenter les paquets installés et valider sur un poste pilote.

## 3. Production — Sécurité

- Ne pas contourner l'absence de KVM par des réglages de privilèges non documentés.

## Validation et retour arrière

- **Validation** : `/dev/kvm` existe et `libvirtd` est actif.
- **Retour arrière** : `sudo apt remove` des paquets ajoutés si le poste doit être restauré.

## Si le problème n'est pas résolu

- [GNS3 — installation Linux](https://docs.gns3.com/docs/getting-started/installation/linux)
- [Debian — paquet qemu-kvm](https://packages.debian.org/trixie/qemu-kvm)
- [Guide complet GNS3 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/77-deploiement-gns3-2-2-61-debian-13#2-installer-les-dependances-debian-13)
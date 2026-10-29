---
title: "Fiche Simple - VM Debian 13 OpenMediaVault Reprise"
description: "Savoir reprendre OMV après un échec réseau ou avant une modification majeure."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "openmediavault", "reprise", "omv-firstaid", "fstab"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_OpenMediaVault_Reprise.md

- **Environnement** : OpenMediaVault 8 sur Debian 13 minimal
- **OS / Version** : Debian 13; OpenMediaVault 8.0 Synchrony
- **Catégorie** : stockage / reprise
- **Tags** : `debian13`, `openmediavault`, `reprise`, `omv-firstaid`, `fstab`

---

## Problème précis à résoudre

Savoir reprendre OMV après un échec réseau ou avant une modification majeure.

## 1. Hors-Production (Lab / Test / POC)

1. Avant mise à niveau ou changement de stockage, vérifier l'état des disques :
   ```bash
   lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS
   sudo smartctl --scan-open
   ```
   👉 Explication : Confirme les volumes avant intervention.

2. En cas d'échec réseau, utiliser la console locale :
   ```bash
   sudo omv-firstaid
   ```
   👉 Explication : Menu de reprise OMV pour reconfigurer réseau et accès Web.

3. Contrôler les journaux du service Web :
   ```bash
   sudo journalctl -u nginx -n 50 --no-pager
   ```
   👉 Explication : Aide à diagnostiquer l'interface après un incident.

## 2. Production — Contrôles

Disposer d'une sauvegarde restaurable des données et d'un accès console avant toute mise à niveau majeure.

## 3. Production — Sécurité

- Ne pas éditer directement les portions gérées de `/etc/fstab` ni de `smb.conf`.
- Ces procédures n'ont pas été testées sur une VM : valider en environnement de test.

## Validation et retour arrière

- **Validation** : réseau et interface Web retrouvés, données montées.
- **Retour arrière** : restaurer la sauvegarde ou l'instantané.

## Si le problème n'est pas résolu

- [OpenMediaVault — installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html)
- [OpenMediaVault — prérequis](https://docs.openmediavault.org/en/latest/prerequisites.html)
- [Guide complet OpenMediaVault Debian 13](/02-fiches-completes/debian/13/installation-deploiement/66-deploiement-openmediavault-8-debian-13#8-reprise-et-limites)
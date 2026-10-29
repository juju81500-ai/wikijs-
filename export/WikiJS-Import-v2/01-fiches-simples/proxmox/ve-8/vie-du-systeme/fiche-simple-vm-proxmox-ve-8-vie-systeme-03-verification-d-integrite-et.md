---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 03 Verification D Integrite Et"
description: "Prouver que l'ISO n'est ni corrompue ni modifiée."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-03"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-03`

---

## Problème précis à résoudre

Prouver que l'ISO n'est ni corrompue ni modifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Comparer l'empreinte SHA-256 :
   ```bash
   sha256sum -c SHA256SUMS --ignore-missing
   ```
   👉 Explication : doit afficher `proxmox-ve_X.Y-Z.iso: OK`.

2. Sinon, comparer à la main avec l'empreinte publiée sur la page de téléchargement :
   ```bash
   sha256sum proxmox-ve_*.iso
   ```
   👉 Explication : les deux valeurs doivent être strictement identiques.

3. Consigner la date, le nom de l'ISO et l'empreinte dans le dossier.
   👉 Explication : traçabilité en cas d'audit.

## 2. Production — Contrôles

Conserver l'empreinte validée avec l'ISO dans le dépôt interne.

## 3. Production — Sécurité

Si la vérification échoue : supprimer l'image et la retélécharger depuis une autre connexion.

## Validation et retour arrière

- **Validation** : `OK` affiché par `sha256sum -c`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
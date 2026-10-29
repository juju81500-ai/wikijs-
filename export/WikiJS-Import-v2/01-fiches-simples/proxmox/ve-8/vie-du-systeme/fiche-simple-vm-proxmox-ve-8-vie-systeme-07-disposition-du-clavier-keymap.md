---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 07 Disposition Du Clavier Keymap"
description: "Que les touches saisies correspondent au clavier physique."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-07"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-07`

---

## Problème précis à résoudre

Que les touches saisies correspondent au clavier physique.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : champ **Keyboard Layout** = French.
   👉 Explication : évite les erreurs de saisie du mot de passe root.

2. Après installation :
   ```bash
   localectl status
   localectl set-keymap fr
   ```
   👉 Explication : affiche puis définit la disposition sur la console.

3. Tester sur la console (GUI : console iDRAC) en saisissant des caractères spéciaux (`|`, `/`, `&`).
   👉 Explication : valide la disposition avant de poursuivre.

## 2. Production — Contrôles

Idem sur tous les nœuds.

## 3. Production — Sécurité

Un mauvais clavier peut fausser le mot de passe : vérifier avant validation.

## Validation et retour arrière

- **Validation** : Les caractères spéciaux sont corrects en console.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
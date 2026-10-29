---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 07 Disposition Du Clavier Keymap"
description: "Que les touches saisies correspondent au clavier physique."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-07"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-07`

---

## Problème précis à résoudre

Que les touches saisies correspondent au clavier physique.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : écran **Select a Keyboard Layout** = French. Pour modifier ensuite (DCUI : **F2 > Configure Keyboard**).
   👉 Explication : évite les erreurs de saisie du mot de passe root.

2. Contrôler depuis le shell (SSH) :
   ```sh
   esxcli system settings keyboard layout get
   esxcli system settings keyboard layout set -l French
   ```
   👉 Explication : affiche puis définit la disposition de la console.

3. Tester sur la console en saisissant des caractères spéciaux.
   👉 Explication : valide la disposition avant de poursuivre.

## 2. Production — Contrôles

Idem sur tous les hôtes.

## 3. Production — Sécurité

Un mauvais clavier peut fausser le mot de passe : vérifier avant validation.

## Validation et retour arrière

- **Validation** : Les caractères spéciaux sont corrects en console.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
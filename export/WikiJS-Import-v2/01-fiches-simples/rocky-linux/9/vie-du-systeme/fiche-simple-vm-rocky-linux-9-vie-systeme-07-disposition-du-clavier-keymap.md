---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 07 Disposition Du Clavier Keymap"
description: "Configurer le clavier de la console."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-07"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-07`

---

## Problème précis à résoudre

Configurer le clavier de la console.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les dispositions françaises :
   ```bash
   localectl list-keymaps | grep -i '^fr'
   ```
   👉 Explication : repère `fr` ou `fr-latin9`.

2. Appliquer la disposition :
   ```bash
   sudo localectl set-keymap fr
   ```
   👉 Explication : écrit `/etc/vconsole.conf` (KEYMAP=fr).

3. Contrôler :
   ```bash
   localectl status
   ```
   👉 Explication : affiche `VC Keymap: fr`.

## 2. Production — Contrôles

Documenter la disposition utilisée en salle serveur.

## 3. Production — Sécurité

Un mauvais clavier fausse la saisie des mots de passe; tester avant de valider.

## Validation et retour arrière

- **Validation** : Les caractères saisis en console correspondent aux touches.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)
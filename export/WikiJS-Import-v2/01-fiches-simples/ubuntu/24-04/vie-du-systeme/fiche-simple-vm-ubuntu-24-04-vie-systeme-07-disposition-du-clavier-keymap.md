---
title: "Fiche Simple - VM Ubuntu 24.04 Vie Systeme 07 Disposition Du Clavier Keymap"
description: "Régler le clavier de la console."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2404", "vie-du-systeme", "cycle-de-vie", "etape-07"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-07`

---

## Problème précis à résoudre

Régler le clavier de la console.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir la disposition :
   ```bash
   sudo dpkg-reconfigure keyboard-configuration
   sudo localectl set-keymap fr
   localectl status
   ```
   👉 Explication : sélection du clavier (par exemple `fr`) et affichage de la configuration.

2. Appliquer sans redémarrer :
   ```bash
   sudo setupcon
   ```
   👉 Explication : recharge la disposition sur la console.

## 2. Production — Contrôles

Documenter la disposition pour l'accès console de secours.

## 3. Production — Sécurité

Vérifier le clavier avant de saisir un mot de passe fort.

## Validation et retour arrière

- **Validation** : Les caractères spéciaux sont corrects en console.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
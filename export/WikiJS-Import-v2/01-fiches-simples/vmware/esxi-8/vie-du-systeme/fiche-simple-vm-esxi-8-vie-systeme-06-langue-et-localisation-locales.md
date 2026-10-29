---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 06 Langue Et Localisation Locales"
description: "Choisir la langue de l'interface et du clavier d'installation."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-06"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-06`

---

## Problème précis à résoudre

Choisir la langue de l'interface et du clavier d'installation.

## 1. Hors-Production (Lab / Test / POC)

1. L'installateur ESXi est en anglais; seule la disposition du clavier se choisit. Pour l'interface web (Host Client), la langue suit le navigateur.
   👉 Explication : il n'y a pas de locale à générer comme sous Linux.

2. Après installation, vérifier la version et la langue du système :
   ```sh
   vmware -vl
   esxcli system version get
   ```
   👉 Explication : affiche version et build.

3. Conserver les consoles et journaux en anglais pour faciliter les recherches de support.
   👉 Explication : messages d'erreur reconnus par le support Broadcom.

## 2. Production — Contrôles

Garder la même configuration sur tous les hôtes.

## 3. Production — Sécurité

Aucun risque particulier.

## Validation et retour arrière

- **Validation** : `esxcli system version get` renvoie la version attendue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
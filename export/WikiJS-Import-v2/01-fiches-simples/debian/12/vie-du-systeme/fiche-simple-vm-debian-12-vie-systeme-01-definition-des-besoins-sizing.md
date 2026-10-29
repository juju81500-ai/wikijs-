---
title: "Fiche Simple - VM Debian 12 Vie Systeme 01 Definition Des Besoins Sizing"
description: "Dimensionner la machine avant de la créer."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-01"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-01`

---

## Problème précis à résoudre

Dimensionner la machine avant de la créer.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les ressources actuelles ou cibles :
   ```bash
   nproc
   free -h
   lsblk -o NAME,SIZE,TYPE
   uname -m
   ```
   👉 Explication : nombre de vCPU, RAM, disques et architecture (`x86_64` ou `aarch64`) pour comparer au besoin.

2. Mesurer les entrées/sorties d'une machine comparable :
   ```bash
   sudo apt install sysstat
   iostat -x 1 5
   ```
   👉 Explication : `%util` et `await` élevés indiquent un stockage à surdimensionner.

3. Noter vCPU, RAM, disque, IOPS, réseau et architecture dans le dossier du projet.
   👉 Explication : ce tableau sert de référence pour l'hyperviseur et pour la recette.

## 2. Production — Contrôles

Ajouter 20 à 30 % de marge, valider le dimensionnement avec le propriétaire du service.

## 3. Production — Sécurité

Prévoir un disque séparé pour `/var` ou les données si le service écrit beaucoup.

## Validation et retour arrière

- **Validation** : Tableau de sizing signé et conservé avec le dossier.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)
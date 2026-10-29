---
title: "Fiche Simple - VM OPNsense Vie Systeme 15 Chargeur D Amorcage"
description: "S'assurer que le pare-feu redémarre seul."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-15"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-15`

---

## Problème précis à résoudre

S'assurer que le pare-feu redémarre seul.

## 1. Hors-Production (Lab / Test / POC)

1. Laisser l'installateur écrire le chargeur d'amorçage sur le disque, retirer l'ISO puis redémarrer (console option 6 « Reboot »).
   👉 Explication : l'écran de démarrage FreeBSD puis le menu console s'affichent.

2. Contrôler les environnements de démarrage et l'amorçage :
   ```sh
   bectl list
   sysctl machdep.bootmethod
   ```
   👉 Explication : `bectl list` montre l'environnement actif (`NR`); Système > Snapshots donne la même vue dans l'interface.

## 2. Production — Contrôles

Prendre un environnement de démarrage avant chaque mise à jour.

## 3. Production — Sécurité

Retirer le média d'installation après l'installation.

## Validation et retour arrière

- **Validation** : Le pare-feu redémarre sans média et affiche le menu console.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)
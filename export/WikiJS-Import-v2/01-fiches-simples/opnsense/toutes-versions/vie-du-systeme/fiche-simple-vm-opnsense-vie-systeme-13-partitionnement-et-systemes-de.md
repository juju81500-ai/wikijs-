---
title: "Fiche Simple - VM OPNsense Vie Systeme 13 Partitionnement Et Systemes De"
description: "Choisir le système de fichiers de l'installation."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-13"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-13`

---

## Problème précis à résoudre

Choisir le système de fichiers de l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur, choisir `Guided Installation` en `ZFS` (recommandé) ou `UFS` pour un matériel très limité; ZFS permet les points de restauration.
   👉 Explication : ZFS active les environnements de démarrage (Système > Snapshots) pour annuler une mise à jour.

2. Choisir un disque en stripe (un disque) ou en `mirror` (deux disques) puis valider l'effacement du disque.
   👉 Explication : le miroir protège contre la panne d'un disque.

3. Contrôler l'état après installation :
   ```sh
   zpool status
   df -h
   gpart show
   ```
   👉 Explication : montre le pool, l'espace libre et la table de partitions.

## 2. Production — Contrôles

Surveiller l'espace disque (Lobby > Tableau de bord) pour que les journaux n'emplissent pas le disque.

## 3. Production — Sécurité

Ne pas installer sur un disque contenant des données à conserver.

## Validation et retour arrière

- **Validation** : `zpool status` indique `ONLINE` sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)
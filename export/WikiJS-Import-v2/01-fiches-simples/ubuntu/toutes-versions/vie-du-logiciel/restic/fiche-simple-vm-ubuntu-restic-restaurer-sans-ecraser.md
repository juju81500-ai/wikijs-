---
title: "Fiche Simple - VM Ubuntu Restic Restaurer Sans Ecraser"
description: "Restaurer d'abord vers une zone temporaire."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu", "restic", "sauvegarde", "restauration", "retention"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_Restic_Restaurer_Sans_Ecraser.md

- **Environnement** : VM Ubuntu Server avec destination de sauvegarde indépendante
- **OS / Version** : Ubuntu Server (toutes versions supportées); paquet restic des dépôts Ubuntu
- **Catégorie** : sauvegarde / restauration
- **Tags** : `ubuntu`, `restic`, `sauvegarde`, `restauration`, `retention`

---

## Problème précis à résoudre

Restaurer d'abord vers une zone temporaire.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les snapshots puis restaurer (ID_SNAPSHOT est à remplacer par l'identifiant choisi) :
   ```bash
   restic snapshots
   restic restore ID_SNAPSHOT --target /mnt/restore-test
   ```
   👉 Explication : la restauration se fait hors production.

2. Contrôler propriétaires, permissions, complétude, cohérence des dumps et ouverture des fichiers.
   👉 Explication : on prouve que la sauvegarde est exploitable.

3. Restaurer ensuite en production avec le service arrêté et un plan de retour arrière préparé.
   👉 Explication : on évite d'écraser des données vivantes.

## 2. Production — Contrôles

Préparer un plan de retour arrière avant la restauration réelle.

## 3. Production — Sécurité

- Ne jamais restaurer directement sur `/` ou sur les données de production sans plan.

## Validation et retour arrière

- **Validation** : Les fichiers restaurés sont complets et exploitables.
- **Retour arrière** : Supprimer `/mnt/restore-test` après contrôle.

## Si le problème n'est pas résolu

- [Restic — Documentation officielle](https://restic.readthedocs.io/en/stable/)
- [Ubuntu — Documentation serveur](https://documentation.ubuntu.com/server/)
- [Guide complet sauvegarde Ubuntu Server Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic#6-restaurer-sans-ecraser)
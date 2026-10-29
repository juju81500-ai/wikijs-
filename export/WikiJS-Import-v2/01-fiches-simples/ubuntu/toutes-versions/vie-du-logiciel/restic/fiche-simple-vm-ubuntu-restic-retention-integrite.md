---
title: "Fiche Simple - VM Ubuntu Restic Retention Integrite"
description: "Appliquer la politique de rétention puis contrôler le dépôt."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu", "restic", "sauvegarde", "restauration", "retention"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_Restic_Retention_Integrite.md

- **Environnement** : VM Ubuntu Server avec destination de sauvegarde indépendante
- **OS / Version** : Ubuntu Server (toutes versions supportées); paquet restic des dépôts Ubuntu
- **Catégorie** : sauvegarde / restauration
- **Tags** : `ubuntu`, `restic`, `sauvegarde`, `restauration`, `retention`

---

## Problème précis à résoudre

Appliquer la politique de rétention puis contrôler le dépôt.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier d'abord que plusieurs sauvegardes récentes existent :
   ```bash
   restic snapshots
   ```
   👉 Explication : on ne purge pas sans sauvegarde de remplacement.

2. Appliquer la rétention puis contrôler l'intégrité :
   ```bash
   restic forget --tag ubuntu-server --keep-daily 7 --keep-weekly 5 --keep-monthly 12 --prune
   restic check
   ```
   👉 Explication : `forget --prune` supprime des données devenues inutiles; `check` vérifie la cohérence du dépôt.

## 2. Production — Contrôles

Planifier `forget --prune`, suivre son résultat et protéger la rétention contre l'altération si le backend le permet.

## 3. Production — Sécurité

- `forget --prune` est destructif : vérifier la politique avant.

## Validation et retour arrière

- **Validation** : `restic check` ne signale aucune erreur.
- **Retour arrière** : Les données purgées ne reviennent pas : restaurer depuis un autre dépôt si nécessaire.

## Si le problème n'est pas résolu

- [Restic — Documentation officielle](https://restic.readthedocs.io/en/stable/)
- [Ubuntu — Documentation serveur](https://documentation.ubuntu.com/server/)
- [Guide complet sauvegarde Ubuntu Server Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic#5-retention-et-controle-dintegrite)
---
title: "Fiche Simple - VM Ubuntu Restic Effectuer Sauvegarde"
description: "Lancer une première sauvegarde contrôlée."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu", "restic", "sauvegarde", "restauration", "retention"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_Restic_Effectuer_Sauvegarde.md

- **Environnement** : VM Ubuntu Server avec destination de sauvegarde indépendante
- **OS / Version** : Ubuntu Server (toutes versions supportées); paquet restic des dépôts Ubuntu
- **Catégorie** : sauvegarde / restauration
- **Tags** : `ubuntu`, `restic`, `sauvegarde`, `restauration`, `retention`

---

## Problème précis à résoudre

Lancer une première sauvegarde contrôlée.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le montage et l'espace de destination :
   ```bash
   mountpoint -q /mnt/backup && echo monte
   df -h /mnt/backup
   ```
   👉 Explication : la destination doit être montée avec de l'espace libre.

2. Sauvegarder les chemins validés (adapter les chemins au serveur) :
   ```bash
   restic backup /etc /home /srv /var/backups --tag ubuntu-server
   restic snapshots
   ```
   👉 Explication : le tag permet de cibler la rétention; la commande ne sauvegarde pas les données applicatives situées ailleurs.

## 2. Production — Contrôles

Exclure pseudo-systèmes, caches, secrets temporaires et volumes de base en cours d'écriture; vérifier les dumps de bases avant.

## 3. Production — Sécurité

- Ne pas inclure de secrets temporaires.

## Validation et retour arrière

- **Validation** : Un snapshot récent apparaît dans `restic snapshots`.
- **Retour arrière** : Supprimer un snapshot erroné avec `restic forget ID_SNAPSHOT` (ID réel à indiquer).

## Si le problème n'est pas résolu

- [Restic — Documentation officielle](https://restic.readthedocs.io/en/stable/)
- [Ubuntu — Documentation serveur](https://documentation.ubuntu.com/server/)
- [Guide complet sauvegarde Ubuntu Server Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic#4-effectuer-une-sauvegarde)
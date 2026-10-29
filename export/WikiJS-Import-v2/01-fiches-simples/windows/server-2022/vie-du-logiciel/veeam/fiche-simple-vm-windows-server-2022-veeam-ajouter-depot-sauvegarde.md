---
title: "Fiche Simple - VM Windows Server 2022 Veeam Ajouter Depot Sauvegarde"
description: "Ajouter un dépôt dédié, de préférence immuable pour les données critiques."
published: true
date: 2026-10-29T20:14:10Z
tags: ["windows-server-2022", "veeam", "backup-replication", "hyper-v", "repository", "immutabilite"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Veeam_Ajouter_Depot_Sauvegarde.md

- **Environnement** : Serveur Windows Server 2022 dédié au serveur de sauvegarde Veeam (pilote autonome) et hôte Hyper-V autorisé
- **OS / Version** : Windows Server 2022; Veeam Backup & Replication 13.1.2.57
- **Catégorie** : sauvegarde VM / dépôt
- **Tags** : `windows-server-2022`, `veeam`, `backup-replication`, `hyper-v`, `repository`, `immutabilite`

---

## Problème précis à résoudre

Ajouter un dépôt dédié, de préférence immuable pour les données critiques.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'espace du volume dédié :
   ```powershell
   Get-Volume | Select-Object DriveLetter, SizeRemaining, Size
   ```
   👉 Explication : dimensionner capacité, IOPS, rétention et espace de restauration.

2. Ajouter le dépôt : **Console Veeam > Backup Infrastructure > Backup Repositories > Add Repository**
   👉 Explication : choisir un chemin qui ne recoupe pas un autre dépôt Veeam.

3. Pour les données critiques, ajouter un dépôt Linux durci immuable ou un stockage objet avec verrouillage : **Add Repository > Direct attached storage > Linux (Hardened Repository)**
   👉 Explication : l'immuabilité empêche la suppression des copies pendant la période de rétention.

## 2. Production — Contrôles

L'immuabilité ne remplace ni une copie hors site ni des identifiants séparés.

## 3. Production — Sécurité

- Restreindre l'administration du dépôt.
- Empêcher que le compte Veeam puisse supprimer facilement les copies protégées.

## Validation et retour arrière

- **Validation** : le dépôt apparaît avec sa capacité et passe le test.
- **Retour arrière** : **Backup Repositories > clic droit sur le dépôt > Remove** (aucune donnée n'est supprimée du disque).

## Si le problème n'est pas résolu

- [Veeam 13 — guide utilisateur](https://helpcenter.veeam.com/docs/vbr/userguide/)
- [Veeam 13 — installer Backup & Replication](https://helpcenter.veeam.com/docs/vbr/userguide/install_vbr.html)
- [Veeam 13 — dépôt durci](https://helpcenter.veeam.com/docs/vbr/userguide/hardened_repository.html)
- [Guide complet Veeam Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/58-deploiement-veeam-backup-replication-13-windows-server-2022#3-ajouter-un-depot-de-sauvegarde)
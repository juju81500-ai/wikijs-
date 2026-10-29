---
title: "Fiche Simple - VM Windows Server 2022 Veeam Dimensionner Infrastructure"
description: "Vérifier que le futur serveur Veeam respecte les minimums annoncés."
published: true
date: 2026-10-29T20:14:10Z
tags: ["windows-server-2022", "veeam", "backup-replication", "hyper-v", "dimensionnement"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Veeam_Dimensionner_Infrastructure.md

- **Environnement** : Serveur Windows Server 2022 dédié au serveur de sauvegarde Veeam (pilote autonome) et hôte Hyper-V autorisé
- **OS / Version** : Windows Server 2022; Veeam Backup & Replication 13.1.2.57
- **Catégorie** : sauvegarde VM / cadrage
- **Tags** : `windows-server-2022`, `veeam`, `backup-replication`, `hyper-v`, `dimensionnement`

---

## Problème précis à résoudre

Vérifier que le futur serveur Veeam respecte les minimums annoncés.

## 1. Hors-Production (Lab / Test / POC)

1. Lire cœurs, mémoire et version Windows :
   ```powershell
   Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores
   Get-CimInstance Win32_ComputerSystem | Select-Object @{n='RAM_Go';e={[math]::Round($_.TotalPhysicalMemory/1GB,1)}}
   (Get-CimInstance Win32_OperatingSystem).Caption
   ```
   👉 Explication : le minimum annoncé est 8 cœurs et 16 Go de RAM, plus 500 Mo par job concurrent.

2. Lire l'espace disque des volumes :
   ```powershell
   Get-Volume | Select-Object DriveLetter, FileSystemLabel, @{n='Libre_Go';e={[math]::Round($_.SizeRemaining/1GB,1)}}, @{n='Taille_Go';e={[math]::Round($_.Size/1GB,1)}}
   ```
   👉 Explication : dimensionner la capacité du dépôt, du catalogue et de la restauration.

3. GUI équivalent : **Gestionnaire de serveur > Serveur local**
   👉 Explication : affiche OS, processeurs et mémoire.

## 2. Production — Contrôles

Calculer débit, concurrence, catalogue, fenêtre, rétention, capacité, copie hors site et bande passante de restauration; prévoir un serveur distinct des hôtes protégés.

## 3. Production — Sécurité

- Une installation autonome n'est pas une architecture HA/PRA.
- Utiliser des comptes de service dédiés et un stockage à accès restreint.

## Validation et retour arrière

- **Validation** : ressources conformes aux exigences courantes de la version.
- **Retour arrière** : lecture seule: rien à annuler.

## Si le problème n'est pas résolu

- [Veeam 13 — guide utilisateur](https://helpcenter.veeam.com/docs/vbr/userguide/)
- [Veeam 13 — installer Backup & Replication](https://helpcenter.veeam.com/docs/vbr/userguide/install_vbr.html)
- [Veeam 13 — exigences du serveur de sauvegarde](https://helpcenter.veeam.com/docs/vbr/userguide/system_requirements_backup_server.html)
- [Guide complet Veeam Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/58-deploiement-veeam-backup-replication-13-windows-server-2022#1-dimensionner-linfrastructure)
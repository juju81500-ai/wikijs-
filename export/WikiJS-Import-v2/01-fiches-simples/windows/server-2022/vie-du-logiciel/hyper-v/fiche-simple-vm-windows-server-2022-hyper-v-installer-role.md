---
title: "Fiche Simple - VM Windows Server 2022 Hyper V Installer Role"
description: "Installer le rôle et ses outils de gestion."
published: true
date: 2026-10-29T20:14:10Z
tags: ["hyper-v", "windows-server-2022", "virtualisation", "vm", "powershell"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Installer_Role.md

- **Environnement** : Hôte Hyper-V autonome Windows Server 2022 (hors cluster)
- **OS / Version** : Windows Server 2022 Standard ou Datacenter
- **Catégorie** : virtualisation / installation
- **Tags** : `hyper-v`, `windows-server-2022`, `virtualisation`, `vm`, `powershell`

---

## Problème précis à résoudre

Installer le rôle et ses outils de gestion.

## 1. Hors-Production (Lab / Test / POC)

1. Dans une session PowerShell élevée :
   ```powershell
   Install-WindowsFeature -Name Hyper-V -IncludeManagementTools -Restart
   ```
   👉 Explication : installe le rôle et redémarre l'hôte.

2. GUI équivalente : **Server Manager > Manage > Add Roles and Features > Hyper-V**.
   👉 Explication : même résultat par l'assistant.

3. Après redémarrage, confirmer :
   ```powershell
   Get-WindowsFeature Hyper-V
   Get-VMHost
   ```
   👉 Explication : le rôle doit être `Installed` et l'hôte lisible.

4. Valider privilèges, WinRM et chemin de gestion avant toute configuration à distance.
   👉 Explication : évite de perdre l'accès.

## 2. Production — Contrôles

Faire l'installation dans une fenêtre approuvée avec console hors bande.

## 3. Production — Sécurité

- Accès d'administration limité.

## Validation et retour arrière

- **Validation** : `Get-WindowsFeature Hyper-V` indique `Installed`.
- **Retour arrière** : Avant retrait du rôle : arrêter ou migrer les VM, sauvegarder, puis suivre la procédure Microsoft.

## Si le problème n'est pas résolu

- [Microsoft — installer Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-hyper-v)
- [Microsoft — créer un commutateur virtuel](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines)
- [Guide complet — 2. Installer le rôle Hyper-V](/02-fiches-completes/windows/server-2022/installation-deploiement/55-deploiement-hyper-v-windows-server-2022#2-installer-le-role-hyper-v)
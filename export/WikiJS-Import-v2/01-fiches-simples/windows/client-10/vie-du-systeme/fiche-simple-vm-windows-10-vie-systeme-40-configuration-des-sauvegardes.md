---
title: "Fiche Simple - VM Windows 10 Vie Systeme 40 Configuration Des Sauvegardes"
description: "Sauvegarder les données et l'état du poste."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows10", "vie-du-systeme", "cycle-de-vie", "etape-40"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_40_Configuration_Des_Sauvegardes

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 40 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-40`

---

## Problème précis à résoudre

Sauvegarder les données et l'état du poste.

## 1. Hors-Production (Lab / Test / POC)

1. Activer l'historique des fichiers ou OneDrive : **Paramètres > Comptes > Sauvegarde Windows**, **Paramètres > Système > Stockage**, ou **Panneau de configuration > Historique des fichiers**.
   ```powershell
   Get-Service fhsvc | Select-Object Name,Status,StartType
   ```
   👉 Explication : le service d'historique des fichiers doit être disponible.

2. Rediriger les dossiers Documents, Bureau et Images vers OneDrive Entreprise (Known Folder Move) par GPO ou Intune.
   ```powershell
   Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders' | Select-Object Personal,Desktop
   ```
   👉 Explication : montre où pointent les dossiers utilisateur.

3. Créer une sauvegarde système si la politique l'exige.
   ```powershell
   wbadmin start backup -backupTarget:\\SERVEUR\Sauvegardes -include:C: -allCritical -quiet
   ```
   👉 Explication : sauvegarde le volume système vers un partage (`SERVEUR\Sauvegardes`).

4. Activer la protection du système et un point de restauration : **Panneau de configuration > Système > Protection du système**.
   ```powershell
   Enable-ComputerRestore -Drive 'C:\'
   Get-ComputerRestorePoint
   ```
   👉 Explication : permet un retour arrière après une mise à jour ou un changement.

## 2. Production — Contrôles

Les données vivent sur un espace sauvegardé (OneDrive, partage); le poste lui-même est réinstallable.

## 3. Production — Sécurité

Chiffrer les sauvegardes et ne pas stocker de clé dans le même emplacement.

## Validation et retour arrière

- **Validation** : Dernière sauvegarde réussie et restauration d'un fichier test confirmée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
---
title: "Fiche Simple - VM Windows 11 Vie Systeme 23 Outils D Administration Fondamentaux"
description: "Installer les outils indispensables à l'administration et au dépannage."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows11", "vie-du-systeme", "cycle-de-vie", "etape-23"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_23_Outils_D_Administration_Fondamentaux

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 23 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-23`

---

## Problème précis à résoudre

Installer les outils indispensables à l'administration et au dépannage.

## 1. Hors-Production (Lab / Test / POC)

1. Installer PowerShell 7 et Windows Terminal : **Microsoft Store** ou WinGet.
   ```powershell
   winget install --id Microsoft.PowerShell -e
   winget install --id Microsoft.WindowsTerminal -e
   ```
   👉 Explication : installe les versions officielles à jour.

2. Installer les outils d'administration à distance (RSAT) : **Paramètres > Système > Fonctionnalités facultatives > Ajouter une fonctionnalité > RSAT**.
   ```powershell
   Get-WindowsCapability -Online -Name 'Rsat.ActiveDirectory*' | Add-WindowsCapability -Online
   ```
   👉 Explication : ajoute les outils Active Directory.

3. Installer Sysinternals pour le diagnostic.
   ```powershell
   winget install --id Microsoft.Sysinternals.ProcessExplorer -e
   winget install --id Microsoft.Sysinternals.Autoruns -e
   ```
   👉 Explication : installe Process Explorer et Autoruns depuis la source officielle.

4. Vérifier les versions installées.
   ```powershell
   $PSVersionTable.PSVersion
   winget list | Select-String 'PowerShell|Terminal|Sysinternals'
   ```
   👉 Explication : contrôle les composants installés.

## 2. Production — Contrôles

Outils standardisés et déployés par Intune ou le catalogue interne.

## 3. Production — Sécurité

Installer seulement depuis des sources officielles et vérifier la signature (`Get-AuthenticodeSignature`).

## Validation et retour arrière

- **Validation** : Les outils démarrent et leurs versions sont consignées.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows 11 PowerShell7 Installer Version Stable](</01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-installer-version-stable>)
- [Fiche détaillée : VM Windows 11 Sysinternals Telecharger Verifier](</01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-telecharger-verifier>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
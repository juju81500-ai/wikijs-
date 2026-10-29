---
title: "Fiche Simple - VM Windows 11 PowerShell Valider Shell Admin"
description: "Vérifier PowerShell 7, différencier le shell 5.1, puis effectuer des contrôles locaux en lecture seule sans modifier une stratégie de sécurité."
published: true
date: 2026-10-29T20:14:10Z
tags: ["[windows-11]", "[powershell]", "[pwsh]", "[diagnostic]", "[administration]", "[securite]"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_11_PowerShell_Valider_Shell_Admin.md

- **Environnement** : VM ou poste Windows 11 de test; compte standard puis élévation uniquement si requise
- **OS / Version** : Windows 11 x64; PowerShell 7.6.9 et Windows PowerShell 5.1 côte à côte
- **Catégorie** : administration / diagnostic / scripting
- **Tags** : `[windows-11]`, `[powershell]`, `[pwsh]`, `[diagnostic]`, `[administration]`, `[securite]`

## Problème précis à résoudre

Vérifier PowerShell 7, différencier le shell 5.1, puis effectuer des contrôles locaux en lecture seule sans modifier une stratégie de sécurité.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le MSI x64 de la publication officielle PowerShell 7.6.9 après contrôle Authenticode et SHA-256.
2. Ouvrir PowerShell 7 et confirmer le shell :
   ```powershell
   $PSVersionTable | Select-Object PSVersion, PSEdition, Platform
   $PSHOME
   ```
3. Vérifier que la version historique reste disponible et comparer l'exécutable courant :
   ```powershell
   Get-Command pwsh, powershell -ErrorAction SilentlyContinue | Select-Object Name, Source
   (Get-Process -Id $PID).Path
   ```
4. Exécuter des contrôles en lecture seule :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-NetIPConfiguration
   Get-Service | Where-Object Status -eq 'Running' | Select-Object Name, DisplayName
   ```

**Équivalent interface graphique :**

- Clic droit sur **Démarrer > Terminal (administrateur)**, valider l'invite **UAC**; le titre de la fenêtre commence par « Administrateur ».
  👉 Explication : équivalent graphique pour obtenir un shell élevé.

## 2. Production — Contrôles

Exécuter avec un compte standard, vérifier la version avant un script, utiliser des modules approuvés et ne demander une élévation UAC que pour les commandes qui la nécessitent. Respecter les stratégies d'exécution et de journalisation imposées par l'organisation.

## 3. Production — Sécurité

- Ne pas utiliser `Bypass` ou `Unrestricted` pour « réparer » l'exécution d'un script.
- Lire et vérifier source, cible, version et effets; privilégier `-WhatIf` lorsque la commande le supporte.
- Ne pas stocker de secrets dans le profil, l'historique ou un transcript.
- Ne pas activer WinRM/PowerShell Remoting ni déployer un script sur plusieurs machines depuis cette fiche.

## Validation et retour arrière

- **Validation** : MSI signé, version attendue, les deux shells sont identifiables, contrôles lecture seule effectués.
- **Retour arrière** : PowerShell 7 s'ajoute côte à côte; désinstaller uniquement cette version via **Applications installées** si elle pose problème. Ne pas supprimer Windows PowerShell 5.1.

## Si le problème n'est pas résolu

- [Microsoft Learn — Installation PowerShell sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [Microsoft Learn — Stratégies d'exécution](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy)
- [Guide complet PowerShell 7.6.9 Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11)
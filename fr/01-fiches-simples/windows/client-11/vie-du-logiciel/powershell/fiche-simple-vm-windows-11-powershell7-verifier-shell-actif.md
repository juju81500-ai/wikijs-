---
title: "fiche-simple-vm-windows-11-powershell7-verifier-shell-actif"
description: "Confirmer que la session utilise bien PowerShell 7."
published: true
date: 2026-11-03T14:22:28Z
tags: ["windows-11", "powershell", "pwsh", "administration", "scripts", "securite"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# fiche-simple-vm-windows-11-powershell7-verifier-shell-actif.md

- **Environnement** : [[Glossary:VM]] ou poste Windows 11 de test; compte standard puis élévation uniquement si requise
- **OS / Version** : Windows 11 x64; PowerShell 7.6.9 Stable ([[Glossary:LTS]])
- **Catégorie** : administration / PowerShell
- **Tags** : `windows-11`, `powershell`, `pwsh`, `administration`, `scripts`, `securite`

---

## Problème précis à résoudre

Confirmer que la session utilise bien PowerShell 7.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Menu Démarrer > PowerShell 7**.
   👉 Explication : on lance le nouveau shell et non Windows PowerShell 5.1.

2. Contrôler version et chemin d'exécutable :
   ```powershell
   $PSVersionTable | Select-Object PSVersion, PSEdition, Platform
   $PSHOME
   (Get-Process -Id $PID).Path
   Get-Command pwsh, powershell -ErrorAction SilentlyContinue | Select-Object Name, Source
   ```
   👉 Explication : `pwsh` identifie PowerShell 7; `powershell.exe` lance 5.1.

## 2. Production — Contrôles

Vérifier `$PSVersionTable` avant d'exécuter un script dont le support de version est limité.

## 3. Production — Sécurité

- Ne pas exécuter en administrateur pour un simple contrôle.

## Validation et retour arrière

- **Validation** : PSVersion 7.6.9 et chemin sous `C:\Program Files\PowerShell\7`.
- **Retour arrière** : Fermer le shell; aucune modification n'a été faite.

## Si le problème n'est pas résolu

- [Microsoft Learn — Installer PowerShell 7 sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [PowerShell — publication v7.6.9](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9)
- [Guide complet PowerShell 7.6.9 Windows 11](/fr/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11#3-verifier-le-shell-actif)
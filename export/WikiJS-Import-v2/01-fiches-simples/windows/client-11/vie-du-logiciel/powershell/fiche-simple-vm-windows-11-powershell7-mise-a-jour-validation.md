---
title: "Fiche Simple - VM Windows 11 PowerShell7 Mise A Jour Validation"
description: "Mettre à jour PowerShell 7 et valider l'état final."
published: true
date: 2026-10-29T20:14:10Z
tags: ["windows-11", "powershell", "pwsh", "administration", "scripts", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_11_PowerShell7_Mise_A_Jour_Validation.md

- **Environnement** : VM ou poste Windows 11 de test; compte standard puis élévation uniquement si requise
- **OS / Version** : Windows 11 x64; PowerShell 7.6.9 Stable (LTS)
- **Catégorie** : administration / PowerShell
- **Tags** : `windows-11`, `powershell`, `pwsh`, `administration`, `scripts`, `securite`

---

## Problème précis à résoudre

Mettre à jour PowerShell 7 et valider l'état final.

## 1. Hors-Production (Lab / Test / POC)

1. Suivre les publications PowerShell et le cycle de support Microsoft.
   👉 Explication : on planifie les mises à jour.

2. Mettre à jour avec la même méthode que l'installation, revérifier signature et hash comme à l'étape d'installation.
   👉 Explication : on ne dégrade pas le niveau de contrôle.

3. Valider le résultat :
   ```powershell
   pwsh -NoProfile -Command '$PSVersionTable.PSVersion'
   Get-Command powershell | Select-Object Name, Source
   Get-ExecutionPolicy -List
   ```
   👉 Explication : `pwsh` lance la version attendue, Windows PowerShell 5.1 reste disponible et aucune stratégie n'a été remplacée.

4. Tester les scripts et modules concernés sur un poste pilote.
   👉 Explication : on évite une régression de compatibilité.

## 2. Production — Contrôles

Vérifier que les modules employés sont connus, approuvés et compatibles.

## 3. Production — Sécurité

- Aucun secret dans le profil ou le journal.
- Ne pas remplacer une politique d'exécution de l'organisation.

## Validation et retour arrière

- **Validation** : Version attendue, 5.1 disponible, scripts pilotes valides.
- **Retour arrière** : Réinstaller le MSI de la version précédente après vérification de signature et de hash.

## Si le problème n'est pas résolu

- [Microsoft Learn — Installer PowerShell 7 sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [PowerShell — publication v7.6.9](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9)
- [Guide complet PowerShell 7.6.9 Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11#8-mise-a-jour-et-validation)
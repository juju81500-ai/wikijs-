# Fiche_Simple_-_VM_Windows_11_PowerShell7_Versions_Perimetre.md

- **Environnement** : VM ou poste Windows 11 de test; compte standard puis élévation uniquement si requise
- **OS / Version** : Windows 11 x64; PowerShell 7.6.9 Stable (LTS)
- **Catégorie** : administration / PowerShell

---

## Problème précis à résoudre

Identifier les shells PowerShell présents et le périmètre de l'administration locale.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Menu Démarrer > Windows PowerShell** (5.1) et noter son existence.
   👉 Explication : PowerShell 7 s'installe côte à côte et ne remplace pas Windows PowerShell 5.1.

2. Lire la version du shell courant :
   ```powershell
   $PSVersionTable | Select-Object PSVersion, PSEdition
   ```
   👉 Explication : Windows PowerShell affiche 5.1 (`Desktop`); PowerShell 7 affiche 7.x (`Core`).

3. Vérifier quels exécutables sont présents :
   ```powershell
   Get-Command pwsh, powershell -ErrorAction SilentlyContinue | Select-Object Name, Source
   ```
   👉 Explication : `pwsh.exe` est PowerShell 7, `powershell.exe` est 5.1; certains modules d'administration restent propres à 5.1.

## 2. Production — Contrôles

Choisir le shell et tester la compatibilité du module avant toute opération. Ce périmètre exclut Remoting, WinRM, JEA, stratégie d'exécution de parc, MECM/Intune.

## 3. Production — Sécurité

- Ne pas activer PowerShell Remoting sans demande et runbook d'entreprise.
- Ne pas lancer de shell administrateur sans besoin.

## Validation et retour arrière

- **Validation** : Les shells présents et leurs versions sont identifiés.
- **Retour arrière** : Aucune modification n'est faite; rien à annuler.

## Si le problème n'est pas résolu

- [Microsoft Learn — Installer PowerShell 7 sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [PowerShell — publication v7.6.9](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9)
- [Guide complet PowerShell 7.6.9 Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11#1-versions-et-perimetre)
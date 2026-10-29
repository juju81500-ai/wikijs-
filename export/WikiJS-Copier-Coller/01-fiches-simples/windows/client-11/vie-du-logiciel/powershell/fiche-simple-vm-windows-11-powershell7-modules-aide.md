# Fiche_Simple_-_VM_Windows_11_PowerShell7_Modules_Aide.md

- **Environnement** : VM ou poste Windows 11 de test; compte standard puis élévation uniquement si requise
- **OS / Version** : Windows 11 x64; PowerShell 7.6.9 Stable (LTS)
- **Catégorie** : administration / PowerShell

---

## Problème précis à résoudre

Inventorier les modules et mettre à jour l'aide locale sans installer de source non approuvée.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les modules disponibles :
   ```powershell
   Get-Module -ListAvailable | Sort-Object Name, Version | Select-Object Name, Version, Path
   Get-Command -Module Microsoft.PowerShell.Management
   ```
   👉 Explication : la présence d'un module ne garantit pas sa compatibilité avec PowerShell 7.

2. Mettre à jour l'aide locale (Internet ou dépôt interne approuvé requis) :
   ```powershell
   Update-Help -ErrorAction Continue
   Get-Help Get-Process -Full
   ```
   👉 Explication : la mise à jour peut échouer derrière un proxy; l'aide complète s'affiche ensuite.

## 2. Production — Contrôles

N'installer un module que depuis une source approuvée, après vérification de l'éditeur, de la version, des dépendances et des autorisations.

## 3. Production — Sécurité

- Une publication PowerShell Gallery n'est pas une approbation de sécurité.

## Validation et retour arrière

- **Validation** : Modules inventoriés, aide à jour, compatibilité vérifiée.
- **Retour arrière** : Désinstaller le module ajouté (`Uninstall-Module -Name NOM_DU_MODULE`, remplacer par le nom réel) si un module a été installé.

## Si le problème n'est pas résolu

- [Microsoft Learn — Installer PowerShell 7 sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [PowerShell — publication v7.6.9](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9)
- [Microsoft Learn — Compatibilité des modules](https://learn.microsoft.com/en-us/powershell/whats-new/module-compatibility)
- [Guide complet PowerShell 7.6.9 Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11#5-modules-et-aide)
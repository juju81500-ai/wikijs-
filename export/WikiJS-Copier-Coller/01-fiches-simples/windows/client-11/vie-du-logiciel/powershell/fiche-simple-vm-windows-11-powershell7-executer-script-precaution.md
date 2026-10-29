# Fiche_Simple_-_VM_Windows_11_PowerShell7_Executer_Script_Precaution.md

- **Environnement** : VM ou poste Windows 11 de test; compte standard puis élévation uniquement si requise
- **OS / Version** : Windows 11 x64; PowerShell 7.6.9 Stable (LTS)
- **Catégorie** : administration / PowerShell

---

## Problème précis à résoudre

Lire, simuler puis exécuter un script sans affaiblir la stratégie d'exécution.

## 1. Hors-Production (Lab / Test / POC)

1. Avant exécution, lire le script et ses dépendances, vérifier son origine, la version requise, ses chemins et ses effets.
   👉 Explication : on évite d'exécuter du code non compris.

2. Examiner les stratégies d'exécution effectives :
   ```powershell
   Get-ExecutionPolicy -List
   Get-ExecutionPolicy
   ```
   👉 Explication : une stratégie limite certains lancements accidentels mais n'est pas une frontière de sécurité.

3. Simuler une action avec `-WhatIf` (fichier d'exemple à remplacer) :
   ```powershell
   Get-Help Remove-Item -Parameter WhatIf
   Remove-Item -LiteralPath 'C:\Lab\fichier-test.txt' -WhatIf
   ```
   👉 Explication : `-WhatIf` affiche ce qui serait supprimé sans le faire; il n'existe pas pour toutes les commandes et ne remplace pas une sauvegarde.

## 2. Production — Contrôles

Dans les scripts, préférer chemins explicites, filtres ciblés, gestion d'erreur observable et confirmation avant modification.

## 3. Production — Sécurité

- Ne pas définir globalement `Bypass` ou `Unrestricted`, ni affaiblir une stratégie imposée par GPO.
- Ne pas lancer en administrateur si l'opération ne le requiert pas.

## Validation et retour arrière

- **Validation** : Script relu, simulé et exécuté avec les droits minimaux.
- **Retour arrière** : Restaurer les fichiers modifiés depuis la sauvegarde préalable.

## Si le problème n'est pas résolu

- [Microsoft Learn — Installer PowerShell 7 sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [PowerShell — publication v7.6.9](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9)
- [Microsoft Learn — Set-ExecutionPolicy](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy)
- [Guide complet PowerShell 7.6.9 Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11#6-executer-un-script-avec-precaution)
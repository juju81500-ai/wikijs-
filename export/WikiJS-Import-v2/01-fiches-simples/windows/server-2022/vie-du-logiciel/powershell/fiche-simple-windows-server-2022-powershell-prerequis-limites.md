---
title: "Fiche Simple - Windows Server 2022 PowerShell Prerequis Limites"
description: "Cadrer PowerShell sur Windows Server 2022 : Windows PowerShell 5.1 intégré, PowerShell 7 en installation côte à côte, différences et limites."
published: true
date: 2026-10-29T20:58:17Z
tags: ["windows-server-2022", "powershell", "pwsh", "scripting", "remoting"]
editor: markdown
dateCreated: 2026-10-29T20:58:17Z
dateModified: 2026-10-29T20:58:17Z
---

# Fiche_Simple_-_Windows_Server_2022_PowerShell_Prerequis_Limites

- **Environnement** : Windows Server 2022 de laboratoire (Desktop Experience ou Core), session administrateur
- **OS / Version** : Windows Server 2022
- **Catégorie** : shell / scripting
- **Tags** : `windows-server-2022`, `powershell`, `pwsh`, `scripting`, `remoting`

---

## Problème précis à résoudre

Cadrer PowerShell sur Windows Server 2022 : Windows PowerShell 5.1 intégré, PowerShell 7 en installation côte à côte, différences et limites.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier le shell et la version actifs. GUI : menu Démarrer > Windows PowerShell (5.1) ; PowerShell 7 n'apparaît qu'après installation. Ligne de commande :
   ```powershell
   $PSVersionTable | Select-Object PSVersion,PSEdition
   Get-Command powershell,pwsh -ErrorAction SilentlyContinue | Select-Object Name,Source
   ```
   👉 Explication : Windows PowerShell 5.1 (`powershell.exe`, édition Desktop) est livré avec Windows Server 2022 ; PowerShell 7 (`pwsh.exe`, édition Core) est un produit distinct, installé à côté, qui ne le remplace pas.

2. Noter les différences utiles :
   👉 Explication : 5.1 : basé sur .NET Framework, modules Windows historiques (ServerManager, ActiveDirectory, etc.), remoting WinRM (`-ComputerName`). 7 : basé sur .NET, multiplateforme, remoting SSH (`-HostName`) en plus de WinRM ; certains modules Windows ne se chargent que via la couche de compatibilité (`Import-Module -UseWindowsPowerShell`) — vérifier module par module.

3. Vérifier le type d'installation du serveur (Server Core ou Desktop Experience) :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName,WindowsInstallationType
   ```
   👉 Explication : sur Server Core il n'y a pas d'interface graphique : seules les commandes sont applicables, les chemins GUI de ces fiches ne s'appliquent pas.

4. Vérifier la stratégie d'exécution en vigueur :
   ```powershell
   Get-ExecutionPolicy -List
   ```
   👉 Explication : affiche chaque portée ; la valeur par défaut d'un Windows Server est documentée comme `RemoteSigned` (à confirmer par cette commande).

## 2. Production — Contrôles

Décider de la version PowerShell 7 à déployer, du mode de remoting (WinRM ou SSH) et de la politique de signature avant d'installer. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne pas supprimer ni remplacer Windows PowerShell 5.1 : des composants Windows en dépendent.
- Exécuter en administrateur seulement ce qui l'exige.

## Validation et retour arrière

- **Validation** : versions, éditions et stratégie d'exécution relevées.
- **Retour arrière** : aucune modification n'est faite par cette fiche.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer PowerShell sur Windows](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-windows)
- [Microsoft Learn — différences 5.1 / 7](https://learn.microsoft.com/powershell/scripting/whats-new/differences-from-windows-powershell)
- [Guide complet Windows 11 (référence PowerShell 7)](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11)
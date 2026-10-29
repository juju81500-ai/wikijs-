---
title: "Administrer Windows 11 avec PowerShell 7.6.9"
description: "Fiche simple : [comprendre versions et périmètre](../../../../01-Fiches-Simples/Windows/Client-11/Vie-du-logiciel/PowerShell/FicheSimple-VMWindows11PowerShell7VersionsPerimetre.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["powershell", "windows11", "administration", "diagnostic", "scripts", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Administrer Windows 11 avec PowerShell 7.6.9

- **OS / Version** : Windows 11 x64; PowerShell 7.6.9 Stable (LTS)
- **Type de fiche** : Administration
- **Rôle** : installer PowerShell 7 et effectuer des contrôles locaux reproductibles
- **Périmètre** : shell local, objets/pipeline, aide, modules et diagnostic en lecture seule
- **Tags** : `powershell`, `windows11`, `administration`, `diagnostic`, `scripts`, `securite`

## 1. Versions et périmètre

Fiche simple : [comprendre versions et périmètre](/01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-versions-perimetre).

PowerShell 7.6.9 est la dernière version stable disponible au 27 octobre 2026. PowerShell 7 (`pwsh.exe`) s'installe côte à côte avec Windows PowerShell 5.1 (`powershell.exe`) et ne le remplace pas. Des modules d'administration restent spécifiques à Windows PowerShell 5.1; choisir le shell et tester la compatibilité du module avant toute opération. Cette fiche porte sur Windows 11 et des contrôles locaux. Elle ne configure pas PowerShell Remoting, WinRM, JEA, une stratégie d'exécution de parc ou un déploiement MECM/Intune.

## 2. Installer la version stable

Fiche simple : [installer la version stable](/01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-installer-version-stable).

Télécharger le MSI x64 depuis la publication officielle PowerShell `v7.6.9` sur GitHub :

```powershell
$download = Join-Path $HOME 'Downloads\PowerShell-7.6.9'
New-Item -ItemType Directory -Force -Path $download | Out-Null
$msi = Join-Path $download 'PowerShell-7.6.9-win-x64.msi'
Invoke-WebRequest -Uri 'https://github.com/PowerShell/PowerShell/releases/download/v7.6.9/PowerShell-7.6.9-win-x64.msi' -OutFile $msi
```

Vérifier la signature Authenticode et comparer le SHA-256 à celui de la publication officielle avant l'installation :

```powershell
$signature = Get-AuthenticodeSignature -FilePath $msi
$signature.Status
$signature.SignerCertificate.Subject
Get-FileHash -Path $msi -Algorithm SHA256
```

Le statut doit être `Valid`, le signataire doit être Microsoft et le hash doit correspondre à la valeur de l'asset dans les notes de version v7.6.9. Pour le MSI x64, le SHA-256 publié est `50D33C7494AAF82B987CFD4DE3F232D04F91FDD4C0DEECA8A669CCED3E7CF8F9`. Refuser un MSI dont la signature ou le hash diffère. Lancer ensuite l'installateur validé et conserver les options de mise à jour par Microsoft Update/WSUS selon la politique du poste.

```powershell
Start-Process msiexec.exe -Wait -ArgumentList '/i', $msi
```

Le MSI x64 ajoute le binaire `pwsh.exe` au chemin par défaut et peut nécessiter l'approbation UAC. Ne pas activer PowerShell Remoting pendant l'installation sans demande et runbook d'entreprise explicites.

## 3. Vérifier le shell actif

Fiche simple : [vérifier le shell actif](/01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-verifier-shell-actif).

Ouvrir **PowerShell 7** depuis le menu Démarrer, puis contrôler la version et l'exécutable en cours :

```powershell
$PSVersionTable | Select-Object PSVersion, PSEdition, Platform
$PSHOME
(Get-Process -Id $PID).Path
Get-Command pwsh, powershell -ErrorAction SilentlyContinue | Select-Object Name, Source
```

`pwsh` identifie PowerShell 7; `powershell.exe` lance Windows PowerShell 5.1. Vérifier `$PSVersionTable` avant d'exécuter un script dont le support de version est limité.

## 4. Prendre en main les commandes et objets

Fiche simple : [prendre en main commandes et objets](/01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-commandes-objets).

La sortie PowerShell est constituée d'objets .NET. Filtrer et sélectionner les propriétés avant d'afficher; éviter de transformer en texte avec `Format-Table` avant un export ou une autre étape de pipeline.

```powershell
Get-Command -Verb Get -Noun Service
Get-Service | Where-Object Status -eq 'Running' | Sort-Object DisplayName | Select-Object Status, Name, DisplayName
Get-NetIPConfiguration
Get-Help Get-Service -Examples
```

Pour examiner un poste sans le modifier, collecter uniquement les propriétés nécessaires :

```powershell
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
Get-NetAdapter | Select-Object Name, Status, LinkSpeed
Get-Service | Where-Object Status -eq 'Stopped' | Select-Object Name, DisplayName
Get-WinEvent -FilterHashtable @{ LogName = 'System'; Level = 2; StartTime = (Get-Date).AddHours(-24) } -MaxEvents 50 |
    Select-Object TimeCreated, Id, ProviderName, LevelDisplayName, Message
```

Les journaux peuvent contenir des identifiants, noms internes ou données d'activité. Ne pas copier leur contenu dans un ticket public; réduire le périmètre et protéger les exports. Certaines informations exigent des droits supplémentaires.

## 5. Modules et aide

Fiche simple : [gérer modules et aide](/01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-modules-aide).

Inventorier les modules disponibles avant d'en installer ou d'en importer un. La présence d'un module ne garantit pas sa compatibilité avec PowerShell 7 :

```powershell
Get-Module -ListAvailable | Sort-Object Name, Version | Select-Object Name, Version, Path
Get-Command -Module Microsoft.PowerShell.Management
```

L'aide locale peut être mise à jour au besoin; la première commande requiert Internet ou un dépôt interne approuvé et peut échouer derrière un proxy :

```powershell
Update-Help -ErrorAction Continue
Get-Help Get-Process -Full
```

N'installer un module que depuis une source approuvée, après vérification de son éditeur, sa version, ses dépendances et ses autorisations. Un nom connu ou une publication PowerShell Gallery n'est pas à lui seul une approbation de sécurité.

## 6. Exécuter un script avec précaution

Fiche simple : [exécuter un script avec précaution](/01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-executer-script-precaution).

Avant exécution, lire le script et ses dépendances, vérifier son origine, sa version requise, ses chemins et ses effets. Une stratégie d'exécution limite certains lancements accidentels mais n'est pas une frontière de sécurité; un utilisateur peut la contourner. Ne pas définir globalement `Bypass` ou `Unrestricted`, ni affaiblir une stratégie imposée par GPO. Examiner les portées effectives :

```powershell
Get-ExecutionPolicy -List
Get-ExecutionPolicy
```

Pour une action qui supporte `-WhatIf`, commencer par la simulation et vérifier chaque cible. Le paramètre n'est pas disponible pour toutes les commandes et ne remplace pas une sauvegarde :

```powershell
Get-Help Remove-Item -Parameter WhatIf
Remove-Item -LiteralPath 'C:\Lab\fichier-test.txt' -WhatIf
```

Dans les scripts d'administration, préférer des chemins explicites, des filtres ciblés, une gestion d'erreur observable et une confirmation avant les modifications. Éviter les suppressions récursives ou les changements de configuration larges copiés sans adaptation; ne pas lancer en administrateur si l'opération ne le requiert pas.

## 7. Profils, journalisation et secrets

Fiche simple : [gérer profils, journalisation et secrets](/01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-profils-journalisation-secrets).

Un profil PowerShell est un script exécuté automatiquement à l'ouverture du shell. Vérifier son chemin et son contenu avant de le créer ou de l'utiliser :

```powershell
$PROFILE
Test-Path -LiteralPath $PROFILE
```

Ne jamais y stocker de mot de passe, jeton, clé privée ou secret en clair. Le transcript PowerShell peut enregistrer commandes et sorties, y compris les informations sensibles accidentellement affichées. Ne l'activer que si la politique l'exige, dans un emplacement protégé, et vérifier les règles de rétention.

## 8. Mise à jour et validation

Fiche simple : [mettre à jour et valider](/01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell7-mise-a-jour-validation).

Suivre les publications PowerShell et le cycle de support Microsoft. Mettre à jour avec la même méthode que celle utilisée à l'installation, revérifier la signature et le hash, puis tester les scripts et modules concernés sur un poste pilote.

- `pwsh` lance la version attendue et Windows PowerShell 5.1 reste disponible si nécessaire.
- Les commandes de diagnostic renvoient les informations attendues sans modification de configuration.
- Les modules employés sont connus, approuvés et compatibles avec la version de shell choisie.
- Aucune politique d'exécution de l'organisation n'a été remplacée et aucun secret n'est inscrit dans le profil ou le journal.

## Sources

- [Microsoft Learn — Installer PowerShell 7 sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [PowerShell — publication officielle v7.6.9 et sommes SHA-256](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9)
- [Microsoft Learn — stratégies d'exécution et leurs portées](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy)
- [Microsoft Learn — Compatibilité des modules PowerShell 7](https://learn.microsoft.com/en-us/powershell/whats-new/module-compatibility)
- [Microsoft Learn — Get-AuthenticodeSignature](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-authenticodesignature)

L'installation, les commandes et la compatibilité des modules n'ont pas été testées sur un poste Windows réel. Essayer les scripts et modules sur un environnement pilote avant toute généralisation.
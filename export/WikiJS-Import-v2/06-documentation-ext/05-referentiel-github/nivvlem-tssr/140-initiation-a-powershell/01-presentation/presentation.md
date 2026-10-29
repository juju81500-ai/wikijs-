---
title: "Présentation du langage PowerShell"
description: "- Apparue en 2006 (v1.0), intégrée à Windows depuis Vista / Server 2008"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Présentation du langage PowerShell

## 📜 Historique & Versions

### PowerShell classique (Windows PowerShell)

- Apparue en 2006 (v1.0), intégrée à Windows depuis Vista / Server 2008
- PowerShell 5.1 est installé par défaut sur Windows 10 / Server 2019

### PowerShell Core / PowerShell 7 (Open Source)

- Multiplateforme : Windows, macOS, Linux (Debian, Ubuntu, Fedora, etc.)
- Dépend de .NET Core
- Exécution stricte sous Linux (sensible à la casse, certaines commandes indisponibles)

> 📦 Cmdlet spéciale : `$PSVersionTable` pour afficher la version en cours

---

## ⚙️ Cmdlets : les commandes PowerShell

### Structure

```powershell
<Verbe>-<Nom>
```

Exemples : `Get-Process`, `Get-ChildItem`, `Set-ExecutionPolicy`

- Les noms sont au **singulier**
- Les **paramètres** sont introduits par `-`

### Liste des verbes reconnus

```powershell
Get-Verb
```

> Exemples avec paramètres :

```powershell
Get-LocalUser -Name "nom"
Get-LocalGroupMember -Group "Groupe"
```

---

## 🔍 Rechercher les Cmdlets disponibles

### `Get-Command`

```powershell
Get-Command -Name *-Service
Get-Command -Verb Stop
```

> 🔧 Utile pour lister toutes les commandes ou filtrer sur un nom ou verbe

---

## 📖 Aide intégrée PowerShell

### `Get-Help`

```powershell
Get-Help Get-Service
Get-Help Get-Service -Full
Get-Help Get-Service -Examples
Get-Help Get-Service -ShowWindow
```

- `-Full` → toutes les sections
- `-ShowWindow` → aide dans une fenêtre avec champ de recherche
- `-Online` → vers docs Microsoft

### Sections générales

```powershell
Get-Help about_*    # aide sur les concepts (about_Arrays, about_If, etc.)
```

### Mise à jour de l’aide

```powershell
Update-Help
Update-Help -SourcePath D:\PowerShell -UICulture en-US
```

> ❗ Requiert une console **administrateur**

---

## 🔐 Exécution des scripts

### Politique de sécurité (Execution Policy)

```powershell
Get-ExecutionPolicy
Set-ExecutionPolicy Unrestricted   # ⚠️ nécessite droits admin
```

Niveaux disponibles :

- Restricted (par défaut)
- AllSigned
- RemoteSigned
- Unrestricted
- Bypass, Default, Undefined

> ⚠️ Modifier ce paramètre impacte la sécurité du système

---

## 📦 Gestion des modules PowerShell

### Qu’est-ce qu’un module ?

- Ensemble de Cmdlets (fichier .psm1)

### Commandes utiles

```powershell
Get-Module
$env:PSModulePath                # répertoires des modules autorisés
Import-Module AWSPowershell      # importer un module
Get-Command -Module AWSPowershell
```

> Exemple : le module AWS PowerShell ajoute près de 8000 Cmdlets

---

## 🎨 Personnalisation de la console

### Interface utilisateur

- Clic droit sur la barre → Propriétés
- Modifier la police, les couleurs, etc.

### Script de profil utilisateur

```powershell
New-Item -Path $Profile -Type File -Force
```

- Ce fichier `.ps1` s’exécute à chaque ouverture de la console PowerShell
- Il peut afficher un message de bienvenue, personnaliser le prompt, charger des modules, etc.

---

## ✅ À retenir pour les révisions

- PowerShell est structuré autour des Cmdlets : `Verbe-Nom` + `-Paramètres`
- `Get-Command`, `Get-Help`, `Update-Help` permettent de s’orienter
- L’exécution de scripts est restreinte pour des raisons de sécurité → `Set-ExecutionPolicy`
- PowerShell Core est open source, multiplateforme et différent de la version 5.1
- Modules et profils permettent une personnalisation avancée de l’environnement

---

## 📌 Bonnes pratiques professionnelles

- Toujours exécuter PowerShell **en tant qu’administrateur** pour les commandes système
- Personnaliser le profil PowerShell pour gagner en productivité (alias, fonctions, chargement de modules)
- Conserver les scripts utiles dans un répertoire versionné (Git)
- Tester les scripts dans un environnement de **test** avant usage en production
- Maintenir les aides à jour avec `Update-Help`

---

## 🔗 Commandes utiles

```powershell
Get-Command
Get-Help -Name NomCommande [-Full|-Examples|-Online]
Update-Help
Set-ExecutionPolicy -ExecutionPolicy Unrestricted
Import-Module -Name NomModule
New-Item -Path $Profile -Type File -Force
```

## Ressources complémentaires

- [https://docs.microsoft.com/powershell](https://docs.microsoft.com/powershell)
- [https://learn.microsoft.com/powershell/scripting/overview](https://learn.microsoft.com/powershell/scripting/overview)
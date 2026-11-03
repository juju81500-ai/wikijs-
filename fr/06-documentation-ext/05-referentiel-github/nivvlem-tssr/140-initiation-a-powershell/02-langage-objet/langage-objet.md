---
title: "PowerShell : langage objet"
description: "Contrairement à Bash ou CMD, PowerShell retourne des objets issus du .NET Framework (v5.1) ou .NET Core (PowerShell 7)."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# PowerShell : langage objet

## 🧱 PowerShell = langage objet

Contrairement à Bash ou CMD, PowerShell **retourne des objets** issus du .NET Framework (v5.1) ou .NET Core (PowerShell 7).

Exemple :

```powershell
Get-Service
```

Renvoie des objets `System.ServiceProcess.ServiceController` avec **propriétés** (Status, DisplayName…) et **méthodes** (Start, Stop…)

---

## 🔍 Inspecter un objet : `Get-Member`

### Syntaxe

```powershell
<commande> | Get-Member
```

### Affiche :

- **TypeName** : le type d’objet
- **MemberType** : Propriété, Méthode, Alias…
- **Name** : nom de la propriété ou méthode

### Exemple

```powershell
Get-Service | Get-Member
```

---

## 🧾 Propriétés d’un objet

### Qu’est-ce qu’une propriété ?

- Une **information contenue dans l’objet** (nom, état, type, etc.)
- Son **type** est important : String, Int, Bool, Array, etc.

### Manipulation

```powershell
(Get-Service -Name Wsearch).DisplayName
(Get-LocalUser -Name 'Utilisateur').Enabled
```

### Modification (via Cmdlet de type `Set-`)

```powershell
Set-Service -Name Wsearch -DisplayName "Recherche Windows"
```

> 🔐 Certaines modifications nécessitent **les droits administrateur**

---

## 🔧 Méthodes d’un objet

### Qu’est-ce qu’une méthode ?

- Une **action exécutée** sur ou par un objet (≠ propriété statique)
- Exemple : `.Start()`, `.Stop()`, `.AddDays()`

### Syntaxe d’utilisation

```powershell
(Get-Service -Name Wsearch).Stop()
(Get-Date).AddDays(1)
```

- L’objet est entouré de **parenthèses**
- On utilise le **point `.`** pour accéder à la méthode
- Les **parenthèses** de la méthode accueillent les **paramètres éventuels**

---

## 📚 Exemples de types de propriétés

|Type|Exemple de valeur|
|---|---|
|String|"Utilisateur1"|
|Int|1234|
|Bool|`$true`, `$false`|
|Array|`@(1,2,3)`|
|Object|Une propriété peut elle-même contenir un objet complet|

---

## ✅ À retenir pour les révisions

- PowerShell retourne des objets complets avec propriétés + méthodes
- `Get-Member` est **essentiel** pour comprendre comment manipuler un objet
- La **notation pointée** (objet.propriété ou objet.méthode()) est au cœur du langage
- Modifier une propriété nécessite d’utiliser la Cmdlet `Set-` associée

---

## 📌 Bonnes pratiques professionnelles

- Toujours analyser les objets avec `Get-Member` avant d’en exploiter les valeurs
- Ne jamais modifier un objet système sans comprendre le type de propriété concernée
- Séparer l’extraction (Get-), l’inspection (`Get-Member`) et la modification (`Set-`)
- Tester les manipulations sur des objets non critiques dans un environnement de test

---

## 🔗 Commandes utiles

```powershell
Get-Command
Get-Help Get-Member -Full
Get-Service | Get-Member
(Get-Service -Name Wsearch).Status
(Get-Date).AddDays(3)
Set-Service -Name Wsearch -DisplayName "Recherche Windows"
```

## Ressources complémentaires

- [https://learn.microsoft.com/powershell/scripting/learn/ps101/04-working-with-objects](https://learn.microsoft.com/powershell/scripting/learn/ps101/04-working-with-objects)
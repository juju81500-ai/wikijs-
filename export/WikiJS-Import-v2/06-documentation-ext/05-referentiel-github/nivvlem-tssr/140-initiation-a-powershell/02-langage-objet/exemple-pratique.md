---
title: "TP – L'objet en PowerShell"
description: "Get-Service | Get-Member"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – L'objet en PowerShell

## 🧱 Inspection d’un objet PowerShell

### 🔍 Afficher les propriétés et méthodes du type `System.ServiceProcess.ServiceController`

```powershell
Get-Service | Get-Member
```

### ✅ Propriétés de type `string`

- `DisplayName`
- `MachineName`

### ✅ Méthodes par type

- **Méthode Bool** : `Equals(System.Object obj)`
- **Méthode Int** : `GetHashCode()`

---

## 📄 Manipulation des objets

### 📋 Propriétés du service `Spooler`

```powershell
Get-Service -Name Spooler | Get-Member -MemberType Property
Get-Service -Name Spooler
```

- Propriétés affichées : `Status`, `Name`, `DisplayName`
- Valeurs : `Running`, `Spooler`, `Print Spooler`

### 📋 Propriétés de l’utilisateur local `Adara Mcintyre`

````powershell
Get-LocalUser -Name "Adara Mcintyre"\```
- Propriétés affichées : `Name`, `Enabled`, `Description`
- Valeurs : `Adara Mcintyre`, `$true`, `Technician`

### ✏️ Mise à jour de la propriété `Description`
```powershell
Set-LocalUser -Name "Adara Mcintyre" -Description "Administrateur"
````

---

## 🛑 Contrôle d’un service via méthode

### Afficher le statut du service `Spooler`

```powershell
Get-Service -Name Spooler
```

### Utiliser la méthode `.Stop()` sur un objet

```powershell
(Get-Service -Name Spooler).Stop()
```

### Vérification post-exécution

```powershell
Get-Service -Name Spooler
```

---

## 🧪 Bonus – Manipulation avancée de propriété avec `Get-Date`

### Définir `AccountExpires` avec une date +48h (ex : utilisateur `Axel Rios`)

```powershell
Set-LocalUser -Name "Axel Rios" -AccountExpires (Get-Date).AddDays(2)
```

### Vérification

```powershell
Get-LocalUser -Name "Axel Rios" | Select-Object *
```

---

## ✅ À retenir pour les révisions

- Les objets PowerShell exposent des **propriétés** et des **méthodes** via `Get-Member`
- Les méthodes s’exécutent avec `()` et les propriétés se consultent en pointé (`.`)
- L’édition de certaines propriétés se fait **uniquement** via les Cmdlets `Set-*`
- `Get-Date` est un objet manipulable avec `.AddDays()`

---

## 📌 Bonnes pratiques professionnelles

- Tester toutes les manipulations en console avant de les intégrer dans des scripts
- Ne modifier une propriété que sans connaître son impact
- Toujours **vérifier** après modification (via `Get-*` ou `Select-Object *`)
- Utiliser `Get-Member` pour découvrir les possibilités réelles de chaque objet

---

## 🔗 Commandes utiles

```powershell
Get-Service | Get-Member
Get-Service -Name Spooler
(Get-Service -Name Spooler).Stop()
Get-LocalUser -Name "Nom"
Set-LocalUser -Name "Nom" -Description "..."
Set-LocalUser -Name "Nom" -AccountExpires (Get-Date).AddDays(2)
```
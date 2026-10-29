# Manipulation des objets

## 🔄 Le pipeline PowerShell

### Concept clé

- Le **pipeline** (`|`) permet de **chaîner** des Cmdlets : la sortie de l'une devient l'entrée de l'autre
- Exemple :

```powershell
Get-Service | Where-Object {$_.Status -eq 'Running'}
```

---

## 🧩 Cmdlets de manipulation de base

### 🎯 `Select-Object`

- Sélection de propriétés, dédoublonnage

```powershell
Get-Process | Select-Object -Property Name, CPU
Get-Process | Select-Object -First 5
```

### 📊 `Measure-Object`

- Statistiques (count, sum, average…)

```powershell
Get-Process | Measure-Object -Property CPU -Sum -Average
```

### 🔃 `Sort-Object`

- Tri par propriété

```powershell
Get-Service | Sort-Object -Property Status
```

### 🔎 `Where-Object`

- Filtrage conditionnel

```powershell
Get-Process | Where-Object {$_.CPU -gt 10}
```

---

## 🖼️ Formatage de l'affichage

### `Format-Table` (Ft)

- Affichage en tableau

```powershell
Get-Process | Format-Table -Property Name, CPU -AutoSize
```

### `Format-Wide`

- Affichage en colonnes (1 propriété)

```powershell
Get-Service | Format-Wide -Property Name -Column 3
```

### `Format-List`

- Affichage détaillé (liste verticale)

```powershell
Get-Process | Format-List -Property *
```

> ⚠️ Les Cmdlets Format-* doivent être utilisées **en fin de pipeline**

---

## 💾 Exportation, conversion, importation

### 📤 `Export-Csv`

```powershell
Get-Process | Export-Csv -Path .\process.csv -NoTypeInformation -Encoding UTF8
```

### 🔁 `ConvertTo-Json` / `ConvertTo-Html`

```powershell
Get-Process | ConvertTo-Json
Get-Service | ConvertTo-Html | Out-File .\services.html
```

### 📥 `Get-Content` & `Import-Csv`

```powershell
Get-Content .\log.txt
Import-Csv .\process.csv | Format-Table
```

---

## 🔧 Propriétés calculées

### Utiliser des expressions personnalisées avec `Select-Object`

```powershell
Get-Process | Select-Object Name, @{Name="RAM(MB)";Expression={[math]::Round($_.WS / 1MB, 2)}}
```

- `@{Name=...; Expression=...}` permet de renommer et manipuler dynamiquement des valeurs

---

## ✅ À retenir pour les révisions

- Le **pipeline** permet de chaîner efficacement les commandes
- `Select-`, `Where-`, `Sort-`, `Measure-` : les outils fondamentaux de tri et filtrage
- Les Cmdlets `Format-*` modifient l’affichage (non les objets)
- `Export-Csv`, `ConvertTo-*`, `Import-Csv` permettent la persistance et l’exploitation des données
- Les **propriétés calculées** offrent une grande souplesse dans l'analyse

---

## 📌 Bonnes pratiques professionnelles

- Travailler sur des objets structurés et non sur du texte brut
- Toujours vérifier les résultats de tri/filtrage avec `Format-Table` ou `Out-GridView`
- Conserver une trace des exports (CSV, HTML, JSON) avec nom, date et encodage précisé
- Utiliser des propriétés calculées pour adapter les données aux besoins métiers
- Tester les conversions et importations en environnement de test

---

## 🔗 Commandes utiles

```powershell
Get-Service | Where-Object {$_.Status -eq 'Running'}
Get-Process | Select-Object -Property Name, CPU
Get-Process | Measure-Object -Property CPU -Average
Get-Service | Sort-Object Status
Get-Process | Export-Csv .\data.csv -NoTypeInformation
Import-Csv .\data.csv | Format-Table
```
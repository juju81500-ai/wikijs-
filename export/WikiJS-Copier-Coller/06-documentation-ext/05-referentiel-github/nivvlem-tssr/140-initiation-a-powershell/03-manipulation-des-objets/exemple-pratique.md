# TP – Manipuler des objets
## 🧱 Partie 1 – Utilisateurs Active Directory (AD)

### 📋 Liste des utilisateurs avec certaines propriétés

```powershell
Get-ADUser -Filter * | Select-Object GivenName, Name, Enabled, Department, City
```

### 💡 Afficher toutes les propriétés disponibles

```powershell
Get-ADUser -Filter * -Properties *
```

### 📘 Aide détaillée

```powershell
Get-Help Get-ADUser -ShowWindow
```

### 🔢 Afficher les 5 premiers utilisateurs

```powershell
Get-ADUser -Filter * | Select-Object -First 5
```

### 🏙️ Trier les utilisateurs par ville, puis par département

```powershell
Get-ADUser -Filter * -Properties * |
Select Name, Enabled, Department, City |
Sort-Object City, Department
```

### 🔎 Filtrer sur les noms contenant un "r"

```powershell
Get-ADUser -Filter * -Properties * |
Where-Object { $_.Name -like '*r*' } |
Sort-Object Department, City
```

### ❌ Désactiver les utilisateurs dont le nom commence par un D

```powershell
Get-ADUser -Filter 'Name -like "D*"' | Disable-ADAccount
```

---

## 🧱 Partie 2 – Filtres et mesures avancées

### ✅ Afficher uniquement les utilisateurs actifs

```powershell
Get-ADUser -Filter * | Where-Object Enabled -eq $true
```

### 🔤 Filtrer par initiales (A ou F)

```powershell
Get-ADUser -Filter * | Where-Object { $_.Enabled -eq $true -and ($_.Name -match '^[AF]') }
```

### 📊 Compter les utilisateurs actifs/inactifs

```powershell
Get-ADUser -Filter * | Where-Object Enabled -eq $true | Measure-Object
Get-ADUser -Filter * | Where-Object Enabled -eq $false | Measure-Object
```

---

## 🧱 Partie 3 – Manipulation de fichiers

### 📂 Lister tous les fichiers

```powershell
Get-ChildItem \\CD01\Partage -File -Recurse
```

### 📏 Taille moyenne des fichiers

```powershell
Get-ChildItem \\CD01\Partage -File -Recurse | Measure-Object -Property Length -Average
```

### 📈 Taille min/max

```powershell
Measure-Object -Property Length -Minimum -Maximum
```

### 🔎 Fichiers entre 10 Mo et 100 Mo

```powershell
Get-ChildItem \\CD01\Partage -File -Recurse |
Where-Object { $_.Length -gt 10MB -and $_.Length -lt 100MB } |
Select Name, Length, Mode |
Sort-Object Name -Descending
```

---

## 🧱 Partie 4 – Formatage et affichage

### 🖼️ Affichage en colonnes (Wide)

```powershell
Get-ADUser -Filter * | Format-Wide -Column 5
```

### 📊 Tableau d'utilisateurs actifs

```powershell
Get-ADUser -Filter * -Properties * |
Where-Object Enabled -eq $true |
Format-Table Name, Enabled, Department, City
```

### 👥 Groupes AD triés par scope

```powershell
Get-ADGroup -Filter * -Properties * |
Format-Table Name, Description, Created -GroupBy GroupScope
```

### 🖥️ Ordinateurs du domaine, triés par OS

```powershell
Get-ADComputer -Filter * -Properties * |
Format-List Name, DNSHostName, DistinguishedName, IPv4Address -GroupBy OperatingSystem
```

---

## 🧱 Partie 5 – Journal système et exportations

### 📆 Événements système formatés

```powershell
Get-EventLog System | Select TimeWritten, Index, Message
```

### Version complète avec affichage maximal

```powershell
Get-EventLog System | Format-List TimeWritten, Index, Message
```

### 📤 Export en CSV

```powershell
Get-ADUser -Filter * | Export-Csv \\CD01\Partage\Exports\CSV\Users.csv -Delimiter '.'
```

### 🌐 Export en HTML

```powershell
Get-ADUser -Filter * -Properties * |
ConvertTo-Html | Out-File \\CD01\Partage\Exports\CSV\Users.html
```

### ➕ Ajouter ordinateurs au CSV existant

```powershell
Get-ADComputer -Filter * |
Export-Csv \\CD01\Partage\Exports\CSV\Users.csv -Append -Delimiter ';'
```

---

## 🧱 Partie 6 – Importation & Propriété personnalisée

### 🛠️ Modifier nom de colonne + importer

```powershell
Import-Csv -Path \\CD01\Partage\Exports\CSV\Users.csv -Delimiter ';' |
Select-Object @{Name="Name";Expression={$_.Nom}} | New-ADUser
```

### 📥 Nettoyage avant import

```powershell
Get-ADUser -Filter * | Remove-ADUser -Confirm:$false
```

---

## 🧪 Bonus – Conversion & format personnalisé

### 📊 Afficher fichiers du partage avec noms traduits + taille en Go

```powershell
Get-ChildItem \\CD01\Partage -File -Recurse |
Select @{n="Nom";e={$_.Name}}, @{n="Taille";e={[math]::Round($_.Length / 1GB, 2)}} |
Format-List
```

---

## ✅ À retenir pour les révisions

- `Select-`, `Sort-`, `Where-`, `Measure-`, `Format-` sont au cœur de la manipulation
- `Export-Csv`, `Import-Csv`, `ConvertTo-*` permettent de structurer, persister, réutiliser les données
- Active Directory est un **fournisseur riche** à manipuler avec précaution

---

## 📌 Bonnes pratiques professionnelles

- Tester les filtres sur un échantillon avant de les appliquer à grande échelle
- Toujours **vérifier** les imports/exports : structure, encodage, délimiteur
- Privilégier les formats **structurés et typés** (CSV, JSON) pour les scripts automatisés
- Documenter les scripts par blocs : filtrage, sélection, export, logs

---

## 🔗 Commandes utiles

```powershell
Get-ADUser -Filter * | Select GivenName, Name, Enabled, Department, City
Get-ChildItem \\CD01\Partage -File -Recurse | Measure-Object -Property Length -Average
Import-Csv -Path "..." | Select @{n="Name";e={$_.Nom}} | New-ADUser
Export-Csv -Path "..." -Append -Delimiter ';'
```
# TP – PowerShell : redirection, pipeline, filtrage, formatage

## 🔧 Exercices pratiques et solutions

### 1. Afficher la date du jour et le quantième de l’année

```powershell
Get-Date | Select-Object DayOfYear, Date
```

### 2. Afficher les événements du journal de sécurité

```powershell
Get-EventLog -LogName Security
```

### 3. Filtrer sur l’EventID 4624 (connexion réussie)

```powershell
Get-EventLog -LogName Security | Where-Object { $_.EventID -eq 4624 }
```

### 4. N’afficher que l’EventID, la date et le message

```powershell
Get-EventLog -LogName Security | Where-Object { $_.EventID -eq 4624 } |
  Select-Object EventID, TimeWritten, Message
```

### 5. Afficher les règles de pare-feu activées

```powershell
Get-NetFirewallRule -Enabled True
```

### 6. Afficher uniquement nom, profil, direction et action

```powershell
Get-NetFirewallRule -Enabled True |
  Select-Object DisplayName, Profile, Direction, Action
```

### 7. Lister les volumes disques

```powershell
Get-Volume
```

### 8. Volumes avec plus de 8 Go libres

```powershell
Get-Volume | Where-Object { $_.SizeRemaining -gt 8GB }
```

### 9. Volumes ≤ 25 Go

```powershell
Get-Volume | Where-Object { $_.Size -le 25GB }
```

### 10. Volumes avec > 8 Go libres **et** ≤ 25 Go

```powershell
Get-Volume | Where-Object {
  $_.SizeRemaining -gt 8GB -and $_.Size -le 25GB
} | Format-List FileSystemLabel, DriveLetter, FileSystemType
```

### 11. Services en cours d’exécution au démarrage

```powershell
Get-Service | Where-Object {
  $_.Status -eq 'Running' -and $_.StartType -eq 'Automatic'
} | Select-Object Name, Status
```

### 12. Membres du groupe `L_HA_Ventes` avec leur SID

```powershell
Get-LocalGroupMember L_HA_Ventes | Select-Object Name, SID
```

### 13. Partages administratifs

```powershell
Get-SmbShare | Where-Object { $_.Name -like '*$' } |
  Select-Object Name, Path | Format-List
```

### 14. Volumes CD-ROM sains

```powershell
Get-Volume | Where-Object {
  $_.DriveType -eq 'CD-ROM' -and $_.HealthStatus -eq 'Healthy'
} | Select-Object DriveLetter, DriveType, HealthStatus
```

### 15. Informations imprimante HP LaserJet

```powershell
Get-Printer -Name '*HP*' |
  Format-List Name, Type, DriverName, ShareName
```

---

## ✅ À retenir pour les révisions

- `Where-Object` permet un filtrage avancé des objets via `{}`
- `Select-Object` limite les colonnes visibles
- `Format-List` et `Format-Table` modifient la présentation des résultats
- La redirection (`>`, `2>`, `>>`) permet de consigner des résultats dans un fichier

---

## 📌 Bonnes pratiques professionnelles

|Pratique recommandée|Raison professionnelle|
|---|---|
|Toujours filtrer avant de formater|Optimise les performances et la lisibilité|
|Utiliser `2>` pour isoler les erreurs|Utile en script pour debugger ou journaliser|
|Préférer les pipelines chaînés|Réduction des variables temporaires inutiles|
|Commenter ses scripts pour chaque étape|Facilite le transfert de connaissances|
|Vérifier la documentation avec `Get-Help`|S’assurer de la bonne syntaxe et options disponibles|
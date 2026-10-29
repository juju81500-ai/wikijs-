# TP – Variables et structures 

## 🧱 Partie 1 – Manipulation de variables et journal système

### 📥 Stocker le journal système dans une variable

```powershell
$logs = Get-EventLog -LogName System
```

### 🔍 Afficher l’entrée numéro 10 et sa valeur d’index

```powershell
$logs[9]  # car l’index PowerShell commence à 0
$logs[9].Index
```

### ➕ Addition des index des entrées 10 et 20

```powershell
$addition = $logs[9].Index + $logs[19].Index
```

---

## 🧠 Partie 2 – Deviner la date de naissance (DoWhile + If)

### 🎯 Script de devinette

```powershell
$birthdate = Read-Host "Définissez une date de naissance (format AAAAMMJJ)"
$essais = 0
Do {
    $saisie = Read-Host "Essayez de deviner la date"
    $essais++
    If ($saisie -lt $birthdate) {
        Write-Host "Trop tôt"
    } ElseIf ($saisie -gt $birthdate) {
        Write-Host "Trop tard"
    }
} While ($saisie -ne $birthdate)
Write-Host "Bravo ! Trouvé en $essais essai(s)."
```

---

## 👥 Partie 3 – Utilisateurs AD : tableaux + comptage

### 🧾 Script avec `ForEach` et `If`

```powershell
$users = Get-ADUser -Filter *
$UserActif = New-Object System.Collections.ArrayList
$UserInActif = New-Object System.Collections.ArrayList

ForEach ($i in $users) {
    if ($i.Enabled -eq $true) {
        $UserActif.Add($i) | Out-Null
    } else {
        $UserInActif.Add($i) | Out-Null
    }
}

Write-Host "Voici le nombre d'utilisateur actif : " -NoNewline ; ($UserActif | Measure-Object).Count
Write-Host "Voici le nombre d'utilisateur inactifs : " -NoNewline ; ($UserInActif | Measure-Object).Count
```

---

## 🖥️ Partie 4 – Menu interactif (While + Switch)

### 🗂️ Script de menu

```powershell
Do {
    Clear-Host
    Write-Host "Bienvenue dans l'outil d'inventaire, choisissez :"
    Write-Host "1) Afficher ordinateurs du domaine"
    Write-Host "2) Afficher groupes de domaine locaux"
    Write-Host "3) Importer utilisateurs AD depuis CSV"
    Write-Host "4) Quitter"
    $choix = Read-Host "Votre choix"

    Switch ($choix) {
        '1' { Get-ADComputer -Filter * | Select Name }
        '2' { Get-ADGroup -Filter * | Where {$_.GroupScope -eq "DomainLocal"} }
        '3' {
            Import-Csv \\CD01\Partage\Users.csv | ForEach-Object {
                New-ADUser -Name $_.Nom -GivenName $_.Prenom -SamAccountName $_.Login
            }
        }
        '4' { Write-Host "Au revoir !" }
        Default { Write-Host "Saisie incorrecte. Réessayez..."; Start-Sleep 1 }
    }
} While ($choix -ne '4')
```

---

## 🔁 Partie 5 – Réinitialisation utilisateurs AD

### 📋 Chargement dans une variable

```powershell
$users = Get-ADUser -Filter *
```

### 🔄 Pour chaque utilisateur : reset mot de passe et activation

```powershell
ForEach ($u in $users) {
    Set-ADAccountPassword -Identity $u -Reset -NewPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force)
    If (-not $u.Enabled) {
        Enable-ADAccount -Identity $u
    }
}
```

---

## ✅ À retenir pour les révisions

- Les variables peuvent stocker des objets complexes (`Get-EventLog`, `Get-ADUser`, etc.)
- Les structures `DoWhile`, `Switch`, `If`, `ForEach` sont à combiner pour créer des scripts interactifs
- `$variable.Count` permet de compter le nombre d’éléments dans un tableau

---

## 📌 Bonnes pratiques professionnelles

- Valider les fichiers CSV avant import
- Ne pas faire de boucle infinie sans condition d’arrêt claire
- Toujours tester la logique du script dans un environnement isolé
- Séparer les blocs logiques (lecture, traitement, affichage)

---

## 🔗 Commandes utiles

```powershell
Get-EventLog -LogName System
Get-ADUser -Filter {Enabled -eq $true}
Set-ADAccountPassword -Identity $user -Reset -NewPassword ...
Switch ($var) { ... }
Do { ... } While (...)
```
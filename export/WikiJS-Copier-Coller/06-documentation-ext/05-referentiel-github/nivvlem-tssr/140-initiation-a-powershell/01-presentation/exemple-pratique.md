# TP – Premières commandes PowerShell
## 🧱 Partie 1 – Découverte de PowerShell et PowerShell Core

### 📥 Comparer les deux consoles

```powershell
Get-Command | Measure
```

> En PowerShell 5.1 : ~2855 cmdlets / PowerShell Core : ~2825 cmdlets

### 📑 Verbes PowerShell

```powershell
Get-Verb | Measure
```

> PowerShell 5.1 : 98 verbes / Core : 100 verbes (légère évolution)

### 🔍 Filtrage de cmdlets

```powershell
Get-Command -Verb New
Get-Command -Noun *User*
```

> Cmdlet pour créer un utilisateur local : `New-LocalUser`

---

## 🧪 Partie 2 – Requête sur utilisateurs locaux

### 📋 Liste des 5 premiers utilisateurs sur chaque machine

```powershell
Get-LocalUser | Select-Object -First 5
```

### ✏️ Modifier la description d’un utilisateur

```powershell
Set-LocalUser -Name "Nom" -Description "TP"
```

---

## 📖 Partie 3 – Utilisation de l’aide

### Afficher l’aide d’une cmdlet

```powershell
Get-Help Get-Service
Get-Help Get-Service -ShowWindow
Get-Help Get-Service -Full
```

### Aide en ligne

```powershell
Get-Help Get-LocalGroup -Online
```

### Mise à jour depuis un dépôt local

```powershell
Update-Help -SourcePath "\\CD01\Partage\Depot\CLI01\" -UICulture en-US
Update-Help -SourcePath "\\CD01\Partage\Depot\CLI01\" -UICulture fr-FR
```

> ⚠️ Peu de modules ont une traduction disponible en `fr-FR`

---

## 📦 Partie 4 – Modules PowerShell

### Liste des modules et origine d’une commande

```powershell
Get-Module | Measure
Get-Command Get-LocalUser | Select-Object Module
```

> Module : `Microsoft.PowerShell.LocalAccounts`

### Emplacements des modules

```powershell
$env:PSModulePath -split ';'
```

### Importer un module distant (ex : AWS)

```powershell
Import-Module "\\CD01\Partage\Modules\AWSPowerShell"
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Exemples de cmdlets AWS

```powershell
Get-AWSCredential
New-EC2Instance
Get-S3Bucket
```

---

## 🎨 Partie 5 – Personnalisation et profil

### Créer un profil utilisateur

```powershell
New-Item -Path $PROFILE -ItemType File -Force
notepad $PROFILE
```

- Exemple : ajouter `Get-Help Get-Command -Examples`

### Modifier le prompt avec script externe

```powershell
function Get-Time {
    return (Get-Date).ToLongTimeString()
}

function prompt {
    $time = Get-Time
    $path = $(Get-Location).Path.Replace($HOME, "~")

    Write-Host "[" -NoNewline
    Write-Host $time -ForegroundColor DarkYellow -NoNewline
    Write-Host "] " -NoNewline
    Write-Host $path -ForegroundColor DarkGreen -NoNewline
    Write-Host $(if ($nestedpromptlevel -ge 1) { '>>' }) -NoNewline
    return "> "
}

function IsAdmin {
    $CurrentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object System.Security.Principal.WindowsPrincipal($CurrentUser)
    return $principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Couleur de fond selon les droits
if (IsAdmin) {
    $ElevationMode = 'Privilégiée'
    $host.UI.RawUI.BackgroundColor = 'DarkRed'
    Clear-Host
} else {
    $ElevationMode = 'Non Privilégiée'
    $host.UI.RawUI.BackgroundColor = 'DarkMagenta'
    Clear-Host
}

# Message d’accueil au lancement
$time = Get-Time
$CurrentUser = [System.Security.Principal.WindowsIdentity]::GetCurrent()

Write-Host '+---------------------------------------------------+'
Write-Host ("+- Bonjour {0}, il est {1}" -f ($CurrentUser.Name).Split('\')[1], $time)
Write-Host '+---------------------------------------------------+'
```

---

## ✅ À retenir pour les révisions

- PowerShell est structuré autour de Cmdlets et de modules
- `Get-Command`, `Get-Help`, `Update-Help` sont des outils fondamentaux
- Le profil PowerShell permet de personnaliser l’environnement utilisateur
- L’exécution de scripts est contrôlée via `ExecutionPolicy`

---

## 📌 Bonnes pratiques professionnelles

- Toujours exécuter PowerShell en administrateur pour les actions système
- Ne jamais désactiver les protections (`ExecutionPolicy`) sans raison
- Tester les modules importés avant usage régulier
- Organiser son profil utilisateur pour automatiser ses routines (import, alias, aide)

---

## 🔗 Commandes utiles

```powershell
Get-Command -Verb New
Get-Help Get-Service -ShowWindow
Update-Help -SourcePath "\\CD01\Partage\Depot\CLI01" -UICulture en-US
Import-Module "\\CD01\Partage\Modules\AWSPowerShell"
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
New-Item -Path $PROFILE -Type File -Force
. "$PROFILE"
```
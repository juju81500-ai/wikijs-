# TP – Outils pour le scripting
## 🧱 Partie 1 – Script de test de présence d’un service

### Script principal

```powershell
$services = @("Spooler", "InvalidService", "W32Time")
$nonTrouves = @()

ForEach ($service in $services) {
    Try {
        Get-Service -Name $service -ErrorAction Stop | Out-Null
    } Catch {
        $nonTrouves += $service
    }
}

Write-Host "Vérification terminée."
```

### Affichage conditionnel

```powershell
If ($nonTrouves.Count -gt 0) {
    Write-Host "Services non trouvés : $($nonTrouves -join ", ")"
}
```

---

## 🔁 Partie 2 – Transformation en fonction

### Fonction paramétrée

```powershell
Function Test-Service {
    Param(
        [Parameter(Mandatory)]
        [string[]]$Noms
    )
    $nonTrouves = @()
    ForEach ($s in $Noms) {
        Try {
            Get-Service -Name $s -ErrorAction Stop | Out-Null
        } Catch {
            $nonTrouves += $s
        }
    }
    If ($nonTrouves.Count -gt 0) {
        Write-Host "Non trouvés : $($nonTrouves -join ", ")"
    }
    Else {
        Write-Host "Tous les services existent."
    }
}

Test-Service -Noms "Spooler", "FakeService"
```

---

## 🌐 Partie 3 – Remoting : connexion à un serveur distant

### Créer une session distante vers CD01

```powershell
$session = New-PSSession -ComputerName CD01
```

---

## 🧮 Partie 4 – Ordinateurs AD & extinction conditionnelle

### Script d’extinction (hors contrôleurs de domaine)

```powershell
$pcs = Get-ADComputer -Filter * -Properties OperatingSystem

ForEach ($pc in $pcs) {
    If ($pc.OperatingSystem -notlike "*Domain Controller*") {
        Stop-Computer -ComputerName $pc.Name -Force
    }
}
```

---

## 🔁 Partie 5 – Transformation en fonction (paramètre : nom de domaine)

### Fonction avec domaine en paramètre

```powershell
Function Eteindre-MachinesNonDC {
    Param(
        [string]$Domaine
    )
    $pcs = Get-ADComputer -Filter {DNSHostName -like "*.$Domaine"} -Properties OperatingSystem
    ForEach ($pc in $pcs) {
        If ($pc.OperatingSystem -notlike "*Domain Controller*") {
            Stop-Computer -ComputerName $pc.Name -Force
        }
    }
}

Eteindre-MachinesNonDC -Domaine "ad.campus-eni.fr"
```

---

## ⚙️ Partie 6 – Modification du comportement d’erreur dans l’ISE et la console

### Stockage automatique des erreurs dans une variable

```powershell
$ErrorActionPreference = "SilentlyContinue"
```

### Exemple : désactivation de message d’erreur visible

```powershell
Get-Item C:\inexistant -ErrorAction SilentlyContinue -ErrorVariable erreurScript
```

> 📌 Cette configuration peut être ajoutée dans le profil ISE : `$PROFILE`

---

## ✅ À retenir pour les révisions

- Un script modulaire s’organise autour de **fonctions avec paramètres**
- Le **remoting** PowerShell est puissant mais doit être sécurisé
- La gestion d’erreurs permet un comportement **fiable et silencieux** dans un script automatisé

---

## 📌 Bonnes pratiques professionnelles

- Toujours capturer les erreurs dans une variable (`-ErrorVariable`)
- Documenter chaque fonction (`.SYNOPSIS`, `.DESCRIPTION` dans des blocs de commentaires)
- Tester les scripts avec **Verbose** et **WhatIf** si disponible
- Ne jamais éteindre un parc de machines sans vérification claire du rôle

---

## 🔗 Commandes utiles

```powershell
New-PSSession -ComputerName CD01
Invoke-Command -Session $session -ScriptBlock {...}
Stop-Computer -ComputerName ...
$ErrorActionPreference = "SilentlyContinue"
```
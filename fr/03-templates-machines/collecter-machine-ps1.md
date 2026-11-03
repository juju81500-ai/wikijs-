---
title: "Lecture seule : relève les infos de la machine Windows locale et écrit une fiche machine pré-remplie."
description: "param([string]$Out = \"fiche-machine$env:COMPUTERNAME.md\")"
published: true
date: 2026-11-03T09:36:14Z
tags: ["fiche-machine", "windows"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Lecture seule : relève les infos de la machine Windows locale et écrit une fiche machine pré-remplie.
# Les champs non détectables restent « [à compléter] ».
# Usage : .\collecter-machine.ps1 [-Out fichier.md]   (PowerShell administrateur conseillé)
param([string]$Out = "fiche-machine_$env:COMPUTERNAME.md")

$todo = '[à compléter]'
$os = Get-CimInstance Win32_OperatingSystem
$cs = Get-CimInstance Win32_ComputerSystem
$model = "$($cs.Manufacturer) $($cs.Model)"
$type = if ($cs.HypervisorPresent -or $model -match 'Virtual|VMware|KVM|QEMU|Xen|Hyper-V') { "VM ($model)" } else { 'Physique' }

$ips = (Get-NetIPAddress -AddressFamily IPv4 -ErrorAction SilentlyContinue |
    Where-Object { $_.IPAddress -notmatch '^(127\.|169\.254\.)' } |
    ForEach-Object { "$($_.InterfaceAlias): $($_.IPAddress)/$($_.PrefixLength)" }) -join ', '
$disks = (Get-CimInstance Win32_LogicalDisk -Filter 'DriveType=3' |
    ForEach-Object { "$($_.DeviceID) $([math]::Round($_.Size / 1GB)) Go" }) -join ', '
$roles = if (Get-Command Get-WindowsFeature -ErrorAction SilentlyContinue) {
    (Get-WindowsFeature | Where-Object { $_.Installed -and $_.FeatureType -eq 'Role' }).Name -join ', ' } else { '' }
$services = (Get-Service | Where-Object Status -eq 'Running' | Select-Object -First 40 -ExpandProperty Name) -join ', '
$ports = (Get-NetTCPConnection -State Listen -ErrorAction SilentlyContinue |
    Select-Object -ExpandProperty LocalPort -Unique | Sort-Object | ForEach-Object { "tcp/$_" }) -join ', '
$fw = (Get-NetFirewallProfile | ForEach-Object { "$($_.Name)=$(if ($_.Enabled) {'actif'} else {'inactif'})" }) -join ', '
$today = Get-Date -Format 'yyyy-MM-dd'
function Or-Todo($v) { if ($v) { $v } else { $todo } }

@"
# 📄 ${todo}_$($env:COMPUTERNAME)_$($os.Caption)

- **Tags** : ``fiche-machine``, ``windows``

---

### 📌 1. Identification & Métadonnées
* **Machine Physique / Hôte** : $todo
* **Environnement** : $todo
* **Type d'équipement** : $type
* **Nom de la Machine** : $env:COMPUTERNAME
* **Système d'Exploitation (OS)** : $($os.Caption) (build $($os.BuildNumber))
* **Statut Opérationnel** : $todo

---

### 📋 2. Rôle, Utilisation & Besoins (Ressources)
* **Rôle et Utilisation** : $todo
* **Besoins (Allocation ressources)** :
  * **vCPU** : $($cs.NumberOfLogicalProcessors)
  * **RAM** : $([math]::Round($cs.TotalPhysicalMemory / 1GB, 1)) Go
  * **Stockage** : $(Or-Todo $disks)
  * **Adresse IP** : $(Or-Todo $ips)

---

### 📦 3. Logiciels & Ports
* **Logiciels installés** : $(Or-Todo (($roles, $services) -join ' | '))
* **Ports ouverts** : $(Or-Todo $ports)

---

### 🛡️ 4. Sécurité & Pare-feu
* **Firewall Machine (local)** : $(Or-Todo $fw)
* **Firewall Externe (Hôte / Routeur)** : $todo

---

### 📅 6. Suivi des Dates & Historique
- **Date de création** : $todo
- **Dernière modification** : $today
- **Historique des modifications datées** :
  - ``$today`` : relevé automatique par collecter-machine.ps1
"@ | Set-Content -Path $Out -Encoding UTF8
Write-Output "Fiche écrite : $Out"
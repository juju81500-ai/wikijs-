---
title: "La gestion du stockage sous Windows"
description: "diskpart"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# La gestion du stockage sous Windows

## 💾 Terminologie et concepts de base

|Élément|Description|
|---|---|
|Disque de base|Mode classique, partitionné (MBR ou GPT), simple, sans redondance|
|Disque dynamique|Permet la création de volumes fractionnés, étendus ou en miroir|
|Partition|Division logique d'un disque (primaire, étendue, logique)|
|Volume|Représentation logique d'un espace de stockage accessible par une lettre|

> 📌 Windows 11 continue de prendre en charge disques de base et dynamiques.

---

## 🛠️ Table de partitionnement : MBR vs GPT

|Caractéristique|MBR|GPT|
|---|---|---|
|Nombre de partitions|4 partitions primaires max|128 partitions principales|
|Taille disque supportée|Jusqu'à 2 To|Jusqu'à 18 exaoctets|
|Compatible BIOS|Oui|Non (UEFI uniquement)|
|Compatible UEFI|Non|Oui|
|Résilience|Faible (table unique)|Excellente (réplication et CRC intégrés)|

> 📌 Windows 11 impose UEFI + disque GPT pour l'installation.

---

## 📚 Systèmes de fichiers sous Windows

|Système de fichiers|Caractéristiques principales|
|---|---|
|NTFS|Sécurisé, journalisé, quotas de disque, compression|
|ReFS (Windows Server)|Résilient, orienté très grands volumes, tolérance aux erreurs|
|FAT32|Compatibilité maximale, limité à 4 Go par fichier|
|exFAT|Remplacement moderne de FAT32 pour supports amovibles|

> 📌 NTFS reste le système par défaut pour les volumes Windows 10/11.

---

## 🧩 Outils de gestion du stockage sous Windows

### 🔹 Interface graphique

- **Gestion des disques** (diskmgmt.msc)
- **Paramètres > Système > Stockage**
- **Explorateur de fichiers** (attribution de lettres, formater)

### 🔹 Ligne de commande

|Outil|Usage principal|
|---|---|
|`diskpart`|Gestion avancée des disques/partitions|
|`format`|Formatage de volumes|
|`chkdsk`|Vérification et réparation de volumes|
|`Get-Partition`, `Get-Disk` (PowerShell)|Manipulations modernes via cmdlets|

### 🔹 Exemples de commandes courantes

```bash
diskpart
list disk
select disk 0
clean
convert gpt
create partition primary
format fs=ntfs quick
assign letter=E
```

```powershell
Get-Disk
Get-Partition
Get-Volume
New-Partition -DiskNumber 1 -UseMaximumSize -AssignDriveLetter | Format-Volume -FileSystem NTFS
```

---

## ✅ À retenir pour les révisions

- **MBR** est obsolète sur le matériel récent, préférer **GPT**
- **NTFS** est recommandé pour tous les disques internes (sécurité, performances)
- `diskmgmt.msc` permet une gestion rapide graphique ; `diskpart` est plus puissant pour des scripts
- **PowerShell** offre une gestion fine et scriptable des disques modernes
- Toujours identifier et vérifier les disques avant de les modifier (`list disk`, `Get-Disk`)

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Convertir les disques en GPT dès que possible|Support de grandes tailles, meilleure fiabilité|
|Utiliser NTFS pour les disques système et données|Bénéficier de la sécurité, des ACLs et de la résilience|
|Sauvegarder avant de partitionner ou formater|Prévenir toute perte accidentelle de données|
|Privilégier l'automatisation via PowerShell|Gain de temps, cohérence sur des parcs importants|
|Surveiller régulièrement l’état SMART des disques|Prévenir les pannes matérielles|
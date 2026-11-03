---
title: "TP – Gestion du stockage sous Windows"
description: "- Ajouter deux disques de 60 Go chacun à la VM Win10-MD"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Gestion du stockage sous Windows

## 🖥️ Préparation des disques dans VMware Workstation

- Ajouter deux disques de **60 Go** chacun à la VM `Win10-MD`
- Type : **SCSI**, stockage en **fichier unique**

---

## 🔸 Étapes graphiques avec `diskmgmt.msc`

### 1. Initialisation des disques

- Initialiser les **disques 1 et 2** au format **GPT**

### 2. Création des partitions sur disque 1

- **Trois partitions de 15 Go** chacune (non formatées, sans lettre)
- **Une partition de 7 Go**, non formatée, sans lettre

### 3. Formatage des partitions

- **Partition 1 (15 Go)** → NTFS, nom : `DATA`, lettre : `D`
- **Partition 2 (15 Go)** → NTFS, nom : `TOOLS`, lettre : `E`
- **Partition 4 (7 Go)** → FAT32, nom : `ARCHIVE`, lettre : `F`

### 4. Extension de volume

- Étendre le volume `DATA` avec **15 Go du disque 2**
    - Windows transforme les disques en **dynamiques** automatiquement

---

## 🔸 Étapes en ligne de commande (CMD + `diskpart`)

### 1. Formatage de la 3e partition (disque 1)

```shell
diskpart
select disk 1
list volume
select volume 2
format fs=ntfs label=COMMUN quick
assign letter=G
```

### 2. Extension de `COMMUN` avec l’espace libre de disque 1

```shell
select volume 2
extend
```

### 3. Suppression et recréation du volume `DATA`

```shell
select volume D
delete volume
create partition primary
format fs=ntfs label=DATA quick
assign letter=D
```

> Si l'espace est réparti entre disque 1 et 2, utiliser `extend` après création.

---

## 🔹 Investigation sur la VM Discovery avec PowerShell

### 1. Informations disque

```powershell
Get-Disk | Select Number, Size, PartitionStyle
```

### 2. Infos sur les volumes nommés

```powershell
Get-Volume -FriendlyName * | Select DriveLetter, FileSystem, Size, FileSystemLabel
```

### 3. Renommer le volume `C:`

```powershell
Set-Volume -DriveLetter C -NewFileSystemLabel "System"
```

---

## ✅ Vérifications

- ✅ **Volumes visibles dans l’explorateur** avec les bons noms et lettres
- ✅ **Volumes DATA** et **COMMUN** étendus avec succès


---

## 📌 Bonnes pratiques professionnelles

|Bonnes pratiques|Pourquoi ?|
|---|---|
|Toujours initialiser les disques en GPT|Compatibilité UEFI, résilience, gestion >2 To|
|Libérer les lettres de lecteur si déjà prises|Éviter les conflits lors d'attribution|
|Étendre un volume uniquement si disque dynamique|Fonction non disponible en disque de base|
|Préférer `diskpart` pour automatisation|Scripting possible, idéal pour grandes infrastructures|
|Documenter toute manipulation de disque|Traçabilité et partage de la configuration|
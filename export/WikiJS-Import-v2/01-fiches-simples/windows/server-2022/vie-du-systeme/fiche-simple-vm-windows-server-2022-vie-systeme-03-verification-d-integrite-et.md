---
title: "Fiche Simple - VM Windows Server 2022 Vie Systeme 03 Verification D Integrite Et"
description: "S'assurer que l'ISO n'est ni corrompue ni modifiée."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windowsserver2022", "vie-du-systeme", "cycle-de-vie", "etape-03"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-03`

---

## Problème précis à résoudre

S'assurer que l'ISO n'est ni corrompue ni modifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Calculer l'empreinte SHA-256 du fichier (clic droit sur l'ISO > **Propriétés** ne suffit pas; utiliser PowerShell) :
   ```powershell
   Get-FileHash -Algorithm SHA256 -Path C:\ISO\FICHIER.iso
   ```
   👉 Explication : affiche l'empreinte à comparer; remplacer `FICHIER.iso` par le nom réel de l'image.

2. Comparer avec l'empreinte publiée par Microsoft ou le contrat (remplacer `EMPREINTE_PUBLIEE` par la valeur officielle) :
   ```powershell
   (Get-FileHash -Algorithm SHA256 C:\ISO\FICHIER.iso).Hash -eq 'EMPREINTE_PUBLIEE'
   ```
   👉 Explication : renvoie `True` si l'image est identique à celle publiée (la casse est ignorée).

3. Monter l'image pour contrôler son contenu (explorateur : clic droit > **Monter**) :
   ```powershell
   $m = Mount-DiskImage -ImagePath C:\ISO\FICHIER.iso -PassThru
   Get-Volume -DiskImage $m | Select-Object DriveLetter, FileSystemLabel
   Dismount-DiskImage -ImagePath C:\ISO\FICHIER.iso
   ```
   👉 Explication : vérifie que le volume contient `setup.exe` et le dossier `sources`, puis démonte l'image.

## 2. Production — Contrôles

Conserver l'empreinte dans le dossier du projet avec la date et la source.

## 3. Production — Sécurité

Une empreinte différente impose de supprimer le fichier et de le retélécharger depuis la source officielle.

## Validation et retour arrière

- **Validation** : `Get-FileHash` renvoie la même valeur que la source officielle.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
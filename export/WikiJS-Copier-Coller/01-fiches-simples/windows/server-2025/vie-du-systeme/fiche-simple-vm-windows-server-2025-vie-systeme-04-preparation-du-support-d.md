# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Préparer le support qui démarrera l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Machine virtuelle : attacher l'ISO (Hyper-V : **Gestionnaire Hyper-V > Paramètres > Lecteur de DVD > Fichier image**) :
   ```powershell
   Set-VMDvdDrive -VMName NOM_VM -Path C:\ISO\FICHIER.iso
   Set-VMFirmware -VMName NOM_VM -FirstBootDevice (Get-VMDvdDrive -VMName NOM_VM)
   ```
   👉 Explication : `NOM_VM` est le nom de la VM; le lecteur DVD devient le premier périphérique d'amorçage (VM de génération 2).

2. Serveur physique : créer une clé USB amorçable avec **Rufus** (schéma de partition GPT, système cible UEFI) ou avec l'outil du constructeur. En PowerShell, repérer d'abord la clé :
   ```powershell
   Get-Disk | Where-Object BusType -eq 'USB' | Select-Object Number, FriendlyName, @{n='Taille_Go';e={[math]::Round($_.Size/1GB)}}
   ```
   👉 Explication : identifie le numéro de disque USB pour éviter d'écraser un autre disque; Rufus formate la clé entièrement.

3. Si l'image dépasse 4 Go, utiliser une clé formatée en NTFS (option Rufus) ou en FAT32 avec `install.wim` fractionné :
   ```powershell
   Dism /Split-Image /ImageFile:D:\sources\install.wim /SWMFile:E:\sources\install.swm /FileSize:3800
   ```
   👉 Explication : FAT32 limite les fichiers à 4 Go; `D:` est l'ISO montée et `E:` la clé.

## 2. Production — Contrôles

Préparer deux supports identiques pour un parc physique et les étiqueter.

## 3. Production — Sécurité

Garder la clé sous clé après usage et l'effacer si elle contient des fichiers de réponse.

## Validation et retour arrière

- **Validation** : La machine démarre sur l'écran d'installation « Windows Server 2025 ».
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
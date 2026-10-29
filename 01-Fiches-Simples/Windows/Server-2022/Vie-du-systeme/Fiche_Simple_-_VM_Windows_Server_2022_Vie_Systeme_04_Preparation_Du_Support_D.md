# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-04`

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

- **Validation** : La machine démarre sur l'écran d'installation « Windows Server 2022 ».
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows Server 2022 Hyper V Creer VM Pilote](<../Vie-du-logiciel/Hyper-V/Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Creer_VM_Pilote.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)

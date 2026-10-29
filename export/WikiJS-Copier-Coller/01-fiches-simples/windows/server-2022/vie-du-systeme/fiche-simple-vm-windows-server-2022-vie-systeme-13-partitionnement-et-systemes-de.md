# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Organiser les disques système et de données.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Gestion des disques** (`diskmgmt.msc`) ou **Gestionnaire de serveur > Services de fichiers et de stockage > Volumes > Disques**.
   ```powershell
   Get-Disk | Select-Object Number, FriendlyName, PartitionStyle, OperationalStatus, @{n='Taille_Go';e={[math]::Round($_.Size/1GB)}}
   ```
   👉 Explication : repère le disque de données vierge (`PartitionStyle` à `RAW`).

2. Initialiser, partitionner et formater en NTFS ou ReFS (remplacer `N` par le numéro du disque de données) :
   ```powershell
   Initialize-Disk -Number N -PartitionStyle GPT
   New-Partition -DiskNumber N -UseMaximumSize -DriveLetter D | Format-Volume -FileSystem NTFS -NewFileSystemLabel DONNEES -AllocationUnitSize 65536
   ```
   👉 Explication : disque GPT, volume `D:` nommé `DONNEES`; un cluster de 64 Ko convient aux bases et aux machines virtuelles. **Vérifier `N` pour ne pas effacer le disque système.**

3. Contrôler les volumes :
   ```powershell
   Get-Volume | Select-Object DriveLetter, FileSystem, HealthStatus, @{n='Libre_Go';e={[math]::Round($_.SizeRemaining/1GB,1)}}
   ```
   👉 Explication : confirme le système de fichiers et la santé.

## 2. Production — Contrôles

Séparer système (C:) et données (D:); ReFS est adapté aux volumes Hyper-V et de sauvegarde.

## 3. Production — Sécurité

Appliquer des quotas et des permissions NTFS strictes sur les volumes de données.

## Validation et retour arrière

- **Validation** : Volumes sains avec la bonne étiquette et la bonne taille.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
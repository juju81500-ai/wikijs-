# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-13`

---

## Problème précis à résoudre

Définir la disposition des disques : GPT, partition système EFI, partition de récupération, volume NTFS.

## 1. Hors-Production (Lab / Test / POC)

1. Pendant l'installation : à l'écran **Où voulez-vous installer Windows ?**, choisir le disque vierge (**Non alloué > Suivant**) pour laisser Windows créer les partitions EFI, MSR, système et récupération.
   👉 Explication : disposition GPT standard et compatible BitLocker et WinRE.

2. Contrôler après installation : **Gestion des disques (diskmgmt.msc)** ou PowerShell.
   ```powershell
   Get-Disk | Select-Object Number,PartitionStyle,@{n='Taille_Go';e={[math]::Round($_.Size/1GB)}}
   Get-Partition | Select-Object DiskNumber,PartitionNumber,Type,@{n='Taille_Go';e={[math]::Round($_.Size/1GB,1)}}
   Get-Volume | Select-Object DriveLetter,FileSystemLabel,FileSystem,SizeRemaining
   ```
   👉 Explication : doit afficher `GPT`, une partition `System` (EFI), `Reserved`, `Basic` (C:) et `Recovery`.

3. Créer un volume de données séparé si besoin : **Gestion des disques > clic droit sur l'espace > Nouveau volume simple**.
   ```powershell
   New-Partition -DiskNumber NUMERO_DISQUE -UseMaximumSize -DriveLetter D | Format-Volume -FileSystem NTFS -NewFileSystemLabel 'DONNEES'
   ```
   👉 Explication : crée un volume NTFS D: (`NUMERO_DISQUE` est le disque cible, vérifié avec `Get-Disk`).

4. Vérifier l'environnement de récupération.
   ```powershell
   reagentc /info
   ```
   👉 Explication : `Windows RE status : Enabled` est attendu.

## 2. Production — Contrôles

Garder au moins 20 % d'espace libre sur C:; séparer les données utilisateur si la politique l'impose (redirection de dossiers ou OneDrive).

## 3. Production — Sécurité

Chiffrer tous les volumes fixes avec BitLocker et ne pas laisser de partition de données ouverte.

## Validation et retour arrière

- **Validation** : `Get-Disk` indique GPT et `reagentc /info` indique Enabled.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)

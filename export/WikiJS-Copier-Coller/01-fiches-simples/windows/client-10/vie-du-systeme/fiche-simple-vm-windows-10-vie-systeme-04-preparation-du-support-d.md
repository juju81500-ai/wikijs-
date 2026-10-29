# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Créer la clé USB d'installation ou le support de démarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Brancher une clé USB d'au moins 8 Go (son contenu sera effacé) et lancer le **Media Creation Tool > Créer un support d'installation > Clé USB**.
   👉 Explication : méthode graphique officielle : l'outil télécharge Windows et prépare la clé.

2. Variante en ligne de commande avec l'ISO : identifier la clé avec soin avant tout effacement.
   ```powershell
   Get-Disk | Where-Object BusType -eq 'USB' | Select-Object Number,FriendlyName,@{n='Taille_Go';e={[math]::Round($_.Size/1GB)}}
   ```
   👉 Explication : liste uniquement les disques USB; noter le numéro (`NUMERO_DISQUE`) de la clé.

3. Formater la clé en GPT/FAT32 et copier le contenu de l'ISO montée (remplacer `NUMERO_DISQUE` et `LETTRE_ISO`, lettre du lecteur de l'ISO montée; remplacer `U` si la lettre attribuée à la clé diffère).
   ```powershell
   Clear-Disk -Number NUMERO_DISQUE -RemoveData -Confirm:$false
   Initialize-Disk -Number NUMERO_DISQUE -PartitionStyle GPT
   $P = New-Partition -DiskNumber NUMERO_DISQUE -UseMaximumSize -DriveLetter U
   Format-Volume -Partition $P -FileSystem FAT32 -NewFileSystemLabel 'WINSETUP'
   robocopy 'LETTRE_ISO:\' 'U:\' /E /XF install.wim
   ```
   👉 Explication : prépare une clé compatible UEFI; `install.wim` est exclu car il dépasse 4 Go.

4. Copier `install.wim` en le scindant en fichiers de moins de 4 Go.
   ```powershell
   dism /Split-Image /ImageFile:LETTRE_ISO:\sources\install.wim /SWMFile:U:\sources\install.swm /FileSize:3800
   ```
   👉 Explication : crée les fichiers `install.swm` que le programme d'installation sait lire sur FAT32.

## 2. Production — Contrôles

Étiqueter la clé (version, date) et la conserver dans un lieu fermé; Ventoy ou outils tiers uniquement s'ils sont approuvés.

## 3. Production — Sécurité

Une erreur de numéro de disque efface le mauvais disque : vérifier `Number` et la taille avant `Clear-Disk`.

## Validation et retour arrière

- **Validation** : La clé démarre en UEFI et affiche l'écran d'installation de Windows.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
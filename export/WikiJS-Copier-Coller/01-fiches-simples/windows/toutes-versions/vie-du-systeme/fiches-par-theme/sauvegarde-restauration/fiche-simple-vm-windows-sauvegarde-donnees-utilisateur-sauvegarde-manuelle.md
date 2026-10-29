# Fiche_Simple_-_VM_Windows_Sauvegarde_Donnees_Utilisateur_Sauvegarde_Manuelle.md

- **Environnement** : Poste Windows géré ou autonome, données de profil utilisateur
- **OS / Version** : Windows 10 et Windows 11
- **Catégorie** : sauvegarde / copie

---

## Problème précis à résoudre

Copier un dossier utilisateur de façon non destructive.

## 1. Hors-Production (Lab / Test / POC)

1. Connecter le volume de sauvegarde approuvé et vérifier son identité et sa capacité :
   ```powershell
   Get-Volume | Format-Table DriveLetter, FileSystemLabel, SizeRemaining, Size
   ```
   👉 Explication : confirme la lettre `E:` utilisée dans l'exemple (à adapter).

2. Copier avec Robocopy :
   ```powershell
   $Source = "$env:USERPROFILE\Documents"
   $Destination = "E:\Sauvegardes\$env:COMPUTERNAME\Documents"
   New-Item -ItemType Directory -Force -Path $Destination
   robocopy $Source $Destination /E /COPY:DAT /DCOPY:DAT /R:2 /W:2 /XJ /LOG:"$env:TEMP\robocopy-documents.log"
   $LASTEXITCODE
   ```
   👉 Explication : copie récursive sans suppression; adapter explicitement les chemins. Code de sortie < 8 : pas d'échec de copie; ≥ 8 : au moins une erreur.

3. Lire le journal même si le code est inférieur à 8.
   👉 Explication : confirme la présence des fichiers attendus.

## 2. Production — Contrôles

Utiliser un dossier de destination daté.

## 3. Production — Sécurité

- Ne pas ajouter `/MIR` ni `/PURGE` pour une première copie : ces options peuvent supprimer des fichiers dans la destination.

## Validation et retour arrière

- **Validation** : Journal sans erreur, fichiers présents à destination.
- **Retour arrière** : Supprimer le dossier de destination créé pour l'essai.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Microsoft Learn — Known Folder Move](https://learn.microsoft.com/en-us/sharepoint/redirect-known-folders)
- [Guide complet — 2. Préparer une sauvegarde manuelle de fichiers](/02-fiches-completes/windows/toutes-versions/autres/27-sauvegarde-restauration-donnees-utilisateur-windows#2-preparer-une-sauvegarde-manuelle-de-fichiers)
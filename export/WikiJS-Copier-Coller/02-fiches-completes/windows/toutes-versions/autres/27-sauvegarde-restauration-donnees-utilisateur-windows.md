# Sauvegarder et restaurer les données utilisateur Windows

- **Type de fiche** : Autres — sauvegarde / migration
- **Environnement** : Poste Windows géré ou autonome, données de profil utilisateur
- **OS / Version** : Windows 10 et Windows 11; valider les outils selon l'édition et la politique en place
- **Rôle** : Définir une sauvegarde vérifiable et restaurer les fichiers d'un utilisateur

## 1. Définir le périmètre

Fiche simple : [définir le périmètre](/01-fiches-simples/windows/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-vm-windows-sauvegarde-donnees-utilisateur-definir-perimetre).

Identifier les emplacements de données réellement utilisés, les volumes, les fichiers hors ligne, les données applicatives et la durée de conservation requise. Une copie de fichiers ne sauvegarde ni Windows, ni les applications, ni nécessairement tout le profil.

Pour un parc d'entreprise, utiliser en priorité la solution administrée et supervisée par l'organisation (par exemple OneDrive avec Known Folder Move ou un agent de sauvegarde approuvé). Pour un poste autonome, choisir une destination distincte du disque système et protéger les supports contre le vol et les rançongiciels.

## 2. Préparer une sauvegarde manuelle de fichiers

Fiche simple : [préparer une sauvegarde manuelle](/01-fiches-simples/windows/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-vm-windows-sauvegarde-donnees-utilisateur-sauvegarde-manuelle).

Connecter un volume de sauvegarde approuvé, vérifier son identité et sa capacité, puis créer un répertoire de destination daté. Exemple de copie non destructive avec Robocopy :

```powershell
$Source = "$env:USERPROFILE\Documents"
$Destination = "E:\Sauvegardes\$env:COMPUTERNAME\Documents"
New-Item -ItemType Directory -Force -Path $Destination
robocopy $Source $Destination /E /COPY:DAT /DCOPY:DAT /R:2 /W:2 /XJ /LOG:"$env:TEMP\robocopy-documents.log"
$LASTEXITCODE
```

Adapter explicitement les chemins et vérifier le journal. Ne pas ajouter `/MIR` ou `/PURGE` pour une première copie : ces options peuvent supprimer des fichiers dans la destination.

Robocopy retourne un code de statut : un code inférieur à 8 n'indique pas d'échec de copie, tandis qu'un code égal ou supérieur à 8 signale au moins une erreur. Examiner le journal même pour un code inférieur à 8 et confirmer la présence des fichiers attendus.

## 3. Vérifier la copie et protéger le support

Fiche simple : [vérifier la copie et protéger le support](/01-fiches-simples/windows/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-vm-windows-sauvegarde-donnees-utilisateur-verifier-copie).

- Comparer les journaux, nombres de fichiers et tailles; ouvrir plusieurs fichiers restaurables.
- Pour les données critiques, comparer des empreintes sur un échantillon ou utiliser la vérification intégrée de la solution de sauvegarde.
- Déconnecter ou verrouiller le support quand la copie est terminée; chiffrer les sauvegardes selon la politique.
- En environnement géré, contrôler l'état de synchronisation et la politique de rétention depuis la console d'administration.

## 4. Restaurer sans écraser les données existantes

Fiche simple : [restaurer sans écraser](/01-fiches-simples/windows/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-vm-windows-sauvegarde-donnees-utilisateur-restaurer-sans-ecraser).

Restaurer d'abord vers un répertoire temporaire, confirmer l'identité de l'utilisateur et la date de sauvegarde, puis comparer avec les fichiers présents. Fusionner seulement les dossiers approuvés; ne pas écraser en bloc `AppData`, les profils système ou les ACL sans procédure propre à l'application.

Avec Robocopy, inverser source et destination après contrôle, commencer par une simulation (`/L`) et lire la liste des opérations avant la copie réelle. Ne pas utiliser `/MIR` pour une restauration de profil.

## 5. Recette et incidents

Fiche simple : [recetter et traiter les incidents](/01-fiches-simples/windows/toutes-versions/vie-du-systeme/fiches-par-theme/sauvegarde-restauration/fiche-simple-vm-windows-sauvegarde-donnees-utilisateur-recette-incidents).

- Vérifier ouverture, contenu et permissions des fichiers restaurés avec l'utilisateur.
- Contrôler les chemins connus, applications concernées, synchronisation cloud et espace disque.
- En cas de chiffrement, corruption ou fichiers manquants, suspendre toute nouvelle écriture sur le support source et escalader; préserver les éléments nécessaires à l'analyse.

## Sources

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Microsoft Learn — Known Folder Move](https://learn.microsoft.com/en-us/sharepoint/redirect-known-folders)
- [Microsoft Support — Historique des fichiers](https://support.microsoft.com/en-us/windows/backup-and-restore-with-file-history-7bf065bf-f1ea-0a78-c1cf-7dcf51cc8bfc)
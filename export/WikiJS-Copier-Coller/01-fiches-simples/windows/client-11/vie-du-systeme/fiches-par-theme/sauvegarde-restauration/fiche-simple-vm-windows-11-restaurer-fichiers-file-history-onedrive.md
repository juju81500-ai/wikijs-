# 📄 Fiche_Simple_-_VM_Windows_11_Restaurer_Fichiers_File_History_OneDrive.md

- **Environnement** : Windows 11 et solution de sauvegarde/synchronisation configurée
- **OS / Version** : Windows 11
- **Catégorie** : Restauration / fichiers utilisateur

---

## 🎯 Problème précis à résoudre

Récupérer un fichier supprimé ou une version précédente sans écraser d'abord l'original.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Identifier source, compte propriétaire, date de version et autorisation de restauration.
   👉 Explication : sans autorisation du propriétaire, ne pas restaurer.

2. File History (GUI) : dans l'**Explorateur**, aller au dossier d'origine, clic droit > **Propriétés > Versions précédentes** (ou **Panneau de configuration > Système et sécurité > Historique des fichiers > Restaurer des fichiers personnels**), choisir une version.
   👉 Explication : l'écran liste les versions datées.

3. Restaurer sans écraser : bouton **Restaurer vers...** (ou clic droit sur la version > **Restaurer vers**), dossier temporaire, puis comparer :
   ```powershell
   Get-FileHash C:\Temp\restore\fichier.docx -Algorithm SHA256
   Get-Item C:\Temp\restore\fichier.docx | Select-Object Length, LastWriteTime
   ```
   👉 Explication : comparer contenu, taille et date avec l'attendu.

4. OneDrive : ouvrir **onedrive.com > Corbeille** du compte approprié > sélectionner l'élément > **Restaurer**; sinon **Paramètres OneDrive (icône) > Aide et paramètres > Restaurer votre OneDrive** pour une restauration par date.
   👉 Explication : vérifier ensuite l'état du client de synchronisation (icône dans la zone de notification).

5. Contrôler l'intégrité et les droits avant remise :
   ```powershell
   Get-Acl C:\Temp\restore\fichier.docx | Format-List
   ```
   👉 Explication : ne remettre le fichier à l'utilisateur qu'après validation.

## ⚡ 2. Production — Façon Simplifiée

1. Définir incident, périmètre et point de restauration; restaurer d'abord à un emplacement alternatif :
   ```powershell
   robocopy C:\Temp\restore D:\Alternatif /E /COPY:DAT /R:1 /W:1
   ```
   👉 Explication : coordonner ensuite le remplacement avec le propriétaire du fichier; `robocopy` sans `/MIR` pour ne rien supprimer.

## 🔒 3. Production — Façon Sécurisée

- Vérifier l'identité du propriétaire et ne pas restaurer des données vers un autre profil sans autorisation.
- Une suppression définitive dans la corbeille OneDrive ou l'expiration de rétention peut rendre la récupération impossible.
- Ne pas partager les liens de récupération ou augmenter l'accès au dossier pour faciliter l'opération.

## ✅ Validation et retour arrière

- **Validation** : fichier ouvre, somme/format attendus, permissions héritées conformes, synchronisation sans conflit.
- **Retour arrière** : garder la version actuelle et effectuer une copie avant remplacement; si la restauration est incorrecte, conserver les deux versions et escalader au propriétaire.

## 🔗 Si le problème n'est pas résolu

- [Microsoft — Restaurer des fichiers avec File History](https://support.microsoft.com/en-us/windows/back-up-and-restore-with-file-history-7bf065bf-f1ea-0a78-c1cf-7dcf51cc8bfc)
- [Microsoft — Restaurer des fichiers supprimés de OneDrive](https://support.microsoft.com/en-us/onedrive/restore-your-onedrive-files)
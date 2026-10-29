# Fiche_Simple_-_VM_Windows_Sauvegarde_Donnees_Utilisateur_Recette_Incidents.md

- **Environnement** : Poste Windows géré ou autonome, données de profil utilisateur
- **OS / Version** : Windows 10 et Windows 11
- **Catégorie** : sauvegarde / validation

---

## Problème précis à résoudre

Valider la restauration avec l'utilisateur et réagir en cas d'incident.

## 1. Hors-Production (Lab / Test / POC)

1. Faire ouvrir les fichiers restaurés par l'utilisateur et vérifier contenu et permissions.
   👉 Explication : seul l'utilisateur sait si c'est complet.

2. Contrôler chemins connus, applications concernées, synchronisation cloud et espace disque :
   ```powershell
   Get-PSDrive -PSProvider FileSystem
   ```
   👉 Explication : montre l'espace libre restant.

3. En cas de chiffrement, corruption ou fichiers manquants : suspendre toute nouvelle écriture sur le support source.
   👉 Explication : préserve les éléments d'analyse.

4. Escalader l'incident avec les journaux Robocopy.
   👉 Explication : le support dispose des preuves.

## 2. Production — Contrôles

Archiver le journal de recette.

## 3. Production — Sécurité

- Ne pas continuer à écrire sur un support suspect.

## Validation et retour arrière

- **Validation** : L'utilisateur confirme la recette.
- **Retour arrière** : Reprendre depuis la sauvegarde précédente non altérée.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Microsoft Learn — Known Folder Move](https://learn.microsoft.com/en-us/sharepoint/redirect-known-folders)
- [Guide complet — 5. Recette et incidents](/02-fiches-completes/windows/toutes-versions/autres/27-sauvegarde-restauration-donnees-utilisateur-windows#5-recette-et-incidents)
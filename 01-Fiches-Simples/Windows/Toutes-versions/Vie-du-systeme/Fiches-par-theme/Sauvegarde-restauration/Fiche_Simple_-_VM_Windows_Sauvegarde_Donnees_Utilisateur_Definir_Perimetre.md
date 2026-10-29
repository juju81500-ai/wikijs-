# Fiche_Simple_-_VM_Windows_Sauvegarde_Donnees_Utilisateur_Definir_Perimetre.md

- **Environnement** : Poste Windows géré ou autonome, données de profil utilisateur
- **OS / Version** : Windows 10 et Windows 11
- **Catégorie** : sauvegarde / cadrage
- **Tags** : `windows`, `windows10`, `windows11`, `sauvegarde`, `restauration`, `robocopy`

---

## Problème précis à résoudre

Lister ce qui doit être sauvegardé avant de copier quoi que ce soit.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les dossiers du profil et leur taille :
   ```powershell
   Get-ChildItem $env:USERPROFILE -Directory | ForEach-Object { '{0} : {1:N0} Mo' -f $_.Name, ((Get-ChildItem $_.FullName -Recurse -File -ErrorAction SilentlyContinue | Measure-Object Length -Sum).Sum / 1MB) }
   ```
   👉 Explication : (dérivé) donne une idée du volume à sauvegarder par dossier.

2. Identifier volumes, fichiers hors ligne, données applicatives et durée de conservation.
   👉 Explication : une copie de fichiers ne sauvegarde ni Windows ni les applications.

3. En entreprise, privilégier la solution administrée (par ex. OneDrive Known Folder Move ou agent approuvé); pour un poste autonome, choisir une destination distincte du disque système.
   👉 Explication : limite les pertes et les risques de rançongiciel.

## 2. Production — Contrôles

Faire valider le périmètre et la rétention par le responsable des données.

## 3. Production — Sécurité

- Protéger les supports contre le vol et les rançongiciels.

## Validation et retour arrière

- **Validation** : Périmètre et destination écrits.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Microsoft Learn — Known Folder Move](https://learn.microsoft.com/en-us/sharepoint/redirect-known-folders)
- [Guide complet — 1. Définir le périmètre](../../../../../../02-Fiches-Completes/Windows/Toutes-versions/Autres/27_Sauvegarde_Restauration_Donnees_Utilisateur_Windows.md#1-definir-le-perimetre)

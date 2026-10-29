# Fiche_Simple_-_VM_Windows_Sauvegarde_Donnees_Utilisateur_Verifier_Copie.md

- **Environnement** : Poste Windows géré ou autonome, données de profil utilisateur
- **OS / Version** : Windows 10 et Windows 11
- **Catégorie** : sauvegarde / contrôle

---

## Problème précis à résoudre

Prouver que la copie est exploitable et protégée.

## 1. Hors-Production (Lab / Test / POC)

1. Comparer nombre de fichiers et tailles source/destination (chemins de l'étape précédente) :
   ```powershell
   (Get-ChildItem $Source -Recurse -File | Measure-Object).Count
   (Get-ChildItem $Destination -Recurse -File | Measure-Object).Count
   ```
   👉 Explication : (dérivé) les deux nombres doivent correspondre.

2. Comparer des empreintes sur un échantillon de fichiers (nom d'exemple à remplacer) :
   ```powershell
   Get-FileHash "$Source\rapport.docx" -Algorithm SHA256
   Get-FileHash "$Destination\rapport.docx" -Algorithm SHA256
   ```
   👉 Explication : (dérivé) des empreintes identiques prouvent une copie fidèle.

3. Ouvrir plusieurs fichiers restaurables.
   👉 Explication : vérifie qu'ils ne sont pas corrompus.

4. Déconnecter ou verrouiller le support; chiffrer les sauvegardes selon la politique.
   👉 Explication : protège contre vol et chiffrement malveillant.

## 2. Production — Contrôles

En environnement géré, contrôler synchronisation et rétention depuis la console d'administration.

## 3. Production — Sécurité

- Support chiffré et déconnecté après copie.

## Validation et retour arrière

- **Validation** : Nombres et empreintes concordent.
- **Retour arrière** : Refaire la copie après correction.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Microsoft Learn — Known Folder Move](https://learn.microsoft.com/en-us/sharepoint/redirect-known-folders)
- [Guide complet — 3. Vérifier la copie et protéger le support](/02-fiches-completes/windows/toutes-versions/autres/27-sauvegarde-restauration-donnees-utilisateur-windows#3-verifier-la-copie-et-proteger-le-support)
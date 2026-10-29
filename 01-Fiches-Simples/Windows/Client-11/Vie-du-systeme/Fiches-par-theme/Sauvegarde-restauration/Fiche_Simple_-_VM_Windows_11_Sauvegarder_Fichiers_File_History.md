# 📄 Fiche_Simple_-_VM_Windows_11_Sauvegarder_Fichiers_File_History.md

- **Environnement** : Poste Windows 11 géré ou autonome
- **OS / Version** : Windows 11
- **Catégorie** : Sauvegarde / poste de travail
- **Tags** : `windows11`, `sauvegarde`, `file-history`, `fichiers`, `poste`

---

## 🎯 Problème précis à résoudre

Protéger les dossiers utilisateur avec File History vers une cible approuvée et vérifier la dernière sauvegarde.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Confirmer l'outil autorisé : Windows Backup grand public s'appuie sur un compte Microsoft personnel; ne pas le supposer compatible avec un compte professionnel.
   👉 Explication : valider le scénario de gestion du poste avant de continuer.

2. Connecter un disque externe dédié ou un partage approuvé, puis le repérer :
   ```powershell
   Get-Volume | Select-Object DriveLetter, FileSystemLabel, Size, SizeRemaining
   Test-Path \\serveur\partage
   ```
   👉 Explication : remplacer le partage; File History ne sauvegarde pas sur le disque système.

3. Activer : **Panneau de configuration > Système et sécurité > Historique des fichiers > Sélectionner un lecteur**, choisir la cible, puis **Activer**.
   👉 Explication : GUI; en ligne de commande, l'outil `fhmanagew.exe -cleanup 30` sert au nettoyage des anciennes versions.

4. Ajouter les dossiers de test : **Explorateur > Bibliothèques (ou Dossier) > Propriétés > Inclure un dossier** ; exclusions via **Historique des fichiers > Exclure des dossiers**.
   👉 Explication : dossiers non sensibles uniquement.

5. Vérifier dernière exécution et espace : **Historique des fichiers** (« Les fichiers ont été copiés le ... ») :
   ```powershell
   Get-Volume -DriveLetter E | Select-Object SizeRemaining, Size
   ```
   👉 Explication : remplacer la lettre; chiffrer le support (**BitLocker To Go**) et le protéger physiquement.


## ⚡ 2. Production — Façon Simplifiée

1. Pour un poste d'entreprise, utiliser en priorité la solution gérée par l'organisation : **OneDrive > Paramètres > Sauvegarde > Gérer la sauvegarde** (Known Folder Move) ou la solution endpoint.
   ```powershell
   Get-ItemProperty 'HKCU:\Software\Microsoft\OneDrive\Accounts\Business1' | Select-Object UserEmail, UserFolder
   ```
   👉 Explication : File History n'est approprié que si cible, rétention, chiffrement et support sont approuvés.


## 🔒 3. Production — Façon Sécurisée

- Ne pas utiliser un partage ouvert ou un compte administrateur partagé; limiter l'accès aux données du propriétaire.
- Ne pas conserver la seule copie sur le même disque physique que le poste.
- Éviter d'inclure caches, fichiers temporaires ou données sensibles non approuvées; vérifier la stratégie de rétention.

## ✅ Validation et retour arrière

- **Validation** : ouvrir File History, confirmer cible/dernière exécution, puis restaurer un fichier de test vers un autre emplacement.
- **Retour arrière** : désactiver File History et supprimer la cible uniquement après transfert/validation de toute donnée à conserver.

## 🔗 Si le problème n'est pas résolu

- [Microsoft — Configurer et restaurer File History](https://support.microsoft.com/en-us/windows/back-up-and-restore-with-file-history-7bf065bf-f1ea-0a78-c1cf-7dcf51cc8bfc)
- [Microsoft — Windows Backup et limites compte personnel/professionnel](https://support.microsoft.com/en-us/windows/backup-and-restore-your-pc-352091d2-bb9d-3ea3-ed18-52ef2b88cbef)
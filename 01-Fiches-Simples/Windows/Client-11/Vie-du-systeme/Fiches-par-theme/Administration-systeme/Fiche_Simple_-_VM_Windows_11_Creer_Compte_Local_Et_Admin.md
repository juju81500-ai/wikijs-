# 📄 VM_Win11_Utilisateurs_Creer-Compte-Local-Et-Admin.md

- **Environnement** : VM / Poste client (Windows 11 / Windows 10)
- **OS / Version** : Windows 11 Pro / Enterprise / Windows 10 - Famille Windows Client
- **Catégorie** : Utilisateurs & Droits / Gestion des Comptes Clients
- **Tags** : `[windows-11]`, `[windows-10]`, `[windows-client]`, `[utilisateurs]`, `[admin-local]`, `[gui]`, `[powershell]`

---

## 🎯 Problème précis à résoudre
Créer un compte utilisateur local standard et un compte administrateur local sous Windows 11/10 via la nouvelle interface Paramètres, la console classique lusrmgr.msc ou en ligne de commande PowerShell.

---

## 🖥️ Méthode Interface Graphique (GUI Pas-à-Pas)

##### Option A : Via les Paramètres Windows 11
1. **Win + I** > **Comptes** > **Autres utilisateurs** > **Ajouter un compte**.
   👉 Explication : ouvre l'assistant de création de compte.
2. **Je ne dispose pas des informations de connexion de cette personne** > **Ajouter un utilisateur sans compte Microsoft**, puis saisir le nom (ex. `jdupont`) et le mot de passe.
   👉 Explication : crée un compte local.
3. Cliquer sur le compte > **Changer le type de compte** > **Administrateur**.
   👉 Explication : n'élever que si le besoin est justifié.

##### Option B : Via la console `lusrmgr.msc`
1. **Win + R**, saisir `lusrmgr.msc`, **Entrée**.
   👉 Explication : console des utilisateurs et groupes locaux (absente sur Windows Famille : utiliser l'option A ou PowerShell).
2. Clic droit sur **Utilisateurs** > **Nouvel utilisateur...**, saisir nom et mot de passe, **Créer**.
   👉 Explication : crée le compte.
3. Double-clic sur l'utilisateur > onglet **Membre de** > **Ajouter** > `Administrateurs`.
   👉 Explication : accorde les droits d'administration locale.

---

## ⚡ Méthode Ligne de commande PowerShell (en administrateur)

1. Créer le compte (le mot de passe est saisi sans s'afficher) :
   ```powershell
   $Password = Read-Host "Mot de passe" -AsSecureString
   New-LocalUser -Name "jdupont" -Password $Password -FullName "Jean Dupont"
   ```
   👉 Explication : remplacer `jdupont`; le mot de passe ne figure ni dans la commande ni dans l'historique.
2. Ajouter à l'administration locale :
   ```powershell
   Add-LocalGroupMember -Group "Administrateurs" -Member "jdupont"
   ```
   👉 Explication : sur un Windows en anglais, le groupe se nomme `Administrators`.
3. Retirer des administrateurs :
   ```powershell
   Remove-LocalGroupMember -Group "Administrateurs" -Member "jdupont"
   ```
   👉 Explication : repasse le compte en utilisateur standard.
4. Désactiver ou réactiver, puis vérifier :
   ```powershell
   Disable-LocalUser -Name "jdupont"
   Enable-LocalUser -Name "jdupont"
   Get-LocalUser jdupont | Select-Object Name, Enabled
   ```
   👉 Explication : désactiver est réversible, supprimer ne l'est pas.

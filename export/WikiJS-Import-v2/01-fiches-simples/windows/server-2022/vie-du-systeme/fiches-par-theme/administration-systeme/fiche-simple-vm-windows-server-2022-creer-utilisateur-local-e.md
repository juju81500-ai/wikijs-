---
title: "VM_WinSrv_2022_Utilisateurs_Creer-Utilisateur-Local-Et-Admin"
description: "Créer un compte utilisateur local standard (sans privilèges) et un compte administrateur local sous Windows Server 2022 en utilisant l'interface graphique (GUI) ou la ligne de commande PowerShell, et attribuer/retirer les droits d'administration."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[winsrv2022]", "[windows-server]", "[utilisateurs]", "[admin-local]", "[gui]", "[powershell]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_WinSrv_2022_Utilisateurs_Creer-Utilisateur-Local-Et-Admin.md

- **Environnement** : VM / Serveur Physique (Windows Server 2022)
- **OS / Version** : Windows Server 2022 Standard / Datacenter - Famille Windows Server
- **Catégorie** : Utilisateurs & Droits / Gestion des Comptes Locaux
- **Tags** : `[winsrv2022]`, `[windows-server]`, `[utilisateurs]`, `[admin-local]`, `[gui]`, `[powershell]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Créer un compte utilisateur local standard (sans privilèges) et un compte administrateur local sous Windows Server 2022 en utilisant l'interface graphique (GUI) ou la ligne de commande PowerShell, et attribuer/retirer les droits d'administration.

---

## 🖥️ Méthode Interface Graphique (GUI Pas-à-Pas - "Clic-Clic")
> Cette procédure concerne un serveur autonome ou membre d'un domaine, pas un contrôleur de domaine : celui-ci ne possède pas de comptes locaux gérés par `lusrmgr.msc`. Pour un compte de domaine, utiliser Utilisateurs et ordinateurs Active Directory (`dsa.msc`).


1. **Ouvrir la console de gestion des utilisateurs et groupes locaux** :
   - Appuyer sur les touches Win + R du clavier.
   - Saisir lusrmgr.msc puis appuyer sur Entrée.
   - 👉 *Explication : Cela ouvre directement la console de gestion des comptes locaux.*

2. **Créer un utilisateur local classique (sans privilèges)** :
   - Cliquer sur le dossier Utilisateurs.
   - Faire un clic droit dans la zone centrale ➔ Nouvel utilisateur...
   - Nom d'utilisateur : user_std
   - Saisir le mot de passe et valider.
   - 👉 *Explication : Crée un compte utilisateur membre uniquement du groupe restreint "Utilisateurs".*

3. **Créer un utilisateur administrateur local (Droits Admin)** :
   - Refaire un clic droit dans le dossier Utilisateurs ➔ Nouvel utilisateur...
   - Nom d'utilisateur : adm-local
   - Saisir le mot de passe puis cliquer sur Créer.
   - Faire un double-clic sur le compte adm-local ➔ Onglet Membre de ➔ Ajouter le groupe Administrateurs.
   - 👉 *Explication : Accorde les privilèges d'administration totale de la machine au compte adm-local.*

---

## ⚡ Méthode Ligne de commande PowerShell
1. **Création d'un compte utilisateur standard** :
   ```powershell
   $Password = Read-Host "Mot de passe" -AsSecureString
   New-LocalUser -Name "jdupont" -Password $Password -FullName "Jean Dupont"
   ```
2. **Création du compte administrateur local TSSR** :
   ```powershell
   $AdminPassword = Read-Host "Mot de passe administrateur" -AsSecureString
   New-LocalUser -Name "adm-jdupont" -Password $AdminPassword -FullName "ADM Jean Dupont"
   $AdminGroup = Get-LocalGroup -SID 'S-1-5-32-544'
   Add-LocalGroupMember -Group $AdminGroup.Name -Member "adm-jdupont"
   ```
3. Vérifier qu'un second compte d'administration et un accès de récupération sont opérationnels avant de désactiver ou renommer le compte Administrateur intégré. Ne pas désactiver ce compte par défaut sans politique testée.
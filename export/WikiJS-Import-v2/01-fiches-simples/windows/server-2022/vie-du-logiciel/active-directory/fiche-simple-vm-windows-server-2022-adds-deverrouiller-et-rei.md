---
title: "VM_WinSrv_2022_ADDS_Deverrouiller-Et-Reinitialiser-MotDePasse-Utilisateur"
description: "Déverrouiller un compte utilisateur bloqué suite à plusieurs échecs de mot de passe dans l'Active Directory, ou réinitialiser son mot de passe et forcer son changement à la prochaine connexion."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[winsrv2022]", "[active-directory]", "[user-management]", "[password-reset]", "[unlock]", "[gui]", "[powershell]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 VM_WinSrv_2022_ADDS_Deverrouiller-Et-Reinitialiser-MotDePasse-Utilisateur.md

- **Environnement** : VM / Contrôleur de Domaine AD DS
- **OS / Version** : Windows Server 2022 Standard / Datacenter
- **Catégorie** : Active Directory / Gestion des Utilisateurs
- **Tags** : `[winsrv2022]`, `[active-directory]`, `[user-management]`, `[password-reset]`, `[unlock]`, `[gui]`, `[powershell]`

---

## 🎯 Problème précis à résoudre
Déverrouiller un compte utilisateur bloqué suite à plusieurs échecs de mot de passe dans l'Active Directory, ou réinitialiser son mot de passe et forcer son changement à la prochaine connexion.

---

## 🖥️ Méthode Interface Graphique (GUI Pas-à-Pas - "Clic-Clic")

1. **Ouvrir la console Utilisateurs et ordinateurs Active Directory** :
   - Appuyer sur les touches `Win + R` du clavier.
   - Saisir `dsa.msc` puis appuyer sur `Entrée`.
   - 👉 *Explication : Ouvre la console d'administration principale de l'annuaire Active Directory.*

2. **Rechercher le compte utilisateur** :
   - Faire un **clic droit** sur le nom du domaine (ex: `lab.local`) ou sur l'Unité d'Organisation (OU).
   - Sélectionner **Rechercher...**.
   - Dans la case *Nom*, saisir le nom de l'utilisateur (ex: `jdupont`) puis cliquer sur **Rechercher maintenant**.
   - Faire un **double-clic** (ou clic droit ➔ *Propriétés*) sur le compte trouvé.
   - 👉 *Explication : Localise précisément l'objet compte utilisateur dans l'annuaire.*

3. **Déverrouiller le compte utilisateur** :
   - Aller dans l'onglet **Compte**.
   - Cocher la case **Déverrouiller le compte. Ce compte est actuellement verrouillé sur ce contrôleur de domaine Active Directory.**
   - Cliquer sur **Appliquer**.
   - 👉 *Explication : Remet immédiatement le compteur d'échecs de mot de passe à zéro et autorise la connexion.*

4. **Réinitialiser le mot de passe** :
   - Dans la console ou la fenêtre de recherche, faire un **clic droit** sur l'utilisateur ➔ **Réinitialiser le mot de passe...**
   - Saisir le nouveau mot de passe temporaire et le confirmer.
   - Laisser la case **L'utilisateur doit changer de mot de passe à la prochaine ouverture de session** **cochée**.
   - Cliquer sur **OK**.
   - 👉 *Explication : Modifie le mot de passe et oblige l'utilisateur à définir son propre secret dès son login.*

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. **Déverrouillage rapide d'un compte utilisateur en PowerShell** :
   ```powershell
   Unlock-ADAccount -Identity "jdupont"
   ```
   👉 *Explication : Tu fais ça, le compte jdupont est débloqué immédiatement.*

---

## ⚡ 2. Production — Façon Simplifiée
1. **Réinitialisation du mot de passe avec changement obligatoire à la connexion** :
   ```powershell
   $TemporaryPassword = Read-Host "Mot de passe temporaire" -AsSecureString
   Set-ADAccountPassword -Identity "jdupont" -NewPassword $TemporaryPassword -Reset
   Set-ADUser -Identity "jdupont" -ChangePasswordAtLogon $true
   Unlock-ADAccount -Identity "jdupont"
   ```
   👉 *Explication : Le mot de passe est saisi sans être affiché ni inscrit en clair dans le script. Le transmettre à l'utilisateur par un canal distinct et sécurisé.*

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. **Rechercher l'événement de verrouillage dans le journal Sécurité d'un contrôleur de domaine** :
   - En GUI, ouvrir l'Observateur d'événements (`eventvwr.msc`), puis **Journaux Windows > Sécurité > Filtrer le journal actuel...** et saisir l'ID d'événement `4740`.
   - Ouvrir l'événement correspondant à l'utilisateur et relever le contrôleur de domaine, l'heure et le nom du poste appelant. Répéter sur les contrôleurs concernés si nécessaire; les événements dépendent de la stratégie d'audit et de la rétention des journaux.
   ```powershell
   Get-WinEvent -FilterHashtable @{ LogName = 'Security'; Id = 4740; StartTime = (Get-Date).AddDays(-1) } | Where-Object { $_.Message -match '(?i)jdupont' } | Select-Object TimeCreated, MachineName, Message
   ```
   👉 *Explication : L'événement 4740 indique le verrouillage et le poste appelant; ce contrôle n'est pas à lui seul une preuve d'attaque par force brute.*
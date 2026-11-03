---
title: "Active Directory (AD)"
description: "Active Directory est un service d’annuaire développé par Microsoft. Il centralise la gestion des utilisateurs, des ordinateurs, des groupes, des droits d’accès, des GPO et plus encore, dans un environnement Windows Server. Il est fondamental pour l’administration d’un domaine (ex : entreprise.local)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Active Directory (AD)

## 📌 Présentation

Active Directory est un service d’annuaire développé par Microsoft. Il centralise la gestion des utilisateurs, des ordinateurs, des groupes, des droits d’accès, des GPO et plus encore, dans un environnement Windows Server. Il est fondamental pour l’administration d’un domaine (ex : `entreprise.local`).

---

## 🏗️ Structure de base

- **Forêt (Forest)** : ensemble logique de domaines
- **Domaine (Domain)** : unité principale (`ad.entreprise.local`)
- **Contrôleur de domaine (DC)** : serveur gérant AD
- **Unité d’organisation (OU)** : conteneur logique pour structurer les objets AD

---

## 🔧 Outils principaux

| Outil | Description | Exemple |
|-------|-------------|---------|
| `dsa.msc` | Console « Utilisateurs et ordinateurs Active Directory » | Gérer les utilisateurs, groupes, machines |
| `dnsmgmt.msc` | Gestion du DNS intégré à AD | Vérifier les zones de recherche directe/inverse |
| `gpmc.msc` | Console de gestion des GPO | Lier GPO à une OU |
| `Active Directory Sites and Services` | Gérer la réplication entre sites | Configuration multi-sites |

---

## 🧰 Cmdlets PowerShell utiles

| Cmdlet | Description | Exemple |
|--------|-------------|---------|
| `Get-ADUser` | Liste ou recherche des utilisateurs | `Get-ADUser -Filter *` |
| `New-ADUser` | Crée un utilisateur | `New-ADUser -Name "Toto" -SamAccountName toto -AccountPassword (Read-Host -AsSecureString)` |
| `Get-ADComputer` | Liste les ordinateurs | `Get-ADComputer -Filter *` |
| `Get-ADGroupMember` | Liste les membres d’un groupe | `Get-ADGroupMember -Identity "IT"` |
| `Add-ADGroupMember` | Ajoute un membre à un groupe | `Add-ADGroupMember -Identity "IT" -Members "toto"` |
| `Set-ADUser` | Modifie un compte | `Set-ADUser -Identity toto -Title "Technicien"` |

---

## 🔎 Cas d’usage courant

- Création et organisation des comptes utilisateurs et ordinateurs
- Définition de groupes de sécurité (accès partages, applications, imprimantes)
- Mise en place d’OU pour appliquer des GPO spécifiques
- Gestion centralisée des mots de passe et verrouillage de compte
- Association AD avec d’autres services (IIS, NAS, VPN, etc.)

---

## ⚠️ Erreurs fréquentes

- Créer tous les objets dans `Users` au lieu de structurer avec des OU
- Ne pas documenter la politique de nommage (objets incohérents)
- Attribuer trop de privilèges aux comptes standards (utilisateurs dans `Administrateurs`) 
- Ne pas tester les droits via un utilisateur « test »
- Mauvaise configuration DNS → empêche la jonction au domaine

---

## ✅ Bonnes pratiques

- Créer une **arborescence claire d’OU** (par site, service, type d’objet)
- Utiliser des **groupes de sécurité** pour gérer les accès (pas les utilisateurs directement)
- Automatiser la création de comptes via PowerShell + CSV
- Sécuriser les comptes privilégiés (MFA, mot de passe fort, audit)
- Documenter les stratégies de nommage et d’attribution de droits

---

## 📚 Ressources complémentaires

- [Cmdlets ActiveDirectory PowerShell](https://learn.microsoft.com/en-us/powershell/module/activedirectory/)
- `dsa.msc`, `gpmc.msc`, `dnsmgmt.msc`
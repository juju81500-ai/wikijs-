---
title: "TP – Gestion des utilisateurs et des groupes sous Windows"
description: "- LInformatiques"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Gestion des utilisateurs et des groupes sous Windows

## 🧩 Création des comptes et groupes

### 🔹 Groupes à créer

- `L_Informatiques`
- `L_Responsables`
- `L_Collegues`

### 🔹 Utilisateurs à créer

|Nom|Prénom|Login|Groupe(s)|Particularités|
|---|---|---|---|---|
|François|François|francois|L_Informatiques, L_Responsables|Mot de passe sans expiration|
|Yann|Yann|yann|L_Informatiques, L_Responsables|-|
|Pauline|Pauline|pauline|L_Collegues|-|
|Alix|Alix|alix|L_Collegues|-|

> 📌 Créer les groupes avant d’ajouter les utilisateurs à ceux-ci.

**Interface graphique (lusrmgr.msc)** :

1. Clic droit sur "Utilisateurs" > _Nouvel utilisateur_ > remplir champs
2. Décocher "changer le mot de passe à la prochaine ouverture de session"
3. Cocher "le mot de passe n’expire jamais" pour François
4. Clic droit sur "Groupes" > _Nouveau groupe_ > ajouter membres

---

## 🛡️ Attribution des privilèges

|Utilisateur|Groupe à ajouter|Rôle attribué|
|---|---|---|
|François|Administrateurs|Admin du poste Win10-XX|
|Yann|Lecteurs des journaux d’événements,Opérateurs de configuration réseau|Consultation journaux + config réseau|
|Pauline,Alix|Opérateurs de sauvegarde|Sauvegarde du poste Win10-XX|

**⚠️** L'imbrication de groupes locaux n'est pas fonctionnelle sous SAM : ajouter chaque utilisateur directement.

**Suppression d’un utilisateur d’un groupe :**

- Clic droit > Propriétés > Onglet _Membre de_ > _Supprimer_ le groupe `Utilisateurs`

---

## 🔍 Exploration des propriétés utilisateurs/groupes (GUI)

### Utilisateur

- Nom complet, description
- Appartenances aux groupes
- Options de mot de passe et activation du compte
- Profils, scripts, lecteurs mappés

### Groupe

- Description, liste des membres

---

## 💻 Gestion par ligne de commande (CMD)

```bash
net user francois                   # Infos détaillées sur le compte
net localgroup administrateurs     # Liste des membres du groupe admin
net user Romain * /add             # Crée Romain avec saisie masquée du mot de passe
net localgroup L_Responsables Romain /add
```

> L’ajout d’un utilisateur ou d’un groupe modifie la base SAM locale – nécessite CMD en tant qu’admin

---

## 🖥️ Gestion complémentaire via l’interface

- `logoff` : pour fermer une session
- Observation via `sysdm.cpl > Profils utilisateurs` : seuls les utilisateurs ayant ouvert une session ont un profil créé dans `C:\Users`

---

## 🔍 SID et groupes (CMD)

```bash
whoami /user     # Affiche le SID de l'utilisateur connecté
whoami /groups   # Liste les groupes et SID associés
```

---

## ⚡ PowerShell – Gestion avancée

### Afficher tous les utilisateurs avec nom, SID, description

```powershell
Get-LocalUser | Select Name,SID,Description
```

### Informations détaillées sur un utilisateur (ex : james)

```powershell
Get-LocalUser -Name james | Select FullName,Description,ObjectClass,LastLogon
```

### Modifier la description d’un utilisateur

```powershell
Set-LocalUser -Name adm -Description "Compte générique admin de secours"
```

### Afficher les membres d’un groupe local

```powershell
Get-LocalGroupMember -Name L_SupportInfo | Select Name,SID
```

---

## ✅ Vérifications

- ✅ Groupes et utilisateurs bien créés
- ✅ Affectations correctes aux groupes
- ✅ François possède les droits d’administration
- ✅ Vérification des SID, profils et propriétés via GUI et CLI

---

## 📌 Bonnes pratiques professionnelles

|Bonnes pratiques|Pourquoi ?|
|---|---|
|Désactiver les comptes inutiles|Réduire la surface d’attaque|
|Créer un compte par utilisateur|Garantir la traçabilité|
|Nommer clairement utilisateurs et groupes|Facilité de gestion et d’administration|
|Vérifier régulièrement les appartenances|Éviter les privilèges excessifs involontaires|
|Utiliser PowerShell pour des actions en lot|Gain de temps, reproductibilité|
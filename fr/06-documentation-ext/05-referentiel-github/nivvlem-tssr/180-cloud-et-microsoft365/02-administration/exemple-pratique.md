---
title: "TP – Administration Microsoft 365 : utilisateurs, groupes et synchronisation AD"
description: "- Zachary Ramablag – Formateur – Pédagogie – Canada – Login : Zachary"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Administration Microsoft 365 : utilisateurs, groupes et synchronisation AD
## 🧾 TP 1 – Gestion des utilisateurs et groupes M365 (console + PowerShell)

### 1. Création des utilisateurs (console graphique)

- Zachary Ramablag – Formateur – Pédagogie – Canada – Login : Zachary
- Vishnou Lapaix – Formateur – Pédagogie – USA – Login : Vishnou
- Oussama Lairbon – Cuisinier – Restauration – France – Login : Oussama
- Mot de passe temporaire à noter pour chacun

### 2. Création en PowerShell

```powershell
New-MsolUser -UserPrincipalName Sacha@domaine.tld -DisplayName "Sacha Touille" -FirstName Sacha -LastName Touille -Department Restauration -Title Cuisinier -Password Pa55w.rd -UsageLocation JP -ForceChangePassword $true
```

### 3. Connexion avec Sacha – échec sans licence ➜ Attribution obligatoire :

```powershell
Set-MsolUserLicense -UserPrincipalName Sacha@domaine.tld -AddLicenses "tenant:ENTERPRISEPACK"
```

### 4. Gestion des rôles et fonctions

```powershell
Add-MsolRoleMember -RoleName "Company Administrator" -RoleMemberEmailAddress "labeni@domaine.tld"
Set-MsolUser -UserPrincipalName Oussama@domaine.tld -Title "Chef Cuisinier"
```

### 5. Suppression/restauration utilisateurs

```powershell
Remove-MsolUser -UserPrincipalName Vishnou@domaine.tld
Restore-MsolUser -UserPrincipalName Vishnou@domaine.tld
Remove-MsolUser -UserPrincipalName Sacha@domaine.tld
Restore-MsolUser -UserPrincipalName Sacha@domaine.tld
```

### 6. Attribution de licences

- Via GUI pour Oussama
    

```powershell
Set-MsolUserLicense -UserPrincipalName Zachary@domaine.tld -AddLicenses "tenant:ENTERPRISEPACK"
```

- Sacha sans certains services :
    

```powershell
$opt = New-MsolLicenseOptions -AccountSkuId "tenant:ENTERPRISEPACK" -DisabledPlans "SWAY", "BI_AZURE_P2", "RMS_S_ENTERPRISE"
Set-MsolUserLicense -UserPrincipalName Sacha@domaine.tld -LicenseOptions $opt
```

- Vishnou sans Office Online, puis réactivation via GUI
    

### 7. Création de groupes Microsoft 365 (GUI)

- GO_Restauration, GO_Commercial, GO_Pedagogie, GO_Informatique, GO_CE, GO_Direction, etc.
    
- Affectation des utilisateurs à leur groupe et service
    

### 8. Groupe de sécurité

```powershell
New-MsolGroup -DisplayName "GDS_Jedemolet"
Add-MsolGroupMember -GroupObjectId <id_du_groupe> -GroupMemberObjectId <id_utilisateur>
```

### 9. Gestion des rôles étendus

```powershell
Add-MsolRoleMember -RoleName "Password Administrator" -RoleMemberEmailAddress Vishnou@domaine.tld
Set-MsolUserPassword -UserPrincipalName Oussama@domaine.tld -NewPassword 'Pa55w.rd123'
Add-MsolRoleMember -RoleName "Billing Administrator" -RoleMemberEmailAddress Oussama@domaine.tld
```

### 10. Vérifications pratiques

- Connexion Outlook Web avec Vishnou
    
- Envoi d’un mail au groupe Pédagogie
    
- Réception du mail par les membres
    
- Réinitialisation du mot de passe de Zachary par Vishnou
    

---

## 🛠️ TP 2 – Déploiement Azure AD Connect

### 1. Prérequis techniques

- AD DS installé sur `cheouamXX.lcl`
    
- Nom du contrôleur : `CD-2k19-XX` – IP : `10.65.0.1/24`
    
- Création OU et utilisateurs :
    
    - [lfer@cheouamXX.lcl](mailto:lfer@cheouamXX.lcl), [edanlos@cheouamXX.lcl](mailto:edanlos@cheouamXX.lcl), [pamploi@cheouamXX.lcl](mailto:pamploi@cheouamXX.lcl)…
        
    - Fonction, service renseignés dans les attributs AD
        

### 2. Arborescence recommandée

```
OU=_cheouamXX
  ├── OU_Utilisateurs
  ├── OU_Comptes de service
  ├── OU_Groupes
  │   ├── Domaine Local
  │   └── Groupe Global
  └── OU_Archives
```

### 3. Préparation AD

- Ajout d’un suffixe UPN : `domaine.public`
    
- Remappage du login UPN pour chaque utilisateur à synchroniser
    
- Création d’un compte de service (membre des Admins de l’entreprise)
    
- Création d’un compte global admin dans M365 (non licencié)
    

### 4. Installation Azure AD Connect

- Télécharger `AzureADConnect.msi`
    
- Lancer installation en mode **personnalisé**
    
- Sélectionner :
    
    - **Mot de passe hash sync**
        
    - **Connexion avec compte admin Azure** + compte service AD
        
    - **Filtrage par OU** : synchroniser uniquement utilisateurs + groupes
        

### 5. Forcer une synchronisation

```powershell
Import-Module ADSync
Start-ADSyncSyncCycle -PolicyType Delta
```

### 6. Vérifications post-sync

- Apparaît dans le portail Microsoft 365 : Utilisateurs synchronisés
    
- Ajouter licence depuis la console M365
    
- Connexion à Outlook Web ➜ accès OK
    

### 7. Alias et attributs proxyAddresses

- Ajouter via éditeur d’attributs (ADUC) :
    
    - `SMTP:adresseprincipale@domaine.tld`
        
    - `smtp:alias1@domaine.tld`, etc.
        
- Forcer synchronisation après modification
    

---

## ✅ À retenir pour les révisions

- La gestion des utilisateurs peut se faire intégralement via PowerShell
    
- Les **groupes Microsoft 365** permettent collaboration + distribution
    
- Les **groupes de sécurité** sont utilisés pour les droits (accès, filtres)
    
- Azure AD Connect synchronise comptes AD locaux + attributs vers Azure
    

---

## 📌 Bonnes pratiques professionnelles

- Documenter les utilisateurs, rôles, licences et groupes créés
    
- Ne jamais activer la synchro globale sur tout l’AD → filtrer par OU
    
- Séparer les OU de **comptes, services, groupes, archives** dès le départ
    
- Surveiller les synchronisations automatiques (`delta` toutes les 30 min par défaut)
    
- Ne pas désactiver un compte local avant d’avoir retiré sa licence dans Azure
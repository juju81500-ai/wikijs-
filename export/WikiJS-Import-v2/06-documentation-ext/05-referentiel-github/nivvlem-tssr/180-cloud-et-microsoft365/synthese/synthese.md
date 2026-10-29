---
title: "Synthèse – Cloud et Microsoft 365"
description: "- Création via [microsoft.com/365/try](https://www.microsoft.com/365/try)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Synthèse – Cloud et Microsoft 365
## ☁️ Concepts fondamentaux du Cloud

### Modèles SPI

|Modèle|Description|Exemples|
|---|---|---|
|**SaaS**|Logiciel en tant que service|Outlook Web, Teams, Gmail|
|**PaaS**|Plateforme (hébergement applicatif)|Azure App Services|
|**IaaS**|Infrastructure (VM, stockage)|Azure VM, AWS EC2|

### Types de Cloud

|Type|Description|
|---|---|
|Public|Mutualisé (Azure, AWS, GCP)|
|Privé|Dédié à une entité (on-prem ou datacenter)|
|Hybride|Mix local/Cloud (Azure AD Connect)|

---

## 🧱 Microsoft 365 – Architecture et services

### Composants principaux

- **Exchange Online** : messagerie, antispam, archivage
- **Teams** : réunions, tchat, visio, canaux, travail collaboratif
- **SharePoint Online** : intranet, GED, socle documentaire Teams
- **OneDrive** : stockage personnel, synchronisation
- **Azure Active Directory** : gestion des identités et rôles

### Licences courantes

|Public|Licences|
|---|---|
|PME|Business Basic, Standard, Premium|
|Entreprises|E3, E5|
|Secteur public / scolaire|A1, A3, F3|

### Tenant Microsoft 365

- Création via [microsoft.com/365/try](https://www.microsoft.com/365/try)
- Lien avec domaine personnalisé via enregistrement **TXT** DNS
- Ajout des enregistrements **MX, SPF, DKIM, DMARC, CNAME** pour la messagerie

---

## 👥 Utilisateurs, groupes et rôles

### Gestion des comptes

- Création manuelle ou en masse (CSV ou PowerShell)
- Restauration / suppression via `Remove-MsolUser`, `Restore-MsolUser`

### Groupes

|Type|Usage|
|---|---|
|Microsoft 365|Collaboration, distribution, Teams|
|Sécurité|Affectation de droits (SharePoint, GPO…)|

### Rôles RBAC

```powershell
Add-MsolRoleMember -RoleName "Company Administrator" -RoleMemberEmailAddress admin@domain.tld
```

---

## ⚙️ PowerShell et administration

### Connexions essentielles

```powershell
Connect-MsolService                  # Module MSOnline
Connect-ExchangeOnline               # Exchange
Connect-MicrosoftTeams               # Teams
Connect-IPPSSession                  # Protection & conformité
```

### Licences

```powershell
Set-MsolUserLicense -UserPrincipalName user@domain.tld -AddLicenses "tenant:ENTERPRISEPACK"
```

### Groupes, rôles et boîtes partagées

```powershell
New-Mailbox -Shared -Name "Support"
Add-MailboxPermission -Identity "Support" -User "user@domain.tld" -AccessRights FullAccess
```

---

## 🔁 Synchronisation Active Directory – Azure AD Connect

### Préparation

- Créer UPN `@domain.tld`
- Filtrage par **OU** (jamais toute l’arborescence)

### Installation

- Mode personnalisé recommandé
- Sync mot de passe (hash SHA256)
- Compte global admin + compte de service AD requis

### Commandes utiles

```powershell
Start-ADSyncSyncCycle -PolicyType Delta
```

---

## 🔐 Sécurité, conformité et gouvernance

### Protection messagerie

|Mécanisme|Fonction|
|---|---|
|SPF|Autorise les IP d’envoi|
|DKIM|Signature cryptographique|
|DMARC|Politique de vérification|

### MFA (Multi-Factor Auth)

- Obligatoire sur tous comptes admin
- Recommandé sur tous les utilisateurs
- Configurable par compte ou globalement via Azure AD

### DLP, audit et journaux

- Centre sécurité [security.microsoft.com](https://security.microsoft.com/)
- **Audit log**, **rétention**, **archivage**, **quarantaine**

### Sauvegarde

- Microsoft 365 ne garantit pas la **sauvegarde complète**
- Solutions tierces recommandées : Veeam, SkyKick, Acronis

---

## 🗂️ Office, SharePoint, OneDrive, Teams

### Office 365 ProPlus

- Déploiement via GPO : `setup.exe /configure Configuration.xml`
- Canaux de mise à jour : Mensuel, Semi-annuel (ciblé ou non)

### SharePoint Online

- Sites, bibliothèques, droits (AGDLP synchronisé)
- Stockage par site : 25 To, limitations sur poids fichiers
- Gouvernance stricte des droits et synchronisation

### OneDrive

- Par défaut activé pour tous les utilisateurs
- Centre admin dédié pour configurer partages, quotas, synchronisation

### Teams

- Plateforme centralisée (chat, fichiers, visioconférence)
- Scripts PowerShell pour **restreindre la création des groupes**
- Sécurisation des partages externes / invités

---

## ✅ À retenir pour les révisions

- Microsoft 365 s’articule autour de **5 grands piliers** : Exchange, Teams, OneDrive, SharePoint, Azure AD
- La sécurité repose sur **MFA, DNS, audit, sensibilisation et gouvernance**
- L’administration se fait via **portail et PowerShell**
- La synchronisation locale (AD Connect) doit être filtrée et documentée
- Un **plan de sauvegarde** externe est indispensable même avec le Cloud

---

## 📌 Bonnes pratiques professionnelles

- Toujours créer un compte **break-glass** sans MFA (monitoré, en lecture seule)
- Éviter les GPO d’installation sur tout le domaine sans test préalable
- Ne jamais exposer l’accès global à la création de groupes M365
- Activer les **stratégies de sécurité par défaut** pour les petits environnements
- Documenter systématiquement tous les éléments suivants :
    - Identifiants du tenant
    - Licences utilisées
    - Groupes créés
    - Synchronisations AD
    - Scripts PowerShell
    - Topologie DNS du domaine (SPF, DKIM, DMARC)
# Découverte de Microsoft 365

## ☁️ Qu'est-ce qu'une plateforme Cloud ?

> **SaaS (Software as a Service)** : modèle de distribution d'applications où le logiciel est hébergé à distance et accessible via Internet, généralement par abonnement.

**Avantages** :

- Pas de maintenance locale
- Accès depuis n’importe quel appareil
- Mise à jour centralisée
- Réduction des coûts d’infrastructure

**Bonnes pratiques** :

- Toujours vérifier la conformité RGPD du fournisseur
- Évaluer la résilience et la localisation des datacenters

---

## 🏢 Présentation de Microsoft 365

### Points clés :

- Offre Cloud de Microsoft
- Suite de services pour particuliers, entreprises, associations et secteur public
- Applications incluses : Exchange Online, SharePoint, Teams, OneDrive, Office, Azure AD, etc.
- Multiplateforme (PC, mobile, navigateur)

### Chiffres (mai 2020)

- 75 millions d'utilisateurs actifs par jour
- 4 datacenters en France (gains en latence et conformité)

### Concurrents principaux

- Google Workspace
- Zoho Workplace
- OnlyOffice, etc.

---

## 🧾 Les licences Microsoft 365

### Exemples de plans :

- **Particuliers** : Personnel, Famille
- **PME** : Business Basic, Standard, Premium
- **Éducation** : A1, A3, A5
- **Gouvernement et secteur public** : E1, E3, E5
- **Entreprises** : F3, E3, E5, Apps for Enterprise

**Bonnes pratiques** :

- Toujours adapter le plan aux usages réels et au profil de l'organisation
- Centraliser la gestion des licences via l’interface d’administration Microsoft 365

---

## 🧰 Applications principales de Microsoft 365

|Application|Fonction principale|
|---|---|
|**Exchange Online**|Messagerie professionnelle (emails, calendrier)|
|**OneDrive**|Stockage et partage de fichiers|
|**SharePoint**|Intranet collaboratif et gestion documentaire|
|**Teams**|Communication unifiée (chat, visio, téléphonie)|
|**Yammer**|Réseau social d’entreprise|
|**Delve**|Activités et contenu pertinent par utilisateur|
|**Stream**|Partage de vidéos internes à l'organisation|
|**OneNote**|Bloc-notes numérique collaboratif|
|**Dynamics 365**|CRM et gestion métier|

---

## 🗂️ SharePoint Online en pratique

- **Organisation** : gestion des droits, des utilisateurs, de l'information
- **Partage et collaboration** : sites d'équipe, boîtes aux lettres partagées, bibliothèque de documents
- **Gestion** : règles d'affichage, moteurs de recherche personnalisables
- **Création** : applications métiers avec PowerApps, design avec Application Design Manager

**Bonnes pratiques** :

- Utiliser les **Groupes Microsoft 365** pour centraliser les ressources
- Structurer les sites SharePoint par service ou projet pour plus de clarté

---

## 🏠 Notion de Tenant Microsoft 365

### Définition

> Un **Tenant** est l’environnement propre à une organisation abonnée à Microsoft 365, lié à un nom de domaine spécifique.

### Exemple : `admin@monentreprise.onmicrosoft.com`

- L’utilisateur qui crée le tenant est **Administrateur global**
- L’adresse `@onmicrosoft.com` est attribuée par défaut
- Il est **possible d’associer un domaine personnalisé** (ex: @votreentreprise.fr)

**Bonnes pratiques** :

- Choisir un nom de tenant clair et représentatif dès le départ (non modifiable)
- Documenter l’arborescence des utilisateurs, groupes, et droits dès l’origine

---

## 🛠️ Création d’un Tenant Microsoft 365

### Étapes :

1. Sélection du plan (ex : Business Basic, E5…)
2. Saisie d’une adresse email valide
3. Informations sur l’entreprise (nom, taille, secteur)
4. Choix du nom du tenant (ex: `nomdelentreprise.onmicrosoft.com`)
5. Validation de l’inscription

**Bonnes pratiques** :

- Réserver son domaine personnalisé dès le départ pour une image professionnelle
- Définir une politique de sécurité dès l’initialisation (MFA, mot de passe, etc.)

---

## 🌍 Location d’un domaine internet

- Permet d’utiliser des adresses email en `@votreentreprise.fr`
- Intégration facile via l’interface Microsoft 365 Admin
- Possibilité de configurer : DNS, SPF, DKIM, DMARC

**Bonnes pratiques** :

- Vérifier que le registrar permet la gestion DNS complète
- Mettre en place un enregistrement SPF dès la configuration

---

## ✅ À retenir pour l'examen

- Microsoft 365 est une plateforme SaaS riche, modulaire et adaptée à tous types de structures
- Le **Tenant** est l’environnement de base à bien configurer dès le début
- L’**administrateur global** est le rôle clé pour la gestion du Tenant
- Les **licences** sont nombreuses : bien les adapter aux besoins
- **SharePoint**, **Teams** et **OneDrive** sont au cœur de la collaboration

## 📌 Bonnes pratiques professionnelles

- Mettre en place des **bonnes pratiques de sécurité** dès la création
- Structurer l’environnement selon une **organisation claire et documentée**
- Nommer les utilisateurs, groupes et sites selon une **convention cohérente et durable**
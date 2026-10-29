---
title: "TP – Cloud et Microsoft 365 : étude de cas et création d’un tenant"
description: "- Haut niveau de sécurité et de confidentialité exigé"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Cloud et Microsoft 365 : étude de cas et création d’un tenant

## 🧾 TP 1 – Adapter une réponse à des contraintes métiers

### 🔍 Contexte 1 : Entreprise étrangère exigeante

#### Données du contexte :

- Haut niveau de sécurité et de confidentialité exigé
- Accès à une ligne Internet haut débit
- Prise en charge de l’infrastructure par un prestataire externe

#### Analyse :

- Risque RGPD ou Patriot Act si données hébergées hors UE
- Pas de ressources internes pour l’infogérance

#### Solution proposée :

✅ **Cloud privé managé** chez un hébergeur français agréé HDS ou ISO 27001

- Serveurs virtualisés sur hyperviseur Proxmox ou VMware
- Tunnel VPN vers le prestataire pour la supervision

---

### 🔍 Contexte 2 : Chaîne de magasins – multi-sites

#### Données du contexte :

- 25 sites répartis sur le territoire
- Connexions ADSL parfois instables
- Nécessité d’applications de simulation 3D

#### Analyse :

- Problèmes de bande passante sur les sites = risque d’indisponibilité SaaS
- Applications gourmandes en ressources = mauvais candidats au SaaS

#### Solution proposée :

✅ **Infrastructure hybride**

- Serveurs applicatifs centralisés dans un Cloud public (Azure ou AWS)
- Machines locales performantes dans les magasins pour la 3D (postes lourds)
- Synchronisation différée des projets vers SharePoint ou OneDrive
- Redondance ADSL/4G pour garantir une continuité minimum

---

### 🔍 Contexte 3 : PME avec infrastructure vieillissante

#### Données du contexte :

- Infrastructure interne : 40 VMs, 5 To, sauvegardes sur bande
- Disponibilité élevée requise
- Envisage une montée en charge

#### Analyse :

- Coût d’un IaaS élevé à long terme (stockage + performance)
- Besoin de redondance, mais contrôle fort sur l’infrastructure

#### Solution proposée :

✅ **Cloud privé avec extension vers un cloud public pour la scalabilité**

- Serveurs en hyperconvergence (ex : Synology, TrueNAS, VMware vSAN)
- Archivage Cloud (Azure Blob / Amazon S3) pour les snapshots mensuels
- Déploiement progressif d’Office 365 et Azure AD Connect

---

## 🛠️ TP 2 – Création complète d’un tenant Microsoft 365 avec domaine personnalisé

### 1. Achat d’un nom de domaine chez un registrar

- Se connecter sur [https://www.ovh.com/auth](https://www.ovh.com/auth)
- Rechercher un domaine pas cher en `.xyz`, `.online`, `.tech`, etc.
- Créer un compte ou se connecter avec un existant
- Choisir **mode de renouvellement manuel**, pour éviter les paiements automatiques
- Finaliser le paiement et accéder au **manager OVH > Domaines**

### 2. Création du tenant Microsoft 365 (version d’essai)

- Se rendre sur : [https://www.microsoft.com/fr-fr/microsoft-365/try](https://www.microsoft.com/fr-fr/microsoft-365/try)
- Choisir une offre d’essai (Microsoft 365 Business Basic / E3 Trial)
- Renseigner les informations de contact, entreprise fictive si besoin
- Créer un compte admin :
    - Nom d’utilisateur : `admin@nivvlem.onmicrosoft.com`
    - Mot de passe fort à sauvegarder
- Valider via **code SMS** envoyé sur un numéro jetable

### 3. Lier le domaine personnalisé au tenant

- Aller dans **Centre d’administration Microsoft 365 > Paramètres > Domaines**
- Cliquer sur **Ajouter un domaine** > Saisir le domaine OVH
- Choisir méthode de vérification : **enregistrement TXT** recommandé
- Dans OVH :
    - Aller dans **Domaines > Zone DNS**
    - Ajouter un champ TXT :

```txt
Nom : @
Type : TXT
Valeur : MS=xxxxxxxxx
```

- Attendre quelques minutes, puis cliquer sur **Vérifier** côté Microsoft

### 4. Nettoyage de la zone DNS OVH

- Supprimer tout champ **MX**, **A**, **CNAME** inutile par défaut (hors champ de vérification)

### 5. Ajout des enregistrements DNS nécessaires à Microsoft 365

- Enregistrements essentiels :

```txt
MX       domaine.tld → priorité 0 → nom Microsoft
TXT      domaine.tld → v=spf1 include:spf.protection.outlook.com -all
CNAME    autodiscover → autodiscover.outlook.com
CNAME    sip, lyncdiscover → pour Teams/Skype Entreprise (optionnel)
```

- Copier-coller exactement les valeurs indiquées par Microsoft

### 6. Création d’un utilisateur et test de la messagerie

- **Centre d’admin > Utilisateurs actifs > Ajouter un utilisateur**
    - Nom d’utilisateur : `test@domaine.tld`
    - Licence : attribuer une licence d’essai (Microsoft 365 E3)
- Modifier l’alias principal (UPN) si nécessaire
- Se connecter à Outlook Web : [https://outlook.office365.com](https://outlook.office365.com/)
- Envoyer un mail vers une adresse personnelle (ex : Gmail)
- Vérifier la réception et l’envoi

---

## ✅ À retenir pour les révisions

- Adapter une solution Cloud, c’est **analyser besoins, risques et budgets**
- Microsoft 365 impose une **configuration DNS rigoureuse**
- Un **tenant trial** est utilisable gratuitement pendant 30 jours avec toutes les fonctions

---

## 📌 Bonnes pratiques professionnelles

- Toujours **centraliser les accès et identifiants** utilisés (tenant, registrar, utilisateurs)
- Capturer les **écrans clés** (TXT, MX, validation) pour preuve de configuration
- Vérifier la **délivrabilité SMTP** avec des outils en ligne (Mail Tester, MXToolbox)
- Nommer clairement les utilisateurs et domaines (pas d’abréviations obscures)
- Prévoir un plan d’**escalade** en cas d’échec de validation DNS
- Nettoyer les enregistrements DNS inutiles ou redondants pour éviter les erreurs de routage
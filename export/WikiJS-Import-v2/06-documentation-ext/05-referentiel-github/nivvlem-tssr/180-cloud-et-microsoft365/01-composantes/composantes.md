---
title: "Les composantes du Cloud et de Microsoft 365"
description: "- Le Cloud désigne la mise à disposition de ressources informatiques à la demande via Internet"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Les composantes du Cloud et de Microsoft 365
## ☁️ Qu’est-ce que le Cloud ?

- Le Cloud désigne la mise à disposition de ressources informatiques **à la demande via Internet**
- Avantages :
    - Accès à des ressources performantes sans gestion matérielle
    - Facturation à l’usage → **visibilité budgétaire**
    - Disponibilité, sécurité, redondance des datacenters
- Inconvénients / limites :
    - **Dépendance à l’Internet**
    - **Localisation des données** (RGPD, HDS…)
    - Confidentialité, souveraineté des données

---

## 📊 Le modèle SPI : SaaS / PaaS / IaaS

### SaaS – Software as a Service

- Utilisation directe d’une application hébergée (ex : Teams, Gmail, Outlook Web)
- Avantages : simplicité, évolutivité, pas d’admin locale
- Inconvénients : dépendance éditeur, peu de contrôle

### PaaS – Platform as a Service

- Mise à disposition d’environnements pour déployer ses apps (OS, base de données…)
- Ex : Azure App Services, Google App Engine

### IaaS – Infrastructure as a Service

- Accès à des VM, stockage, réseau (ex : Azure VM, AWS EC2)
- Administration complète possible (sauf physique)

---

## 🌐 Types de Cloud

|Type|Description|
|---|---|
|**Public**|Mutualisé, extensible, opéré par un tiers (Azure, AWS…)|
|**Privé**|Dédié à une seule entité (interne ou hébergé dans un datacenter)|
|**Hybride**|Combinaison local + Cloud (ex : AD local + Azure AD)|

### Disponibilité selon niveau de datacenter

|Tier|Taux de dispo|Interruption max/an|
|---|---|---|
|Tier 1|99.67 %|~28 h|
|Tier 4|99.995 %|~26 min|

---

## 🏢 Hébergement interne vs Cloud

### On-premise

- Avantages : maîtrise, personnalisation, pas de redevance mensuelle
- Inconvénients : matériel à gérer, sécurité physique, obsolescence

### Cloud

- Avantages : évolutivité, redondance, peu de maintenance
- Inconvénients : dépendance réseau, coûts sur la durée, maîtrise réduite

### Choix selon critères :

- Criticité ?
- Budget / GTR ligne internet ?
- Données sensibles ?
- Compétences internes ?

---

## 🧩 Microsoft 365 : écosystème et licences

### Principaux services inclus

- **Exchange Online** (messagerie)
- **Teams** (collaboration, visioconférence)
- **SharePoint Online** (intranet, GED)
- **OneDrive** (stockage personnel)
- **Azure AD** (annuaire cloud)

### Licences disponibles

|Type|Exemples|
|---|---|
|Particuliers|Famille, Personnel|
|Education|A1, A3, A5|
|Associations|E1, E3, E5 dédiés|
|PME|Business Basic, Premium|
|Entreprises|E3, E5|
|Terrain|F3|

---

## 📬 Messagerie : composants techniques

### Architecture

- **MUA** : Mail User Agent (client Outlook, Gmail…)
- **MSA** : Mail Submission Agent (soumet le mail à un MTA)
- **MTA** : Mail Transfer Agent (serveur SMTP)
- **MDA** : Mail Delivery Agent (stocke les mails dans les boîtes)

### Protocoles

- Envoi : SMTP (via MSA et MTA)
- Réception : POP3, IMAP4, ActiveSync, MAPI, HTTPS

---

## 🌐 DNS et enregistrement pour la messagerie

|Type|Rôle|
|---|---|
|**SOA**|Start of Authority de la zone DNS|
|**NS**|Nom(s) du/des serveurs DNS autoritaires|
|**A/AAAA**|Résolution de nom en IPv4 / IPv6|
|**SRV**|Services spécifiques (LDAP, SIP…)|
|**MX**|Serveur de messagerie (réception)|
|**SPF**|Envoi autorisé depuis des IPs données (anti-spam)|

---

## 🏗️ Création d’un Tenant Microsoft 365

### Étapes

1. Sélectionner un plan d’essai ou payant
2. Créer un identifiant : `exemple@nom.onmicrosoft.com`
3. Ajouter un domaine personnalisé si nécessaire (`@entreprise.fr`)
4. Vérifier la propriété via **enregistrement TXT** dans la zone DNS
5. Ajouter les enregistrements DNS nécessaires (MX, SPF, CNAME…)
6. Tester l’envoi et la réception

### Hébergement DNS externe

- Fournisseur DNS externe → publier enregistrements recommandés

---

## ✅ À retenir pour les révisions

- Le Cloud se décline en **SaaS, PaaS, IaaS**, et peut être **public, privé ou hybride**
- Microsoft 365 regroupe des services collaboratifs avec **différents niveaux de licences**
- Le fonctionnement d’une messagerie repose sur des agents : MUA, MSA, MTA, MDA
- Les **enregistrements DNS** (MX, SPF…) sont essentiels au bon acheminement des mails
- Créer un **tenant 365** permet de tester toute la plateforme (Exchange, Teams…)

---

## 📌 Bonnes pratiques professionnelles

- Choisir la **bonne offre cloud** en fonction du besoin réel (et pas du marketing)
- Toujours configurer les **enregistrements DNS de sécurité** (SPF, DKIM, DMARC)
- Conserver les **informations de propriété du domaine** (accès au registrar)
- Tester la **messagerie interne et externe** dès l’intégration DNS
- Documenter la **topologie M365 et DNS**, les enregistrements créés et la stratégie d’accès
- Utiliser les **outils de diagnostic Microsoft** pour tester les flux SMTP et les redirections DNS
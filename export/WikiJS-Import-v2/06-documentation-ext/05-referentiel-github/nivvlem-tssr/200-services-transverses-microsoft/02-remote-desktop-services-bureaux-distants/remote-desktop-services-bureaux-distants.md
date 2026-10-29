---
title: "Remote Desktop Services (RDS) - Bureaux distants"
description: "- Permet de virtualiser un bureau Windows sur un serveur centralisé"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Remote Desktop Services (RDS) - Bureaux distants
## 🧩 Principe de fonctionnement

### RDS (anciennement TSE)

- Permet de **virtualiser un bureau Windows** sur un serveur centralisé
- Les utilisateurs accèdent à un **environnement distant** via RDP (Remote Desktop Protocol)

### Architecture typique

```text
Client RDP → Serveur RDS → Applications + Bureau Windows
```

### Fonctionnement du protocole RDP

- **Affichage** déporté vers le client (peu de bande passante)
- **Clavier / souris** remontés vers le serveur
- Impressions et disques clients peuvent être redirigés

---

## ✅ Avantages et inconvénients

### Avantages

- Mutualisation des ressources matérielles (moins de postes lourds)
- Centralisation des mises à jour / maintenance
- Moindre consommation de bande passante (vs. VDI complet)
- Accès possible depuis l’extérieur (VPN, Gateway RDS)

### Inconvénients

- Montée en charge : nécessite **dimensionnement précis**
- Coût de licences CAL RDS
- Nécessite des clients compatibles RDP
- Expérience utilisateur un peu différente du poste classique

---

## 🛠️ Services apportés par RDS

|Service|Description|
|---|---|
|Bureau distant|Session complète Windows déportée|
|Publication d’applications|Application unique affichée sur le poste client|
|Gestion centralisée|GPO, profils itinérants|
|Redirection de périphériques|Imprimantes, disques, ports COM, audio|

---

## 📊 Principales solutions du marché

|Solution|Type|
|---|---|
|Microsoft RDS|Intégré aux Windows Server|
|Citrix Virtual Apps|Tiers, plus avancé (payant)|
|VMware Horizon|Solution VDI complète|
|Parallels RAS|Alternative économique|

---

## 🔍 Réflexion préalable à l'installation

### Points clés à évaluer

- **Nombre d’utilisateurs simultanés**
- Types d’applications → consommation CPU/RAM
- Redondance (NLB, plusieurs hôtes RDS)
- Sécurité (accès RDP direct ou via Gateway VPN)
- Stockage des **profils utilisateurs** (FSLogix, profils itinérants, UPD)
- Licences CAL RDS nécessaires (User CAL ou Device CAL)

---

## 🏛️ Services de rôle RDS

|Service|Rôle|
|---|---|
|RD Session Host (RD SH)|Héberge les sessions utilisateurs (obligatoire)|
|RD Connection Broker|Répartition de charge + réaffectation des sessions|
|RD Licensing|Gestion des licences CAL RDS|
|RD Gateway|Accès RDS sécurisé depuis Internet|
|RD Web Access|Portail Web d’accès aux applications|

---

## ⚙️ Installation du rôle RDS

### Méthodes

- Via **Server Manager** (Assistant Gestion des rôles)
- Via **PowerShell** (plus automatisable)

### Commande PowerShell

```powershell
# Installation du rôle RDS Session Host
Install-WindowsFeature -Name RDS-RD-Server -IncludeAllSubFeature -IncludeManagementTools
```

### Points d’attention

- Nécessite un **serveur membre du domaine** (sauf Gateway autonome)
- RD Licensing obligatoire après 120j de période de grâce

---

## 🛠️ Outils de gestion du service

|Outil|Usage|
|---|---|
|Server Manager|Gestion centralisée des rôles RDS|
|Remote Desktop Services Manager|Gestion des sessions en cours|
|PowerShell RDS|Automatisation et supervision avancée|
|GPO|Gestion fine des restrictions et profils|

---

## 🗂️ Création d'une collection

### Qu’est-ce qu’une collection ?

- Ensemble logique regroupant :
    - les serveurs **RD Session Host**
    - les **applications publiées**
    - les **paramètres utilisateurs**

### Processus

1️⃣ Créer une nouvelle collection via **Server Manager**  
2️⃣ Ajouter les serveurs **RD Session Host**  
3️⃣ Ajouter les **applications distantes** (si usage RemoteApp)

### Bonnes pratiques

- **1 collection = 1 type d’usage** (bureaux / RemoteApp)
- Ne pas mélanger usage lourd et léger dans la même collection

---

## 💻 Client d’accès

### Clients compatibles

- Client **Remote Desktop** (Windows, Linux, Mac)
- Application mobile officielle (Android/iOS)
- Accès via **RD Web Access** (HTML5)

### Configuration typique

```text
Adresse : rdp://nom_du_serveur_ou_gateway
Options : redirection imprimantes, disques, audio, presse-papiers
```

---

## 🔄 Gestion des connexions

### Points clés

- **Restriction des connexions simultanées**
- Politique de **timeout** des sessions inactives
- Limitation de la **redirection de périphériques**
- Surveillance de la charge CPU / RAM sur les serveurs RDS

### GPO utiles

```text
Ordinateur > Stratégies > Modèles d'administration > Composants Windows > Services Bureau à distance
```

- Limiter la durée des sessions actives
- Déconnexion des sessions inactives
- Redirection des périphériques

---

## ✅ À retenir pour les révisions

- RDS permet une **centralisation** des postes de travail et applications
- Le protocole **RDP** permet un accès léger mais efficace
- La **réflexion préalable** est essentielle pour un déploiement réussi
- Il existe plusieurs **rôles** dans une architecture RDS complète
- Les **collections** structurent les usages par type d’application
- La sécurité passe par l’usage d’une **Gateway** + VPN + GPO restrictives

---

## 📌 Bonnes pratiques professionnelles

- Ne jamais exposer directement un port RDP sur Internet → utiliser une **Gateway**
- Toujours **chiffrer les communications RDP** (TLS activé par défaut)
- Mettre en place des **GPO adaptées** pour contrôler l’environnement RDS
- Planifier la **redondance** pour la haute disponibilité (N+1 minimum)
- Superviser la **santé des serveurs** et des sessions
- Vérifier la **conformité des licences** RDS (CAL utilisateurs ou devices)
- Tester régulièrement la **qualité de l’expérience utilisateur** (latence, compatibilité applis)
- Mettre à jour régulièrement les **clients RDP**
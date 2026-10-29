---
title: "🛡️ TP - Configuration du NAT sur pfSense"
description: "1️⃣ Depuis votre machine physique ou depuis une VM sur le réseau Bridge :"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# 🛡️ TP - Configuration du NAT sur pfSense

## 🏗️ Étape 1 — Préparation de l’infrastructure

### 🔸 1.1 — Connexion au Routeur Formateur

1️⃣ Depuis votre machine physique ou depuis une VM sur le réseau **Bridge** :

- Accédez à : http://192.168.150.100
- Identifiants :
    - Login : `stag`
    - Password : `stag`

2️⃣ Ajouter **des routes statiques** pour vos réseaux privés sur ce routeur :

- Objectif : permettre au Routeur Formateur de **joindre vos réseaux internes**.
- Ici :
    - `192.168.150.100/24` → Gateway : **votre IP WAN pfSense**.


3️⃣ Tester la **connexion Internet** depuis vos machines internes (Clients et Serveurs) pour vérifier que la route est bien prise en compte.

---

## 🔐 Étape 2 — Configuration du NAT sur pfSense

### 🔸 2.1 — Mise à jour des règles sur l’interface WAN

1️⃣ Aller dans pfSense → menu **Firewall > Rules > WAN**.  
2️⃣ **Recréer ou vérifier les règles** du TP1 sur l'interface WAN.

- Objectif : protéger les flux entrants.
- Exemple :
    - Bloquer tout sauf les flux explicitement autorisés.

---

### 🔸 2.2 — Création d’un **Alias** pour SRV-MBR

1️⃣ Aller dans pfSense → **Firewall > Aliases** → **Add**.  
2️⃣ Créer un **Alias de type "Host(s)"** :

- Nom : `SRV-MBR`
- IP : `172.20.200.128`

3️⃣ Enregistrer l’alias.

- Objectif : faciliter la maintenance des règles NAT en cas de changement d’IP.

---

### 🔸 2.3 — Configuration de la redirection NAT (Port Forward)

Objectif : permettre **l’accès distant en RDP** (Remote Desktop Protocol) à SRV-MBR depuis l’extérieur.

1️⃣ Aller dans **Firewall > NAT > Port Forward**.  
2️⃣ Ajouter une nouvelle règle :

- **Interface** : WAN
- **Protocol** : TCP
- **Destination port range** : `3389` (RDP)
- **Redirect target IP** : utiliser l’Alias `SRV-MBR`
- **Redirect target port** : `3389`
- **Description** : `RDP vers SRV-MBR`

3️⃣ Cocher l’option **"Add associated filter rule"** (pour générer automatiquement une règle Firewall WAN correspondante).

4️⃣ **Appliquer les modifications**.

---

## 🖥️ Étape 3 — Configuration du SRV-MBR

### 🔸 3.1 — Activation du bureau à distance

1️⃣ Sur `SRV-MBR`, ouvrir **Paramètres Système > Bureau à distance**.  
2️⃣ Activer le **Remote Desktop**.  
3️⃣ Autoriser uniquement les membres du groupe **GG-IT**.  
4️⃣ Vérifier que les utilisateurs GG-IT peuvent se connecter en RDP.

---

## 🧪 Étape 4 — Tests d’accès distant

### 🔸 4.1 — Mise en place du client de test

Option 1️⃣ : depuis un **poste binôme externe**.  
Option 2️⃣ : depuis la VM **CLT-NAT** (fournie dans `CLT-NAT.ovf`).

Procédure pour CLT-NAT :

1️⃣ Importer la VM `CLT-NAT.ovf`.  
2️⃣ Modifier l’adresse IP selon le fichier de configuration fourni.  
3️⃣ Identifiants :

- ID : `stag`
- Password : `P@ssw0rd`

---

### 🔸 4.2 — Test de la connexion RDP

1️⃣ Depuis le client externe (CLT-NAT ou autre PC du réseau formateur) :

- Lancer un **client RDP** (mstsc sous Windows).
- Cibler l’**IP WAN** de votre pfSense (adresse publique / fournie par le Routeur Formateur).
- Port utilisé : `3389`.

2️⃣ Se connecter avec un compte membre du groupe **GG-IT**.

---

## ✅ Bonnes pratiques

- **Utiliser des Aliases** pour faciliter la gestion des règles NAT.
- Ne pas laisser des règles NAT permanentes si non nécessaires.
- Protéger l’accès RDP :
    - Par **ACL IP** (plages autorisées).
    - Par **VPN** en amont (meilleure pratique pro).
- Toujours **activer les logs** sur les règles WAN/NAT.

---

## ⚠️ Pièges courants à éviter

- Oublier d’ajouter la route statique sur le Routeur Formateur → NAT ne fonctionnera pas.
- Ne pas tester la connectivité avant de configurer le NAT.
- Laisser un NAT ouvert sur RDP → **risque énorme en prod !**
- Mal associer les règles WAN → accès refusé.
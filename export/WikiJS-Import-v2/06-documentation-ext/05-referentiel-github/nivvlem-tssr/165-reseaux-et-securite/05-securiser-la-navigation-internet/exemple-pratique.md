---
title: "🛡️ TP - Sécuriser la navigation Internet via un proxy et un portail captif"
description: "1️⃣ Se connecter à l’interface web de pfSense."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# 🛡️ TP - Sécuriser la navigation Internet via un proxy et un portail captif
## 🛠️ Étape 1 — Paramétrage de Squid (Proxy)

### 🔸 1.1 — Activation de Squid

1️⃣ Se connecter à l’interface web de pfSense.  
2️⃣ Aller dans **Services > Squid Proxy Server**.

---

### 🔸 1.2 — Onglet "General"

✅ Cochez **"Enable Squid Proxy"**.  
✅ Interface : sélectionner **LANCLIENT** (ou **LAN** selon votre config).  
✅ Port : `3128`.  
✅ (Optionnel) **Transparent HTTP Proxy** : cocher si vous souhaitez rediriger automatiquement le trafic HTTP.

👉 En mode transparent, les navigateurs n’ont pas besoin de configuration manuelle.

---

### 🔸 1.3 — Onglet "Local Cache"

✅ **Hard Disk Cache Size** : mettre par exemple `1024` Mo (ou plus).  
✅ Cliquer sur **Save**.

---

### 🔸 1.4 — Onglet "ACLs"

✅ Ajouter votre réseau client dans les réseaux autorisés :

- Exemple : `172.20.200.0/24` ou `172.20.200.0/25`.

✅ Bloquer un domaine : exemple : **openai.com**.

---

### 🔸 1.5 — Règle de pare-feu pour rediriger le trafic HTTP (si mode transparent)

1️⃣ Aller dans **Firewall > Rules > LAN**.  
2️⃣ Ajouter une règle :

|Champ|Valeur|
|---|---|
|Action|Pass|
|Interface|LAN|
|Protocol|TCP|
|Source|LAN net|
|Destination|any|
|Destination port|HTTP (port 80)|
|Redirect target IP|127.0.0.1|
|Redirect target port|3128|

---

### 🔸 1.6 — Installation du certificat CA

1️⃣ Télécharger le **certificat CA-TP5** fourni.  
2️⃣ L’installer manuellement sur les clients Windows / navigateurs.

👉 Ceci permet d’éviter les erreurs HTTPS sur les sites filtrés.

---

### 🔸 1.7 — Configuration des navigateurs (si non transparent)

- Si vous n’utilisez PAS le mode transparent :
    - Aller dans les navigateurs clients.
    - Paramétrer le proxy HTTP/HTTPS → IP pfSense (LAN) → Port `3128`.

---

## 🛠️ Étape 2 — Paramétrage de SquidGuard (Filtrage web avancé)

### 🔸 2.1 — Activation de SquidGuard

1️⃣ Aller dans **Services > Proxy Filter**.

---

### 🔸 2.2 — Onglet "General settings"

✅ Cochez **"Enable"**.  
✅ Choisir une **Blacklist** (ici : UT Capitole : https://dsi.ut-capitole.fr/blacklists/).

👉 **Télécharger et importer la blacklist** dans pfSense.

---

### 🔸 2.3 — Onglet "Common ACL"

✅ Créer une règle pour bloquer des catégories :

- Adultes
- Gaming
- Astrology
- Etc.

✅ Créer votre propre liste "MyfirstBlackList" et y ajouter des domaines personnalisés.

---

### 🔸 2.4 — Intégration SquidGuard → Squid

1️⃣ Aller dans **Services > Squid Proxy Server > General**.  
2️⃣ **Redirect Program** : `/usr/local/bin/squidGuard`.

👉 Ceci permet d’interconnecter Squid et SquidGuard.

---

### 🔸 2.5 — Tests de filtrage

✅ Depuis un client Windows :

|Type de site|Résultat attendu|
|---|---|
|Site autorisé|OK|
|Site bloqué (catégorie blacklistée)|Blocage avec message de SquidGuard|

---

### 🔸 2.6 — Vérification des logs

1️⃣ Aller dans **Status > Proxy Filter**.  
2️⃣ Consulter les logs :

- Tentatives de navigation bloquées.
- Sites visités.

---

## 🛠️ Étape 3 — Mise en place d’un portail captif (bonus)
### 🔸 3.1 — Activation du portail captif

1️⃣ Aller dans **Services > Captive Portal**.  
2️⃣ Cliquer sur **Add** → Créer une zone : `LAN_Portal`.  
3️⃣ Cochez **Enable captive portal**.  
4️⃣ Sélectionnez l’interface **LAN**.

---

### 🔸 3.2 — Paramétrage du portail

|Option|Valeur|
|---|---|
|Session timeout|ex: 60 minutes|
|Reauthenticate connected users every minute|Enable|
|Idle timeout|ex: 15 minutes|
|Enable logout popup window|Enable|

---

### 🔸 3.3 — Personnalisation

✅ Modifier le contenu de la page :

- Ajouter un logo.
- Message de bienvenue.

---

### 🔸 3.4 — Authentification

1️⃣ Méthode recommandée : **Local User Manager**.  
2️⃣ Créer quelques utilisateurs de test :

- Aller dans **System > User Manager**.

---

### 🔸 3.5 — Règles de pare-feu associées

1️⃣ Aller dans **Firewall > Rules > LAN**.  
2️⃣ Vérifier qu’il existe une règle permettant le trafic vers le portail captif.

---

### 🔸 3.6 — Tests

✅ Depuis un client Linux/Windows :

|Étape|Résultat attendu|
|---|---|
|Ouvrir un navigateur|Affichage du portail captif|
|Authentification|Demande d’identifiants|
|Navigation Internet après login|OK|

---

## ✅ Bonnes pratiques

- **Filtrage par proxy** est préférable à un simple filtrage DNS.
- Toujours utiliser un **certificat valide** pour l’inspection HTTPS.
- **Journaliser** toutes les tentatives de navigation.
- Limiter l’exposition du proxy → ne pas le rendre accessible depuis l’extérieur.
- **Portail captif** → utile pour les réseaux "visiteurs".

---

## ⚠️ Pièges courants à éviter

- Ne pas oublier d’installer le **certificat CA** sur les clients → sinon erreurs HTTPS.
- Attention à la **position des règles de pare-feu**.
- Ne pas autoriser le trafic direct HTTP/HTTPS sans passer par le proxy.
- Vérifier que les règles LAN ne contournent pas le portail captif.
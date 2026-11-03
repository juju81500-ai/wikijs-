---
title: "🛡️ TP - Services hébergés dans une DMZ"
description: "1️⃣ Importer le bundle SRV-WEB.ovf ou SRV-Apache.ova fourni."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# 🛡️ TP - Services hébergés dans une DMZ
## 🏗️ Étape 1 — Installation du serveur WEB en DMZ

### 🔸 1.1 — Déploiement de la VM

1️⃣ Importer le bundle `SRV-WEB.ovf` ou `SRV-Apache.ova` fourni.  
2️⃣ Configurer la VM sur le réseau **VMnet12** (DMZ).  
3️⃣ Attribuer à la VM :

- **Adresse IP** : 172.20.200.192/26

---

### 🔸 1.2 — Configuration du serveur

1️⃣ Se connecter en root (mot de passe `P@ssw0rd`).  
2️⃣ Modifier les fichiers suivants :

- `/etc/hosts` : ajouter les noms d’hôte et IP de votre infrastructure.
- `/etc/resolv.conf` : configurer le serveur DNS pointant vers `SRV-CD`.  
    3️⃣ Vérifier la **résolution DNS** depuis le serveur WEB.

---

## 🛠️ Étape 2 — Enregistrement DNS du service

### 🔸 2.1 — Création d’un enregistrement DNS interne

1️⃣ Sur `SRV-CD` :

- Ouvrir le gestionnaire DNS.  
    2️⃣ Exécuter le script fourni :
- `D:/scripts/AddDnsZone.ps1` ou `Script-TP3-AddDnsZone.ps1`.  
    3️⃣ Ajouter un enregistrement pour :
- `extra.nivvlem.eni` pointant vers l’IP du serveur WEB.

### 🔸 2.2 — Vérification

- Depuis un client Windows interne :
    - Résolution DNS de `extra.nivvlem.eni`.
    - Ping ou navigation vers `https://extra.nivvlem.eni`.

---

## 🔐 Étape 3 — Configuration de la publication du service via pfSense

---

### 🔸 3.1 — Création d’un alias URL (optionnel)

1️⃣ Aller dans : `Firewall > Aliases`.  
2️⃣ Créer un alias :

- Type : **Host(s)**.
- Nom : `WEB-EXTRA`.
- IP : 172.20.200.192

---

### 🔸 3.2 — Création de la redirection NAT

1️⃣ Aller dans : `Firewall > NAT > Port Forward`.  
2️⃣ Ajouter une règle NAT :

- **Interface** : WAN.
- **Protocol** : TCP.
- **Destination Port Range** : `443` (HTTPS).
- **Redirect Target IP** : `WEB-EXTRA` (ou directement l'IP du serveur WEB).
- **Redirect Target Port** : `443`.
- **Description** : `HTTPS vers WEB DMZ`.

3️⃣ Cocher **"Add associated filter rule"**.

---

### 🔸 3.3 — Vérification des règles de pare-feu WAN

1️⃣ Aller dans : `Firewall > Rules > WAN`.  
2️⃣ Vérifier qu’une règle "Pass" existe pour le port `443` vers `WAN address`.  
3️⃣ Bloquer tous les autres flux non nécessaires (principe de moindre privilège).

---

## 🧪 Étape 4 — Tests d’accès au service Web

---

### 🔸 4.1 — Depuis l’extérieur (Routeur Formateur ou CLT-NAT)

1️⃣ Depuis votre machine physique OU depuis `CLT-NAT` :

- Naviguer vers : `https://192.168.150.100`.  
    2️⃣ Le serveur WEB de la DMZ doit répondre.

---

### 🔸 4.2 — Depuis le réseau interne

1️⃣ Depuis un **client Windows** interne :

- Naviguer vers : `https://extra.nivvlem.eni`.  
    2️⃣ Vérifier que le **FQDN interne** fonctionne correctement.

---

## ✅ Bonnes pratiques

- Toujours **séparer** la DMZ du LAN interne.
- Appliquer le **principe de moindre privilège** sur les flux :
    - DMZ → LAN : strictement interdit (sauf réponses).
    - WAN → DMZ : uniquement les ports nécessaires (ex : 443).
- **Journaliser** les tentatives d’accès sur le WAN.
- Ne pas exposer de services superflus en DMZ.
- Garder la DMZ **indépendante du domaine AD** si possible (dans un contexte réel).

---

## ⚠️ Pièges courants à éviter

- Ne pas oublier de vérifier :
    - Résolution DNS interne.
    - Résolution externe (vers l’IP WAN).
    - Configuration correcte de la **passerelle** sur le serveur WEB.
- Ne pas exposer **tout le port 80 + 443** si le site n’utilise que HTTPS.
- Oublier de **sécuriser les flux WAN** (ne pas autoriser `ANY` vers DMZ).
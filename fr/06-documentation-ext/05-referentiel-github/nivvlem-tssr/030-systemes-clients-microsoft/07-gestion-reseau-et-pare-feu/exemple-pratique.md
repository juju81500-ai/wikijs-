---
title: "TP – Gestion du réseau et du pare-feu sous Windows"
description: "- Dans VMware Workstation : clic droit sur la VM > Settings > Network Adapter > Bridged"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Gestion du réseau et du pare-feu sous Windows

## 🖧 1. Configuration IP statique

### 🔹 Connexion au réseau Bridged

- Dans **VMware Workstation** : clic droit sur la VM > Settings > Network Adapter > **Bridged**

### 🔹 Récupération des paramètres réseau du Campus

```cmd
ipconfig /all
```

- **Adresse réseau** : même réseau que la machine physique (ici : `172.28.0.0/16`)
- **Passerelle** et **DNS préféré** : identiques à la VM Campus

### 🔹 Construction de l'adresse IP fixe

- Basée sur les lettres de mon **prénom** et **nom** (rang alphabétique)
    - Ici, M = 13, D = 4 → IP = `172.28.13.4`
- **Masque** : `255.255.0.0`

### 🔹 Application

```bash
ncpa.cpl → Ethernet0 → Propriétés
→ TCP/IPv4 → Utiliser l'adresse IP suivante
```

- Adresse IP : `172.28.13.4`
- Masque : `255.255.0.0`
- Passerelle : `172.28.0.254`
- DNS préféré : `172.28.0.4`

---

## 🌐 2. Tests de connectivité

### 🔹 Commandes utilisées

```bash
ping
tracert 
```

### 🔹 Cibles de test

|Cible|Résultat attendu|Niveau réseau|
|---|---|---|
|Passerelle (ex: .254)|Réponse ICMP immédiate|Réseau local|
|VM Discovery|Réponse directe, sur le même réseau|Réseau local|
|[www.facebook.com](http://www.facebook.com)|Réponse via routeurs multiples|Réseau Internet|

> Le `tracert` vers Facebook montre les **sauts (hops)** intermédiaires

---

## 🔍 3. Résolution DNS avec `nslookup`

### 🔹 Cibles

```cmd
nslookup www.hadopi.fr
nslookup www.amendes.gouv.fr
nslookup www.facebook.com
```

### 🔹 Résultats observés (exemple)

|Domaine|Adresse IPv4 obtenue|
|---|---|
|[www.hadopi.fr](http://www.hadopi.fr)|`217.115.114.160`|
|[www.amendes.gouv.fr](http://www.amendes.gouv.fr)|`90.102.115.80`|
|[www.facebook.com](http://www.facebook.com)|`185.60.216.35`|

> 🔎 Le serveur DNS interrogé est `172.28.0.4`, hébergeant `dceel.ad.campus-eni.fr`

---

## 🔒 4. Gestion du pare-feu Windows

### 🔹 Vérification des profils actifs

```bash
firewall.cpl
```

- Profil actif : Privé ou Public selon la détection du réseau

### 🔹 Autoriser une application spécifique (GUI)

```bash
Pare-feu > Autoriser une application
→ Activer **Bureau à distance** uniquement pour le **profil privé**
```

### 🔹 Autoriser les pings entrants (ICMP)

```bash
wf.msc
→ Règles de trafic entrant
→ "Partage de fichiers et d’imprimantes (Demande d’écho – ICMPv4)"
→ Activer la règle pour le bon profil (Privé ou Public)
```

### 🔹 Test final

- Depuis la **VM Discovery**, faire un `ping` vers Win10-XX
- La communication doit fonctionner si les règles ICMP sont activées correctement

---

## ✅ Vérifications

|Élément|Validation|
|---|---|
|Adresse IP fixe configurée|Visible via `ipconfig`|
|Ping de la passerelle|Fonctionnel|
|Ping de VM Discovery|Fonctionnel|
|Résolution DNS|Réponses obtenues via `nslookup`|
|Ping d’un site distant|Fonctionnel (sauts multiples en `tracert`)|
|Bureau à distance (profil privé)|Activé uniquement dans profil privé|
|ICMP entrant autorisé|Vérifié dans `wf.msc`|

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Conserver une **documentation IP**|Facilite les dépannages et évite les doublons|
|Tester systématiquement via `ping`/`tracert`|Diagnostiquer les niveaux réseau concernés|
|Sécuriser le pare-feu selon les profils|Ne jamais exposer trop d’ouvertures en Public|
|Utiliser `wf.msc` plutôt que GUI simple|Permet un contrôle précis (ports, programmes, profils)|
|Préférer les IP dynamiques en prod|Pour une gestion centralisée via DHCP|
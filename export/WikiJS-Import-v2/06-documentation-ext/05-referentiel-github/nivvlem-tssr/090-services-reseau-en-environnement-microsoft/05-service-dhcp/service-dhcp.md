---
title: "Le service DHCP"
description: "DHCP = Dynamic Host Configuration Protocol"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Le service DHCP

## 📡 Qu’est-ce que le DHCP ?

DHCP = **Dynamic Host Configuration Protocol**

- Permet à un poste client d’obtenir automatiquement une **adresse IP**, un **masque**, une **passerelle** et des **options supplémentaires** (DNS, suffixe DNS…)

### 🔁 Le cycle DORA (processus de bail DHCP)

1. **D**iscover : le client cherche un serveur DHCP (broadcast)
2. **O**ffer : le serveur propose une IP
3. **R**equest : le client demande l’adresse offerte
4. **A**ck : le serveur confirme et envoie la config complète

> 📦 Le bail contient l’IP, la durée d’utilisation, les options et la MAC du client

---

## 🛠️ Installation et configuration du serveur DHCP

### 🔹 GUI (via Server Manager)

- `Gérer > Ajouter des rôles et fonctionnalités`
- Rôle : **DHCP Server**, puis finaliser la configuration (autorisation dans l’AD)

### 🔹 PowerShell

```powershell
Install-WindowsFeature -Name DHCP -IncludeManagementTools
Add-DhcpServerInDC -DnsName "srvdhcp.monentreprise.local" -IpAddress 192.168.1.1
```

---

## 📦 Configuration d’une étendue (scope)

### 📐 Étendue = plage d’adresses à attribuer

```powershell
Add-DhcpServerv4Scope -Name "LAN_Serveurs" -StartRange 192.168.1.50 -EndRange 192.168.1.200 -SubnetMask 255.255.255.0 -LeaseDuration ([TimeSpan]::FromDays(2))
```

### 🛑 Exclusion (plage réservée aux IP statiques)

```powershell
Add-DhcpServerv4ExclusionRange -ScopeId 192.168.1.0 -StartRange 192.168.1.100 -EndRange 192.168.1.110
```

### 📌 Réservations

```powershell
Add-DhcpServerv4Reservation -ScopeId 192.168.1.0 -IPAddress 192.168.1.5 -ClientId "00-15-5D-6E-6E-03" -Description "SRVFIC"
```

---

## 🧩 Configuration des options DHCP

### 🔹 Exemples d’options :

|Code|Nom|Description|
|---|---|---|
|003|Routeur|Passerelle par défaut|
|006|DNS Servers|Adresse(s) IP du/des DNS|
|015|DNS Domain Name|Suffixe DNS|

### 🔹 Application possible :

- Au niveau du **serveur** → tous les scopes
- Au niveau de l’**étendue**
- Au niveau d’une **réservation** (prioritaire)

> 🧪 Vérifier avec : `ipconfig /renew` puis `ipconfig /all` sur le client

---

## 🔀 Fractionnement d’étendue (Split-scope)

Permet de répartir une étendue sur **deux serveurs DHCP**, avec exclusion croisée

- Ex : 192.168.1.0/24
    - SRV1 gère .50 à .150 (80%)
    - SRV2 gère .151 à .200 (20%)

### 🔹 GUI : clic droit sur l’étendue > Advanced > Split-scope

### 🔹 Activer l’étendue sur le second serveur après synchronisation

> ⚠️ Les modifications ne sont **pas synchronisées automatiquement** entre serveurs

---

## 🔄 Gestion, audit et dépannage

### 🔹 Autorisation dans l’AD

```powershell
Add-DhcpServerInDC -DnsName "SRV-DHCP" -IpAddress 192.168.1.1
```

### 🔹 Fichiers de logs

- `C:\Windows\System32\dhcp\` → 1 fichier .log par jour
- Journal d’événements Windows : Source = `DHCP-Server`

### 🔹 Sauvegarde et restauration

```powershell
Backup-DhcpServer -Path "C:\BackupDHCP"
Restore-DhcpServer -Path "C:\BackupDHCP" -Force
```

---

## 🧠 À retenir pour les révisions

- Le DHCP simplifie la gestion des IP mais nécessite **structure et rigueur**
- Le **cycle DORA** est la base de tout échange client-serveur DHCP
- L’**étendue** doit être correctement planifiée : plage, exclusions, réservations
- Les **options** enrichissent la configuration IP
- Le **fractionnement d’étendue** apporte une tolérance de panne simple

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Toujours exclure les IP statiques|Évite les conflits d’adressage|
|Réserver les IP critiques|Associer MAC/IP fixe pour serveurs, imprimantes…|
|Surveiller les journaux DHCP|Anticiper les erreurs de saturation ou conflits|
|Sauvegarder la configuration régulièrement|Garantir la reprise rapide en cas de panne|
|Sécuriser le DHCP (filtrage MAC, AD)|Limiter les attributions non autorisées|
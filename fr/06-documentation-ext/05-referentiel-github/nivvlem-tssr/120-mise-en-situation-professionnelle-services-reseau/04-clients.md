---
title: "Mise en situation professionnelle : Services réseau"
description: "Dans cette étape, nous allons déployer deux postes clients (Windows 10 et Debian GUI) sur le réseau LAN Clients (192.168.52.0/24). Ils serviront à tester la connectivité, les résolutions DNS, l’accès au domaine Active Directory et les partages de fichiers."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Mise en situation professionnelle : Services réseau

## Clients

## 🚀 Ajout et configuration des postes clients

Dans cette étape, nous allons déployer deux postes clients (Windows 10 et Debian GUI) sur le réseau **LAN Clients (192.168.52.0/24)**. Ils serviront à tester la connectivité, les résolutions DNS, l’accès au domaine Active Directory et les partages de fichiers.

---

## 📁 Clients à déployer

|Nom de la machine|OS|Adresse IP|Rôle(s)|VMNet|
|---|---|---|---|---|
|CLT-WIN-MD|Windows 10 Pro|192.168.52.10|Tests AD, GPO, partage|VMNet3|
|CLT-LNX-MD|Debian GUI|192.168.52.1|Tests DNS, DHCP, navigation|VMNet3|

> Convention : `CLT-<OS>-MD`

---

## 🔧 Création des VMs

### Caractéristiques recommandées

- **Windows 10** : 2 vCPU, 2 Go RAM, 40 Go disque
- **Debian GUI** : 2 vCPU, 2 Go RAM, 20 Go disque
- **Réseau** : VMNet3 (LAN Clients)

> Utilisation des images "sysprep" pour accélérer la déploiement.

---

## 🔌 Configuration réseau des clients

> Pour le moment, l’adressage est **statique** en attendant le déploiement du DHCP.

### Windows 10 (CLT-WIN-MD)

1. **Panneau de configuration > Centre Réseau et partage**.
2. **Modifier les paramètres de la carte**.
3. Interface Ethernet > **Propriétés**.
4. **Protocole Internet version 4 (TCP/IPv4)**.
5. **Utiliser l’adresse IP suivante** :
    - IP : `192.168.52.10`
    - Masque : `255.255.255.0`
    - Passerelle : `192.168.52.254`
    - DNS : `192.168.52.254` (pfSense)
6. OK > Fermer.

### Debian GUI (CLT-LNX-MD)

1. Connexion en root.
2. Fichier `/etc/network/interfaces` :

```bash
auto ens33
iface ens33 inet static
  address 192.168.52.1
  netmask 255.255.255.0
  gateway 192.168.52.254
  dns-nameservers 192.168.52.254
```

3. Redémarrage du service :

```bash
sudo systemctl restart networking
```

---

## 🚧 Vérifications

### Depuis les clients

- `ping 192.168.52.254` (pfSense)
- `ping 192.168.55.101` (AD) ou `.102` (SVC)

### Depuis pfSense

- **Diagnostics > Ping**
- Test vers `192.168.52.10` et `192.168.52.1`

### Pare-feu Windows

- Sur le client Windows, autoriser temporairement les ping (ICMP) :

```powershell
netsh advfirewall firewall add rule name="ICMP Allow" protocol=icmpv4:8,any dir=in action=allow
```

---

## ⚖️ Bonnes pratiques

- Toujours commencer avec une config IP **statique et documentée**
- Valider les communications entre clients et serveurs avant déploiement DHCP / DNS / AD
- Nommer les VMs de manière cohérente et explicite

---

## 📄 Synthèse

|Client|Adresse IP|OS|Objectifs de test|
|---|---|---|---|
|CLT-WIN-MD|192.168.52.10|Windows 10 Pro|AD, GPO, partage|
|CLT-LNX-MD|192.168.52.1|Debian GUI|DNS, navigation, dépôts|
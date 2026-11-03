---
title: "TP – Paramétrage d’un serveur OpenVPN pour les clients nomades"
description: "Mettre en place une infrastructure VPN nomade sécurisée avec pfSense et OpenVPN, permettant à un utilisateur distant de se connecter au réseau interne de l’entreprise via un paquet client exporté, une authentification LDAP, et des certificats générés localement."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Paramétrage d’un serveur OpenVPN pour les clients nomades

## 🧠 Objectif

Mettre en place une **infrastructure VPN nomade sécurisée** avec pfSense et OpenVPN, permettant à un utilisateur distant de se connecter au réseau interne de l’entreprise via un **paquet client exporté**, une **authentification LDAP**, et des **certificats générés localement**.

---

## 🧾 Environnement de travail

- Routeur : `pfSense` (interface WAN + LAN)
- Contrôleur de domaine : `AD-DNS` (LDAP, DNS)
- Client distant : poste Windows déplacé sur réseau WAN (en mode **bridged**)

---

## 🔐 Étapes de configuration VPN nomade OpenVPN avec pfSense

### 1. Création de l’autorité de certification (AC) sur pfSense

- Aller dans **System > Cert. Manager > CAs**
- Cliquer sur **Add**
    - CA Name : `VPN-CA`
    - Method : `Create internal Certificate Authority`
    - Key Length : 2048 ou 4096 bits
    - Digest Algorithm : SHA256 ou SHA512
    - Remplir les champs d’identité (CN = VPN-CA, pays, etc.)

### 2. Création du certificat serveur OpenVPN

- Aller dans **System > Cert. Manager > Certificates**
- Cliquer sur **Add/Sign**
    - Certificate type : Server Certificate
    - Associated CA : `VPN-CA`
    - Common Name : `openvpn.nivvlem.md`

### 3. Ajout de l’authentification LDAP (Active Directory)

- Aller dans **System > User Manager > Authentication Servers** > Add
- Type : LDAP
- Hostname/IP : `192.168.159.121`
- Port : 389
- Transport : TCP – Standard
- Base DN : `dc=nivvlem,dc=md`
- Authentication containers : `CN=Users,DC=nivvlem,DC=md`
- Bind Credentials : compte AD avec droits de lecture (ex: `ldapbind@nivvlem.md`)
- Test via : **Diagnostics > Authentication**

### 4. Configuration DNS dans pfSense

- Aller dans **System > General Setup**
    - Domain : `nivvlem.md`
    - DNS Server : `192.168.159.121`
    - Décocher : "Allow DNS override"

### 5. Assistant OpenVPN

- Aller dans **VPN > OpenVPN > Wizards**
- Backend Authentication : `LDAP`
- Choose CA : `VPN-CA`
- Server Certificate : `openvpn.nivvlem.md`
- Interface : `WAN`
- Protocol : UDP ou TCP
- Tunnel Network : `10.0.8.0/24`
- Local Network : `192.168.159.0/24`
- Enable Redirect Gateway
- DNS : IP AD-DNS (et WINS si souhaité)
- Firewall Rules : cocher "Add a firewall rule to allow traffic"

### 6. Installer le paquet `openvpn-client-export`

- **System > Package Manager > Available Packages** > Rechercher `openvpn-client-export`
- Installer

### 7. Génération du profil client

- **VPN > OpenVPN > Client Export**
- Sélectionner un utilisateur LDAP valide
- Format : `Windows Installer (.exe)`
- Télécharger l’installateur

---

## 💻 Configuration du poste client nomade

### 1. Modifier la carte réseau du client Windows

- Mettre en mode **bridged** (VMware/VirtualBox)
- Configurer en **DHCP automatique**
- Vérifier qu’une IP publique est attribuée et que le client ne peut plus ping le LAN

### 2. Installer le paquet OpenVPN exporté

- Exécuter l’installateur `.exe`
- Lancer OpenVPN GUI en mode administrateur
- Se connecter avec un compte LDAP valide

### 3. Vérifications de connectivité

- `ping 192.168.159.126` (interface LAN pfSense)
- `ping 192.168.159.121` (AD)
- `nslookup wwi.nivvlem.md` → doit résoudre grâce au DNS interne
- `http://wwi.nivvlem.md` dans navigateur = accès au serveur IIS

---

## 🔥 Paramétrage du pare-feu

### Règle interface WAN

- Autoriser le port choisi (1194 UDP ou TCP) vers pfSense WAN

### Règle interface OpenVPN

- Autoriser tous les paquets (test)
- En production : restreindre aux IP / services nécessaires uniquement

---

## ✅ À retenir pour les révisions

- Un **client distant connecté via VPN** agit comme s’il était local
- OpenVPN + pfSense + LDAP = solution robuste, gratuite, interopérable
- L’utilisation de l’assistant et du paquet `openvpn-client-export` simplifie le déploiement

---

## 📌 Bonnes pratiques professionnelles

- Toujours **tester l’authentification LDAP** avant de lancer l’assistant OpenVPN
- Restreindre les **groupes AD autorisés** à utiliser le VPN
- Séparer les **règles de pare-feu WAN / OpenVPN**
- Documenter chaque certificat, configuration VPN et règles appliquées
- Prévoir un **système d’alerte ou de supervision** des connexions VPN
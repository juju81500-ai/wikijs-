---
title: "VM_Win11_Reseau_Fixer-IP-PowerShell"
description: "Fixer une adresse IP statique, la passerelle et les serveurs DNS sur un poste client Windows 11 via PowerShell, puis sécuriser la pile réseau client."
published: true
date: 2026-10-29T19:28:52Z
tags: ["[windows-11]", "[windows-client]", "[powershell]", "[ip-statique]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T19:28:52Z
dateModified: 2026-10-29T19:28:52Z
---

# 📄 VM_Win11_Reseau_Fixer-IP-PowerShell.md

- **Environnement** : VM / Poste client (Windows 11)
- **OS / Version** : Windows 11 - Famille Windows Client
- **Catégorie** : Réseau / Configuration IP
- **Tags** : `[windows-11]`, `[windows-client]`, `[powershell]`, `[ip-statique]`, `[hardening]`

## 🎯 Problème précis à résoudre
Fixer une adresse IP statique, la passerelle et les serveurs DNS sur un poste client Windows 11 via PowerShell, puis sécuriser la pile réseau client.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identification de l'index de la carte réseau :
   `Get-NetAdapter`
   👉 Explication : Affiche la liste des interfaces réseau physiques et virtuelles.
2. Assignation rapide d'une adresse IP statique et passerelle :
   `New-NetIPAddress -InterfaceIndex 12 -IPAddress 192.168.1.150 -PrefixLength 24 -DefaultGateway 192.168.1.1`
   👉 Explication : Applique l'IP 192.168.1.150/24 et la passerelle par défaut sur l'interface ciblée.
3. Configuration du serveur DNS local :
   `Set-DnsClientServerAddress -InterfaceIndex 12 -ServerAddresses ("192.168.1.10")`
   👉 Explication : Définit le serveur DNS primaire pour la résolution de noms.

**Équivalent interface graphique :**

- **Win + R** > `ncpa.cpl` > clic droit sur la carte > **Propriétés > Protocole Internet version 4 (TCP/IPv4) > Propriétés**, cocher **Utiliser l'adresse IP suivante** et saisir IP, masque, passerelle, DNS, puis **OK**.
  👉 Explication : équivalent de `New-NetIPAddress` et `Set-DnsClientServerAddress`; adapter les valeurs d'exemple.

## ⚡ 2. Production — Façon Simplifiée
1. Modification d'une configuration existante de DHCP vers Statique :
   `Set-NetIPInterface -InterfaceIndex 12 -Dhcp Disabled`
   👉 Explication : Désactive le client DHCP sur la carte réseau client.
2. Application simultanée de l'IP et des serveurs DNS principal et secondaire :
   `New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.1.150 -PrefixLength 24 -DefaultGateway 192.168.1.1`
   `Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses ("192.168.1.10", "192.168.1.11")`
   👉 Explication : Configure de manière permanente l'adressage IP et la tolérance de panne DNS.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Désactivation des protocoles d'authentification et de résolution obsolètes (LLMNR / NetBIOS / mDNS) :
   `Disable-NetAdapterBinding -Name "Ethernet" -ComponentID ms_tcpip6`
   👉 Explication : Bloque IPv6 non utilisé et désactive la résolution mDNS pour éviter le spoofing de nom sur le LAN.
2. Activation de DNS-over-HTTPS (DoH) sur Windows 11 :
   `Set-DNSClientDohServerAddress -ServerAddress "192.168.1.10" -DohTemplate "https://dns.lab.local/dns-query" -AllowFallbackToUdp $false`
   👉 Explication : Force le chiffrement HTTPS des requêtes DNS transmises par le poste client.
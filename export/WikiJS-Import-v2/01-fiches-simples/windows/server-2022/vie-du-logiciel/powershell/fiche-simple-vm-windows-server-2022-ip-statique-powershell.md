---
title: "VM_WinSrv_2022_Reseau_Fixer-IP-PowerShell"
description: "Fixer une adresse IP statique, configurer les serveurs DNS et sécuriser la carte réseau sur Windows Server 2022 en ligne de commande PowerShell."
published: true
date: 2026-10-29T19:29:06Z
tags: ["[winsrv2022]", "[windows-server]", "[reseau]", "[ip-statique]", "[powershell]", "[firewall-windows]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T19:29:06Z
dateModified: 2026-10-29T19:29:06Z
---

# 📄 VM_WinSrv_2022_Reseau_Fixer-IP-PowerShell.md

- **Environnement** : VM (Hyper-V / Proxmox VE / VMware)
- **OS / Version** : Windows Server 2022 Datacenter / Standard - Famille Windows
- **Catégorie** : Réseau
- **Tags** : `[winsrv2022]`, `[windows-server]`, `[reseau]`, `[ip-statique]`, `[powershell]`, `[firewall-windows]`, `[hardening]`

## 🎯 Problème précis à résoudre
Fixer une adresse IP statique, configurer les serveurs DNS et sécuriser la carte réseau sur Windows Server 2022 en ligne de commande PowerShell.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identification de l'index de la carte réseau :
   `Get-NetAdapter | Select-Object Name, InterfaceIndex, Status`
   👉 Explication : Affiche les cartes réseau présentes et repère le numéro d'index (ex: InterfaceIndex 12) correspondant à la carte à modifier.
2. Configuration rapide de l'IP et de la passerelle :
   `New-NetIPAddress -InterfaceIndex 12 -IPAddress 192.168.1.50 -PrefixLength 24 -DefaultGateway 192.168.1.1`
   👉 Explication : Assigne immédiatement l'adresse 192.168.1.50/24 et la passerelle 192.168.1.1 sur l'interface ciblée.
3. Test instantané de connectivité :
   `Test-NetConnection -ComputerName 192.168.1.1`
   👉 Explication : Vérifie la réponse ICMP (Ping) vers la passerelle.

**Équivalent interface graphique :**

- **Gestionnaire de serveur > Serveur local > Ethernet**, ou **Win + R** > `ncpa.cpl` > clic droit sur la carte > **Propriétés > Protocole Internet version 4 (TCP/IPv4) > Propriétés**, saisir IP, masque, passerelle et DNS, **OK**.
  👉 Explication : équivalent de `New-NetIPAddress`; adapter les valeurs d'exemple.

## ⚡ 2. Production — Façon Simplifiée
1. Attribution persistante de l'IP statique :
   `New-NetIPAddress -InterfaceAlias "Ethernet0" -IPAddress 192.168.1.50 -PrefixLength 24 -DefaultGateway 192.168.1.1`
   👉 Explication : Enregistre définitivement la configuration IPv4 sur la carte réseau nommée "Ethernet0".
2. Définition des serveurs DNS primaires et secondaires :
   `Set-DnsClientServerAddress -InterfaceAlias "Ethernet0" -ServerAddresses ("192.168.1.10", "192.168.1.1")`
   👉 Explication : Configure les adresses des résolveurs DNS d'entreprise pour la carte.
3. Validation du statut réseau :
   `Get-NetIPConfiguration -InterfaceAlias "Ethernet0"`
   👉 Explication : Affiche le récapitulatif complet de la pile IP/DNS configurée.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Désactivation de la résolution de noms NetBIOS sur TCP/IP :
   `Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Services\NetBT\Parameters\Interfaces\Tcpip_*' -Name NetbiosOptions -Value 2`
   👉 Explication : Bloque les attaques par empoisonnement de nom NetBIOS/LLMNR sur le réseau local.
2. Désactivation de l'autoconfiguration IPv6 et du Router Discovery :
   `Set-NetIPInterface -InterfaceAlias "Ethernet0" -AddressFamily IPv6 -RouterDiscovery Disabled`
   👉 Explication : Empêche l'injection de fausses routes IPv6 (Rogue Router Advertisements).
3. Verrouillage du profil réseau sur "DomainAuthenticated" ou "Private" :
   `Set-NetConnectionProfile -InterfaceAlias "Ethernet0" -NetworkCategory Private`
   👉 Explication : Empêche le système de classifier le réseau en profil "Public" restrictif ou non supervisé.
4. Activation des règles de pare-feu réseau restreintes :
   `New-NetFirewallRule -Name "Block-External-Subnet" -DisplayName "Blocage Sous-Réseaux Inconnus" -Direction Inbound -Action Block -RemoteAddress "10.0.0.0/8"`
   👉 Explication : Verrouille les flux entrants aux seuls sous-réseaux d'administration autorisés.
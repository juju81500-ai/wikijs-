---
title: "VM_WinSrv_2022_Reseau_Fixer-IP-Et-DNS"
description: "Fixer une adresse IP statique, définir la passerelle par défaut, configurer les serveurs DNS préférés et auxiliaires, et vider le cache DNS sous Windows Server 2022 via l'interface graphique (GUI) pas-à-pas ou la ligne de commande PowerShell."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[winsrv2022]", "[windows-server]", "[reseau]", "[ip-statique]", "[dns]", "[gui]", "[powershell]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_WinSrv_2022_Reseau_Fixer-IP-Et-DNS.md

- **Environnement** : VM (Hyper-V / Proxmox VE / VSphere)
- **OS / Version** : Windows Server 2022 Standard / Datacenter - Famille Windows
- **Catégorie** : Réseau / Adressage IP & DNS
- **Tags** : `[winsrv2022]`, `[windows-server]`, `[reseau]`, `[ip-statique]`, `[dns]`, `[gui]`, `[powershell]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Fixer une adresse IP statique, définir la passerelle par défaut, configurer les serveurs DNS préférés et auxiliaires, et vider le cache DNS sous Windows Server 2022 via l'interface graphique (GUI) pas-à-pas ou la ligne de commande PowerShell.

---

## 🖥️ Méthode Interface Graphique (GUI Pas-à-Pas - "Clic-Clic")
Avant de modifier une carte à distance, prévoir un accès console ou un moyen de retour arrière : le changement d'IP peut couper la session. Vérifier également que l'adresse choisie est libre ou réservée dans le plan DHCP.

1. **Ouvrir la fenêtre des connexions réseau** :
   - Appuyer sur la combinaison de touches `Win + R` du clavier pour ouvrir la boîte de dialogue *Exécuter*.
   - Saisir `ncpa.cpl` puis appuyer sur `Entrée` (ou cliquer sur *OK*).
   - 👉 *Explication : Ouvre directement le panneau de configuration des cartes réseau.*

2. **Accéder aux propriétés de la carte réseau** :
   - Faire un **clic droit** sur l'interface réseau active (ex: *Ethernet0* ou *Connexion au réseau local*).
   - Cliquer sur **Propriétés**.
   - 👉 *Explication : Affiche la liste des composants et protocoles réseau installés.*

3. **Saisir les paramètres IP et DNS** :
   - Sélectionner **Protocole Internet version 4 (TCP/IPv4)** puis cliquer sur le bouton **Propriétés**.
   - Cocher le bouton radio **Utiliser l'adresse IP suivante :**
     - *Adresse IP* : `192.168.1.50`
     - *Masque de sous-réseau* : `255.255.255.0`
     - *Passerelle par défaut* : `192.168.1.1`
   - Cocher le bouton radio **Utiliser l'adresse de serveur DNS suivante :**
     - *Serveur DNS préféré* : `192.168.1.10` (Adresse de votre serveur DNS / Contrôleur AD)
   - *Serveur DNS auxiliaire* : laisser vide ou saisir un autre DNS interne AD si disponible.
   - Cliquer sur **OK** puis sur **Fermer**.
   - 👉 *Explication : Enregistre et applique immédiatement la configuration IP fixe sur la carte.*

   Pour une machine jointe au domaine, ne pas configurer un DNS public (par exemple `1.1.1.1`) comme DNS auxiliaire : les requêtes Active Directory pourraient lui être envoyées. Configurer les redirecteurs Internet sur le serveur DNS AD.

4. **Vider le cache DNS local via l'invite de commande** :
   - Appuyer sur `Win + R`, saisir `cmd` et appuyer sur `Entrée`.
   - Saisir la commande `ipconfig /flushdns` puis appuyer sur `Entrée`.
   - 👉 *Explication : Purge la mémoire cache du résolveur DNS pour forcer la prise en compte immédiate des nouveaux serveurs DNS.*

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. **Assignation d'une IP statique temporaire** :
   ```powershell
   New-NetIPAddress -InterfaceAlias "Ethernet0" -IPAddress 192.168.1.50 -PrefixLength 24 -DefaultGateway 192.168.1.1
   ```
   👉 *Explication : Tu fais ça, ça applique l'adresse IP 192.168.1.50 et la passerelle immédiatement sur la carte.*

2. **Configuration du serveur DNS principal** :
   ```powershell
   Set-DnsClientServerAddress -InterfaceAlias "Ethernet0" -ServerAddresses ("192.168.1.10")
   ```
   👉 *Explication : Tu définis l'adresse IP du serveur de résolution DNS.*

---

## ⚡ 2. Production — Façon Simplifiée
1. **Désactivation du DHCP et fixation de l'IP permanente** :
   ```powershell
   Set-NetIPInterface -InterfaceAlias "Ethernet0" -Dhcp Disabled
   New-NetIPAddress -InterfaceAlias "Ethernet0" -IPAddress 192.168.1.50 -PrefixLength 24 -DefaultGateway 192.168.1.1
   ```
   👉 *Explication : Tu désactives l'obtention automatique d'adresse et tu lies l'IP fixe à la carte réseau.*

2. **Configuration du DNS interne** :
   ```powershell
   Set-DnsClientServerAddress -InterfaceAlias "Ethernet0" -ServerAddresses ("192.168.1.10")
   ```
   👉 *Explication : Tu configures le DNS interne AD. Pour une machine membre du domaine, ne pas ajouter de DNS public; configurer les redirecteurs Internet sur le DNS AD.*

3. **Nettoyage du cache DNS local** :
   ```powershell
   Clear-DnsClientCache
   ```
   👉 *Explication : Tu effaces la mémoire cache DNS de la machine.*

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. **Désactivation de la résolution de noms vulnérable NetBIOS et LLMNR** :
   ```powershell
   Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Services\NetBT\Parameters\Interfaces\Tcpip_*' -Name NetbiosOptions -Value 2
   ```
   👉 *Explication : Tu coupes le protocole NetBIOS pour empêcher l'usurpation de noms sur le réseau local.*

2. **Désactivation de l'IPv6 Router Discovery (anti-Rogue RA)** :
   ```powershell
   Set-NetIPInterface -InterfaceAlias "Ethernet0" -AddressFamily IPv6 -RouterDiscovery Disabled
   ```
   👉 *Explication : Tu empêches l'injection de fausses routes réseau via IPv6.*
# 📄 VM_WinSrv_2022_Reseau_Fixer-IP-Et-DNS.md

- **Environnement** : VM (Hyper-V / Proxmox VE / VSphere)
- **OS / Version** : Windows Server 2022 Standard / Datacenter - Famille Windows
- **Catégorie** : Réseau / Adressage IP & DNS

---

## 🎯 Problème précis à résoudre
Fixer une adresse IP statique, configurer la passerelle et les serveurs DNS sous Windows Server 2022 en utilisant l'interface graphique (GUI) pas-à-pas ou la ligne de commande PowerShell.

---

## 🖥️ Méthode Interface Graphique (GUI Pas-à-Pas - "Clic-Clic")
Avant de modifier une carte à distance, prévoir un accès console ou un moyen de retour arrière : le changement d'IP peut couper la session. Vérifier également que l'adresse choisie est libre ou réservée dans le plan DHCP.

1. **Ouvrir la fenêtre des connexions réseau** :
   - Appuyer sur les touches `Win + R` du clavier pour ouvrir la boîte de dialogue *Exécuter*.
   - Taper `ncpa.cpl` puis appuyer sur `Entrée` (ou cliquer sur *OK*).
   - 👉 *Explication : Cela ouvre directement la fenêtre du Panneau de configuration "Connexions réseau".*

2. **Accéder aux propriétés de la carte réseau** :
   - Faire un **clic droit** sur l'interface réseau (ex: *Ethernet0*).
   - Cliquer sur **Propriétés**.
   - 👉 *Explication : Affiche la liste des protocoles et services rattachés à la carte.*

3. **Configurer IPv4 et le serveur DNS** :
   - Dans la liste, cliquer une fois sur **Protocole Internet version 4 (TCP/IPv4)**.
   - Cliquer sur le bouton **Propriétés** en bas à droite (ou double-cliquer sur la ligne).
   - Cocher l'option : **Utiliser l'adresse IP suivante :**
     - *Adresse IP* : `192.168.1.50`
     - *Masque de sous-réseau* : `255.255.255.0`
     - *Passerelle par défaut* : `192.168.1.1`
   - Cocher l'option : **Utiliser l'adresse de serveur DNS suivante :**
     - *Serveur DNS préféré* : `192.168.1.10` (Adresse du serveur DNS local/AD)
   - *Serveur DNS auxiliaire* : laisser vide ou saisir un autre DNS interne AD si disponible.
   - Cliquer sur **OK**, puis sur **Fermer**.
   - 👉 *Explication : Applique et enregistre immédiatement l'adresse IP et les serveurs DNS de manière permanente.*

   Pour une machine jointe au domaine, ne pas configurer un DNS public (par exemple `1.1.1.1`) comme DNS auxiliaire : les requêtes Active Directory pourraient lui être envoyées. Configurer les redirecteurs Internet sur le serveur DNS AD.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. **Assignation rapide d'IP temporaire via PowerShell** :
   ```powershell
   New-NetIPAddress -InterfaceIndex 12 -IPAddress 192.168.1.50 -PrefixLength 24 -DefaultGateway 192.168.1.1
   ```
   👉 *Explication : Tu fais ça, ça applique l'adresse IP et la passerelle immédiatement sur la carte.*
2. **Définition du serveur DNS** :
   ```powershell
   Set-DnsClientServerAddress -InterfaceIndex 12 -ServerAddresses ("192.168.1.10")
   ```
   👉 *Explication : Tu indiques l'adresse IP du résolveur DNS.*

---

## ⚡ 2. Production — Façon Simplifiée
1. **Désactivation du DHCP et fixation de l'IP sur la carte nommée Ethernet0** :
   ```powershell
   Set-NetIPInterface -InterfaceAlias "Ethernet0" -Dhcp Disabled
   New-NetIPAddress -InterfaceAlias "Ethernet0" -IPAddress 192.168.1.50 -PrefixLength 24 -DefaultGateway 192.168.1.1
   ```
   👉 *Explication : Tu coupes l'obtention automatique d'IP et tu fixes l'adresse IP statique de production.*
2. **Configuration du DNS interne** :
   ```powershell
   Set-DnsClientServerAddress -InterfaceAlias "Ethernet0" -ServerAddresses ("192.168.1.10")
   ```
   👉 *Explication : Tu configures le DNS interne AD. Pour une machine membre du domaine, ne pas ajouter de DNS public; configurer les redirecteurs Internet sur le DNS AD.*
3. **Vider le cache DNS local** :
   ```cmd
   ipconfig /flushdns
   ```
   👉 *Explication : Tu effaces les anciennes résolutions mémoire du serveur.*

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. **Désactivation des protocoles d'usurpation réseau (NetBIOS / LLMNR)** :
   ```powershell
   Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Services\NetBT\Parameters\Interfaces\Tcpip_*' -Name NetbiosOptions -Value 2
   ```
   👉 *Explication : Tu bloques l'empoisonnement de noms NetBIOS sur le LAN d'entreprise.*
2. **Désactivation de l'autoconfiguration IPv6 Router Discovery** :
   ```powershell
   Set-NetIPInterface -InterfaceAlias "Ethernet0" -AddressFamily IPv6 -RouterDiscovery Disabled
   ```
   👉 *Explication : Tu protèges la machine contre les injections de fausses routes IPv6 (Rogue RA).*
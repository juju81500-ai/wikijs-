---
title: "VM_Win11_Reseau_Fixer-IP-Et-DNS"
description: "Fixer l'adresse IP statique et changer les serveurs DNS sous Windows 11 via la nouvelle interface Paramètres, le classique ncpa.cpl, ou en ligne de commande PowerShell."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-11]", "[windows-client]", "[reseau]", "[ip-statique]", "[dns]", "[gui]", "[powershell]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Win11_Reseau_Fixer-IP-Et-DNS.md

- **Environnement** : VM / Poste client (Windows 11)
- **OS / Version** : Windows 11 Pro / Enterprise - Famille Windows Client
- **Catégorie** : Réseau / Configuration Client
- **Tags** : `[windows-11]`, `[windows-client]`, `[reseau]`, `[ip-statique]`, `[dns]`, `[gui]`, `[powershell]`

---

## 🎯 Problème précis à résoudre
Fixer l'adresse IP statique et changer les serveurs DNS sous Windows 11 via la nouvelle interface Paramètres, le classique `ncpa.cpl`, ou en ligne de commande PowerShell.

---

## 🖥️ Méthode Interface Graphique (GUI Pas-à-Pas)
Avant de modifier une carte à distance, prévoir un accès local ou un moyen de retour arrière. Vérifier que l'adresse IP choisie est libre ou réservée dans le plan DHCP.

### Option A : Via les Paramètres Windows 11 (Nouvelle interface)
1. **Ouvrir les Paramètres Réseau** :
   - Faire un **clic droit** sur le bouton Démarrer (ou raccourci `Win + I`).
   - Cliquer sur **Réseau et Internet**.
   - Cliquer sur **Ethernet** (ou *Wi-Fi*).
2. **Modifier l'attribution d'IP et de DNS** :
   - En face de *Attribution de l'adresse IP*, cliquer sur le bouton **Modifier**.
   - Dans le menu déroulant, passer de *Automatique (DHCP)* à **Manuel**.
   - Activer le commutateur **IPv4**.
   - Saisir les informations :
     - *Adresse IP* : `192.168.1.150`
     - *Masque de sous-réseau* : `255.255.255.0` (ou `24`)
     - *Passerelle* : `192.168.1.1`
   - Cliquer sur **Enregistrer**.

2. **Configurer le DNS** :
    - Dans la page **Ethernet** ou **Wi-Fi**, repérer *Attribution du serveur DNS* et cliquer sur **Modifier**.
    - Choisir **Manuel**, activer **IPv4**, saisir le DNS préféré `192.168.1.10` puis, si disponible, un second DNS interne AD.
    - Cliquer sur **Enregistrer**.
    - Pour un poste joint au domaine, ne pas saisir de DNS public en secours : configurer les redirecteurs Internet sur le DNS AD. Un poste hors domaine peut utiliser les DNS prévus par la politique réseau.

### Option B : Via la commande classique `ncpa.cpl`
1. Appuyer sur `Win + R`, taper `ncpa.cpl` et valider avec `Entrée`.
2. Clic droit sur la carte **Ethernet** -> **Propriétés**.
3. Double-cliquer sur **Protocole Internet version 4 (TCP/IPv4)**.
4. Cocher *Utiliser l'adresse IP suivante* et saisir l'IP, le Masque et la Passerelle.
5. Cocher *Utiliser l'adresse de serveur DNS suivante* et saisir les DNS internes AD si le poste est joint au domaine.
6. Cliquer sur **OK**.

---

## ⚡ Méthode Ligne de commande PowerShell
1. **Fixer l'IP statique et le DNS** :
   ```powershell
   New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.1.150 -PrefixLength 24 -DefaultGateway 192.168.1.1
   Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses ("192.168.1.10")
   ```
   👉 *Explication : Tu appliques l'adressage et le DNS AD. Pour un poste hors domaine, adapter le DNS à la politique réseau.*
2. **Vider le cache DNS local** :
   ```powershell
   Clear-DnsClientCache
   ```
   👉 *Explication : Tu effaces les anciennes entrées DNS gardées en mémoire.*
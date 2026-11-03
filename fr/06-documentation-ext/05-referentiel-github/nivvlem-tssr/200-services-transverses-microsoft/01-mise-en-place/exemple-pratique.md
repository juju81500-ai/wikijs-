---
title: "TP - Mise en œuvre Active Directory"
description: "Réseau : Host-Only (VMware Workstation)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP - Mise en œuvre Active Directory
## 🏗️ Architecture cible

| Nom VM | OS                  | RAM    | IP statique      | DNS                     |
| ------ | ------------------- | ------ | ---------------- | ----------------------- |
| INFRA  | Windows Server 2019 | 2048MB | 192.168.13.1 /24 | 192.168.13.1            |
| RDS    | Windows Server 2019 | 2048MB | 192.168.13.2 /24 | 192.168.13.1            |
| DEPLOY | Windows Server 2019 | 2048MB | 192.168.13.3 /24 | 192.168.13.1            |
| Cli10  | Windows 10          | 1024MB | DHCP             | 192.168.13.1 (via DHCP) |
| CliNvx | Windows 10 (vide)   | 1024MB | Pas d’OS         | -                       |

**Réseau : Host-Only (VMware Workstation)**  
**Pas de gateway par défaut**.

---

## ⚙️ Étapes de mise en œuvre

### 1️⃣ Création des VM

- Créer les 5 VMs (via VMware Workstation)
- Installer les OS (ou utiliser les bases fournies)
- **CliNvx** : VM de type "Windows 10 x64", sans système.

---

### 2️⃣ Configuration réseau

#### INFRA

```
IP : 192.168.13.1
Masque : 255.255.255.0
Passerelle : (vide)
DNS : 192.168.13.1
```

#### RDS

```
IP : 192.168.13.2
Masque : 255.255.255.0
Passerelle : (vide)
DNS : 192.168.13.1
```

#### DEPLOY

```
IP : 192.168.13.3
Masque : 255.255.255.0
Passerelle : (vide)
DNS : 192.168.13.1
```

#### Cli10

```
DHCP activé (IP obtenue dans la plage)
DNS reçu via DHCP : 192.168.13.1
```

---

### 3️⃣ Activation ICMP (ping)

Sur chaque machine Windows :

```powershell
Enable-NetFirewallRule -DisplayGroup "File and Printer Sharing"
```

Tester via :

```powershell
ping 192.168.13.1
ping 192.168.13.2
ping 192.168.13.3
```

---

### 4️⃣ Installation des rôles sur INFRA

#### Installation des rôles :

```powershell
Install-WindowsFeature AD-Domain-Services, DNS, DHCP -IncludeManagementTools
```

---

### 5️⃣ Promotion en contrôleur de domaine

#### Domaine : `nivvlem.tssr.eni`

Via PowerShell :

```powershell
Install-ADDSForest -DomainName "nivvlem.tssr.eni" -InstallDNS
```

---

### 6️⃣ Configuration DHCP

#### Création du scope :

```powershell
Add-DhcpServerv4Scope -Name "Scope_13" -StartRange 192.168.13.100 -EndRange 192.168.13.199 -SubnetMask 255.255.255.0
```

#### Configuration des options :

```powershell
Set-DhcpServerv4OptionValue -DnsServer 192.168.13.1 -DnsDomain "nivvlem.tssr.eni"
```

#### Autoriser le serveur DHCP :

```powershell
Add-DhcpServerInDC -DnsName "nivvlem.tssr.eni" -IPAddress 192.168.13.1
```

---

### 7️⃣ Intégration des machines

#### Cli10 :

```powershell
Add-Computer -DomainName "nivvlem.tssr.eni" -Restart
```

Vérifier que **Cli10** a bien reçu :  
- Une IP entre `.100` et `.199`  
- DNS correct : `192.168.13.1`

#### RDS et DEPLOY :

Configurer IPs fixes puis :

```powershell
Add-Computer -DomainName "nivvlem.tssr.eni" -Restart
```

---

### 8️⃣ Création des OU, utilisateurs et groupes

#### Structure :

```
OU=Direction
OU=Pédagogique
OU=Informatique
```

#### Commandes PowerShell :

**Créer les OU :**

```powershell
New-ADOrganizationalUnit -Name "Direction" -Path "DC=nivvlem,DC=tssr,DC=eni"
New-ADOrganizationalUnit -Name "Pédagogique" -Path "DC=nivvlem,DC=tssr,DC=eni"
New-ADOrganizationalUnit -Name "Informatique" -Path "DC=nivvlem,DC=tssr,DC=eni"
```

**Créer un utilisateur :**

```powershell
New-ADUser -Name "Estelle" -GivenName "Estelle" -Surname "Durand" -SamAccountName "estelle" -UserPrincipalName "estelle@nivvlem.tssr.eni" -Path "OU=Direction,DC=nivvlem,DC=tssr,DC=eni" -AccountPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force) -Enabled $true
```

---

### 9️⃣ Snapshot

- Prendre un snapshot de **chaque VM** : `Atelier 1 OK`

---

## 📌 Bonnes pratiques

- Toujours configurer les DNS **en premier**
- Vérifier que tous les serveurs ont le bon DNS avant l’intégration
- Nommer les OU correctement
- Documenter les comptes et groupes
- Sauvegarder les snapshots **hors production**
- Vérifier que DHCP ne génère pas de conflits
- **Tester la réplication DNS** sur toutes les machines

---

## ⚠️ Pièges à éviter

- DNS mal configuré → impossible d’intégrer au domaine  
- Pare-feu bloquant les pings → fausse impression de non-connectivité  
- DHCP non autorisé → clients sans IP  
- Mauvais mot de passe DSRM → récupération AD impossible  
- Oubli des snapshots → pas de rollback possible !
# Synthèse – Services Réseau en Environnement Microsoft

## 📦 Services et rôles principaux

|Rôle / Service|Objectif principal|
|---|---|
|Active Directory DS|Gestion centralisée des objets (utilisateurs, PC...)|
|DNS|Résolution de noms FQDN ↔ IP|
|DHCP|Attribution dynamique des IP|
|GPO|Configuration centralisée des stations / utilisateurs|
|Routage / NAT / pfSense|Communication inter-réseaux, sécurité, translation|

---

## ⚙️ Commandes PowerShell essentielles

### 🔹 DNS

```powershell
Install-WindowsFeature -Name DNS -IncludeManagementTools
Add-DnsServerPrimaryZone -Name "domaine.local" -DynamicUpdate Secure
Add-DnsServerResourceRecordA -Name "pc1" -ZoneName "domaine.local" -IPv4Address "192.168.0.10"
Add-DnsServerResourceRecordPtr -Name "10" -ZoneName "0.168.192.in-addr.arpa" -PtrDomainName "pc1.domaine.local"
```

### 🔹 DHCP

```powershell
Install-WindowsFeature -Name DHCP -IncludeManagementTools
Add-DhcpServerv4Scope -Name "LAN" -StartRange 192.168.1.50 -EndRange 192.168.1.200 -SubnetMask 255.255.255.0
Add-DhcpServerv4ExclusionRange -ScopeId 192.168.1.0 -StartRange 192.168.1.1 -EndRange 192.168.1.20
Add-DhcpServerv4Reservation -ScopeId 192.168.1.0 -IPAddress 192.168.1.10 -ClientId "MAC" -Description "SRVWEB"
```

### 🔹 Active Directory

```powershell
Install-WindowsFeature AD-Domain-Services -IncludeManagementTools
Install-ADDSForest -DomainName "domaine.local"
New-ADUser -Name "roy" -SamAccountName "roy" -AccountPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force) -Enabled $true
```

### 🔹 Routage / table de routes

```powershell
route add 192.168.3.0 mask 255.255.255.0 192.168.2.254
route print
```

---

## 🛠️ Notions fondamentales à connaître

### 🔸 DNS

- Différence entre **résolveur** (avec redirecteurs) et **hébergeur** (zones directes/inverses)
- Mise en œuvre de **zones secondaires** (lecture seule) pour la tolérance de panne
- **Délégation DNS** : permet à un serveur distant de gérer un sous-domaine
- **Redirection conditionnelle** : optimiser la résolution par domaine cible

### 🔸 DHCP

- DORA : Discover, Offer, Request, Ack
- Étendue, exclusions, réservations, options serveur (003, 006, 015...)
- Failover DHCP : redondance en **load balance** ou **hot standby**

### 🔸 GPO

- LSDOU : Local > Site > Domaine > OU
- Filtrage de sécurité, WMI Filters, bouclage utilisateur par poste
- GPO pratiques : fond d’écran, scripts de connexion, déploiement imprimantes, proxy, etc.

### 🔸 Routage

- Routage entre sous-réseaux via pfSense ou Windows
- NAT / translation d’adresses pour la sortie Internet
- Routage statique via `route add` ou configuration pfSense

---

## ⚠️ Pièges fréquents à éviter

|Situation problématique|Solution recommandée|
|---|---|
|Conflits IP / adresses attribuées en double|Exclure les IP statiques du DHCP et documenter|
|Résolution DNS incomplète|Créer les zones inverses / PTR systématiquement|
|Mauvais filtrage GPO|Toujours tester avec un compte de test|
|Transfert DNS échoue|Vérifier IP autorisées côté primaire / firewall|
|Routage défaillant|Vérifier la gateway et les routes définies dans chaque équipement|

---

## 📌 Bonnes pratiques professionnelles

|Bonnes pratiques|Pourquoi ?|
|---|---|
|Utiliser des IP fixes uniquement pour les serveurs et équipements critiques|Évite les conflits et la perte de service|
|Sauvegarder les zones DNS et config DHCP régulièrement|Pour garantir une restauration rapide en cas de panne|
|Nommer les objets (GPO, serveurs, groupes, zones) de façon explicite|Facilite la compréhension, la maintenance|
|Mettre en place des délégations DNS / GPO|Responsabiliser les administrateurs locaux ou par service|
|Surveiller les logs et activer l’audit|Prévenir les anomalies et analyser les incidents|

---

## 🧠 À retenir

- DNS et DHCP sont au **cœur de tout environnement Microsoft structuré**
- Leur interconnexion avec Active Directory est **essentielle** : DNS = socle AD, DHCP = provisioning postes
- Le routage et les GPO assurent l’**interopérabilité, la sécurité, et la conformité**
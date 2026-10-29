# Mise en place de l'infrastructure
## 🧩 Les composants de base

Une infrastructure Microsoft typique pour un domaine Active Directory repose sur les éléments suivants :

|Composant|Rôle|
|---|---|
|Contrôleur de domaine (DC)|Héberge Active Directory, authentifie les utilisateurs et les ordinateurs|
|Serveur DNS|Résolution des noms internes et externes|
|Serveur DHCP|Attribution automatique des adresses IP|
|Serveur de fichiers|Stockage partagé pour les utilisateurs et services|
|Serveur de déploiement (WDS/MDT)|Installation automatisée de systèmes d’exploitation|
|Services RDS|Publication de bureaux et applications à distance|

---

## 🏛️ Les composantes du domaine Active Directory

### Active Directory Domain Services (AD DS)

- **Base de données** centralisée contenant :
    - Comptes utilisateurs
    - Groupes
    - Ordinateurs
    - Politiques de groupe (GPO)
- Organisation hiérarchique :
    - Forêt
    - Domaine
    - Arborescence
    - UO (Unités Organisationnelles)

### Processus d’authentification

- **Kerberos** → authentification sécurisée
- **LDAP** → interrogation de l’annuaire

### Contrôleur de domaine

- Machine (physique ou VM) ayant le rôle **AD DS** installé
- Tient à jour la **base de l’annuaire** et synchronise avec d’autres DC

---

## 🖧 DHCP (Dynamic Host Configuration Protocol)

### Rôle

- Attribuer automatiquement :
    - Adresse IP
    - Masque de sous-réseau
    - Passerelle par défaut (gateway)
    - Serveurs DNS
    - Autres options (WINS, suffixes DNS, routes...)

### Fonctionnement

```text
DISCOVER → OFFER → REQUEST → ACK
```

### Configuration de base (via GUI ou PowerShell)

#### Via GUI (Server Manager)

1. Ajouter le rôle **DHCP Server**
2. Créer une **nouvelle étendue** :

- Adresse IP de début / de fin
- Plage exclue (réservée)
- Durée du bail
- Options de configuration (DNS, gateway)

#### Via PowerShell

```powershell
# Installation
Install-WindowsFeature -Name DHCP -IncludeManagementTools

# Création d’une étendue
Add-DhcpServerv4Scope -Name "LAN-Scope" -StartRange 192.168.1.100 -EndRange 192.168.1.200 -SubnetMask 255.255.255.0

# Ajout de l’option DNS
Set-DhcpServerv4OptionValue -ScopeId 192.168.1.0 -DnsServer 192.168.1.10 -DnsDomain "mondomaine.local"
```

### Pièges courants

- **Pas de réservation IP** pour les serveurs critiques → préférer IP fixe ou réservation DHCP
- Conflits d’adresses si plusieurs serveurs DHCP non contrôlés sur le réseau

---

## 🌐 DNS (Domain Name System)

### Rôle

- Résolution des **noms en adresses IP** (et inversement)
- Essentiel pour le **fonctionnement d’AD**

### Zones typiques

|Zone|Exemple|
|---|---|
|Zone directe|`mondomaine.local` → 192.168.1.10|
|Zone inverse|192.168.1.10 → `srv-dc.mondomaine.local`|

### Enregistrement clé pour AD

- **SRV records** (services) → localisent les contrôleurs de domaine

### Configuration de base

#### Via GUI (Server Manager > DNS Manager)

- Créer une **zone de recherche directe**
- Créer une **zone de recherche inversée**

#### Via PowerShell

```powershell
# Installation du rôle DNS
Install-WindowsFeature -Name DNS -IncludeManagementTools

# Création d’une zone
Add-DnsServerPrimaryZone -Name "mondomaine.local" -ZoneFile "mondomaine.local.dns"
```

### Pièges courants

- Oublier de configurer **l’auto-enregistrement DNS** des DC et serveurs
- Mauvaise **hiérarchie DNS** → dégradation des performances AD
- Ne pas séparer DNS **interne** et **externe**

---

## 🛠️ Outils de gestion

|Outil|Description|
|---|---|
|**Server Manager**|Interface centrale pour gérer les rôles et fonctionnalités|
|**Active Directory Users and Computers (ADUC)**|Gestion des utilisateurs, groupes, ordinateurs|
|**Active Directory Sites and Services**|Gestion de la réplication inter-sites|
|**DNS Manager**|Gestion des zones et enregistrements DNS|
|**DHCP Manager**|Gestion des étendues DHCP|
|**Group Policy Management Console (GPMC)**|Gestion avancée des GPO|
|**RSAT** (Remote Server Administration Tools)|Installation des consoles sur poste admin|

### Commande pour installer les outils RSAT sur Windows 10/11

```powershell
Get-WindowsCapability -Name RSAT* -Online | Add-WindowsCapability -Online
```

---

## ✅ À retenir pour les révisions

- Un domaine AD repose sur les rôles clés : **AD DS + DNS + DHCP**
- Le DNS interne est **indispensable** au bon fonctionnement d’AD
- Le DHCP doit être configuré avec des **options correctes** (DNS interne !)
- Les outils de gestion RSAT facilitent l’administration quotidienne
- Une bonne **planification de l’adressage** et de la **nomenclature DNS** est essentielle

---

## 📌 Bonnes pratiques professionnelles

- **Documenter** l’infrastructure dès la mise en place (adressage, rôles, noms)
- Prévoir des **réservations DHCP** pour les équipements critiques
- **Sécuriser** le rôle DHCP (1 serveur autorisé par VLAN réseau)
- Mettre en place une **stratégie de sauvegarde** des zones DNS et de l’AD
- Créer des **GPO de base** dès la création du domaine
- Toujours utiliser des **serveurs DNS internes** pour les machines jointes au domaine
- **Surveiller** les rôles DNS et DHCP (éviter pannes silencieuses)
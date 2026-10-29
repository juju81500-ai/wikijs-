# 📄 Windows Server 2016 / 2019 / 2022

- **Environnement** : VM (Windows Server 2022)
- **OS / Version** : Windows Server 2022 (Desktop Experience ou Core, à vérifier sur la version déployée)
- **Version** : Windows Server 2016 / 2019 / 2022 (les cmdlets citées sont celles de 2022, à vérifier sur 2016 et 2019)
- **Catégorie** : Systèmes, annuaires et services

## 🎯 Problème précis à résoudre
Mettre en place les rôles de base d'un serveur Windows : AD DS (forêt et contrôleur de domaine), DNS, DHCP, GPO, WSUS, DFS et RDS. Les étapes sont données en PowerShell, exécuté en administrateur. Les tests se font uniquement sur votre propre domaine de lab.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Nommage du serveur et redémarrage :
```powershell
Rename-Computer -NewName "SRV-AD01" -Restart
```
👉 Explication : Donne un nom NetBIOS court au serveur avant la promotion. Le serveur redémarre automatiquement. Le nom doit être unique dans le lab.

2. Installation des rôles AD DS, DNS et DHCP :
```powershell
Install-WindowsFeature -Name AD-Domain-Services, DNS, DHCP -IncludeManagementTools
Get-WindowsFeature AD-Domain-Services, DNS, DHCP
```
👉 Explication : Installe les rôles et les outils d'administration. La seconde commande affiche l'état `Installed` de chaque rôle.

3. Création de la forêt `corp.lab` avec DNS intégré :
```powershell
Install-ADDSForest -DomainName "corp.lab" -DomainNetbiosName "CORPLAB" -InstallDns -SafeModeAdministratorPassword (Read-Host -AsSecureString "Mot de passe DSRM") -Force
```
👉 Explication : Crée la forêt, installe DNS et demande à l'invite le mot de passe DSRM (mode de restauration des services d'annuaire). Ce mot de passe ne doit pas être écrit dans la commande. Le serveur redémarre à la fin.

4. Contrôle du contrôleur de domaine après redémarrage :
```powershell
Get-ADDomain | Select-Object Name, DNSRoot, NetBIOSName
Get-Service NTDS, DNS, Netlogon | Format-Table Name, Status
dcdiag /test:services
```
👉 Explication : `Get-ADDomain` confirme le domaine `corp.lab`. Les services `NTDS`, `DNS` et `Netlogon` doivent être `Running`. `dcdiag` contrôle la santé du contrôleur.

5. Création d'une étendue DHCP et d'un enregistrement DNS de test :
```powershell
Add-DhcpServerInDC -DnsName "SRV-AD01.corp.lab" -IPAddress 192.168.10.10
Add-DhcpServerv4Scope -Name "LAN-Lab" -StartRange 192.168.10.100 -EndRange 192.168.10.199 -SubnetMask 255.255.255.0
Set-DhcpServerv4OptionValue -ScopeId 192.168.10.0 -Router 192.168.10.1 -DnsServer 192.168.10.10 -DnsDomain "corp.lab"
Add-DnsServerResourceRecordA -ZoneName "corp.lab" -Name "app01" -IPv4Address 192.168.10.30
Resolve-DnsName app01.corp.lab
```
👉 Explication : `Add-DhcpServerInDC` autorise le serveur DHCP dans l'annuaire, sans quoi il ne distribue pas d'adresses sur un domaine. L'étendue `192.168.10.100` à `.199` est distribuée, avec passerelle et DNS. `Resolve-DnsName` vérifie que l'enregistrement de test se résout.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'une GPO de verrouillage d'écran et son lien sur une OU :
```powershell
New-GPO -Name "GPO-Verrouillage-Postes"
New-GPLink -Name "GPO-Verrouillage-Postes" -Target "OU=Postes,DC=corp,DC=lab"
Get-GPO -All | Format-Table DisplayName, GpoStatus
```
👉 Explication : Crée la GPO, la lie à l'OU `Postes` (à créer au préalable avec `New-ADOrganizationalUnit -Name "Postes" -Path "DC=corp,DC=lab"`) et liste les GPO. Les réglages se font ensuite dans la console Gestion des stratégies de groupe.

2. Installation de WSUS (base WID, dossier de contenu dédié) :
```powershell
Install-WindowsFeature -Name UpdateServices -IncludeManagementTools
& "C:\Program Files\Update Services\Tools\wsusutil.exe" postinstall CONTENT_DIR=D:\WSUS
Get-WindowsFeature UpdateServices
```
👉 Explication : Installe WSUS, puis configure le dossier de contenu sur `D:\WSUS`, disque distinct du système. Le chemin `D:\WSUS` doit exister. Le chemin de `wsusutil.exe` est celui de l'installation par défaut.

3. Création d'un espace DFS (espace de noms de domaine) :
```powershell
Install-WindowsFeature -Name FS-DFS-Namespace, FS-DFS-Replication -IncludeManagementTools
New-Item -Path "D:\Partages\Commun" -ItemType Directory
New-SmbShare -Name "Commun" -Path "D:\Partages\Commun" -FullAccess "CORPLAB\Admins du domaine"
New-DfsnRoot -TargetPath "\\SRV-AD01\Partages" -Type DomainV2 -Path "\\corp.lab\Partages"
```
👉 Explication : Installe DFS Namespace et Replication, crée un dossier partagé, puis publie l'espace de noms `\\corp.lab\Partages`. Le groupe `CORPLAB\Admins du domaine` est le libellé français : sur une installation anglaise, utiliser `Domain Admins`. À vérifier.

4. Installation de l'hôte de session RDS (paramétrage ensuite par le Gestionnaire de serveur) :
```powershell
Install-WindowsFeature -Name RDS-RD-Server -IncludeManagementTools
Get-WindowsFeature RDS-RD-Server
```
👉 Explication : Ajoute le rôle Hôte Bureau à distance. Le déploiement complet (courtier, passerelle) passe par l'assistant du Gestionnaire de serveur : ne pas le réduire à ce seul rôle. Point à vérifier selon les licences RDS.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Protection des unités d'organisation contre la suppression accidentelle :
```powershell
Get-ADOrganizationalUnit -Filter * | Set-ADObject -ProtectedFromAccidentalDeletion $true
Get-ADGroupMember -Identity "Admins du domaine" -Recursive | Select-Object Name, SamAccountName
```
👉 Explication : Protège les unités d'organisation contre la suppression. La seconde commande liste les membres du groupe `Admins du domaine` (libellé anglais : `Domain Admins`), à réduire au strict nécessaire.

2. Exigence de signature SMB sur le serveur de fichiers :
```powershell
Set-SmbServerConfiguration -RequireSecuritySignature $true -Force
Get-SmbServerConfiguration | Select-Object RequireSecuritySignature
```
👉 Explication : Impose la signature des échanges SMB. Vérifier auparavant que les postes clients la prennent en charge, sinon ils ne pourront plus accéder aux partages.

3. Audit des événements de sécurité :
```powershell
auditpol /get /category:"Logon/Logoff","Account Logon","Account Management"
```
👉 Explication : Affiche la configuration de l'audit. Les ouvertures de session et la gestion des comptes doivent être journalisées en succès et en échec. La configuration se règle ensuite par GPO (Configuration avancée de l'audit). Les libellés de catégories varient selon la langue.

4. Sauvegarde de l'état système de l'Active Directory :
```powershell
Install-WindowsFeature -Name Windows-Server-Backup
wbadmin start systemstatebackup -backuptarget:E: -quiet
wbadmin get versions -backuptarget:E:
```
👉 Explication : Sauvegarde l'état système, qui contient la base AD, sur le disque `E:` (disque de sauvegarde distinct). Une sauvegarde AD non testée n'est pas fiable : tester une restauration sur un lab.

5. Point à vérifier : WSUS en base WID et la configuration RDS se comportent différemment selon 2016, 2019 et 2022. Confirmer les chemins, les noms de groupes et les rôles sur chaque version avant mise en production.

---
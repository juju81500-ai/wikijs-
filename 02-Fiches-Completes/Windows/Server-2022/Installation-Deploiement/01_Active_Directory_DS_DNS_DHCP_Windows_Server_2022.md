# Active Directory, DNS et DHCP sur Windows Server 2022

- **Environnement** : VM ou serveur dédié, domaine de laboratoire ou d'entreprise
- **Rôles** : AD DS et DNS ; DHCP facultatif et de préférence séparé en production
- **Tags** : `windows-server-2022`, `active-directory`, `dns`, `dhcp`, `gpo`

## 1. Préparer l'architecture

Fiche simple : [préparer l'architecture](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Preparer_Architecture.md).

Définir le nom DNS du domaine, le nom NetBIOS, les sous-réseaux, les réservations, les relais DHCP, les DNS amont et la stratégie de sauvegarde. Réserver une adresse IP statique et vérifier l'heure/NTP. Ne pas créer un domaine de production avant d'avoir défini les rôles FSMO, la réplication, les comptes de secours et la restauration.

Dans PowerShell administrateur, contrôler l'adresse puis renommer avant la promotion :

```powershell
Get-NetIPConfiguration
Rename-Computer -NewName "DC01" -Restart
```

## 2. Créer une nouvelle forêt (laboratoire ou premier contrôleur)

Fiche simple : [créer une nouvelle forêt](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Creer_Nouvelle_Foret.md).

Après redémarrage, utiliser un nom DNS interne détenu par l'organisation :

```powershell
Install-WindowsFeature AD-Domain-Services,DNS -IncludeManagementTools
Install-ADDSForest -DomainName "ad.example.net" -DomainNetbiosName "EXAMPLE" -InstallDNS -SafeModeAdministratorPassword (Read-Host "Mot de passe DSRM" -AsSecureString) -NoRebootOnCompletion
Restart-Computer
```

La promotion modifie durablement le serveur et déclenche un redémarrage. Pour un domaine existant, ne pas exécuter `Install-ADDSForest` : ajouter le rôle puis promouvoir comme contrôleur supplémentaire avec les informations d'identification et le site AD validés.

## 3. Valider AD DS et DNS

Fiche simple : [valider AD DS et DNS](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Valider_ADDS_DNS.md).

```powershell
Get-ADDomain
Get-ADForest
dcdiag /test:dns /v
Resolve-DnsName -Type SRV _ldap._tcp.dc._msdcs.ad.example.net
```

Configurer les redirecteurs DNS uniquement vers des résolveurs approuvés. Vérifier la résolution des zones internes depuis un poste membre avant de poursuivre.

## 4. Ajouter DHCP si ce serveur en a la responsabilité

Fiche simple : [ajouter DHCP](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Ajouter_DHCP.md).

Ne pas activer un second serveur DHCP sur le même VLAN sans conception de bascule. Créer la portée après validation des plages exclues et de la passerelle :

```powershell
Install-WindowsFeature DHCP -IncludeManagementTools
Add-DhcpServerInDC -DnsName "dc01.ad.example.net" -IPAddress 192.0.2.10
Add-DhcpServerv4Scope -Name "LAN" -StartRange 192.0.2.100 -EndRange 192.0.2.199 -SubnetMask 255.255.255.0
Set-DhcpServerv4OptionValue -ScopeId 192.0.2.0 -Router 192.0.2.1 -DnsServer 192.0.2.10 -DnsDomain "ad.example.net"
Get-DhcpServerv4Scope
```

Remplacer tous les exemples par le plan IP réel. Ne pas activer la portée avant d'avoir vérifié qu'elle ne chevauche ni les adresses statiques ni une autre étendue.

## 5. Sauvegarde, sécurité et retour arrière

Fiche simple : [sauvegarder, sécuriser et prévoir le retour arrière](../../../../01-Fiches-Simples/Windows/Server-2022/Vie-du-logiciel/Active-Directory/Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Sauvegarde_Securite_Retour.md).

- Sauvegarder l'état système avec une solution compatible AD DS et tester une restauration hors production.
- Protéger le mot de passe DSRM, limiter les membres des groupes privilégiés et administrer avec des comptes séparés.
- Restreindre les flux aux réseaux nécessaires ; ne pas exposer LDAP, Kerberos, DNS ou DHCP à Internet.
- Une promotion de contrôleur ne se défait pas par simple désinstallation de rôle. En cas d'échec, conserver les journaux et suivre la procédure de rétrogradation/nettoyage AD DS adaptée.

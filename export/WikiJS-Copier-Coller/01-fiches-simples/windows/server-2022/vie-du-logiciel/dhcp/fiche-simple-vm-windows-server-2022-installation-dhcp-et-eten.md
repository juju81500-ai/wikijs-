# 📄 VM_WinSrv_2022_DHCP_Installation-Et-Etendue-Scope.md

- **Environnement** : VM (Hyper-V / Proxmox VE)
- **OS / Version** : Windows Server 2022 - Famille Windows Server
- **Catégorie** : Services Réseau (DHCP)

## 🎯 Problème précis à résoudre
Installer le rôle Serveur DHCP sous Windows Server 2022, autoriser le serveur dans Active Directory et configurer une étendue d'adresses IP sécurisée avec réserves.

---

## 🖥️ Méthode Interface Graphique (GUI pas-à-pas)

### Prérequis
- Configurer une adresse IP statique et les DNS corrects sur le serveur DHCP avant l'installation.
- En domaine AD, avoir un compte autorisé à installer le rôle et autoriser le serveur DHCP. Ne pas brancher un DHCP de laboratoire au réseau de production.

### Installer et autoriser le serveur DHCP
1. Dans **Gestionnaire de serveur** > **Gérer** > **Ajouter des rôles et fonctionnalités**, choisir **Installation basée sur un rôle ou une fonctionnalité**, sélectionner le serveur local et cocher **Serveur DHCP**. Ajouter les outils demandés, puis terminer l'assistant avec **Installer**.
2. À la fin, ouvrir le drapeau **Notifications** du Gestionnaire de serveur et sélectionner **Terminer la configuration DHCP**. Le post-déploiement crée les groupes DHCP locaux et, si le serveur est joint au domaine, permet son autorisation dans AD avec les identifiants appropriés.
3. Ouvrir **Gestionnaire de serveur** > **Outils** > **DHCP** (`dhcpmgmt.msc`). En domaine, vérifier que le serveur est autorisé et que le service est actif ; ne pas démarrer la distribution tant que l'autorisation ou les paramètres AD ne sont pas validés.
4. Créer l'étendue, les exclusions, options et réservations en suivant la [fiche GUI de création d'une étendue DHCP](/01-fiches-simples/windows/server-2022/vie-du-logiciel/dhcp/fiche-simple-vm-windows-server-2022-dhcp-creer-etendue-et-res).
5. Valider sur un client de laboratoire : vérifier le bail attribué, la passerelle, les DNS et le suffixe reçus. En multi-sous-réseaux, vérifier aussi le relais DHCP sur les routeurs.

Référence : [Microsoft Learn — Installer et configurer DHCP Server](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server).

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide du rôle DHCP en ligne de commande :
   `Install-WindowsFeature -Name DHCP -IncludeManagementTools`
   👉 Explication : Installe le rôle serveur DHCP et la console d'administration graphique.
2. Création d'une étendue minimale de test :
   `Add-DhcpServerv4Scope -Name "Scope-Lab" -StartRange 192.168.1.150 -EndRange 192.168.1.200 -SubnetMask 255.255.255.0 -State Active`
   👉 Explication : Crée et active une plage d'attribution de 50 adresses IP pour le laboratoire.

---

## ⚡ 2. Production — Façon Simplifiée
1. Autorisation du serveur DHCP dans le domaine Active Directory :
   `Add-DhcpServerInDC -DnsName "dhcp1.corp.tssr.local" -IPAddress 192.168.1.20`
   👉 Explication : Déclare le serveur DHCP auprès d'Active Directory pour autoriser la distribution des baux IP.
2. Configuration de l'étendue de production complète avec options réseau :
   `Add-DhcpServerv4Scope -Name "Scope-Prod-Clients" -StartRange 192.168.1.100 -EndRange 192.168.1.200 -SubnetMask 255.255.255.0`
   👉 Explication : Définit la plage d'attribution pour les clients du LAN.
3. Configuration des options de groupe (Passerelle & DNS) :
   `Set-DhcpServerv4OptionValue -OptionId 3 -Value "192.168.1.1" -ScopeId 192.168.1.0`
   `Set-DhcpServerv4OptionValue -OptionId 6 -Value "192.168.1.10" -ScopeId 192.168.1.0`
   `Set-DhcpServerv4OptionValue -DnsDomain "corp.tssr.local" -ScopeId 192.168.1.0`
   👉 Explication : Définit respectivement la passerelle (option 003), le DNS AD (option 006) et le suffixe DNS (option 015) ; ces valeurs doivent correspondre au réseau réel.

---

## 🔒 3. Production — Façon Sécurisée (Hardening Enterprise & Rogue DHCP Protection)
1. Restriction de la gestion du serveur DHCP au groupe d'administration dédié :
   `Add-LocalGroupMember -Group "DHCP Administrators" -Member "CORP\AdminReseau"`
   👉 Explication : Délègue l'administration DHCP sans accorder les privilèges élevés d'Administrateur du Domaine.
2. Configuration des plages d'exclusion pour les équipements fixes (Serveurs / Imprimantes) :
   `Add-DhcpServerv4ExclusionRange -ScopeId 192.168.1.0 -StartRange 192.168.1.100 -EndRange 192.168.1.120`
   👉 Explication : Réserve une plage d'adresses au sein de l'étendue pour éviter les conflits d'adresses IP.
3. Activation de la mise à jour dynamique sécurisée des enregistrements DNS :
   `Set-DhcpServerv4DnsSetting -ComputerName "dhcp1.corp.tssr.local" -DynamicUpdates Always -DeleteDnsRRonLeaseExpiry $true`
   `Set-DhcpServerDnsCredential -ComputerName "dhcp1.corp.tssr.local" -Credential (Get-Credential)`
   👉 Explication : Configure l'enregistrement DNS par le DHCP. Utiliser un compte dédié à mises à jour DNS et une zone AD configurée pour les mises à jour sécurisées ; `Get-Credential` demande le secret sans le mettre en clair dans la commande.
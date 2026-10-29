# Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Ajouter_DHCP.md

- **Environnement** : VM ou serveur dédié Windows Server 2022, domaine de laboratoire ou d'entreprise
- **OS / Version** : Windows Server 2022; rôles AD DS, DNS et DHCP
- **Catégorie** : annuaire / services réseau

---

## Problème précis à résoudre

Ajouter DHCP seulement si ce serveur en a la responsabilité.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier qu'aucun autre serveur DHCP n'est actif sur le même VLAN sans conception de bascule.
   👉 Explication : deux DHCP sans bascule causent des conflits.

2. GUI : **Gestionnaire de serveur > Ajouter des rôles et fonctionnalités > Serveur DHCP**, puis **Outils > DHCP > Nouvelle étendue**.
   👉 Explication : équivalent graphique.

3. Installer le rôle et autoriser le serveur dans AD (dc01.ad.example.net et 192.0.2.10 sont des exemples à remplacer) :
   ```powershell
   Install-WindowsFeature DHCP -IncludeManagementTools
   Add-DhcpServerInDC -DnsName "dc01.ad.example.net" -IPAddress 192.0.2.10
   ```
   👉 Explication : un serveur DHCP doit être autorisé dans AD.

4. Créer la portée et ses options (valeurs d'exemple à remplacer par le plan IP réel) :
   ```powershell
   Add-DhcpServerv4Scope -Name "LAN" -StartRange 192.0.2.100 -EndRange 192.0.2.199 -SubnetMask 255.255.255.0
   Set-DhcpServerv4OptionValue -ScopeId 192.0.2.0 -Router 192.0.2.1 -DnsServer 192.0.2.10 -DnsDomain "ad.example.net"
   Get-DhcpServerv4Scope
   ```
   👉 Explication : la portée est créée puis listée; ne pas l'activer avant d'avoir vérifié qu'elle ne chevauche ni adresses statiques ni autre étendue.

## 2. Production — Contrôles

Valider les plages exclues et la passerelle avant activation.

## 3. Production — Sécurité

- Pas de second DHCP sans conception de bascule.
- Ne pas exposer DHCP à Internet.

## Validation et retour arrière

- **Validation** : `Get-DhcpServerv4Scope` affiche la portée prévue et un client reçoit une adresse.
- **Retour arrière** : Supprimer la portée de test (`Remove-DhcpServerv4Scope -ScopeId 192.0.2.0`, exemple à remplacer) après vérification.

## Si le problème n'est pas résolu

- [Microsoft Learn — Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [Microsoft Learn — Install-ADDSForest](https://learn.microsoft.com/en-us/powershell/module/addsdeployment/install-addsforest)
- [Guide complet AD DS, DNS et DHCP Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/01-active-directory-ds-dns-dhcp-windows-server-2022#4-ajouter-dhcp-si-ce-serveur-en-a-la-responsabilite)
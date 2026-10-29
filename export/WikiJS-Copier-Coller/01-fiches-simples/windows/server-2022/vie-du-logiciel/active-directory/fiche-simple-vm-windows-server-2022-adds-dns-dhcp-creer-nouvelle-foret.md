# Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Creer_Nouvelle_Foret.md

- **Environnement** : VM ou serveur dédié Windows Server 2022, domaine de laboratoire ou d'entreprise
- **OS / Version** : Windows Server 2022; rôles AD DS, DNS et DHCP
- **Catégorie** : annuaire / services réseau

---

## Problème précis à résoudre

Promouvoir le premier contrôleur de domaine (laboratoire ou nouvelle forêt).

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités > Services AD DS**, puis **Promouvoir ce serveur en contrôleur de domaine > Ajouter une nouvelle forêt**.
   👉 Explication : équivalent graphique des commandes ci-dessous.

2. Installer les rôles (après redémarrage du renommage) :
   ```powershell
   Install-WindowsFeature AD-Domain-Services,DNS -IncludeManagementTools
   ```
   👉 Explication : ajoute AD DS et DNS avec leurs outils.

3. Créer la forêt (ad.example.net et EXAMPLE sont des exemples à remplacer par un nom DNS interne que vous détenez) :
   ```powershell
   Install-ADDSForest -DomainName "ad.example.net" -DomainNetbiosName "EXAMPLE" -InstallDNS -SafeModeAdministratorPassword (Read-Host "Mot de passe DSRM" -AsSecureString) -NoRebootOnCompletion
   Restart-Computer
   ```
   👉 Explication : le mot de passe DSRM est saisi de façon interactive, jamais en argument; la promotion modifie durablement le serveur.

## 2. Production — Contrôles

Pour un domaine existant, ne pas exécuter `Install-ADDSForest` : ajouter le rôle puis promouvoir comme contrôleur supplémentaire avec les identifiants et le site AD validés.

## 3. Production — Sécurité

- Protéger le mot de passe DSRM dans le coffre.

## Validation et retour arrière

- **Validation** : Le serveur redémarre en tant que contrôleur de domaine.
- **Retour arrière** : Une promotion ne se défait pas par désinstallation de rôle : suivre la procédure de rétrogradation/nettoyage AD DS.

## Si le problème n'est pas résolu

- [Microsoft Learn — Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [Microsoft Learn — Install-ADDSForest](https://learn.microsoft.com/en-us/powershell/module/addsdeployment/install-addsforest)
- [Guide complet AD DS, DNS et DHCP Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/01-active-directory-ds-dns-dhcp-windows-server-2022#2-creer-une-nouvelle-foret-laboratoire-ou-premier-controleur)
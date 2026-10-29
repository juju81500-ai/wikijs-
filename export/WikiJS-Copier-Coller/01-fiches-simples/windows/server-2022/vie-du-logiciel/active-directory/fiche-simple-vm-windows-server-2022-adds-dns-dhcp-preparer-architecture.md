# Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Preparer_Architecture.md

- **Environnement** : VM ou serveur dédié Windows Server 2022, domaine de laboratoire ou d'entreprise
- **OS / Version** : Windows Server 2022; rôles AD DS, DNS et DHCP
- **Catégorie** : annuaire / services réseau

---

## Problème précis à résoudre

Définir l'architecture et renommer le serveur avant la promotion.

## 1. Hors-Production (Lab / Test / POC)

1. Définir le nom DNS du domaine, le nom NetBIOS, les sous-réseaux, les réservations, les relais DHCP, les DNS amont et la stratégie de sauvegarde; réserver une adresse IP statique et vérifier l'heure/NTP.
   👉 Explication : on ne crée pas de domaine de production sans rôles FSMO, réplication, comptes de secours et restauration définis.

2. Dans PowerShell administrateur, contrôler l'adresse :
   ```powershell
   Get-NetIPConfiguration
   ```
   👉 Explication : l'adresse doit être statique et conforme au plan IP.

3. GUI : **Gestionnaire de serveur > Serveur local > Nom de l'ordinateur** pour renommer.
   👉 Explication : équivalent graphique de la commande ci-dessous.

4. Renommer et redémarrer (DC01 est un exemple à remplacer par votre nom) :
   ```powershell
   Rename-Computer -NewName "DC01" -Restart
   ```
   👉 Explication : le renommage doit précéder la promotion.

## 2. Production — Contrôles

Documenter le plan d'adressage et d'architecture.

## 3. Production — Sécurité

- Ne pas créer un domaine de production avant d'avoir défini FSMO, réplication, comptes de secours et restauration.

## Validation et retour arrière

- **Validation** : Nom, adresse IP statique et heure conformes.
- **Retour arrière** : `Rename-Computer` avec l'ancien nom puis redémarrer.

## Si le problème n'est pas résolu

- [Microsoft Learn — Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [Microsoft Learn — Install-ADDSForest](https://learn.microsoft.com/en-us/powershell/module/addsdeployment/install-addsforest)
- [Guide complet AD DS, DNS et DHCP Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/01-active-directory-ds-dns-dhcp-windows-server-2022#1-preparer-larchitecture)
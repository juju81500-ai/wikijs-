# Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Configurer

- **Environnement** : `Serveur Windows Server 2022 (VM ou physique), compte administrateur local ou de domaine nominatif`
- **OS / Version** : `Windows Server 2022 (Desktop Experience ou Core selon support de la version); vérifier la compatibilité et la version courante du produit auprès de l'éditeur`
- **Catégorie** : `stockage / SAN / StarWind`
- **Tags** : `starwind`, `virtual-san`, `windows-server`, `configuration`, `iscsi`

---

## Problème précis à résoudre

Préparer le réseau et les rôles Windows autour de StarWind, puis créer le stockage dans la console selon la documentation de la version.

## 1. Hors-Production (Lab / Test / POC)

1. Renommer les cartes réseau par rôle. PowerShell : `Rename-NetAdapter -Name NOM_ACTUEL -NewName NOM_ROLE`.
```powershell
Rename-NetAdapter -Name NOM_ACTUEL -NewName NOM_ROLE
```
   👉 Explication : NOM_ACTUEL et NOM_ROLE sont à remplacer (exemple de rôles : gestion, iSCSI, synchronisation) ; des noms clairs évitent les erreurs de câblage.

2. Fixer une adresse IP statique par réseau. GUI : propriétés de la carte > **Protocole Internet version 4 (TCP/IPv4)**. PowerShell :
```powershell
New-NetIPAddress -InterfaceAlias NOM_ROLE -IPAddress ADRESSE_IP -PrefixLength LONGUEUR_PREFIXE
```
   👉 Explication : ADRESSE_IP et LONGUEUR_PREFIXE sont à remplacer ; un stockage exige des adresses stables.

3. Si les hôtes consommateurs sont des serveurs Windows, installer MPIO sur ceux-ci. GUI : **Gestionnaire de serveur > Ajouter des rôles et fonctionnalités > Multipath I/O**. PowerShell :
```powershell
Install-WindowsFeature -Name Multipath-IO
```
   👉 Explication : MPIO permet plusieurs chemins vers un même volume ; à confirmer selon l'architecture documentée par l'éditeur.

4. Ouvrir la console de gestion StarWind, ajouter le serveur local comme hôte, puis créer le stockage (dispositif de stockage, cible iSCSI) en suivant le guide éditeur de votre version. Les chemins de menus exacts ne sont pas figés ici : vérifier la version.
   👉 Explication : la création du volume et de la cible est faite dans la console fournie par le produit ; aucune commande n'est supposée.

5. Dans l'initiateur iSCSI du client : **Gestionnaire de serveur > Outils > Initiateur iSCSI**, ou PowerShell :
```powershell
New-IscsiTargetPortal -TargetPortalAddress ADRESSE_IP_ISCSI
Get-IscsiTarget
```
   👉 Explication : ADRESSE_IP_ISCSI est à remplacer par l'IP du réseau iSCSI du serveur StarWind ; la cible doit apparaître.

## 2. Production — Contrôles

- Documenter IP, cibles, volumes et hôtes autorisés.
- Éviter de mélanger gestion et trafic de stockage sur la même carte.

## 3. Production — Sécurité

- Limiter l'accès aux cibles aux seuls initiateurs prévus.
- Utiliser une authentification forte pour l'accès à la console, sans mot de passe dans la fiche.

## Validation et retour arrière

- **Validation** : La cible est visible depuis l'initiateur et le volume est utilisable.
- **Retour arrière** : Déconnecter la cible côté client (`Disconnect-IscsiTarget -NodeAddress IQN_CIBLE`, IQN_CIBLE à remplacer) puis supprimer la cible dans la console ; données du volume à sauvegarder avant.

## Si le problème n'est pas résolu

- [StarWind — site officiel du produit Virtual SAN](https://www.starwindsoftware.com/starwind-virtual-san)
- [StarWind — bibliothèque de ressources et guides officiels](https://www.starwindsoftware.com/resource-library)
- [Fiche d'entrée du logiciel](../../../../Logiciels/06-Stockage-et-SAN-NAS/Fiche_Logiciel_-_StarWind-Virtual-SAN.md)

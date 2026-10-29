# Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Securiser

- **Environnement** : `Serveur Windows Server 2022 (VM ou physique), compte administrateur local ou de domaine nominatif`
- **OS / Version** : `Windows Server 2022 (Desktop Experience ou Core selon support de la version); vérifier la compatibilité et la version courante du produit auprès de l'éditeur`
- **Catégorie** : `stockage / SAN / StarWind`

---

## Problème précis à résoudre

Réduire la surface d'exposition de StarWind : comptes, pare-feu, réseau et chiffrement des accès de gestion.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte administrateur nominatif. GUI : **Gestion de l'ordinateur > Utilisateurs et groupes locaux**. PowerShell : `New-LocalUser -Name NOM_COMPTE -Password MOT_DE_PASSE_SECURISE`, où MOT_DE_PASSE_SECURISE est un SecureString à demander à la saisie.
```powershell
$mdp = Read-Host -AsSecureString 'Mot de passe'
New-LocalUser -Name NOM_COMPTE -Password $mdp
```
   👉 Explication : NOM_COMPTE est à remplacer ; la saisie interactive évite d'écrire un secret.

2. Lister les règles de pare-feu existantes liées à StarWind. PowerShell :
```powershell
Get-NetFirewallRule -DisplayName '*StarWind*' | Format-Table DisplayName,Enabled,Direction,Action
```
   👉 Explication : l'installeur peut créer des règles ; on les contrôle plutôt que d'en supposer.

3. Restreindre l'accès aux ports du produit aux réseaux concernés. Vérifier les ports exacts dans la documentation de la version, puis :
```powershell
New-NetFirewallRule -DisplayName 'StarWind iSCSI restreint' -Direction Inbound -Protocol TCP -LocalPort PORT_ISCSI -RemoteAddress RESEAU_AUTORISE -Action Allow
```
   👉 Explication : PORT_ISCSI et RESEAU_AUTORISE sont à remplacer ; l'iSCSI n'est ouvert qu'aux initiateurs prévus.

4. Isoler le trafic de stockage dans un VLAN ou réseau dédié, non routé vers les postes utilisateurs.
   👉 Explication : le protocole iSCSI n'est pas conçu pour être exposé sur un réseau général.

5. Vérifier dans la documentation éditeur la prise en charge de l'authentification CHAP et du chiffrement de l'accès de gestion pour votre version, et l'activer si disponible.
   👉 Explication : on n'affirme pas une fonction non vérifiée.

## 2. Production — Contrôles

- Revoir périodiquement comptes et règles de pare-feu.
- Journaliser les connexions administrateur Windows.

## 3. Production — Sécurité

- Pas de compte partagé ni de mot de passe dans la fiche.
- Aucune exposition sur Internet.

## Validation et retour arrière

- **Validation** : Seuls les réseaux autorisés atteignent les ports ; comptes nominatifs en place.
- **Retour arrière** : `Disable-NetFirewallRule -DisplayName 'StarWind iSCSI restreint'` puis réévaluer, ou `Remove-NetFirewallRule` ; désactiver le compte créé par erreur dans **Utilisateurs et groupes locaux**.

## Si le problème n'est pas résolu

- [StarWind — site officiel du produit Virtual SAN](https://www.starwindsoftware.com/starwind-virtual-san)
- [StarWind — bibliothèque de ressources et guides officiels](https://www.starwindsoftware.com/resource-library)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/06-stockage-et-san-nas/fiche-logiciel-starwind-virtual-san)
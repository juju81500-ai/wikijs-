# Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Securisation

- **Environnement** : Windows Server 2022, WDS + MDT déjà installés selon la procédure historique
- **OS / Version** : Windows Server 2022; WDS, MDT : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC

---

## Problème précis à résoudre

Contrôler et compléter la sécurisation du serveur de déploiement. La création du compte de lecture MDT et le durcissement du partage sont décrits dans la [procédure historique WDS + MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-simple-wds-mdt) (section sécurisée) : ne pas les refaire ici; cette fiche les contrôle.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la politique de réponse PXE. GUI : `Outils d'administration > Services de déploiement Windows > clic droit sur le serveur > Propriétés > Réponse PXE`.
   ```powershell
   wdsutil /Get-Server /Show:Config
   ```
   👉 Explication : la réponse « à tous les clients » est à réserver au lab; en production, exiger l'approbation administrateur (réglage décrit dans la procédure historique).

2. Contrôler les droits du partage de déploiement :
   ```powershell
   Get-SmbShareAccess -Name "DeploymentShare$"
   Get-Acl "D:\DeploymentShare$" | Select-Object -ExpandProperty Access | Select-Object IdentityReference, FileSystemRights
   ```
   👉 Explication : remplacer `D:\DeploymentShare$` par le chemin réel. Aucun groupe large (Tout le monde, Utilisateurs authentifiés) en écriture; lecture seule pour le compte de lecture dédié.

3. Rechercher des secrets dans les fichiers de configuration :
   ```powershell
   Select-String -Path "D:\DeploymentShare$\Control\*.ini" -Pattern "Password|DomainAdmin" -SimpleMatch
   ```
   👉 Explication : toute ligne trouvée est à examiner; un mot de passe en clair dans `Bootstrap.ini` ou `CustomSettings.ini` est à supprimer et à changer.

4. Contrôler le pare-feu :
   ```powershell
   Get-NetFirewallRule -DisplayGroup "Windows Deployment Services" | Select-Object DisplayName, Enabled, Profile
   ```
   👉 Explication : seules les règles nécessaires doivent être actives, restreintes aux réseaux de déploiement.

## 2. Production — Contrôles

Revue après chaque changement d'image; supprimer les anciens comptes, journaux et images obsolètes selon la politique de rétention.

## 3. Production — Sécurité

- Le compte lié au déploiement n'est pas administrateur de domaine; délégation limitée à l'ajout d'ordinateurs dans une OU dédiée.
- Les secrets vivent dans un coffre-fort, jamais dans les fichiers du partage.
- Isoler le VLAN de déploiement et filtrer les accès au partage.

## Validation et retour arrière

- **Validation** : politique PXE restrictive, ACL minimales, aucun secret dans les fichiers `.ini`, pare-feu restreint.
- **Retour arrière** : ces contrôles sont en lecture seule. Si un correctif a été appliqué, restaurer les ACL ou `.ini` depuis la sauvegarde (fiche Sauvegarde/Restauration).

## Si le problème n'est pas résolu

- [Procédure historique WDS + MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-simple-wds-mdt)
- [Fiche d'entrée WDS/MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-wds-mdt)
- [Microsoft Learn — wdsutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil)
- [Microsoft Learn — Get-SmbShareAccess](https://learn.microsoft.com/en-us/powershell/module/smbshare/get-smbshareaccess)
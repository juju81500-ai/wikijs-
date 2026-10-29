# Fiche_Simple_-_Windows_Server_2025_RDS_Sauvegarder_Restaurer

- **Environnement** : Déploiement RDS de test Windows Server 2025 et dépôt de sauvegarde contrôlé
- **OS / Version** : Windows Server 2025 Desktop Experience
- **Catégorie** : Vie du logiciel / Continuité RDS
- **Tags** : `windows-server-2025`, `rds`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration RDS (collections, certificats, base des licences) d'un serveur Windows Server 2025.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter l'état des collections et licences vers un dépôt contrôlé :
   ```powershell
   New-Item -ItemType Directory -Path DEPOT_SAUVEGARDE -Force
   Get-RDSessionCollection -ConnectionBroker NOM_BROKER | Export-Clixml DEPOT_SAUVEGARDE\collections.xml
   Get-RDLicenseConfiguration -ConnectionBroker NOM_BROKER | Export-Clixml DEPOT_SAUVEGARDE\licences.xml
   ```
   👉 Explication : DEPOT_SAUVEGARDE (dossier chiffré et à accès restreint) et NOM_BROKER sont à remplacer; ces exports servent de référence de reconstruction, non de restauration automatique.
2. Exporter le certificat avec sa clé, mot de passe saisi à l'invite :
   ```powershell
   $Mdp = Read-Host 'Mot de passe PFX' -AsSecureString
   Export-PfxCertificate -Cert Cert:\LocalMachine\My\EMPREINTE -FilePath DEPOT_SAUVEGARDE\rds.pfx -Password $Mdp
   ```
   👉 Explication : EMPREINTE est à remplacer par l'empreinte du certificat (`Get-ChildItem Cert:\LocalMachine\My`); le certificat n'est exportable que si la clé l'est.
3. Sauvegarder le serveur : **Sauvegarde Windows Server** (`wbadmin.msc`) ou :
   ```powershell
   Install-WindowsFeature Windows-Server-Backup
   wbadmin start systemstatebackup -backuptarget:LECTEUR_SAUVEGARDE: -quiet
   ```
   👉 Explication : LECTEUR_SAUVEGARDE est à remplacer par la lettre du volume dédié. Pour le serveur de licences, sauvegarder aussi la base (dossier `lserver` sous `System32`) après avoir arrêté le service TermServLicensing; vérifier la procédure officielle.
4. Restaurer en environnement isolé : réimporter le PFX avec `Import-PfxCertificate`, réinstaller les rôles, recréer les collections d'après `collections.xml`, puis tester.
   👉 Explication : La restauration se valide hors production d'abord; ne jamais écraser un déploiement actif sans fenêtre approuvée.

## 2. Production — Contrôles

- Définir RPO/RTO, rétention et test de restauration périodique.
- Chiffrer et isoler les sauvegardes; contrôler leurs accès.
- Réactiver les licences si le serveur de licences est reconstruit; contacter Microsoft pour la réactivation.

## 3. Production — Sécurité

- Les PFX et sauvegardes contiennent des secrets : stockage chiffré, accès minimal.
- Ne jamais écrire de mot de passe en clair dans un script.

## Validation et retour arrière

- **Validation** : restauration dans un environnement isolé réussie, connexion pilote et licences conformes aux objectifs de reprise.
- **Retour arrière** : conserver les composants sources et les sauvegardes immuables jusqu'à validation formelle du service restauré.

## Si le problème n'est pas résolu

- [Microsoft Learn — Windows Server Backup](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wbadmin)
- [Valider la recette](./Fiche_Simple_-_Windows_Server_2025_RDS_Valider_Recette.md)
- [Mise à jour et retour arrière](./Fiche_Simple_-_Windows_Server_2025_RDS_Mise_A_Jour_Retour_Arriere.md)
- [Équivalent Windows Server 2022](../../../Server-2022/Vie-du-logiciel/Remote-Desktop-Services/Fiche_Simple_-_Windows_Server_2022_RDS_Sauvegarder_Restaurer.md)

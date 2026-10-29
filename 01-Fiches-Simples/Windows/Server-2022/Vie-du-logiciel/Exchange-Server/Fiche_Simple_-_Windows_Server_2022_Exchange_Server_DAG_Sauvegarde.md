# Fiche_Simple_-_Windows_Server_2022_Exchange_Server_DAG_Sauvegarde

- **Environnement** : Windows Server 2022; Exchange Server 2019 CU14 ou ultérieur, ou Exchange Server Subscription Edition (vérifier la matrice de support publiée)
- **OS / Version** : Windows Server 2022
- **Catégorie** : Messagerie / haute disponibilité et sauvegarde
- **Tags** : `windows-server-2022`, `exchange-server`, `messagerie`, `dag`, `sauvegarde`, `wbadmin`, `vss`

---

## Problème précis à résoudre

Mettre en place un groupe de disponibilité de bases de données (DAG) et une sauvegarde cohérente VSS des bases Exchange, avec test de restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Préparer un serveur témoin (serveur de fichiers, pas Exchange) : ajouter le groupe `Exchange Trusted Subsystem` aux administrateurs locaux du témoin.
   ```powershell
   Add-LocalGroupMember -Group Administrators -Member "CONTOSO\Exchange Trusted Subsystem"
   ```
   👉 Explication : à exécuter sur le témoin FS01 ; remplacer `CONTOSO`.

2. Créer le DAG : EAC > Serveurs > Groupes de disponibilité de base de données > + ; ou :
   ```powershell
   New-DatabaseAvailabilityGroup -Name DAG01 -WitnessServer FS01 -WitnessDirectory C:\DAGWitness -DatabaseAvailabilityGroupIpAddresses ([System.Net.IPAddress]::None)
   ```
   👉 Explication : remplacer `DAG01`, `FS01` ; l'adresse `None` crée un DAG sans IP administrative (valeur à valider selon la topologie).

3. Ajouter les membres :
   ```powershell
   Add-DatabaseAvailabilityGroupServer -Identity DAG01 -MailboxServer EXCH01
   Add-DatabaseAvailabilityGroupServer -Identity DAG01 -MailboxServer EXCH02
   ```
   👉 Explication : chaque serveur doit avoir Exchange installé et les mêmes volumes ; remplacer `EXCH02`.

4. Ajouter une copie de base : EAC > Serveurs > Bases de données > base > Ajouter une copie ; ou :
   ```powershell
   Add-MailboxDatabaseCopy -Identity DB01 -MailboxServer EXCH02 -ActivationPreference 2
   ```
   👉 Explication : crée la copie passive et lance l'amorçage.

5. Installer Windows Server Backup et sauvegarder les volumes de bases (VSS, troncature des journaux) :
   ```powershell
   Install-WindowsFeature Windows-Server-Backup
   wbadmin start backup -backupTarget:G: -include:E:,F: -vssFull -quiet
   ```
   👉 Explication : remplacer `G:` (cible), `E:` `F:` (volumes bases et journaux) ; une copie DAG n'est pas une sauvegarde.

6. Tester la restauration dans une base de récupération (jamais sur la base de production) :
   ```powershell
   New-MailboxDatabase -Recovery -Name RDB01 -Server EXCH01 -EdbFilePath R:\RDB01\DB01.edb -LogFolderPath R:\RDB01
   ```
   👉 Explication : après restauration des fichiers, monter la RDB puis utiliser `New-MailboxRestoreRequest`.

## 2. Production — Contrôles

Surveiller `Get-MailboxDatabaseCopyStatus`, l'espace des volumes de journaux, la latence de réplication et le dernier `LastFullBackup` ; documenter la procédure de restauration.

## 3. Production — Sécurité

- Chiffrer et isoler les sauvegardes, accès restreint.
- Réseau de réplication séparé si possible, flux inter-serveurs limités par pare-feu.
- Garder une copie hors site / immuable.

## Validation et retour arrière

- **Validation** : `Test-ReplicationHealth -Identity EXCH01` sans échec, copies `Healthy`, `Get-MailboxDatabase -Status | fl Name,LastFullBackup` à jour, objet de test restauré.
- **Retour arrière** : retirer une copie : `Remove-MailboxDatabaseCopy -Identity DB01\EXCH02` ; supprimer le DAG seulement après avoir retiré tous les membres.

## Si le problème n'est pas résolu

- [Exchange Server — documentation Microsoft](https://learn.microsoft.com/exchange/exchange-server)
- [Matrice de support Exchange Server](https://learn.microsoft.com/exchange/plan-and-deploy/supportability-matrix)
- [Fiche d'entrée Exchange Server](../../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Server.md)

# Fiche_Simple_-_Windows_Server_2022_SQL-Server_Prerequis_Limites

- **Environnement** : VM Windows Server 2022 (SQL Server 2022 Standard ou Developer)
- **OS / Version** : Windows Server 2022; SQL Server 2022 (instance par défaut MSSQLSERVER)
- **Catégorie** : base de données / SQL Server / Prérequis et limites
- **Tags** : `windows-server-2022`, `sql-server`, `sqlserver-2022`, `prerequis`

---

## Problème précis à résoudre

Vérifier que le serveur Windows est prêt pour SQL Server 2022 et connaître les limites du périmètre avant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la version de Windows, le nom et le domaine :
   ```powershell
   Get-ComputerInfo | Select-Object OsName,OsVersion,CsName,CsDomain
   Get-Volume | Select-Object DriveLetter,FileSystemLabel,FileSystem,Size,SizeRemaining
   ```
   👉 Explication : GUI équivalent : Paramètres → Système → À propos. Le nom de l'ordinateur doit être définitif avant l'installation.

2. Prévoir des volumes séparés (données, journaux, sauvegardes) :
   ```powershell
   Get-Disk | Select-Object Number,FriendlyName,Size,PartitionStyle
   fsutil fsinfo ntfsinfo D:
   ```
   👉 Explication : GUI : Gestionnaire de serveur → Services de fichiers et de stockage → Volumes. Formater les volumes de données en NTFS, unité d'allocation de 64 Ko, par exemple avec `Format-Volume -DriveLetter D -FileSystem NTFS -AllocationUnitSize 65536` (action destructive, à valider).

3. Choisir l'édition et le compte de service :
   👉 Explication : Developer pour le lab et les tests (non autorisée en production), Standard ou Enterprise sous licence en production ; compte de service par défaut (compte virtuel) en lab, compte de service géré (gMSA) en production.

4. Contrôler le port 1433 et le pare-feu :
   ```powershell
   Get-NetTCPConnection -LocalPort 1433 -ErrorAction SilentlyContinue
   Get-NetFirewallProfile | Select-Object Name,Enabled
   ```
   👉 Explication : aucun service ne doit déjà utiliser le port 1433 ; le pare-feu Windows doit rester actif.

5. Noter les limites :
   👉 Explication : série pour une instance unique ; Always On, instances en cluster de basculement et SQL Server sur Linux sont hors périmètre ; SSMS s'installe séparément ; vérifier la version publiée de SQL Server 2022 et de SSMS.

## 2. Production — Contrôles

Consigner nom, IP, édition, licence, volumétrie, comptes de service, groupe DBA, RPO/RTO, fenêtre de maintenance.

## 3. Production — Sécurité

- Ne pas installer sur un contrôleur de domaine.
- Prévoir un groupe d'administrateurs SQL dédié plutôt que des comptes individuels.
- Ne jamais utiliser l'édition Developer pour la production.

## Validation et retour arrière

- **Validation** : volumes, ports, édition et responsables validés.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [SQL Server — Installer SQL Server et les outils](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Installer.md)
- [SQL Server — Configurer l'instance](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Configurer.md)
- [SQL Server — Sécuriser (authentification, TLS, pare-feu)](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Securiser.md)
- [SQL Server — Valider (recette)](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Valider.md)
- [SQL Server — Sauvegarder et restaurer](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Sauvegarder_Restaurer.md)
- [SQL Server — Mise à jour et retour arrière](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Mettre_A_Jour.md)
- [SQL Server 2022 — installation](https://learn.microsoft.com/fr-fr/sql/database-engine/install-windows/install-sql-server)
- [SQL Server — sauvegarde et restauration](https://learn.microsoft.com/fr-fr/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases)
- [SQL Server — chiffrement des connexions](https://learn.microsoft.com/fr-fr/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine)

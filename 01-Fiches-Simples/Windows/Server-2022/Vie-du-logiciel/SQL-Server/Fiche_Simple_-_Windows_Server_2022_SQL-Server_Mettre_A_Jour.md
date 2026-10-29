# Fiche_Simple_-_Windows_Server_2022_SQL-Server_Mettre_A_Jour

- **Environnement** : VM Windows Server 2022 (SQL Server 2022 Standard ou Developer)
- **OS / Version** : Windows Server 2022; SQL Server 2022 (instance par défaut MSSQLSERVER)
- **Catégorie** : base de données / SQL Server / Mise à jour et retour arrière
- **Tags** : `windows-server-2022`, `sql-server`, `sqlserver-2022`, `mise-a-jour`

---

## Problème précis à résoudre

Appliquer une mise à jour cumulative (CU) de SQL Server 2022 et savoir revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Relever la version actuelle :
   ```powershell
   sqlcmd -S localhost -E -Q "SELECT SERVERPROPERTY('ProductVersion') AS Version, SERVERPROPERTY('ProductUpdateLevel') AS CU;"
   ```
   👉 Explication : comparer à la dernière CU publiée sur la page Microsoft des versions de SQL Server (à vérifier).

2. Sauvegarder avant la mise à jour :
   ```powershell
   foreach ($b in 'master','msdb','model','APPDB') { Backup-SqlDatabase -ServerInstance localhost -Database $b -BackupFile "B:\Backup\avant-maj_${b}.bak" -CompressionOption On -Checksum }
   ```
   👉 Explication : sauvegardes de bases ; en complément, prendre un point de contrôle Hyper-V (GUI : Gestionnaire Hyper-V → clic droit sur la VM → Point de contrôle) ou un instantané du virtualiseur.

3. Télécharger la CU depuis le Centre de téléchargement Microsoft et contrôler sa signature :
   ```powershell
   Get-AuthenticodeSignature .\SQLServer2022-KBNUMERO-x64.exe | Select-Object Status,SignerCertificate
   ```
   👉 Explication : remplacer `KBNUMERO` (à remplacer) ; `Status` doit valoir `Valid`.

4. GUI — exécuter le programme de la CU, accepter la licence, sélectionner l'instance, Mettre à jour ; PowerShell silencieux :
   ```powershell
   Start-Process .\SQLServer2022-KBNUMERO-x64.exe -ArgumentList '/quiet','/IAcceptSQLServerLicenseTerms','/Action=Patch','/AllInstances' -Wait
   ```
   👉 Explication : un redémarrage peut être demandé ; l'instance est indisponible pendant la mise à jour.

5. Vérifier le résultat :
   ```powershell
   Get-Service MSSQLSERVER,SQLSERVERAGENT | Select-Object Name,Status
   sqlcmd -S localhost -E -Q "SELECT SERVERPROPERTY('ProductVersion'), SERVERPROPERTY('ProductUpdateLevel');"
   ```
   👉 Explication : la version doit avoir progressé et les applications refonctionner.

6. Retour arrière :
   ```powershell
   Get-HotFix | Where-Object Description -like '*Hotfix*' | Select-Object Description,HotFixID
   ```
   👉 Explication : GUI : Panneau de configuration → Programmes et fonctionnalités → Afficher les mises à jour installées → sélectionner le correctif SQL Server (CU) → Désinstaller. À défaut : restaurer le point de contrôle de la VM. Les mises à jour de SQL Server ne se désinstallent pas toujours proprement : prévoir le point de contrôle comme voie de retour principale.

## 2. Production — Contrôles

Pilote d'abord, fenêtre approuvée, point de contrôle de la VM, sauvegardes validées, test applicatif après correctif.

## 3. Production — Sécurité

- Ne pas appliquer une CU en production sans test préalable.
- Conserver sauvegardes et point de contrôle jusqu'à validation.
- Prévenir les utilisateurs de l'indisponibilité.

## Validation et retour arrière

- **Validation** : la version cible est affichée, les services démarrent, les applications fonctionnent.
- **Retour arrière** : désinstaller la CU ou restaurer le point de contrôle de la VM, puis relancer la recette.

## Si le problème n'est pas résolu

- [SQL Server — Prérequis et limites](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Prerequis_Limites.md)
- [SQL Server — Installer SQL Server et les outils](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Installer.md)
- [SQL Server — Configurer l'instance](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Configurer.md)
- [SQL Server — Sécuriser (authentification, TLS, pare-feu)](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Securiser.md)
- [SQL Server — Valider (recette)](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Valider.md)
- [SQL Server — Sauvegarder et restaurer](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Sauvegarder_Restaurer.md)
- [SQL Server 2022 — installation](https://learn.microsoft.com/fr-fr/sql/database-engine/install-windows/install-sql-server)
- [SQL Server — sauvegarde et restauration](https://learn.microsoft.com/fr-fr/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases)
- [SQL Server — chiffrement des connexions](https://learn.microsoft.com/fr-fr/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine)

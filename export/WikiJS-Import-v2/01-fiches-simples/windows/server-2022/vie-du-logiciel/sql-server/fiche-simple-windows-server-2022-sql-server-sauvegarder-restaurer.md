---
title: "Fiche Simple - Windows Server 2022 SQL-Server Sauvegarder Restaurer"
description: "Sauvegarder les bases (complète, différentielle, journal) et prouver la restauration sur une instance de test."
published: true
date: 2026-10-29T20:38:28Z
tags: ["windows-server-2022", "sql-server", "sqlserver-2022", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:38:28Z
dateModified: 2026-10-29T20:38:28Z
---

# Fiche_Simple_-_Windows_Server_2022_SQL-Server_Sauvegarder_Restaurer

- **Environnement** : VM Windows Server 2022 (SQL Server 2022 Standard ou Developer)
- **OS / Version** : Windows Server 2022; SQL Server 2022 (instance par défaut MSSQLSERVER)
- **Catégorie** : base de données / SQL Server / Sauvegarder et restaurer
- **Tags** : `windows-server-2022`, `sql-server`, `sqlserver-2022`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder les bases (complète, différentielle, journal) et prouver la restauration sur une instance de test.

## 1. Hors-Production (Lab / Test / POC)

1. GUI — SSMS : clic droit sur la base → Tâches → Sauvegarder… ; Type : Complète ; Destination : disque ; Options : vérifier, somme de contrôle, compression :
   ```powershell
   Backup-SqlDatabase -ServerInstance localhost -Database APPDB -BackupFile 'B:\Backup\APPDB_complet.bak' -CompressionOption On -Checksum
   ```
   👉 Explication : remplacer `APPDB` et le chemin (à remplacer) ; le volume de sauvegarde ne doit pas être celui des données.

2. Sauvegarder le journal de transactions (récupération FULL) :
   ```powershell
   Backup-SqlDatabase -ServerInstance localhost -Database APPDB -BackupFile 'B:\Backup\APPDB_journal.trn' -BackupAction Log -Checksum
   ```
   👉 Explication : permet la restauration à un instant donné ; planifier dans l'Agent SQL (GUI : SQL Server Agent → Travaux → Nouveau travail).

3. Sauvegarder les bases système :
   ```powershell
   foreach ($b in 'master','msdb','model') { Backup-SqlDatabase -ServerInstance localhost -Database $b -BackupFile "B:\Backup\${b}.bak" -Checksum }
   ```
   👉 Explication : `master` et `msdb` contiennent logins, travaux et configuration.

4. Vérifier la sauvegarde :
   ```powershell
   sqlcmd -S localhost -E -Q "RESTORE VERIFYONLY FROM DISK = 'B:\Backup\APPDB_complet.bak' WITH CHECKSUM;"
   ```
   👉 Explication : vérifie la lisibilité du fichier, pas le contenu applicatif.

5. GUI — SSMS : clic droit sur Bases de données → Restaurer la base de données… (sur l'instance de test) ; PowerShell équivalent :
   ```powershell
   Restore-SqlDatabase -ServerInstance NOM_INSTANCE_TEST -Database APPDB_TEST -BackupFile 'B:\Backup\APPDB_complet.bak' -RelocateFile @(New-Object Microsoft.SqlServer.Management.Smo.RelocateFile('APPDB','D:\Data\APPDB_TEST.mdf'), New-Object Microsoft.SqlServer.Management.Smo.RelocateFile('APPDB_log','L:\Logs\APPDB_TEST_log.ldf'))
   ```
   👉 Explication : remplacer `NOM_INSTANCE_TEST` et les chemins (à remplacer) ; vérifier les noms logiques avec `RESTORE FILELISTONLY` ; ne jamais restaurer sur la production sans copie préalable.

6. Contrôler la base restaurée :
   ```powershell
   sqlcmd -S NOM_INSTANCE_TEST -E -Q "DBCC CHECKDB (APPDB_TEST) WITH NO_INFOMSGS;"
   ```
   👉 Explication : une sauvegarde n'est valable que si une restauration réussie a été prouvée.

## 2. Production — Contrôles

Plan de sauvegarde (complète, différentielle, journal) planifié, copié hors du serveur (voir les fiches Veeam du pack), chiffré, restauré périodiquement ; surveiller la réussite des travaux.

## 3. Production — Sécurité

- Chiffrer les copies : une sauvegarde contient toutes les données.
- Restreindre l'accès au dossier de sauvegarde au compte de service et aux administrateurs.
- Ne pas stocker les sauvegardes sur le volume des données.

## Validation et retour arrière

- **Validation** : restauration testée, `DBCC CHECKDB` sans erreur.
- **Retour arrière** : utiliser la sauvegarde précédente ; ne jamais écraser la dernière sauvegarde saine.

## Si le problème n'est pas résolu

- [SQL Server — Prérequis et limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-prerequis-limites)
- [SQL Server — Installer SQL Server et les outils](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-installer)
- [SQL Server — Configurer l'instance](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-configurer)
- [SQL Server — Sécuriser (authentification, TLS, pare-feu)](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-securiser)
- [SQL Server — Valider (recette)](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-valider)
- [SQL Server — Mise à jour et retour arrière](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-mettre-a-jour)
- [SQL Server 2022 — installation](https://learn.microsoft.com/fr-fr/sql/database-engine/install-windows/install-sql-server)
- [SQL Server — sauvegarde et restauration](https://learn.microsoft.com/fr-fr/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases)
- [SQL Server — chiffrement des connexions](https://learn.microsoft.com/fr-fr/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine)
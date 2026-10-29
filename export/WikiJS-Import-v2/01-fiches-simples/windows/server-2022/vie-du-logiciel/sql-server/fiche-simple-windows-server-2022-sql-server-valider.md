---
title: "Fiche Simple - Windows Server 2022 SQL-Server Valider"
description: "Prouver que SQL Server est opérationnel, chiffré, accessible aux seuls clients prévus et supervisable."
published: true
date: 2026-10-29T20:38:28Z
tags: ["windows-server-2022", "sql-server", "sqlserver-2022", "recette"]
editor: markdown
dateCreated: 2026-10-29T20:38:28Z
dateModified: 2026-10-29T20:38:28Z
---

# Fiche_Simple_-_Windows_Server_2022_SQL-Server_Valider

- **Environnement** : VM Windows Server 2022 (SQL Server 2022 Standard ou Developer)
- **OS / Version** : Windows Server 2022; SQL Server 2022 (instance par défaut MSSQLSERVER)
- **Catégorie** : base de données / SQL Server / Valider (recette)
- **Tags** : `windows-server-2022`, `sql-server`, `sqlserver-2022`, `recette`

---

## Problème précis à résoudre

Prouver que SQL Server est opérationnel, chiffré, accessible aux seuls clients prévus et supervisable.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les services et la version :
   ```powershell
   Get-Service MSSQLSERVER,SQLSERVERAGENT | Select-Object Name,Status
   sqlcmd -S localhost -E -Q "SELECT SERVERPROPERTY('ProductVersion') AS Version, SERVERPROPERTY('ProductUpdateLevel') AS Niveau, SERVERPROPERTY('Edition') AS Edition;"
   ```
   👉 Explication : les services sont `Running` ; consigner version et niveau de correctif.

2. Tester le réseau depuis un poste client :
   ```powershell
   Test-NetConnection -ComputerName NOM_SERVEUR -Port 1433
   ```
   👉 Explication : `TcpTestSucceeded : True` depuis un client autorisé, `False` depuis un client non autorisé. Remplacer `NOM_SERVEUR` (à remplacer).

3. GUI — SSMS : Se connecter au serveur, Options → Chiffrement : Obligatoire, ne pas cocher « Approuver le certificat du serveur » :
   ```powershell
   sqlcmd -S NOM_SERVEUR -E -N -Q "SELECT encrypt_option FROM sys.dm_exec_connections WHERE session_id = @@SPID;"
   ```
   👉 Explication : `-N` demande le chiffrement ; la connexion doit réussir avec une validation normale du certificat.

4. Écrire et relire une donnée de test :
   ```powershell
   sqlcmd -S NOM_SERVEUR -E -N -d APPDB -Q "CREATE TABLE dbo.recette(id INT); INSERT INTO dbo.recette VALUES (1); SELECT * FROM dbo.recette; DROP TABLE dbo.recette;"
   ```
   👉 Explication : valide droits et écriture ; la table de test est supprimée.

5. Contrôler l'intégrité et les journaux :
   ```powershell
   sqlcmd -S localhost -E -Q "DBCC CHECKDB (APPDB) WITH NO_INFOMSGS; EXEC sp_readerrorlog 0,1,'Error';"
   ```
   👉 Explication : aucune erreur de corruption ni erreur récurrente.

## 2. Production — Contrôles

Consigner la recette ; superviser disponibilité du service, espace disque, tâches de sauvegarde, échéance du certificat, journaux d'erreurs.

## 3. Production — Sécurité

- Supprimer toute donnée et tout compte de test.
- Ne pas approuver aveuglément le certificat du serveur.
- Surveiller les échecs d'ouverture de session.

## Validation et retour arrière

- **Validation** : tous les contrôles réussis et consignés.
- **Retour arrière** : revenir à la configuration précédente puis relancer la recette.

## Si le problème n'est pas résolu

- [SQL Server — Prérequis et limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-prerequis-limites)
- [SQL Server — Installer SQL Server et les outils](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-installer)
- [SQL Server — Configurer l'instance](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-configurer)
- [SQL Server — Sécuriser (authentification, TLS, pare-feu)](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-securiser)
- [SQL Server — Sauvegarder et restaurer](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-sauvegarder-restaurer)
- [SQL Server — Mise à jour et retour arrière](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-mettre-a-jour)
- [SQL Server 2022 — installation](https://learn.microsoft.com/fr-fr/sql/database-engine/install-windows/install-sql-server)
- [SQL Server — sauvegarde et restauration](https://learn.microsoft.com/fr-fr/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases)
- [SQL Server — chiffrement des connexions](https://learn.microsoft.com/fr-fr/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine)
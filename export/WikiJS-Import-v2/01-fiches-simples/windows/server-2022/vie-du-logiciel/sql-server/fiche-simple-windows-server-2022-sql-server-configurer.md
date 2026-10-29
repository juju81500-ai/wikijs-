---
title: "Fiche Simple - Windows Server 2022 SQL-Server Configurer"
description: "Paramétrer la mémoire, le parallélisme, TCP/IP et créer une base et un accès applicatif."
published: true
date: 2026-10-29T20:38:28Z
tags: ["windows-server-2022", "sql-server", "sqlserver-2022", "configuration"]
editor: markdown
dateCreated: 2026-10-29T20:38:28Z
dateModified: 2026-10-29T20:38:28Z
---

# Fiche_Simple_-_Windows_Server_2022_SQL-Server_Configurer

- **Environnement** : VM Windows Server 2022 (SQL Server 2022 Standard ou Developer)
- **OS / Version** : Windows Server 2022; SQL Server 2022 (instance par défaut MSSQLSERVER)
- **Catégorie** : base de données / SQL Server / Configurer l'instance
- **Tags** : `windows-server-2022`, `sql-server`, `sqlserver-2022`, `configuration`

---

## Problème précis à résoudre

Paramétrer la mémoire, le parallélisme, TCP/IP et créer une base et un accès applicatif.

## 1. Hors-Production (Lab / Test / POC)

1. GUI — activer TCP/IP : Gestionnaire de configuration SQL Server → Configuration du réseau SQL Server → Protocoles pour MSSQLSERVER → TCP/IP → Activé :
   ```powershell
   Get-Service MSSQLSERVER
   Restart-Service MSSQLSERVER -Force
   ```
   👉 Explication : le redémarrage du service est nécessaire pour appliquer le changement ; relancer l'Agent SQL ensuite (`Start-Service SQLSERVERAGENT`).

2. GUI — SSMS : clic droit sur le serveur → Propriétés → Mémoire ; Paramètres de base de données :
   ```powershell
   sqlcmd -S localhost -E -Q "EXEC sp_configure 'show advanced options',1; RECONFIGURE; EXEC sp_configure 'max server memory (MB)', MEMOIRE_MAX_MB; EXEC sp_configure 'max degree of parallelism', MAXDOP; EXEC sp_configure 'cost threshold for parallelism', 50; RECONFIGURE;"
   ```
   👉 Explication : remplacer `MEMOIRE_MAX_MB` (laisser de la mémoire à Windows) et `MAXDOP` (à remplacer) selon le dimensionnement ; ne pas laisser la mémoire maximale par défaut.

3. Créer une base applicative :
   ```powershell
   sqlcmd -S localhost -E -Q "CREATE DATABASE APPDB; ALTER DATABASE APPDB SET RECOVERY FULL;"
   ```
   👉 Explication : GUI : SSMS → Bases de données → Nouvelle base de données. Remplacer `APPDB` (à remplacer) ; le mode de récupération FULL permet les sauvegardes de journal.

4. Créer un accès applicatif Windows (recommandé) :
   ```powershell
   sqlcmd -S localhost -E -d APPDB -Q "CREATE LOGIN [DOMAINE\COMPTE_APP] FROM WINDOWS; CREATE USER [DOMAINE\COMPTE_APP] FOR LOGIN [DOMAINE\COMPTE_APP]; ALTER ROLE db_datareader ADD MEMBER [DOMAINE\COMPTE_APP]; ALTER ROLE db_datawriter ADD MEMBER [DOMAINE\COMPTE_APP];"
   ```
   👉 Explication : remplacer `DOMAINE\COMPTE_APP` (à remplacer) ; droits limités à la base, jamais `sysadmin`.

5. Option : créer un login SQL avec mot de passe saisi :
   ```powershell
   $mdp = Read-Host -AsSecureString 'Mot de passe'
   $clair = [System.Net.NetworkCredential]::new('', $mdp).Password
   Invoke-Sqlcmd -ServerInstance localhost -Variable "MDP=$clair" -Query "CREATE LOGIN APPLOGIN WITH PASSWORD = '$(MDP)', CHECK_POLICY = ON;"
   Remove-Variable clair,mdp
   ```
   👉 Explication : uniquement si l'authentification mixte est autorisée ; le mot de passe n'est ni écrit ni affiché ; remplacer `APPLOGIN` (à remplacer).

## 2. Production — Contrôles

Configuration documentée (mémoire, MAXDOP, chemins), revue après tout changement de dimensionnement de la VM.

## 3. Production — Sécurité

- Pas de droit `sysadmin` pour une application.
- Ne pas laisser la mémoire maximale illimitée.
- Préférer l'authentification Windows.

## Validation et retour arrière

- **Validation** : la base existe, l'application se connecte avec ses droits minimaux.
- **Retour arrière** : supprimer la base et les accès de test (`DROP DATABASE`, `DROP LOGIN`) ; remettre les anciens paramètres `sp_configure`.

## Si le problème n'est pas résolu

- [SQL Server — Prérequis et limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-prerequis-limites)
- [SQL Server — Installer SQL Server et les outils](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-installer)
- [SQL Server — Sécuriser (authentification, TLS, pare-feu)](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-securiser)
- [SQL Server — Valider (recette)](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-valider)
- [SQL Server — Sauvegarder et restaurer](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-sauvegarder-restaurer)
- [SQL Server — Mise à jour et retour arrière](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-mettre-a-jour)
- [SQL Server 2022 — installation](https://learn.microsoft.com/fr-fr/sql/database-engine/install-windows/install-sql-server)
- [SQL Server — sauvegarde et restauration](https://learn.microsoft.com/fr-fr/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases)
- [SQL Server — chiffrement des connexions](https://learn.microsoft.com/fr-fr/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine)
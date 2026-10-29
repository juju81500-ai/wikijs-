---
title: "SQL Server"
description: "Sur une instance SQL Server 2022 déjà installée sous Windows Server 2022, vérifier qu'une sauvegarde complète est produite et restaurable, contrôler les comptes de service, et ouvrir le port SQL uniquement aux clients prévus. L'installation de SQL Server n'est pas traitée ici. Les tests ne se font q"
published: true
date: 2026-10-29T12:26:25Z
tags: ["[windows-server-2022]", "[sql-server]", "[base-de-donnees]", "[sauvegarde]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:26:25Z
dateModified: 2026-10-29T12:26:25Z
---

# 📄 SQL Server

- **Environnement** : VM (Windows Server 2022)
- **OS / Version** : Windows Server 2022 (Standard ou Datacenter)
- **Version** : SQL Server 2022 (instance par défaut `MSSQLSERVER`, à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données
- **Tags** : `[windows-server-2022]`, `[sql-server]`, `[base-de-donnees]`, `[sauvegarde]`, `[hardening]`

## 🎯 Problème précis à résoudre
Sur une instance SQL Server 2022 déjà installée sous Windows Server 2022, vérifier qu'une sauvegarde complète est produite et restaurable, contrôler les comptes de service, et ouvrir le port SQL uniquement aux clients prévus. L'installation de SQL Server n'est pas traitée ici. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérification de l'instance et des services :
```powershell
Get-Service MSSQLSERVER, SQLSERVERAGENT | Format-Table Name, Status, StartType
sqlcmd -S localhost -E -Q "SELECT @@VERSION"
```
👉 Explication : Les deux services doivent être `Running`. `sqlcmd -E` se connecte avec le compte Windows courant (authentification intégrée). La version affichée confirme SQL Server 2022.

2. Création d'une base et d'un dossier de sauvegarde de test :
```powershell
New-Item -ItemType Directory -Path D:\Sauvegardes -Force
sqlcmd -S localhost -E -Q "CREATE DATABASE [base_test];"
```
👉 Explication : `D:\Sauvegardes` reçoit les fichiers `.bak`. Le lecteur `D:` est un exemple : utiliser un volume distinct de celui des fichiers de données, quand c'est possible.

3. Sauvegarde complète avec contrôle d'intégrité :
```powershell
sqlcmd -S localhost -E -Q "BACKUP DATABASE [base_test] TO DISK = N'D:\Sauvegardes\base_test.bak' WITH INIT, CHECKSUM, COMPRESSION;"
sqlcmd -S localhost -E -Q "RESTORE VERIFYONLY FROM DISK = N'D:\Sauvegardes\base_test.bak' WITH CHECKSUM;"
```
👉 Explication : `CHECKSUM` vérifie les pages pendant la sauvegarde. `RESTORE VERIFYONLY` contrôle que le fichier est lisible. La réponse attendue se termine par `successfully processed`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un compte de service local dédié, sans droits d'administrateur :
```powershell
$mdp = Read-Host -AsSecureString "Mot de passe du compte de service"
New-LocalUser -Name svc_sql -Password $mdp
Get-LocalUser svc_sql
```
👉 Explication : Le mot de passe est saisi de façon masquée et n'apparaît ni dans l'historique ni dans le script. `svc_sql` est le compte à utiliser pour les services SQL. Le mot de passe est à enregistrer dans le coffre-fort du pack. Sur un domaine Active Directory, un compte gMSA est préférable (à vérifier sur l'environnement).

2. Contrôle du compte exécutant chaque service :
```powershell
Get-CimInstance Win32_Service -Filter "Name='MSSQLSERVER' OR Name='SQLSERVERAGENT'" | Select-Object Name, StartName, State
```
👉 Explication : Affiche le compte de connexion de chaque service. Un compte `LocalSystem` ou un administrateur nominatif n'est pas acceptable en production. Le changement de compte se fait dans le SQL Server Configuration Manager, pour que les droits de service soient attribués correctement.

3. Ouverture du pare-feu uniquement pour les clients prévus :
```powershell
New-NetFirewallRule -DisplayName "SQL Server 1433 TCP entrant" -Direction Inbound -Protocol TCP -LocalPort 1433 -RemoteAddress 192.168.10.0/24 -Action Allow
Get-NetFirewallRule -DisplayName "SQL Server 1433 TCP entrant" | Get-NetFirewallAddressFilter
```
👉 Explication : Le port 1433 TCP n'est accessible qu'au sous-réseau `192.168.10.0/24` (à adapter). Si l'instance utilise un port dynamique ou une instance nommée, la règle doit viser le port réel, à vérifier dans le SQL Server Configuration Manager.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Désactivation du compte `sa` et contrôle des connexions :
```powershell
sqlcmd -S localhost -E -Q "ALTER LOGIN [sa] DISABLE;"
sqlcmd -S localhost -E -Q "SELECT name, is_disabled FROM sys.server_principals WHERE type IN ('S','U','G') ORDER BY name;"
```
👉 Explication : Le compte `sa` est le compte administrateur SQL par défaut. Le désactiver réduit la surface d'attaque. La seconde commande liste les connexions : tout compte inutile doit être supprimé, et tout compte `sysadmin` doit être justifié.

2. Sauvegarde complète et journal, avec dossier réservé aux administrateurs :
```powershell
icacls D:\Sauvegardes /inheritance:r /grant:r "BUILTIN\Administrateurs:(OI)(CI)F" "NT SERVICE\MSSQLSERVER:(OI)(CI)M"
sqlcmd -S localhost -E -Q "BACKUP DATABASE [base_appli] TO DISK = N'D:\Sauvegardes\base_appli.bak' WITH INIT, CHECKSUM, COMPRESSION;"
sqlcmd -S localhost -E -Q "BACKUP LOG [base_appli] TO DISK = N'D:\Sauvegardes\base_appli.trn' WITH CHECKSUM;"
```
👉 Explication : `icacls` retire l'héritage des droits et ne laisse l'accès qu'aux administrateurs et au service SQL. La sauvegarde du journal de transactions n'est possible que si le modèle de récupération est `FULL` (à vérifier avec `SELECT name, recovery_model_desc FROM sys.databases;`). Les fichiers doivent être copiés hors du serveur.

3. Restauration de contrôle sur une machine de test, jamais sur la production :
```powershell
sqlcmd -S localhost -E -Q "RESTORE DATABASE [base_appli_test] FROM DISK = N'D:\Sauvegardes\base_appli.bak' WITH MOVE 'base_appli' TO 'D:\Tests\base_appli_test.mdf', MOVE 'base_appli_log' TO 'D:\Tests\base_appli_test_log.ldf', REPLACE;"
```
👉 Explication : Les noms logiques `base_appli` et `base_appli_log` doivent correspondre à ceux de la base (à vérifier avec `RESTORE FILELISTONLY`). Le dossier `D:\Tests` doit exister. Une sauvegarde non restaurée n'est pas validée.

4. Journal des erreurs et règle de pare-feu active :
```powershell
Get-Content "C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Log\ERRORLOG" -Tail 50
Get-NetFirewallRule -DisplayName "SQL Server 1433 TCP entrant" | Select-Object DisplayName, Enabled, Direction, Action
```
👉 Explication : `ERRORLOG` contient les échecs de connexion et les erreurs de service. Le chemin `MSSQL16` correspond à SQL Server 2022 (à vérifier sur la version déployée). Les échecs de connexion répétés doivent être remontés au responsable sécurité.

---
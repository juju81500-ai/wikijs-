# Fiche_Simple_-_Windows_Server_2022_SQL-Server_Securiser

- **Environnement** : VM Windows Server 2022 (SQL Server 2022 Standard ou Developer)
- **OS / Version** : Windows Server 2022; SQL Server 2022 (instance par défaut MSSQLSERVER)
- **Catégorie** : base de données / SQL Server / Sécuriser (authentification, TLS, pare-feu)
- **Tags** : `windows-server-2022`, `sql-server`, `sqlserver-2022`, `securite`

---

## Problème précis à résoudre

Durcir l'authentification, imposer le chiffrement des connexions et limiter l'accès réseau à SQL Server.

## 1. Hors-Production (Lab / Test / POC)

1. GUI — SSMS : clic droit sur le serveur → Propriétés → Sécurité : Authentification Windows ; Audit de connexion : échecs seulement ou toutes :
   ```powershell
   sqlcmd -S localhost -E -Q "SELECT SERVERPROPERTY('IsIntegratedSecurityOnly') AS WindowsOnly;"
   ```
   👉 Explication : `1` signifie authentification Windows uniquement ; un changement de mode nécessite le redémarrage du service.

2. Désactiver le compte sa :
   ```powershell
   sqlcmd -S localhost -E -Q "ALTER LOGIN sa DISABLE;"
   ```
   👉 Explication : le compte `sa` est une cible connue. Vérifier d'abord qu'un groupe DBA est bien sysadmin.

3. GUI — importer un certificat serveur : MMC → Certificats (ordinateur local) → Personnel → Importer ; puis Gestionnaire de configuration SQL Server → Protocoles pour MSSQLSERVER → Propriétés → onglet Certificat, onglet Indicateurs : Forcer le chiffrement = Oui :
   ```powershell
   Get-ChildItem Cert:\LocalMachine\My | Select-Object Subject,Thumbprint,NotAfter,EnhancedKeyUsageList
   ```
   👉 Explication : le certificat doit avoir l'usage Authentification du serveur, un nom correspondant au FQDN du serveur et la clé privée lisible par le compte de service SQL. Redémarrer le service après la sélection.

4. PowerShell — équivalent registre (identifiant d'instance MSSQL16 attendu pour SQL Server 2022) :
   ```powershell
   $cle = 'HKLM:\SOFTWARE\Microsoft\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQLServer\SuperSocketNetLib'
   Set-ItemProperty -Path $cle -Name Certificate -Value 'EMPREINTE_EN_MINUSCULES'
   Set-ItemProperty -Path $cle -Name ForceEncryption -Value 1
   Restart-Service MSSQLSERVER -Force
   ```
   👉 Explication : remplacer `EMPREINTE_EN_MINUSCULES` par l'empreinte du certificat (à remplacer, sans espaces) ; vérifier le chemin exact de l'instance dans le registre avant écriture.

5. Filtrer le port 1433 au pare-feu Windows :
   ```powershell
   New-NetFirewallRule -DisplayName 'SQL Server 1433' -Direction Inbound -Protocol TCP -LocalPort 1433 -RemoteAddress IP_CLIENT -Action Allow
   ```
   👉 Explication : GUI : Pare-feu Windows Defender avec fonctions avancées de sécurité → Règles de trafic entrant → Nouvelle règle → Port TCP 1433, limiter l'étendue aux IP clientes. Remplacer `IP_CLIENT` (à remplacer).

6. Désactiver SQL Server Browser pour une instance par défaut :
   ```powershell
   Stop-Service SQLBrowser -ErrorAction SilentlyContinue
   Set-Service SQLBrowser -StartupType Disabled
   ```
   👉 Explication : le service n'est utile que pour les instances nommées.

## 2. Production — Contrôles

Certificat d'une AC interne avec échéance supervisée, comptes revus périodiquement, journaux de sécurité Windows et d'erreurs SQL centralisés.

## 3. Production — Sécurité

- Jamais de port 1433 ouvert à Internet.
- Clé privée du certificat protégée, droits limités au compte de service.
- `sa` désactivé, aucun mot de passe en clair.
- Ne pas activer la collecte de télémétrie ou le Browser sans besoin.

## Validation et retour arrière

- **Validation** : `SELECT encrypt_option FROM sys.dm_exec_connections WHERE session_id = @@SPID` renvoie `TRUE` depuis un client distant.
- **Retour arrière** : remettre `ForceEncryption` à 0 et vider `Certificate`, redémarrer le service, supprimer la règle de pare-feu de test.

## Si le problème n'est pas résolu

- [SQL Server — Prérequis et limites](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Prerequis_Limites.md)
- [SQL Server — Installer SQL Server et les outils](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Installer.md)
- [SQL Server — Configurer l'instance](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Configurer.md)
- [SQL Server — Valider (recette)](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Valider.md)
- [SQL Server — Sauvegarder et restaurer](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Sauvegarder_Restaurer.md)
- [SQL Server — Mise à jour et retour arrière](Fiche_Simple_-_Windows_Server_2022_SQL-Server_Mettre_A_Jour.md)
- [SQL Server 2022 — installation](https://learn.microsoft.com/fr-fr/sql/database-engine/install-windows/install-sql-server)
- [SQL Server — sauvegarde et restauration](https://learn.microsoft.com/fr-fr/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases)
- [SQL Server — chiffrement des connexions](https://learn.microsoft.com/fr-fr/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine)

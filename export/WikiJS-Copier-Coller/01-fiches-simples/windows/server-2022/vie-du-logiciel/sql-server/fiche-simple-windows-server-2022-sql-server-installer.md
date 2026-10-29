# Fiche_Simple_-_Windows_Server_2022_SQL-Server_Installer

- **Environnement** : VM Windows Server 2022 (SQL Server 2022 Standard ou Developer)
- **OS / Version** : Windows Server 2022; SQL Server 2022 (instance par défaut MSSQLSERVER)
- **Catégorie** : base de données / SQL Server / Installer SQL Server et les outils

---

## Problème précis à résoudre

Installer le moteur de base de données SQL Server 2022 puis SSMS, de façon assistée ou automatisée.

## 1. Hors-Production (Lab / Test / POC)

1. GUI — monter le média : clic droit sur l'ISO SQL Server → Monter, puis lancer `setup.exe` :
   👉 Explication : le Centre d'installation s'ouvre ; vérifier que le média provient du site Microsoft ou d'un dépôt de licences approuvé.

2. GUI — Installation → Nouvelle installation autonome de SQL Server :
   👉 Explication : assistant : édition ou clé → licence → mises à jour → Règles d'installation → Sélection des fonctionnalités : cocher uniquement `Services Moteur de base de données`.

3. GUI — Configuration de l'instance, des comptes de service et du moteur :
   👉 Explication : instance par défaut (MSSQLSERVER) ; onglet Configuration du moteur : mode d'authentification `Windows`, ajouter le groupe DBA comme administrateur SQL Server, définir les répertoires données/journaux/TempDB/sauvegarde sur les volumes dédiés, onglet Mémoire : mémoire maximale recommandée ; aucun mot de passe `sa` n'est demandé en mode Windows.

4. PowerShell — installation automatisée équivalente (invite élevée) :
   ```powershell
   E:\setup.exe /Q /IACCEPTSQLSERVERLICENSETERMS /ACTION=Install /FEATURES=SQLENGINE /INSTANCENAME=MSSQLSERVER /SQLSYSADMINACCOUNTS="DOMAINE\GROUPE_DBA" /SQLUSERDBDIR="D:\Data" /SQLUSERDBLOGDIR="L:\Logs" /SQLTEMPDBDIR="T:\TempDB" /SQLBACKUPDIR="B:\Backup" /TCPENABLED=1 /UPDATEENABLED=0
   ```
   👉 Explication : remplacer `E:` (lecteur du média), `DOMAINE\GROUPE_DBA` et les chemins (à remplacer) ; aucun mot de passe n'est passé en ligne de commande (comptes virtuels par défaut). `/Q` = installation silencieuse.

5. Installer SSMS (GUI : exécuter le programme d'installation téléchargé depuis le site Microsoft ; PowerShell : winget) :
   ```powershell
   winget search "SQL Server Management Studio"
   winget install --id IDENTIFIANT_SSMS -e
   ```
   👉 Explication : remplacer `IDENTIFIANT_SSMS` par l'identifiant relevé par `winget search` (à vérifier selon la version publiée) ; SSMS peut s'installer sur un poste d'administration plutôt que sur le serveur.

6. Installer le module PowerShell SqlServer :
   ```powershell
   Install-Module -Name SqlServer -Scope AllUsers
   Get-Module -ListAvailable SqlServer | Select-Object Name,Version
   ```
   👉 Explication : fournit `Invoke-Sqlcmd`, `Backup-SqlDatabase`, `Restore-SqlDatabase`.

7. Vérifier le service et la version :
   ```powershell
   Get-Service MSSQLSERVER,SQLSERVERAGENT | Select-Object Name,Status,StartType
   sqlcmd -S localhost -E -Q "SELECT @@VERSION;"
   ```
   👉 Explication : GUI : SSMS → Se connecter à `localhost`, authentification Windows. Le service doit être `Running`.

## 2. Production — Contrôles

Consigner version, édition, chemin des fichiers, compte de service et niveau de correctif (voir la fiche Mise à jour).

## 3. Production — Sécurité

- Média d'origine officielle uniquement.
- Pas de mot de passe dans la ligne de commande ni dans un fichier de configuration.
- Installer uniquement les fonctionnalités nécessaires.

## Validation et retour arrière

- **Validation** : `SELECT @@VERSION` renvoie la version attendue, le service est démarré.
- **Retour arrière** : désinstaller : Paramètres → Applications → Applications installées → Microsoft SQL Server 2022 → Désinstaller (les fichiers de données doivent être sauvegardés avant).

## Si le problème n'est pas résolu

- [SQL Server — Prérequis et limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-prerequis-limites)
- [SQL Server — Configurer l'instance](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-configurer)
- [SQL Server — Sécuriser (authentification, TLS, pare-feu)](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-securiser)
- [SQL Server — Valider (recette)](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-valider)
- [SQL Server — Sauvegarder et restaurer](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-sauvegarder-restaurer)
- [SQL Server — Mise à jour et retour arrière](/01-fiches-simples/windows/server-2022/vie-du-logiciel/sql-server/fiche-simple-windows-server-2022-sql-server-mettre-a-jour)
- [SQL Server 2022 — installation](https://learn.microsoft.com/fr-fr/sql/database-engine/install-windows/install-sql-server)
- [SQL Server — sauvegarde et restauration](https://learn.microsoft.com/fr-fr/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases)
- [SQL Server — chiffrement des connexions](https://learn.microsoft.com/fr-fr/sql/database-engine/configure-windows/enable-encrypted-connections-to-the-database-engine)
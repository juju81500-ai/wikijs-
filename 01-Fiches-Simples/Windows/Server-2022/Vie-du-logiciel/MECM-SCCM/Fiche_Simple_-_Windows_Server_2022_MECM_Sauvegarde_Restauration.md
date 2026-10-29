# Fiche_Simple_-_Windows_Server_2022_MECM_Sauvegarde_Restauration

- **Environnement** : Windows Server 2022, site primaire MECM/SCCM, base SQL Server
- **OS / Version** : Windows Server 2022; Configuration Manager et SQL Server : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC
- **Tags** : `windows-server-2022`, `mecm`, `sccm`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Planifier la sauvegarde du site MECM/SCCM et préparer sa restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Activer la tâche de sauvegarde. GUI : `Administration > Configuration du site > Sites > Paramètres > Tâches de maintenance de site > Sauvegarder le serveur de site`; cocher `Activer`, renseigner le chemin (à remplacer : `\\SERVEUR-SAUVEGARDE\MECM_BACKUP`) et le planning.
   👉 Explication : la tâche utilise le service `SMS_SITE_BACKUP`; le chemin doit être accessible en écriture par le compte machine du serveur de site. Pas d'équivalent PowerShell vérifié ici : vérifier la version publiée.

2. Lancer la sauvegarde. GUI : `Services > Services Windows`.
   ```powershell
   Start-Service SMS_SITE_BACKUP
   ```
   👉 Explication : lance la sauvegarde à la demande; suivre `<dossier d'installation>\Logs\smsbkup.log`.

3. Contrôler le résultat :
   ```powershell
   Get-ChildItem "\\SERVEUR-SAUVEGARDE\MECM_BACKUP" -Recurse | Select-Object -First 20 FullName, LastWriteTime
   ```
   👉 Explication : on doit voir un dossier `CODESITEBackup` récent. Sauvegarder aussi le dossier de contenu (sources des applications) et les certificats, qui ne sont pas tous inclus : vérifier la documentation.

4. Tester la restauration en laboratoire sur une VM isolée : exécuter `setup.exe` du média, choisir `Recover a site`, indiquer le dossier de sauvegarde.
   👉 Explication : la restauration réelle suit la page « Recover sites » de Microsoft; elle dépend du scénario (perte du serveur de site ou de la base). Ne jamais tester sur la production.

## 2. Production — Contrôles

Surveiller le succès quotidien (`Surveillance > État des composants > SMS_SITE_BACKUP`) et réaliser un test de restauration périodique. Ajouter une sauvegarde SQL native selon le plan de l'entreprise.

## 3. Production — Sécurité

- Chemin de sauvegarde restreint (ACL) et chiffré; copie hors site.
- Éviter les snapshots de VM comme seule sauvegarde d'un site : risque d'incohérence avec SQL.

## Validation et retour arrière

- **Validation** : sauvegarde récente, `smsbkup.log` sans erreur, restauration testée en lab.
- **Retour arrière** : désactiver la tâche de maintenance de sauvegarde (même chemin GUI); la restauration elle-même ne s'annule pas : conserver les médias et une copie du jeu de sauvegarde.

## Si le problème n'est pas résolu

- [Fiche d'entrée MECM/SCCM](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_Microsoft-MECM-SCCM.md)
- [Microsoft Learn — Sauvegarde et récupération](https://learn.microsoft.com/en-us/intune/configmgr/core/servers/manage/backup-and-recovery)
- [Microsoft Learn — Sauvegarder un site](https://learn.microsoft.com/en-us/intune/configmgr/core/servers/manage/backup-and-recovery#backup-a-site)
- [Microsoft Learn — Récupérer un site](https://learn.microsoft.com/en-us/intune/configmgr/core/servers/manage/recover-sites)

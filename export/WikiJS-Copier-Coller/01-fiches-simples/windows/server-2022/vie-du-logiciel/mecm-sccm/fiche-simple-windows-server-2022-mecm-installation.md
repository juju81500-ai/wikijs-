# Fiche_Simple_-_Windows_Server_2022_MECM_Installation

- **Environnement** : Windows Server 2022, domaine AD DS, SQL Server et ADK/WinPE déjà installés et conformes à la matrice Microsoft
- **OS / Version** : Windows Server 2022; Configuration Manager current branch : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC

---

## Problème précis à résoudre

Installer un site primaire autonome MECM/SCCM, uniquement après validation de la [fiche Prérequis](/01-fiches-simples/windows/server-2022/vie-du-logiciel/mecm-sccm/fiche-simple-windows-server-2022-mecm-prerequis). Le produit ne s'installe pas sans AD DS, SQL et ADK/WinPE conformes.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les variables (à remplacer) :
   ```powershell
   $Media = "D:\MECM_MEDIA"    # à remplacer : dossier des sources téléchargées
   ```
   👉 Explication : les médias proviennent du centre de licences Microsoft ou de l'évaluation; vérifier la version publiée.

2. Lancer le vérificateur de prérequis. GUI : `splash.hta` du média, puis `Prerequisite checker`.
   ```powershell
   & "$Media\SMSSETUP\BIN\X64\prereqchk.exe" /LOCAL
   ```
   👉 Explication : consulter `C:\ConfigMgrPrereq.log` et corriger chaque erreur avant de poursuivre. Syntaxe exacte à vérifier dans la documentation du vérificateur.

3. Préparer le script d'installation `C:\Temp\mecm_install.ini` (GUI : `splash.hta > Install` pour l'assistant) :
   ```
   [Identification]
   Action=InstallPrimarySite
   [Options]
   ProductID=EVAL
   SiteCode=CODESITE
   SiteName=NOM-DU-SITE
   SMSInstallDir=D:\Program Files\Microsoft Configuration Manager
   SDKServer=SERVEUR-MECM.DOMAINE.LOCAL
   PrerequisiteComp=1
   PrerequisitePath=D:\MECM_MEDIA\PREREQS
   AdminConsole=1
   [SQLConfigOptions]
   SQLServerName=SERVEUR-SQL.DOMAINE.LOCAL
   DatabaseName=CM_CODESITE
   ```
   👉 Explication : toutes les valeurs MAJUSCULES sont à remplacer. `ProductID=EVAL` désigne l'évaluation; une clé de licence ne doit jamais être stockée dans la fiche. La liste complète des clés (et d'autres sections requises) est à vérifier selon la version.

4. Lancer l'installation :
   ```powershell
   & "$Media\SMSSETUP\BIN\X64\setup.exe" /HIDDEN /SCRIPT "C:\Temp\mecm_install.ini"
   ```
   👉 Explication : installation sans assistant, longue; suivre `C:\ConfigMgrSetup.log`.

5. Contrôler le résultat :
   ```powershell
   Get-Content C:\ConfigMgrSetup.log -Tail 20
   Get-Service SMS_EXECUTIVE, SMS_SITE_COMPONENT_MANAGER
   ```
   👉 Explication : les deux services doivent être `Running`. GUI : console `Configuration Manager`, `Surveillance > État du site`.

## 2. Production — Contrôles

Sauvegarder la VM et SQL avant l'installation; installer pendant une fenêtre validée; appliquer ensuite les mises à jour du site (voir la fiche Mise à jour).

## 3. Production — Sécurité

- Compte d'installation dédié, retiré des administrateurs de domaine à la fin.
- Aucun mot de passe ni clé de licence dans le fichier `.ini` conservé; le supprimer après usage.

## Validation et retour arrière

- **Validation** : console ouverte, site `Actif`, services `Running`, aucune erreur dans `ConfigMgrSetup.log`.
- **Retour arrière** : restaurer la VM/le snapshot d'avant installation et la base SQL. Pour une désinstallation, suivre la documentation Microsoft de désinstallation d'un site.

## Si le problème n'est pas résolu

- [Fiche d'entrée MECM/SCCM](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-microsoft-mecm-sccm)
- [Microsoft Learn — Installer des sites en ligne de commande](https://learn.microsoft.com/en-us/intune/configmgr/core/servers/deploy/install/use-the-command-prompt-to-install-sites)
- [Microsoft Learn — Vérificateur de prérequis](https://learn.microsoft.com/en-us/intune/configmgr/core/servers/deploy/install/prerequisite-checker)
- [Microsoft Learn — Options de ligne de commande du programme d'installation](https://learn.microsoft.com/en-us/intune/configmgr/core/servers/deploy/install/command-line-options-for-setup)
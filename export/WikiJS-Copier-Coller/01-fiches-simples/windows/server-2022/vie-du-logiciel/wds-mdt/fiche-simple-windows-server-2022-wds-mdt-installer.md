# Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Installer

- **Environnement** : Windows Server 2022, serveur de déploiement dédié (VM de lab ou serveur), droits administrateur local
- **OS / Version** : Windows Server 2022; WDS (rôle intégré), Windows ADK + module WinPE, MDT : vérifier la version publiée et le statut de support
- **Catégorie** : Automatisation, déploiement et IaC

---

## Problème précis à résoudre

Installer le rôle WDS, Windows ADK (avec WinPE) et MDT sur Windows Server 2022. Limite documentée par Microsoft : sur Windows 11 et les versions futures de Windows Server (dont Windows Server 2025), le déploiement WDS depuis le `boot.wim` des médias d'installation est bloqué ; le PXE vers des images de démarrage personnalisées (MDT, Configuration Manager) reste possible. Ce pack ne propose donc pas de série WDS/MDT pour Windows Server 2025 : voir la [fiche Prérequis et limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-prerequis-limites). Configuration ensuite : [fiche Configurer](/01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-configurer).

## 1. Hors-Production (Lab / Test / POC)

1. Installer le rôle WDS. GUI : `Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités > Services de déploiement Windows` (Serveur de déploiement + Serveur de transport).
   ```powershell
   Install-WindowsFeature -Name WDS -IncludeManagementTools
   Get-WindowsFeature WDS*
   ```
   👉 Explication : installe le rôle et ses outils d'administration ; les sous-rôles doivent afficher `Installed`. Aucune initialisation ici (voir fiche Configurer).

2. Télécharger Windows ADK et le module « Windows PE » depuis la page officielle Microsoft (version correspondant au Windows à déployer), puis les installer. GUI : lancer `adksetup.exe` (cocher « Deployment Tools ») puis `adkwinpesetup.exe`.
   ```powershell
   .\adksetup.exe /norestart /quiet /features OptionId.DeploymentTools
   .\adkwinpesetup.exe /norestart /quiet /features OptionId.WindowsPreinstallationEnvironment
   ```
   👉 Explication : exécuter depuis le dossier de téléchargement. Les noms de fonctionnalités et la version de l'ADK sont à vérifier sur Microsoft Learn avant usage.

3. Installer MDT depuis le package téléchargé sur le site officiel Microsoft (vérifier qu'il est toujours disponible et son statut de support) :
   ```powershell
   msiexec /i .\MicrosoftDeploymentToolkit_x64.msi /qn
   ```
   👉 Explication : MDT s'installe dans `C:\Program Files\Microsoft Deployment Toolkit`. Vérifier la version publiée et la compatibilité avec l'ADK installé.

4. Contrôler les installations :
   ```powershell
   Test-Path "C:\Program Files\Microsoft Deployment Toolkit\bin\MicrosoftDeploymentToolkit.psd1"
   Get-Package -Name "*Deployment Toolkit*","*Windows Assessment*" -ErrorAction SilentlyContinue | Select-Object Name, Version
   ```
   👉 Explication : le `Test-Path` doit renvoyer `True`. `Get-Package` peut ne pas lister tous les composants ; GUI équivalent : `Paramètres > Applications > Applications installées`.

5. Prendre un point de reprise de la VM (lab) avant la configuration.
   👉 Explication : permet de revenir à l'état « logiciels installés, non configurés ».

## 2. Production — Contrôles

Serveur dédié et à jour ; volume NTFS séparé pour `RemoteInstall` et le partage ; ADK, MDT et ISO Windows téléchargés depuis des sources officielles, licences confirmées ; fenêtre de changement validée.

## 3. Production — Sécurité

- Installer avec un compte administrateur nominatif ; ne jamais stocker de mot de passe dans un script.
- Vérifier la signature des installeurs : `Get-AuthenticodeSignature .\adksetup.exe`.

## Validation et retour arrière

- **Validation** : rôle WDS `Installed`, ADK/WinPE et MDT présents.
- **Retour arrière** : `Uninstall-WindowsFeature WDS`, désinstallation de MDT/ADK via `Applications installées`, ou restauration du point de reprise de la VM.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-prerequis-limites)
- [Configurer WDS + MDT](/01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-configurer)
- [Fiche d'entrée WDS/MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-wds-mdt)
- [Microsoft Learn — Fonctionnalités supprimées ou dépréciées de Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/removed-deprecated-features-windows-server)
- [Microsoft Learn — Télécharger et installer l'ADK](https://learn.microsoft.com/en-us/windows-hardware/get-started/adk-install)
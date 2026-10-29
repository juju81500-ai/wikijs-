---
title: "WDS + MDT"
description: "Installer WDS et MDT sur Windows Server 2022, créer un partage de déploiement, intégrer une image Windows 11, publier le démarrage PXE via WDS, puis durcir le partage (compte de lecture dédié, pare-feu restreint) et sauvegarder le partage avant d'installer les postes de l'entreprise."
published: true
date: 2026-10-29T12:26:06Z
tags: ["[windows-server-2022]", "[wds]", "[mdt]", "[pxe]", "[deploiement]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:26:06Z
dateModified: 2026-10-29T12:26:06Z
---

# 📄 WDS + MDT

- **Environnement** : VM (Windows Server 2022), disque de données dédié au partage de déploiement
- **OS / Version** : Windows Server 2022 (Standard ou Datacenter), PowerShell 5.1
- **Version** : WDS (rôle Windows Server), MDT 8456 et Windows ADK (versions à vérifier sur la version déployée)
- **Catégorie** : Automatisation, déploiement et IaC
- **Tags** : `[windows-server-2022]`, `[wds]`, `[mdt]`, `[pxe]`, `[deploiement]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer WDS et MDT sur Windows Server 2022, créer un partage de déploiement, intégrer une image Windows 11, publier le démarrage PXE via WDS, puis durcir le partage (compte de lecture dédié, pare-feu restreint) et sauvegarder le partage avant d'installer les postes de l'entreprise.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du rôle WDS et initialisation du serveur :
```powershell
Install-WindowsFeature -Name WDS -IncludeManagementTools
wdsutil /Initialize-Server /RemInst:"C:\RemoteInstall"
wdsutil /Set-Server /AnswerClients:All
Get-WindowsFeature WDS*
```
👉 Explication : Installe le rôle WDS et crée le dossier `C:\RemoteInstall`, qui stocke les images de démarrage réseau. `/AnswerClients:All` répond à tous les postes PXE, réglage de lab uniquement. Le rôle `WDS-Deployment` doit afficher `Installed`.

2. Installation de Windows ADK et de l'extension WinPE :
```powershell
.\adksetup.exe /norestart /quiet /features OptionId.DeploymentTools OptionId.UserStateMigrationTool
.\adkwinpesetup.exe /norestart /quiet /features OptionId.WindowsPreinstallationEnvironment
```
👉 Explication : Ces deux programmes, téléchargés depuis le site Microsoft, installent les outils de déploiement et l'environnement de démarrage WinPE nécessaires à MDT. Les noms des fonctionnalités et la version de l'ADK sont à vérifier sur la version déployée.

3. Installation de MDT :
```powershell
msiexec /i .\MicrosoftDeploymentToolkit_x64.msi /qn
```
👉 Explication : Installation silencieuse de Microsoft Deployment Toolkit (MDT 8456, version à vérifier) dans `C:\Program Files\Microsoft Deployment Toolkit`.

4. Création du partage de déploiement :
```powershell
Import-Module "C:\Program Files\Microsoft Deployment Toolkit\bin\MicrosoftDeploymentToolkit.psd1"
New-Item -ItemType Directory -Path "D:\DeploymentShare$" -Force
New-SmbShare -Name "DeploymentShare$" -Path "D:\DeploymentShare$" -FullAccess "Administrateurs"
New-PSDrive -Name DS001 -PSProvider MDTProvider -Root "D:\DeploymentShare$"
```
👉 Explication : Charge le module MDT, crée le dossier du partage, le publie en partage masqué (`$`) et monte le lecteur `DS001:` pour les commandes MDT. Remplacer `Administrateurs` par le nom du groupe local, à vérifier selon la langue du système.

5. Import d'un système d'exploitation depuis l'ISO monté :
```powershell
Import-MDTOperatingSystem -Path "DS001:\Operating Systems" -SourcePath "E:\" -DestinationFolder "W11-x64"
```
👉 Explication : Copie les fichiers de l'ISO Windows 11 (monté en lecteur `E:`, à adapter) dans le partage, sous le dossier `W11-x64`. L'opération dure plusieurs minutes.

6. Mise à jour du partage et intégration de WDS :
```powershell
Update-MDTDeploymentShare -Path "DS001:"
wdsutil /Add-Image /ImageFile:"D:\DeploymentShare$\Boot\LiteTouchPE_x64.wim" /Server:localhost /ImageType:Boot
Get-ChildItem "D:\DeploymentShare$\Boot"
```
👉 Explication : `Update-MDTDeploymentShare` génère l'image de démarrage `LiteTouchPE_x64.wim`. `wdsutil /Add-Image` la publie dans WDS. Le fichier doit exister dans `D:\DeploymentShare$\Boot`.

7. Création de la séquence de tâches et test PXE :
```powershell
New-MDTTaskSequence -Path "DS001:\Task Sequences" -Name "Deploiement Windows 11" -Template "StandardClient.xml" -ID "W11-001" -OperatingSystemPath "DS001:\Operating Systems\<nom_image_os>" -FullName "<nom_complet>" -OrgName "<nom_organisation>" -HomePage "about:blank"
```
👉 Explication : Crée une séquence de déploiement standard Windows 11 liée à l'image importée. Les paramètres de propriétaire sont à remplacer. Le nom exact de l'image est visible dans `DS001:\Operating Systems`. Le test réel se fait en démarrant un poste de test en PXE (F12 au démarrage).

---

## ⚡ 2. Production — Façon Simplifiée
1. Ouverture du pare-feu pour les services de déploiement :
```powershell
Enable-NetFirewallRule -DisplayGroup "Windows Deployment Services"
Get-NetFirewallRule -DisplayGroup "Windows Deployment Services" | Select-Object DisplayName, Enabled
```
👉 Explication : Active les règles de pare-feu WDS prédéfinies. Restreindre ensuite le réseau source à la plage des postes, dans la console du pare-feu, si l'entreprise l'impose.

2. Réglage du mode de réponse PXE :
```powershell
wdsutil /Set-Server /PxePromptPolicy /Known:OptIn /New:OptIn
wdsutil /Get-Server /Show:Config
```
👉 Explication : Demande une validation manuelle à l'administrateur avant qu'un poste inconnu démarre sur le déploiement. La syntaxe exacte de la stratégie PXE est à vérifier sur la version déployée avec `wdsutil /?`.

3. Contrôle du partage et des services :
```powershell
Get-Service WDSServer, LanmanServer | Select-Object Name, Status
Get-SmbShare -Name "DeploymentShare$"
```
👉 Explication : `WDSServer` et `LanmanServer` doivent être `Running`. Le partage `DeploymentShare$` doit être listé.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Création d'un compte de lecture dédié pour le partage MDT :
```powershell
$mdp = Read-Host -AsSecureString "Mot de passe du compte MDT_BA"
New-LocalUser -Name "MDT_BA" -Password $mdp -PasswordNeverExpires -Description "Lecture seule partage MDT"
Grant-SmbShareAccess -Name "DeploymentShare$" -AccountName "MDT_BA" -AccessRight Read -Force
```
👉 Explication : Le compte `MDT_BA` ne sert qu'à lire le partage pendant l'installation. Il ne doit pas être administrateur. Le mot de passe saisi en lecture sécurisée n'apparaît pas à l'écran, et il est à stocker dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack).

2. Suppression des droits larges sur le partage :
```powershell
Revoke-SmbShareAccess -Name "DeploymentShare$" -AccountName "Tout le monde" -Force
Get-SmbShareAccess -Name "DeploymentShare$"
```
👉 Explication : Retire le droit donné à tous les utilisateurs si présent. La sortie ne doit lister que les administrateurs et `MDT_BA`. Le nom `Tout le monde` est celui de la langue française, à vérifier.

3. Renseignement sécurisé du compte dans la configuration MDT :
```powershell
notepad "D:\DeploymentShare$\Control\Bootstrap.ini"
```
Ajouter, en remplaçant les valeurs entre chevrons :
```
[Settings]
UserID=MDT_BA
UserDomain=<nom_serveur>
```
👉 Explication : Dans MDT, le compte de connexion au partage se renseigne dans `Bootstrap.ini` (et non dans `CustomSettings.ini`). Ne jamais écrire le mot de passe dans ce fichier : il se saisit au démarrage ou se gère avec un outil dédié, à vérifier selon la version de MDT. Le compte `MDT_BA` doit exister sur ce serveur (`UserDomain`).

4. Sauvegarde du partage de déploiement :
```powershell
robocopy "D:\DeploymentShare$" "E:\Sauvegarde\DeploymentShare" /MIR /R:2 /W:5 /LOG:"E:\Sauvegarde\robocopy-$(Get-Date -Format yyyy-MM-dd).log"
```
👉 Explication : Copie miroir du partage (scripts, images, séquences) vers un disque distinct. Le code de sortie de `robocopy` inférieur à 8 indique une copie réussie. Une copie hors du serveur est à prévoir pour les images et la configuration.

---
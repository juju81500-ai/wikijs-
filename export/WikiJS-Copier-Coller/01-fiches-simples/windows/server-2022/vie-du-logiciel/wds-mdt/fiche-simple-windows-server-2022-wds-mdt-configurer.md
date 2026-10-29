# Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Configurer

- **Environnement** : Windows Server 2022, WDS, ADK/WinPE et MDT installés, ISO Windows 11 officiel monté, réseau de lab isolé
- **OS / Version** : Windows Server 2022; WDS, MDT : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC

---

## Problème précis à résoudre

Initialiser WDS, créer le partage de déploiement MDT, importer un système, générer l'image de démarrage LiteTouch, la publier dans WDS et créer une séquence de tâches. Installation préalable : [fiche Installer](/01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-installer). Le durcissement est traité dans la [fiche Sécurisation](/01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-securisation).

## 1. Hors-Production (Lab / Test / POC)

1. Initialiser WDS. GUI : `Outils d'administration > Services de déploiement Windows > clic droit sur le serveur > Configurer le serveur`.
   ```powershell
   wdsutil /Initialize-Server /RemInst:"D:\RemoteInstall"
   wdsutil /Set-Server /AnswerClients:Known
   ```
   👉 Explication : `D:\RemoteInstall` est à remplacer par un volume NTFS dédié. `Known` ne répond qu'aux postes pré-déclarés ; `All` est réservé à un lab isolé.

2. Créer le partage de déploiement MDT. GUI : `Deployment Workbench > Deployment Shares > New Deployment Share`.
   ```powershell
   Import-Module "C:\Program Files\Microsoft Deployment Toolkit\bin\MicrosoftDeploymentToolkit.psd1"
   New-Item -ItemType Directory -Path 'D:\DeploymentShare$' -Force
   New-SmbShare -Name 'DeploymentShare$' -Path 'D:\DeploymentShare$' -ReadAccess "DOMAINE\GROUPE-LECTURE-DEPLOIEMENT"
   New-PSDrive -Name DS001 -PSProvider MDTProvider -Root 'D:\DeploymentShare$'
   ```
   👉 Explication : `DOMAINE\GROUPE-LECTURE-DEPLOIEMENT` est à remplacer par un groupe de lecture dédié (aucun secret dans le script). Le `$` rend le partage masqué ; les apostrophes évitent l'expansion PowerShell.

3. Importer le système d'exploitation depuis l'ISO monté (GUI : `Operating Systems > Import Operating System`) :
   ```powershell
   Import-MDTOperatingSystem -Path "DS001:\Operating Systems" -SourcePath "E:\" -DestinationFolder "W11-x64"
   ```
   👉 Explication : `E:\` est à remplacer par la lettre de l'ISO monté. Image sous licence valide uniquement.

4. Générer l'image de démarrage et la publier dans WDS :
   ```powershell
   Update-MDTDeploymentShare -Path "DS001:"
   wdsutil /Add-Image /ImageFile:'D:\DeploymentShare$\Boot\LiteTouchPE_x64.wim' /Server:localhost /ImageType:Boot
   ```
   👉 Explication : l'image personnalisée LiteTouch est le chemin non bloqué par la dépréciation WDS (voir fiche Prérequis). Ne pas publier le `boot.wim` des médias Windows 11.

5. Créer la séquence de tâches (GUI : `Task Sequences > New Task Sequence`) :
   ```powershell
   New-MDTTaskSequence -Path "DS001:\Task Sequences" -Name "Deploiement Windows 11" -Template "Client.xml" -ID "W11-001" -OperatingSystemPath "DS001:\Operating Systems\NOM-IMAGE-OS" -FullName "NOM-COMPLET" -OrgName "NOM-ORGANISATION" -HomePage "about:blank"
   ```
   👉 Explication : `NOM-IMAGE-OS`, `NOM-COMPLET` et `NOM-ORGANISATION` sont à remplacer ; le nom exact de l'image est visible sous `DS001:\Operating Systems`. Le modèle `Client.xml` est à vérifier dans la version de MDT installée.

## 2. Production — Contrôles

Réponse PXE restreinte, options DHCP 66/67 ou relais validés avec l'équipe réseau, volume dimensionné, séquence de tâches testée sur une VM avant tout poste réel.

## 3. Production — Sécurité

- Aucun mot de passe dans `Bootstrap.ini` ni `CustomSettings.ini` ; compte de jonction au domaine à privilèges minimaux, saisi hors fichier.
- Partage en lecture pour le groupe dédié uniquement ; réseau PXE segmenté.

## Validation et retour arrière

- **Validation** : `wdsutil /Get-AllImages /Show:Boot` liste l'image LiteTouch ; recette PXE dans la [fiche Recette](/01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-recette).
- **Retour arrière** : `wdsutil /Remove-Image` pour l'image, `Remove-SmbShare -Name 'DeploymentShare$'`, ou restauration depuis la [sauvegarde](/01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-sauvegarde-restauration).

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-prerequis-limites)
- [Installer WDS + MDT](/01-fiches-simples/windows/server-2022/vie-du-logiciel/wds-mdt/fiche-simple-windows-server-2022-wds-mdt-installer)
- [Procédure historique WDS + MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-simple-wds-mdt)
- [Microsoft Learn — wdsutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil)
- [Microsoft Learn — Fonctionnalités supprimées ou dépréciées de Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/removed-deprecated-features-windows-server)
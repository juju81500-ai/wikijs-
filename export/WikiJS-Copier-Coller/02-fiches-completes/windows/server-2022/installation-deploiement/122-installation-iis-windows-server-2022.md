# Installer et préparer IIS sur Windows Server 2022

- **OS / Version** : Windows Server 2022; rôle Web Server (IIS) et composants correspondant à l'application
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : ajout du rôle IIS, site pilote statique, validation de base et sauvegarde de configuration
- **Catégorie** : serveur Web / application

## 1. Périmètre et prérequis

Fiche simple : [vérifier périmètre et prérequis](/01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-perimetre-prerequis).

Cette fiche installe IIS sur un serveur pilote et vérifie un site statique local. Elle ne déploie pas de runtime applicatif, base de données, reverse proxy, cluster Web Farm, Active Directory Certificate Services ou application de production.

Prérequis : Windows Server 2022 à jour, accès administrateur approuvé, nom DNS et certificat prévus, pare-feu administré, sauvegarde de la VM et plan de changement. Déterminer les seuls modules IIS nécessaires à l'application; éviter d'installer les fonctionnalités optionnelles par défaut sans revue.

## 2. Installer le rôle Web Server

Fiche simple : [installer le rôle Web Server](/01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-installer-role-web-server).

Dans une session PowerShell élevée, vérifier l'état des fonctionnalités, puis installer le rôle et les outils d'administration :

```powershell
Get-WindowsFeature Web-Server, Web-Mgmt-Tools
Install-WindowsFeature -Name Web-Server -IncludeManagementTools
Get-WindowsFeature Web-Server, Web-Mgmt-Tools
```

L'installation de fonctionnalités modifie le système; effectuer cette opération sur un pilote et suivre la politique de redémarrage de l'organisation. Installer ensuite uniquement les composants (`Web-*`) requis par le runtime ou protocole documenté.

## 3. Préparer un site pilote minimal

Fiche simple : [préparer un site pilote minimal](/01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-site-pilote-minimal).

Créer un répertoire de site distinct et un fichier de test, sans données métier :

```powershell
New-Item -ItemType Directory -Path 'C:\Sites\Pilote' -Force
Set-Content -Path 'C:\Sites\Pilote\index.html' -Value '<!doctype html><title>IIS pilote</title><h1>IIS pilote</h1>' -Encoding UTF8
```

Dans IIS Manager, créer un site nommé `Pilote` sur ce chemin et l'affecter à un pool dédié. Pour une application réelle, choisir l'identité de pool dédiée avec les permissions NTFS minimales sur les seuls fichiers nécessaires; ne pas accorder `Everyone:FullControl` ni utiliser un compte Administrateur. Configurer un binding qui correspond au nom DNS et au certificat prévu.

Ne pas exposer le site à Internet avant d'avoir défini les bindings, TLS, journaux, mises à jour, authentification et règles réseau. Pour un pilote local, limiter le test à localhost ou à un réseau d'administration.

## 4. Vérifier le service et le site

Fiche simple : [vérifier le service et le site](/01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-verifier-service-site).

```powershell
Get-Service W3SVC
& "$env:windir\System32\inetsrv\appcmd.exe" list site
& "$env:windir\System32\inetsrv\appcmd.exe" list apppool 'Pilote'
Invoke-WebRequest -Uri 'http://localhost/' -UseBasicParsing
```

Confirmer le code de réponse, les journaux IIS dans `%SystemDrive%\inetpub\logs\LogFiles`, l'identité et l'état du pool. En environnement cible, tester le nom DNS et le certificat depuis un poste client approuvé.

## 5. Sécurité, sauvegarde et maintenance

Fiche simple : [sécuriser, sauvegarder et maintenir](/01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-securite-sauvegarde-maintenance).

- Autoriser uniquement les ports et sources nécessaires dans Windows Defender Firewall; toute règle entrante doit avoir un profil et un périmètre explicitement définis.
- Utiliser HTTPS avec un certificat valide; désactiver les bindings HTTP uniquement après validation complète de HTTPS et des dépendances de l'application.
- Retirer les modules inutiles, limiter les méthodes HTTP et les permissions, désactiver l'indexation de répertoire et ne pas placer de secrets dans le contenu Web.
- Protéger les journaux, fixer une politique de rétention et surveiller les erreurs, l'espace disque et l'état des pools.
- Avant un changement de configuration, créer une sauvegarde IIS :

```powershell
& "$env:windir\System32\inetsrv\appcmd.exe" add backup 'AvantChangement'
```

Cette sauvegarde couvre la configuration IIS, pas le contenu du site, les certificats privés ni les bases de données. Les sauvegarder séparément par les mécanismes approuvés.

## 6. Retour arrière

Fiche simple : [revenir en arrière](/01-fiches-simples/windows/server-2022/vie-du-logiciel/iis/fiche-simple-vm-windows-server-2022-iis-retour-arriere).

Restaurer la sauvegarde IIS uniquement après avoir identifié l'état à restaurer et conservé la configuration actuelle :

```powershell
& "$env:windir\System32\inetsrv\appcmd.exe" list backup
```

La commande de restauration remplace la configuration IIS active; suivre la procédure Microsoft et pratiquer d'abord sur une VM isolée. Pour un changement applicatif, remettre la version de contenu précédente et confirmer les ACL, bindings, certificat et état du pool. Ne pas désinstaller le rôle pour résoudre un incident sans plan de dépendances.

## Sources

- [Microsoft Learn — documentation IIS](https://learn.microsoft.com/en-us/iis/)
- [Microsoft Learn — installer le rôle Web Server](https://learn.microsoft.com/en-us/windows-server/networking/core-network-guide/cncg/server-certs/install-the-web-server-web1)
- [Microsoft Learn — PowerShell Install-WindowsFeature](https://learn.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Microsoft Learn — AppCmd.exe](https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe)
- [Microsoft Learn — IIS application pools](https://learn.microsoft.com/en-us/iis/configuration/system.applicationhost/applicationpools/)

Le site pilote, les bindings, TLS, les modules et la restauration doivent être validés sur un serveur de test avant production.
---
title: "Fiche Simple - VM Windows Server 2022 Installation IIS Site Web"
description: "Installer le rôle IIS sur Windows Server 2022, vérifier le site par défaut et préparer une ouverture réseau limitée aux flux web réellement nécessaires."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-server-2022]", "[iis]", "[web]", "[installation]", "[gui]", "[powershell]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Installation_IIS_Site_Web.md

- **Environnement** : VM Windows Server
- **OS / Version** : Windows Server 2022
- **Catégorie** : Installation / Services Web
- **Tags** : `[windows-server-2022]`, `[iis]`, `[web]`, `[installation]`, `[gui]`, `[powershell]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer le rôle IIS sur Windows Server 2022, vérifier le site par défaut et préparer une ouverture réseau limitée aux flux web réellement nécessaires.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Dans PowerShell lancé en administrateur, installer IIS avec les outils de gestion :
   ```powershell
   Install-WindowsFeature -Name Web-Server -IncludeManagementTools
   ```
2. Vérifier l'installation et le service :
   ```powershell
   Get-WindowsFeature Web-Server
   Get-Service W3SVC
   ```
3. Depuis le serveur, tester la page locale :
   ```powershell
   Invoke-WebRequest http://localhost -UseBasicParsing
   ```
   👉 *Explication : Le test local vérifie IIS sans exposer le site au réseau.*

## ⚡ 2. Production — Façon Simplifiée
### Installation en interface graphique
1. Ouvrir **Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités**.
2. Choisir **Installation basée sur un rôle ou une fonctionnalité**, sélectionner le serveur cible, puis cocher **Serveur Web (IIS)**.
3. Ajouter uniquement les composants nécessaires à l'application, confirmer l'installation, puis ouvrir **Gestionnaire des services Internet (IIS)**.
4. Vérifier le site et le chemin de contenu dans **Sites > Default Web Site > Paramètres de base...**. Remplacer la page par défaut seulement après validation de l'application.

### Installation avec PowerShell
```powershell
Install-WindowsFeature -Name Web-Server -IncludeManagementTools
Get-WindowsFeature Web-Server
Get-Service W3SVC
```
👉 *Explication : `Web-Server` installe le rôle; les modules d'application et l'ouverture réseau restent à adapter au besoin réel.*

## 🔒 3. Production — Façon Sécurisée
1. Dans **Pare-feu Windows Defender avec fonctions avancées de sécurité**, créer ou vérifier une règle entrante TCP limitée à la source, au profil réseau et aux ports réellement nécessaires (généralement 443; 80 uniquement si le scénario l'exige).
2. Pour un site public, configurer un certificat TLS valide et vérifier le binding HTTPS dans IIS avant d'exposer le service. Ne pas considérer le site de démonstration par défaut comme une application prête pour la production.
3. Installer uniquement les fonctionnalités IIS utilisées, maintenir Windows et l'application à jour, et appliquer des permissions minimales au répertoire de contenu.
4. Avant modification, sauvegarder la configuration IIS et le contenu du site; ne pas désactiver globalement le pare-feu pour résoudre un problème de connectivité.

## ✅ Validation et retour arrière
- Tester le site en local puis depuis un poste autorisé; vérifier le binding, le certificat, les journaux IIS et les règles de pare-feu.
- Pour retirer le rôle après sauvegarde et vérification des dépendances :
  ```powershell
  Uninstall-WindowsFeature -Name Web-Server
  ```
- Après toute modification de binding ou de règle, retester depuis une nouvelle connexion et conserver l'accès d'administration.

## 🔗 Si le problème n'est pas résolu
- Examiner **Observateur d'événements > Journaux Windows > Système/Application** et les journaux de requêtes IIS sous `%SystemDrive%\inetpub\logs\LogFiles`.
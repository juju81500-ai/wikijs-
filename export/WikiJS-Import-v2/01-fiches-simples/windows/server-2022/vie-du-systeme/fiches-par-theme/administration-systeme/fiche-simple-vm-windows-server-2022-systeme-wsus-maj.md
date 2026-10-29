---
title: "Fiche Simple - VM Windows Server 2022 Systeme WSUS Maj"
description: "Installer un serveur WSUS sur Windows Server 2022 pour distribuer les mises à jour Microsoft aux machines du parc, puis pointer les clients vers ce serveur au lieu de Windows Update Internet, et contrôler l'approbation des correctifs."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-server-2022]", "[wsus]", "[windows-update]", "[gpo]", "[powershell]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Systeme_WSUS_Maj

- **Environnement** : VM (Windows Server 2022, serveur WSUS) / Postes et serveurs clients du domaine
- **OS / Version** : Windows Server 2022 - Famille Windows Server
- **Catégorie** : Système & Services / Mises à jour
- **Tags** : `[windows-server-2022]`, `[wsus]`, `[windows-update]`, `[gpo]`, `[powershell]`

## 🎯 Problème précis à résoudre
Installer un serveur WSUS sur Windows Server 2022 pour distribuer les mises à jour Microsoft aux machines du parc, puis pointer les clients vers ce serveur au lieu de Windows Update Internet, et contrôler l'approbation des correctifs.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Préparer le dossier de contenu et installer le rôle WSUS :
   ```powershell
   New-Item -ItemType Directory -Path "D:\WSUS" -Force | Out-Null
   Install-WindowsFeature -Name UpdateServices -IncludeManagementTools
   ```
   👉 Explication : Crée le dossier où WSUS stocke les fichiers de mise à jour, puis installe le rôle avec sa console d'administration.
2. Terminer la configuration WSUS avec la base interne (WID) :
   ```powershell
   & "$env:ProgramFiles\Update Services\Tools\wsusutil.exe" postinstall CONTENT_DIR=D:\WSUS
   ```
   👉 Explication : Lance la post-installation, qui configure le répertoire de contenu et les services WSUS.
3. Vérifier que les services WSUS et IIS sont démarrés :
   ```powershell
   Get-Service -Name WSUSService, W3SVC | Select-Object Name, Status, StartType
   ```
   👉 Explication : Confirme que le serveur répond avant de configurer les clients.

**Équivalent interface graphique :**

- **Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités > Services WSUS**, indiquer le dossier de contenu `D:\WSUS`, puis **Outils > Services WSUS** pour l'assistant de configuration.
  👉 Explication : équivalent de `Install-WindowsFeature` et `wsusutil postinstall`.
- **Win + R** > `services.msc` : vérifier **WSUSService** et **World Wide Web Publishing Service**.
  👉 Explication : équivalent de `Get-Service`.

## ⚡ 2. Production — Façon Simplifiée
1. Pointer un poste ou serveur client vers le WSUS interne :
   ```powershell
   $wu = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate"
   New-Item -Path "$wu\AU" -Force | Out-Null
   Set-ItemProperty -Path $wu -Name "WUServer" -Value "http://<nom_serveur_wsus>:8530" -Type String
   Set-ItemProperty -Path $wu -Name "WUStatusServer" -Value "http://<nom_serveur_wsus>:8530" -Type String
   Set-ItemProperty -Path "$wu\AU" -Name "UseWUServer" -Value 1 -Type DWord
   ```
   👉 Explication : Écrit les clés de stratégie équivalentes à la GPO « Spécifier l'emplacement intranet du service de mise à jour Microsoft ». En production, appliquer ces valeurs par GPO plutôt que localement.
2. Forcer une analyse sur le client et contrôler le résultat :
   ```powershell
   UsoClient.exe StartScan
   Get-WinEvent -LogName "Microsoft-Windows-WindowsUpdateClient/Operational" -MaxEvents 20 | Select-Object TimeCreated, Id, Message
   ```
   👉 Explication : Lance une recherche de mises à jour auprès du WSUS et affiche les derniers événements du client Windows Update.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Lister les correctifs critiques et de sécurité non approuvés sur le WSUS :
   ```powershell
   Import-Module UpdateServices
   Get-WsusUpdate -Classification "Critical Updates" -Approval Unapproved | Select-Object -First 20
   ```
   👉 Explication : Prépare la liste des correctifs à valider. Les mises à jour ne doivent pas être approuvées directement pour tout le parc.
2. Approuver les correctifs critiques uniquement pour un groupe pilote, après test :
   ```powershell
   Get-WsusUpdate -Classification "Critical Updates" -Approval Unapproved | Approve-WsusUpdate -Action Install -TargetGroupName "<nom_groupe_pilote>"
   ```
   👉 Explication : Installe les correctifs sur le groupe pilote, avant un déploiement progressif vers les autres groupes d'ordinateurs.
3. Contrôler la politique de redémarrage automatique et le mode de mise à jour :
   ```powershell
   $au = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"
   Set-ItemProperty -Path $au -Name "AUOptions" -Value 4 -Type DWord
   Set-ItemProperty -Path $au -Name "NoAutoRebootWithLoggedOnUsers" -Value 1 -Type DWord
   ```
   👉 Explication : AUOptions 4 télécharge et planifie l'installation automatiquement. NoAutoRebootWithLoggedOnUsers évite un redémarrage pendant qu'un utilisateur est connecté.
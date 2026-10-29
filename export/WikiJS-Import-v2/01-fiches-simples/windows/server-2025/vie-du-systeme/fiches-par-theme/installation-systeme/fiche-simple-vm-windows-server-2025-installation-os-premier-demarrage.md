---
title: "Fiche Simple - VM Windows Server 2025 Installation OS Premier Demarrage"
description: "Installer Windows Server 2025 en choisissant l'expérience Core/Desktop adaptée et vérifier les prérequis matériels et différences par défaut avant d'appliquer les fiches Windows Server 2022."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-server-2025]", "[installation]", "[vm]", "[server-core]", "[compatibilite]", "[premier-demarrage]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Windows_Server_2025_Installation_OS_Premier_Demarrage.md

- **Environnement** : VM ou serveur Windows
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : Installation / Système / Compatibilité
- **Tags** : `[windows-server-2025]`, `[installation]`, `[vm]`, `[server-core]`, `[compatibilite]`, `[premier-demarrage]`

## 🎯 Problème précis à résoudre
Installer Windows Server 2025 en choisissant l'expérience Core/Desktop adaptée et vérifier les prérequis matériels et différences par défaut avant d'appliquer les fiches Windows Server 2022.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Obtenir l'ISO depuis une source Microsoft autorisée et vérifier édition/licence.
2. Vérifier le modèle CPU virtuel : Server 2025 requiert notamment SSE4.2 et POPCNT. Prévoir au moins 2 Go de RAM pour le setup VM, davantage pour les rôles.
3. Créer la VM avec UEFI/contrôleur disque adaptés, monter l'ISO et choisir explicitement **Server Core** ou **Server with Desktop Experience**.
4. Après installation et premier démarrage, vérifier :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-WindowsFeature | Where-Object Installed
   Get-NetIPConfiguration
   Get-Service sshd -ErrorAction SilentlyContinue
   ```
   👉 *Explication : l'installation Core/Desktop Experience ne se convertit pas après coup; un changement exige une installation propre.*

**Équivalent interface graphique :**

- **Gestionnaire de serveur > Serveur local** (nom, build, réseau), **Gestion des disques** (`diskmgmt.msc`).
  👉 Explication : équivalent graphique des commandes de contrôle après installation.

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier avec l'éditeur de chaque rôle et application que Windows Server 2025 est pris en charge.
2. Installer et mettre à jour le système; configurer hostname, IP/DNS, heure, compte d'administration et console via les fiches serveur correspondantes.
3. Vérifier les nouveaux comportements à l'aide de la fiche de compatibilité Server 2025 avant d'activer des rôles SMB, AD DS, RRAS ou OpenSSH.
4. Installer uniquement les rôles requis, puis effectuer un redémarrage et une sauvegarde initiale avant la mise en service.

## 🔒 3. Production — Façon Sécurisée
1. Ne pas rétrograder les protections SMB/LDAP ou désactiver Credential Guard pour contourner un client ancien sans étude d'impact approuvée.
2. Conserver l'accès console; limiter RDP et SSH aux réseaux d'administration.
3. Tester compatibilité SMB, LDAP, Kerberos et pilotes sur un environnement pilote; les valeurs par défaut de 2025 peuvent refuser des clients 2022 ou tiers mal configurés.

## ✅ Validation et retour arrière
- Confirmer build, édition, option Core/Desktop, prérequis CPU, réseau, rôles, pare-feu, sauvegarde et accès admin.
- Tester les clients réels en préproduction et une restauration de VM isolée.
- Si un rôle essentiel est incompatible, ne pas promouvoir le serveur; conserver la VM pilote et revenir à la version supportée par l'application.

## 🔗 Sources officielles
- [Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Exigences matérielles Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/hardware-requirements)
- [Server Core ou Desktop Experience](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server-core-desktop-experience)
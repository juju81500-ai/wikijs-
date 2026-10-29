---
title: "Fiche Simple - VM Windows Server 2025 Vie Systeme 40 Configuration Des Sauvegardes"
description: "Mettre en place la sauvegarde du serveur."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windowsserver2025", "vie-du-systeme", "cycle-de-vie", "etape-40"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_40_Configuration_Des_Sauvegardes

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 40 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-40`

---

## Problème précis à résoudre

Mettre en place la sauvegarde du serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Installer **Sauvegarde Windows Server** (**Gestionnaire de serveur > Ajouter des fonctionnalités > Sauvegarde Windows Server**) :
   ```powershell
   Install-WindowsFeature Windows-Server-Backup
   ```
   👉 Explication : ajoute `wbadmin` et la console de sauvegarde.

2. Lancer une sauvegarde de l'état système et du volume C: vers un disque dédié `E:` :
   ```powershell
   wbadmin start backup -backupTarget:E: -include:C: -allCritical -systemState -quiet
   ```
   👉 Explication : sauvegarde le système pour une restauration complète; la cible ne doit pas être le disque sauvegardé.

3. Planifier la sauvegarde (**Sauvegarde Windows Server > Planification de la sauvegarde**) :
   ```powershell
   wbadmin enable backup -addtarget:E: -schedule:21:00 -include:C: -allCritical -quiet
   ```
   👉 Explication : exécute la sauvegarde chaque jour à 21 h.

## 2. Production — Contrôles

Appliquer la règle 3-2-1 : 3 copies, 2 supports, 1 copie hors site; utiliser Veeam pour les VM.

## 3. Production — Sécurité

Chiffrer et isoler les sauvegardes (hors domaine ou immuables).

## Validation et retour arrière

- **Validation** : `wbadmin get versions` liste une sauvegarde récente.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
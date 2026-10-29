---
title: "Fiche Simple - VM Windows Server 2025 Vie Systeme 19 Configuration Des Sources De"
description: "Définir où le serveur obtient ses mises à jour."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windowsserver2025", "vie-du-systeme", "cycle-de-vie", "etape-19"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_19_Configuration_Des_Sources_De

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-19`

---

## Problème précis à résoudre

Définir où le serveur obtient ses mises à jour.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Paramètres > Windows Update > Options avancées** ou, pour un serveur géré, **gpedit.msc > Configuration ordinateur > Modèles d'administration > Composants Windows > Windows Update > Spécifier l'emplacement intranet du service de mise à jour Microsoft**.
   ```powershell
   Get-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate' -ErrorAction SilentlyContinue
   ```
   👉 Explication : affiche le serveur WSUS imposé par stratégie, s'il existe.

2. Configurer le serveur WSUS interne (remplacer `URL_WSUS`, ex. `http://WSUS:8530`) :
   ```powershell
   $k='HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate'
   New-Item $k -Force | Out-Null
   Set-ItemProperty $k WUServer 'URL_WSUS'
   Set-ItemProperty $k WUStatusServer 'URL_WSUS'
   Set-ItemProperty "$k\AU" UseWUServer 1 -ErrorAction SilentlyContinue
   ```
   👉 Explication : pointe le client vers le WSUS; en domaine, préférer une GPO.

3. Tester l'accès :
   ```powershell
   Test-NetConnection NOM_WSUS -Port 8530
   ```
   👉 Explication : confirme que le port WSUS répond.

## 2. Production — Contrôles

Utiliser WSUS, Windows Update for Business ou Azure Update Manager selon l'organisation.

## 3. Production — Sécurité

Ne pas ouvrir Internet complet depuis un serveur si un relais interne existe.

## Validation et retour arrière

- **Validation** : Le serveur apparaît dans la console WSUS ou la source attendue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
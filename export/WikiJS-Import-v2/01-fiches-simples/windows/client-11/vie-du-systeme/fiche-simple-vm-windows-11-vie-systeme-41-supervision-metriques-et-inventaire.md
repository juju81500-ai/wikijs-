---
title: "Fiche Simple - VM Windows 11 Vie Systeme 41 Supervision Metriques Et Inventaire"
description: "Faire remonter l'état du poste à l'outil de supervision et d'inventaire."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows11", "vie-du-systeme", "cycle-de-vie", "etape-41"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 41 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-41`

---

## Problème précis à résoudre

Faire remonter l'état du poste à l'outil de supervision et d'inventaire.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les métriques locales : **Gestionnaire des tâches > Performances** ou compteurs.
   ```powershell
   Get-Counter '\Processor(_Total)\% Processor Time','\Memory\Available MBytes' -SampleInterval 5 -MaxSamples 3
   Get-PSDrive C | Select-Object Used,Free
   ```
   👉 Explication : relève processeur, mémoire et espace disque.

2. Installer l'agent de supervision ou d'inventaire (GLPI, Zabbix, Intune, Defender for Endpoint) selon l'outil retenu.
   ```powershell
   Get-Service | Where-Object Name -match 'zabbix|glpi|Intune|Sense' | Select-Object Name,Status
   ```
   👉 Explication : vérifie que l'agent est démarré.

3. Collecter l'inventaire matériel et logiciel.
   ```powershell
   Get-CimInstance Win32_BIOS | Select-Object SerialNumber,SMBIOSBIOSVersion
   Get-CimInstance Win32_ComputerSystem | Select-Object Manufacturer,Model
   Get-CimInstance Win32_NetworkAdapterConfiguration -Filter 'IPEnabled=True' | Select-Object MACAddress,IPAddress
   ```
   👉 Explication : numéro de série, modèle et adresses pour le CMDB.

4. Définir les alertes : disque inférieur à 15 % libre, service critique arrêté, antivirus désactivé.
   👉 Explication : évite de découvrir le problème par l'utilisateur.

## 2. Production — Contrôles

Alertes basées sur des seuils validés; inventaire rafraîchi automatiquement.

## 3. Production — Sécurité

L'agent transmet ses données via TLS et ne contient pas de secret en clair.

## Validation et retour arrière

- **Validation** : Le poste apparaît dans l'outil avec des données récentes.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
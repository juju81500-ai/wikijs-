---
title: "Fiche Simple - VM Windows Server 2025 Vie Systeme 42 Journaux Taille Et Centralisation"
description: "Configurer la conservation et le transfert des journaux."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windowsserver2025", "vie-du-systeme", "cycle-de-vie", "etape-42"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_42_Journaux_Taille_Et_Centralisation

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-42`

---

## Problème précis à résoudre

Configurer la conservation et le transfert des journaux.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Observateur d'événements > Journaux Windows > Sécurité > Propriétés** pour la taille maximale.
   ```powershell
   wevtutil gl Security
   Get-WinEvent -ListLog Security, System, Application | Select-Object LogName, MaximumSizeInBytes, RecordCount
   ```
   👉 Explication : affiche la taille et le nombre d'événements.

2. Augmenter la taille du journal de sécurité (1 Go) :
   ```powershell
   wevtutil sl Security /ms:1073741824
   Limit-EventLog -LogName Application -MaximumSize 256MB
   ```
   👉 Explication : évite d'écraser les événements trop tôt.

3. Activer le transfert vers un collecteur (WEF) :
   ```powershell
   winrm quickconfig
   wecutil qc
   ```
   👉 Explication : prépare la collecte centralisée (`winrm quickconfig` sur la source, `wecutil qc` sur le collecteur).

## 2. Production — Contrôles

Conserver les journaux de sécurité 12 mois ou selon la politique de l'organisation.

## 3. Production — Sécurité

Restreindre la lecture des journaux de sécurité.

## Validation et retour arrière

- **Validation** : Les événements arrivent sur le collecteur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
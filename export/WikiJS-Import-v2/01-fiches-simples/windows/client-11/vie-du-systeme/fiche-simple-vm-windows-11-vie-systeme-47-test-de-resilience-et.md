---
title: "Fiche Simple - VM Windows 11 Vie Systeme 47 Test De Resilience Et"
description: "Vérifier que les protections et alertes se déclenchent bien."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows11", "vie-du-systeme", "cycle-de-vie", "etape-47"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-47`

---

## Problème précis à résoudre

Vérifier que les protections et alertes se déclenchent bien.

## 1. Hors-Production (Lab / Test / POC)

1. Tester la détection antivirus avec le fichier de test EICAR : **Sécurité Windows > Protection contre les virus et menaces > Historique de protection**.
   ```powershell
   Set-Content "$env:TEMP\eicar.txt" 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*'
   Get-MpThreatDetection | Select-Object -First 3 InitialDetectionTime,Resources
   ```
   👉 Explication : Defender doit supprimer le fichier de test et consigner la détection (fichier inoffensif, standardisé).

2. Simuler une perte réseau et vérifier la remontée d'alerte.
   ```powershell
   Disable-NetAdapter -Name 'NOM_INTERFACE' -Confirm:$false
   Start-Sleep 30
   Enable-NetAdapter -Name 'NOM_INTERFACE' -Confirm:$false
   ```
   👉 Explication : coupe puis rétablit la carte; à faire en local seulement, pas à distance.

3. Tester la récupération d'un service arrêté.
   ```powershell
   Stop-Service -Name Spooler
   Start-Sleep 5
   Get-Service Spooler | Select-Object Name,Status
   Start-Service Spooler
   ```
   👉 Explication : vérifie l'alerte et la remise en service du service d'impression.

4. Vérifier que l'alerte a été reçue (outil de supervision, courriel, ticket).
   👉 Explication : preuve que la chaîne d'alerte fonctionne de bout en bout.

## 2. Production — Contrôles

Tests à effectuer en pré-production ou en fenêtre de maintenance annoncée.

## 3. Production — Sécurité

Utiliser uniquement EICAR; jamais de vrai logiciel malveillant.

## Validation et retour arrière

- **Validation** : Détection EICAR consignée, alerte reçue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
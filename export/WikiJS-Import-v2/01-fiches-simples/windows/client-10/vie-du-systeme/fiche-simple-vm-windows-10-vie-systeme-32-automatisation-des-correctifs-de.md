---
title: "Fiche Simple - VM Windows 10 Vie Systeme 32 Automatisation Des Correctifs De"
description: "Automatiser les mises à jour avec WSUS, Windows Update for Business ou Intune."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows10", "vie-du-systeme", "cycle-de-vie", "etape-32"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-32`

---

## Problème précis à résoudre

Automatiser les mises à jour avec WSUS, Windows Update for Business ou Intune.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les paramètres de mise à jour : **Paramètres > Windows Update > Options avancées**, ou GPO **Configuration ordinateur > Modèles d'administration > Composants Windows > Windows Update**.
   ```powershell
   Get-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate' -ErrorAction SilentlyContinue
   ```
   👉 Explication : affiche les stratégies WSUS et de mise à jour appliquées au poste.

2. Pointer vers le serveur WSUS de l'entreprise (`URL_WSUS`) par stratégie.
   ```powershell
   $k='HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate'
   New-Item $k -Force | Out-Null
   Set-ItemProperty $k WUServer 'http://URL_WSUS:8530'
   Set-ItemProperty $k WUStatusServer 'http://URL_WSUS:8530'
   New-Item "$k\AU" -Force | Out-Null
   Set-ItemProperty "$k\AU" UseWUServer 1 -Type DWord
   ```
   👉 Explication : équivalent local de la GPO (à réserver aux essais; en production, passer par la GPO).

3. Variante cloud : **Intune > Appareils > Mises à jour Windows > Anneaux de mise à jour**, avec anneaux pilote puis production.
   👉 Explication : déploie les correctifs par vagues avec échéances.

4. Contrôler la conformité.
   ```powershell
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5
   (New-Object -ComObject Microsoft.Update.Session).CreateUpdateSearcher().Search('IsInstalled=0').Updates.Count
   ```
   👉 Explication : affiche les derniers correctifs et le nombre de mises à jour manquantes.

## 2. Production — Contrôles

Anneaux de test puis déploiement général avec date limite; redémarrages planifiés hors heures de bureau.

## 3. Production — Sécurité

Sur Windows 10 hors ESU, plus de correctifs de sécurité : isoler le poste ou le migrer.

## Validation et retour arrière

- **Validation** : Rapport de conformité à jour dans WSUS ou Intune.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
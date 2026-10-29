---
title: "Fiche Simple - VM Windows 11 Vie Systeme 14 Selection Des Composants De"
description: "Choisir l'édition, les fonctionnalités Windows et la liste minimale de composants."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows11", "vie-du-systeme", "cycle-de-vie", "etape-14"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-14`

---

## Problème précis à résoudre

Choisir l'édition, les fonctionnalités Windows et la liste minimale de composants.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'édition et la version : **Paramètres > Système > À propos de > Spécifications de Windows**.
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName,WindowsVersion,OsBuildNumber
   winver
   ```
   👉 Explication : affiche l'édition (Pro, Entreprise), la version (par exemple 24H2) et le numéro de build.

2. Lister les fonctionnalités optionnelles : **Paramètres > Système > Fonctionnalités facultatives** et **Panneau de configuration > Programmes > Activer ou désactiver des fonctionnalités Windows**.
   ```powershell
   Get-WindowsOptionalFeature -Online | Where-Object State -eq 'Enabled' | Select-Object FeatureName
   Get-WindowsCapability -Online | Where-Object State -eq 'Installed' | Select-Object Name
   ```
   👉 Explication : montre ce qui est activé.

3. Désactiver ce qui est inutile en entreprise (SMB 1, PowerShell 2.0).
   ```powershell
   Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart
   Disable-WindowsOptionalFeature -Online -FeatureName MicrosoftWindowsPowerShellV2Root -NoRestart
   ```
   👉 Explication : retire des protocoles anciens et vulnérables (redémarrage ultérieur).

4. Ajouter l'outil d'administration à distance si prévu : **Paramètres > Système > Fonctionnalités facultatives > Serveur OpenSSH**.
   ```powershell
   Get-WindowsCapability -Online -Name 'OpenSSH.Server*'
   ```
   👉 Explication : affiche la capacité OpenSSH disponible, installée plus tard à l'étape 27.

## 2. Production — Contrôles

Utiliser le même choix d'édition et de composants pour tout le parc, décrit dans l'image de référence.

## 3. Production — Sécurité

Moins de composants = moins de correctifs et de surface d'attaque.

## Validation et retour arrière

- **Validation** : Liste des fonctionnalités conforme au gabarit approuvé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
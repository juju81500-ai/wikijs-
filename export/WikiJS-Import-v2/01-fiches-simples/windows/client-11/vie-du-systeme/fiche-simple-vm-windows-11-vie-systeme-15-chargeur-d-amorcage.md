---
title: "Fiche Simple - VM Windows 11 Vie Systeme 15 Chargeur D Amorcage"
description: "Contrôler le Gestionnaire de démarrage Windows (UEFI) et le mode de démarrage."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows11", "vie-du-systeme", "cycle-de-vie", "etape-15"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-15`

---

## Problème précis à résoudre

Contrôler le Gestionnaire de démarrage Windows (UEFI) et le mode de démarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la configuration de démarrage : **msconfig > Démarrer**, ou en ligne de commande.
   ```powershell
   bcdedit /enum
   Get-CimInstance Win32_BootConfiguration
   ```
   👉 Explication : affiche les entrées du gestionnaire de démarrage et le chargeur `\EFI\Microsoft\Boot\bootmgfw.efi`.

2. Vérifier le mode de démarrage UEFI et le Secure Boot : **msinfo32 > Résumé système**.
   ```powershell
   msinfo32 /report "$env:USERPROFILE\msinfo.txt"
   Select-String -Path "$env:USERPROFILE\msinfo.txt" -Pattern 'Mode BIOS|démarrage sécurisé|BIOS Mode|Secure Boot'
   ```
   👉 Explication : génère le rapport et en extrait le mode BIOS et l'état de Secure Boot.

3. Régler un délai d'affichage du menu court en cas de double démarrage (déconseillé en entreprise).
   ```powershell
   bcdedit /timeout 5
   ```
   👉 Explication : fixe le délai du menu à 5 secondes.

4. Sauvegarder la configuration de démarrage avant toute modification.
   ```powershell
   bcdedit /export "C:\Sauvegarde\bcd.bak"
   ```
   👉 Explication : permet de restaurer avec `bcdedit /import`.

## 2. Production — Contrôles

Ne modifier le BCD qu'avec une sauvegarde et une fenêtre de maintenance.

## 3. Production — Sécurité

Garder Secure Boot actif; ne pas activer le mode test (`bcdedit /set testsigning`) en production.

## Validation et retour arrière

- **Validation** : `bcdedit /enum` retourne le chargeur Windows sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
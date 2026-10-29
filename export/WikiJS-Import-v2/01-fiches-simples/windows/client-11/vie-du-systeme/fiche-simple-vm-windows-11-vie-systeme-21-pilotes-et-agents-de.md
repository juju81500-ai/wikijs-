---
title: "Fiche Simple - VM Windows 11 Vie Systeme 21 Pilotes Et Agents De"
description: "Installer les pilotes matériels du constructeur ou les outils invité de l'hyperviseur."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows11", "vie-du-systeme", "cycle-de-vie", "etape-21"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-21`

---

## Problème précis à résoudre

Installer les pilotes matériels du constructeur ou les outils invité de l'hyperviseur.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les périphériques en erreur : **Gestionnaire de périphériques (devmgmt.msc)**; un point d'exclamation jaune signale un pilote manquant.
   ```powershell
   Get-PnpDevice -PresentOnly | Where-Object Status -ne 'OK' | Select-Object FriendlyName,Class,Status
   ```
   👉 Explication : liste les périphériques non fonctionnels.

2. Installer les pilotes via **Paramètres > Windows Update > Options avancées > Mises à jour facultatives** ou l'outil du constructeur (Dell Command Update, HP Image Assistant, Lenovo System Update).
   ```powershell
   pnputil /enum-drivers | Select-String 'Nom publié|Fournisseur|Published Name|Provider' | Select-Object -First 20
   ```
   👉 Explication : affiche les pilotes du magasin de pilotes.

3. Sur une machine virtuelle, installer les outils invité : Hyper-V (intégrés), VMware Tools, ou VirtIO Guest Tools (Proxmox) puis redémarrer.
   ```powershell
   Get-Service | Where-Object Name -match 'vmtools|VMTools|QEMU|vmic' | Select-Object Name,Status
   ```
   👉 Explication : vérifie que le service de l'agent invité est démarré.

4. Ajouter un pilote en préparation d'image si nécessaire.
   ```powershell
   pnputil /add-driver C:\Pilotes\*.inf /subdirs /install
   ```
   👉 Explication : importe et installe les pilotes d'un dossier.

## 2. Production — Contrôles

Utiliser uniquement les pilotes signés fournis par le constructeur ou Windows Update.

## 3. Production — Sécurité

Ne pas installer de pilote non signé; garder l'intégrité de la mémoire (HVCI) active si compatible.

## Validation et retour arrière

- **Validation** : Aucun périphérique en erreur dans `Get-PnpDevice`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
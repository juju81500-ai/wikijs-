---
title: "Fiche Simple - VM Windows Sauvegarde Donnees Utilisateur Restaurer Sans Ecraser"
description: "Restaurer des fichiers sans détruire ceux qui existent déjà."
published: true
date: 2026-10-29T20:14:10Z
tags: ["windows", "windows10", "windows11", "sauvegarde", "restauration", "robocopy"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_Sauvegarde_Donnees_Utilisateur_Restaurer_Sans_Ecraser.md

- **Environnement** : Poste Windows géré ou autonome, données de profil utilisateur
- **OS / Version** : Windows 10 et Windows 11
- **Catégorie** : sauvegarde / restauration
- **Tags** : `windows`, `windows10`, `windows11`, `sauvegarde`, `restauration`, `robocopy`

---

## Problème précis à résoudre

Restaurer des fichiers sans détruire ceux qui existent déjà.

## 1. Hors-Production (Lab / Test / POC)

1. Restaurer d'abord vers un répertoire temporaire (chemins d'exemple à adapter) :
   ```powershell
   robocopy "E:\Sauvegardes\$env:COMPUTERNAME\Documents" "$env:USERPROFILE\Restauration\Documents" /E /L
   ```
   👉 Explication : `/L` simule seulement : lire la liste des opérations avant la copie réelle.

2. Après contrôle, relancer sans `/L` :
   ```powershell
   robocopy "E:\Sauvegardes\$env:COMPUTERNAME\Documents" "$env:USERPROFILE\Restauration\Documents" /E /COPY:DAT /DCOPY:DAT /R:2 /W:2 /XJ
   ```
   👉 Explication : copie réelle vers le dossier temporaire.

3. Confirmer l'identité de l'utilisateur et la date de sauvegarde, comparer avec les fichiers présents, puis fusionner seulement les dossiers approuvés.
   👉 Explication : évite d'écraser des données plus récentes.

## 2. Production — Contrôles

Ne pas écraser en bloc `AppData`, les profils système ou les ACL sans procédure propre à l'application.

## 3. Production — Sécurité

- Ne pas utiliser `/MIR` pour une restauration de profil.

## Validation et retour arrière

- **Validation** : Les fichiers attendus sont restaurés et lisibles.
- **Retour arrière** : Supprimer le dossier de restauration temporaire; les originaux n'ont pas été modifiés.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Microsoft Learn — Known Folder Move](https://learn.microsoft.com/en-us/sharepoint/redirect-known-folders)
- [Guide complet — 4. Restaurer sans écraser les données existantes](/02-fiches-completes/windows/toutes-versions/autres/27-sauvegarde-restauration-donnees-utilisateur-windows#4-restaurer-sans-ecraser-les-donnees-existantes)
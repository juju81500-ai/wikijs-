---
title: "Fiche Simple - VM Windows Server 2022 Robocopy Preparer"
description: "Définir les chemins et le dossier de journaux avant la copie."
published: true
date: 2026-10-29T20:14:10Z
tags: ["windows-server-2022", "robocopy", "preparation", "powershell"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Robocopy_Preparer.md

- **Environnement** : Windows Server 2022 (Robocopy intégré); partages SMB et volumes NTFS
- **OS / Version** : Windows Server 2022 (Robocopy; non testé sur d'autres versions)
- **Catégorie** : copie / sauvegarde de fichiers
- **Tags** : `windows-server-2022`, `robocopy`, `preparation`, `powershell`

---

## Problème précis à résoudre

Définir les chemins et le dossier de journaux avant la copie.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir PowerShell avec un compte de service limité, pas un administrateur de domaine : **Démarrer > Windows PowerShell**.
   👉 Explication : on limite les dégâts en cas d'erreur de commande.

2. Définir les variables (chemins d'exemple à remplacer) :
   ```powershell
   $Src = 'D:\Data'
   $Dst = '\\sauvegarde\backup\Data'
   $Log = 'C:\Logs\robocopy'
   New-Item -ItemType Directory -Force $Log | Out-Null
   ```
   👉 Explication : la source, la destination et le dossier de journaux sont définis une fois pour toutes.

3. Vérifier source et espace de la destination :
   ```powershell
   Test-Path $Src
   Get-PSDrive D | Select-Object Used,Free
   ```
   👉 Explication : on confirme que la source existe et que l'espace suffit (adapter la lettre de lecteur).

4. Ne pas terminer un chemin entre guillemets par `\`.
   👉 Explication : `"D:\Data\"` casse l'analyse des arguments.

## 2. Production — Contrôles

Utiliser un compte de service dédié avec droits minimaux sur source et destination.

## 3. Production — Sécurité

- Ne pas exécuter Robocopy avec un administrateur de domaine.

## Validation et retour arrière

- **Validation** : Variables définies, source présente et espace suffisant.
- **Retour arrière** : Supprimer le dossier de journaux si inutile : `Remove-Item C:\Logs\robocopy -Recurse`.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Guide complet — préparer](/02-fiches-completes/windows/server-2022/autres/93-copie-sauvegarde-fichiers-robocopy-windows-server-2022#2-preparer)
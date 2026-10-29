---
title: "Fiche Simple - VM Windows Server 2022 Robocopy Retour Arriere"
description: "Annuler une copie ou récupérer après un miroir erroné."
published: true
date: 2026-10-29T20:14:10Z
tags: ["windows-server-2022", "robocopy", "retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Robocopy_Retour_Arriere.md

- **Environnement** : Windows Server 2022 (Robocopy intégré); partages SMB et volumes NTFS
- **OS / Version** : Windows Server 2022 (Robocopy; non testé sur d'autres versions)
- **Catégorie** : copie / sauvegarde de fichiers
- **Tags** : `windows-server-2022`, `robocopy`, `retour-arriere`

---

## Problème précis à résoudre

Annuler une copie ou récupérer après un miroir erroné.

## 1. Hors-Production (Lab / Test / POC)

1. Sans `/PURGE`, `/MIR` ni `/MOV`, supprimer les copies indésirables de la destination après relecture du journal.
   👉 Explication : on ne supprime que ce qui figure dans le journal.

2. Après un `/MIR` ou un `/MOVE` erroné, restaurer depuis une sauvegarde indépendante, une copie shadow ou un snapshot du stockage.
   👉 Explication : Robocopy ne peut pas récupérer ce qu'il a supprimé.

3. Conserver les journaux de chaque exécution :
   ```powershell
   Get-ChildItem $Log
   ```
   👉 Explication : ils servent à comprendre et prouver ce qui a été fait.

## 2. Production — Contrôles

Conserver les journaux selon la politique d'audit.

## 3. Production — Sécurité

- Ne pas supprimer les journaux avant la fin de l'enquête.

## Validation et retour arrière

- **Validation** : Les données redeviennent conformes à l'état attendu.
- **Retour arrière** : C'est l'objet de la fiche.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Guide complet — retour arrière](/02-fiches-completes/windows/server-2022/autres/93-copie-sauvegarde-fichiers-robocopy-windows-server-2022#7-retour-arriere)
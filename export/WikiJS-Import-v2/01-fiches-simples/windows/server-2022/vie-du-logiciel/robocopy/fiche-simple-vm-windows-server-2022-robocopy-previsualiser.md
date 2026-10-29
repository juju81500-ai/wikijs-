---
title: "Fiche Simple - VM Windows Server 2022 Robocopy Previsualiser"
description: "Lister ce que la copie ferait, sans rien copier ni supprimer."
published: true
date: 2026-10-29T20:14:10Z
tags: ["windows-server-2022", "robocopy", "apercu", "dry-run"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Robocopy_Previsualiser.md

- **Environnement** : Windows Server 2022 (Robocopy intégré); partages SMB et volumes NTFS
- **OS / Version** : Windows Server 2022 (Robocopy; non testé sur d'autres versions)
- **Catégorie** : copie / sauvegarde de fichiers
- **Tags** : `windows-server-2022`, `robocopy`, `apercu`, `dry-run`

---

## Problème précis à résoudre

Lister ce que la copie ferait, sans rien copier ni supprimer.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer l'aperçu avec `/L` (liste seulement) :
   ```powershell
   robocopy $Src $Dst /E /COPY:DAT /DCOPY:DAT /R:2 /W:5 /L /FP /NP /LOG:"$Log\preview.log" /TEE
   echo $LASTEXITCODE
   ```
   👉 Explication : `/E` copie les sous-dossiers, `/COPY:DAT` données, attributs, dates; `/R:2 /W:5` limite les tentatives (les valeurs par défaut, 1 000 000 et 30 s, bloquent un travail).

2. Pour conserver les ACL NTFS, ajouter `S` : `/COPY:DATS`.
   👉 Explication : il faut des droits suffisants; `/COPYALL` ajoute propriétaire et audit et exige des privilèges élevés.

3. Relire le journal :
   ```powershell
   Get-Content "$Log\preview.log" -Tail 30
   ```
   👉 Explication : on contrôle ce qui serait copié avant de passer à l'étape suivante.

## 2. Production — Contrôles

Relire le journal d'aperçu avec le responsable des données.

## 3. Production — Sécurité

- Toujours utiliser `/L` avant une première exécution.

## Validation et retour arrière

- **Validation** : Le journal d'aperçu ne contient que les éléments attendus.
- **Retour arrière** : `/L` ne modifie rien : rien à annuler.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Guide complet — prévisualiser (mode par défaut)](/02-fiches-completes/windows/server-2022/autres/93-copie-sauvegarde-fichiers-robocopy-windows-server-2022#3-previsualiser-mode-par-defaut)
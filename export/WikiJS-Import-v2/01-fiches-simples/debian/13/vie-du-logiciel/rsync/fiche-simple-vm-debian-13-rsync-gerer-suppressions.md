---
title: "Fiche Simple - VM Debian 13 rsync Gerer Suppressions"
description: "Éviter une suppression involontaire à destination lors d'une synchronisation miroir rsync."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "rsync", "delete", "dry-run", "backup-dir"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_rsync_Gerer_Suppressions.md

- **Environnement** : Debian 13; copie miroir uniquement après approbation explicite
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : sauvegarde de fichiers / options destructives
- **Tags** : `debian13`, `rsync`, `delete`, `dry-run`, `backup-dir`

---

## Problème précis à résoudre

Éviter une suppression involontaire à destination lors d'une synchronisation miroir rsync.

## 1. Hors-Production (Lab / Test / POC)

1. Comprendre les options destructives avant usage : `--delete` (supprime à la destination ce qui n'existe plus à la source), `--delete-excluded`, `--remove-source-files`, `--inplace`.
   👉 Explication : chacune exige une approbation; `--remove-source-files` ne doit jamais servir à une sauvegarde.

2. Vérifier que la source existe et n'est pas vide :
   ```bash
   mountpoint /srv/data && ls -A /srv/data | head -3
   ```
   👉 Explication : une source vide ou un montage manquant donnerait un miroir vide.

3. Prévisualiser le miroir contrôlé :
   ```bash
   rsync -aHAX --numeric-ids --one-file-system --delete --max-delete=50 --backup --backup-dir=../deleted-$(date +%F) --dry-run --itemize-changes -e ssh "$SRC" "$DST"
   ```
   👉 Explication : `--max-delete=50` plafonne les suppressions; `--backup-dir` (relatif à la destination) conserve les fichiers supprimés ou écrasés.

4. Après relecture et approbation, exécuter en retirant `--dry-run` :
   ```bash
   rsync -aHAX --numeric-ids --one-file-system --delete --max-delete=50 --backup --backup-dir=../deleted-$(date +%F) --itemize-changes -e ssh "$SRC" "$DST"
   ```
   👉 Explication : si le plafond est dépassé, rsync interrompt les suppressions; analyser la cause avant de relever la limite.

## 2. Production — Contrôles

Exiger approbation du propriétaire, seuil maximal de suppressions, revue des exclusions, sauvegarde indépendante et journalisation vérifiable.

## 3. Production — Sécurité

- `--delete`, ses variantes et `--delete-excluded` peuvent supprimer des données à destination.
- Ne jamais employer `--remove-source-files` pour une sauvegarde.
- Ne pas augmenter `--max-delete` pour contourner une interruption sans comprendre sa cause.
- Sans archive ou copie indépendante, les suppressions rsync peuvent être irrécupérables.

## Validation et retour arrière

- **Validation** : aperçu approuvé, plafond configuré, copie de secours vérifiée et tâche exécutée vers la cible attendue.
- **Retour arrière** : restaurer depuis le `backup-dir` ou la sauvegarde indépendante; ne pas improviser une synchronisation inversée.

## Si le problème n'est pas résolu

- [rsync — page de manuel officielle](https://download.samba.org/pub/rsync/rsync.1.html)
- [Guide complet rsync Debian 13](/02-fiches-completes/debian/13/autres/92-sauvegarde-fichiers-rsync-debian-13#5-modes-destructifs-a-nutiliser-qua-avec-une-approbation)
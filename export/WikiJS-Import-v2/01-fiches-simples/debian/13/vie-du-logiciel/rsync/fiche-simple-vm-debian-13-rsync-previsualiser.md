---
title: "Fiche Simple - VM Debian 13 rsync Previsualiser"
description: "Contrôler exactement les changements projetés par rsync avant d'écrire ou de supprimer des fichiers."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "rsync", "dry-run", "previsualisation", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_rsync_Previsualiser.md

- **Environnement** : rsync Debian 13; destination de test vérifiée
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : sauvegarde de fichiers / prévisualisation
- **Tags** : `debian13`, `rsync`, `dry-run`, `previsualisation`, `sauvegarde`

---

## Problème précis à résoudre

Contrôler exactement les changements projetés par rsync avant d'écrire ou de supprimer des fichiers.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les variables :
   ```bash
   SRC=/srv/data/
   DST=utilisateur@sauvegarde.example.net:/srv/backup/data/
   ```
   👉 Explication : la barre oblique finale de la source est significative.

2. Lancer l'aperçu sans modifier la destination :
   ```bash
   rsync -aHAX --numeric-ids --one-file-system --dry-run --itemize-changes --stats -e ssh "$SRC" "$DST"
   ```
   👉 Explication : `-a` préserve droits, dates, liens, propriétaire; `-H` liens physiques; `-A` ACL; `-X` attributs étendus; `--numeric-ids` évite le remappage UID/GID; `--one-file-system` ne traverse pas les autres montages; `--dry-run` ne modifie rien.

3. Relire la liste des changements :
   👉 Explication : vérifier que les fichiers listés sont attendus et que la source n'est pas vide ni démontée.

4. Pour un contrôle plus strict, ajouter `--checksum` à l'aperçu :
   ```bash
   rsync -aHAX --numeric-ids --one-file-system --dry-run --checksum --itemize-changes -e ssh "$SRC" "$DST" | head
   ```
   👉 Explication : lecture complète des fichiers; coûteux sur gros volumes.

## 2. Production — Contrôles

Avant exécution, faire relire l'aperçu par le propriétaire des données; expliquer chaque changement inattendu et consigner l'heure et la cible.

## 3. Production — Sécurité

- Ne pas retirer `--dry-run` tant que les changements projetés n'ont pas été approuvés.
- Une source vide ou un montage absent peut ressembler à une demande de suppression de masse.
- Vérifier les exclusions et les privilèges du compte exécutant.
- Ne pas inclure de secrets dans les noms de fichiers transmis ou les journaux.

## Validation et retour arrière

- **Validation** : aperçu cohérent, source montée, destination et volume attendus.
- **Arrêt** : interrompre avant écriture si le nombre de fichiers ou les changements diffèrent de l'attendu.

## Si le problème n'est pas résolu

- [rsync — page de manuel officielle](https://download.samba.org/pub/rsync/rsync.1.html)
- [Guide complet rsync Debian 13](/02-fiches-completes/debian/13/autres/92-sauvegarde-fichiers-rsync-debian-13#3-previsualiser-mode-par-defaut)
---
title: "Fiche Simple - VM Debian 13 rsync Valider Restaurer"
description: "Vérifier que les fichiers copiés sont exploitables et que la procédure de restauration ne touche pas les données actives."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "rsync", "restore", "checksum", "validation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_rsync_Valider_Restaurer.md

- **Environnement** : Debian 13; restauration pilote depuis une copie rsync vers une cible temporaire
- **OS / Version** : Debian 13 Trixie; rsync du dépôt Debian
- **Catégorie** : sauvegarde de fichiers / validation et restauration
- **Tags** : `debian13`, `rsync`, `restore`, `checksum`, `validation`

---

## Problème précis à résoudre

Vérifier que les fichiers copiés sont exploitables et que la procédure de restauration ne touche pas les données actives.

## 1. Hors-Production (Lab / Test / POC)

1. Relancer la copie en aperçu :
   ```bash
   rsync -aHAX --numeric-ids --one-file-system --dry-run --itemize-changes -e ssh "$SRC" "$DST"
   ```
   👉 Explication : aucune ligne de changement ne doit apparaître.

2. Restaurer vers un répertoire de test (jamais vers la source active), toujours en aperçu d'abord :
   ```bash
   mkdir -p /tmp/restore-test
   rsync -aHAX --numeric-ids --dry-run --itemize-changes -e ssh "$DST" /tmp/restore-test/
   ```
   👉 Explication : source et destination sont inversées; vérifier la liste avant de continuer.

3. Exécuter la restauration de test :
   ```bash
   rsync -aHAX --numeric-ids --itemize-changes -e ssh "$DST" /tmp/restore-test/
   ```
   👉 Explication : on retire seulement `--dry-run`.

4. Contrôler propriétaires, ACL et échantillon de fichiers :
   ```bash
   ls -la /tmp/restore-test | head
   getfacl -R /tmp/restore-test | head
   diff -rq /srv/data /tmp/restore-test | head
   ```
   👉 Explication : tester l'ouverture de quelques fichiers avec leur application.

## 2. Production — Contrôles

Planifier des restaurations périodiques et vérifier fichiers, métadonnées, RPO/RTO, compte rendu et capacité de la destination.

## 3. Production — Sécurité

- Ne jamais restaurer directement sur les données actives pendant un test.
- Valider chaque chemin avant d'inverser source et destination.
- Protéger les données restaurées selon leur classification.
- Traiter tout code retour non nul comme un échec à diagnostiquer, pas comme un succès partiel.

## Validation et retour arrière

- **Validation** : aperçu sans changement inattendu, contrôles d'intégrité et de métadonnées concluants.
- **Retour arrière** : conserver l'original et supprimer seulement les fichiers d'essai après vérification de la cible.

## Si le problème n'est pas résolu

- [rsync — page de manuel officielle](https://download.samba.org/pub/rsync/rsync.1.html)
- [Guide complet rsync Debian 13](/02-fiches-completes/debian/13/autres/92-sauvegarde-fichiers-rsync-debian-13#6-valider-et-restaurer)
---
title: "Fiche Simple - VM Debian 13 draw io Creer Diagramme"
description: "Produire un diagramme lisible avec source et exports séparés."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "drawio", "diagramme", "architecture", "documentation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_draw_io_Creer_Diagramme.md

- **Environnement** : draw.io Desktop sur poste Debian 13
- **OS / Version** : Debian 13 Trixie amd64; draw.io Desktop 32.6.1
- **Catégorie** : documentation / diagramme
- **Tags** : `debian13`, `drawio`, `diagramme`, `architecture`, `documentation`

---

## Problème précis à résoudre

Produire un diagramme lisible avec source et exports séparés.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le dossier du livrable :
   ```bash
   mkdir -p "$HOME/Documents/schema-exemple/source" "$HOME/Documents/schema-exemple/exports"
   ```
   👉 Explication : `schema-exemple` est un nom à remplacer; `source/` reçoit le fichier modifiable, `exports/` les copies.

2. Dans draw.io : **Fichier > Nouveau > Diagramme vierge**, choisir la taille de page et nommer le fichier avec date ou version.
   👉 Explication : un nom explicite facilite la revue.

3. Séparer zones, composants, interfaces et flux, avec une légende, un titre, la date et le propriétaire.
   👉 Explication : les flux autorisés se distinguent des flux à valider; les ports ne sont notés que s'ils sont confirmés.

4. Enregistrer avec **Fichier > Enregistrer sous** en `.drawio` dans `source/`.
   👉 Explication : le format `.drawio` conserve le diagramme modifiable.

## 2. Production — Contrôles

Nommer limites de confiance, segmentation réseau et dépendances; flèches orientées dans le sens du flux.

## 3. Production — Sécurité

- Aucun secret ni donnée personnelle dans le dessin.

## Validation et retour arrière

- **Validation** : le fichier `.drawio` existe dans `source/` et se rouvre correctement.
- **Retour arrière** : supprimer le dossier du livrable de test.

## Si le problème n'est pas résolu

- [draw.io Desktop — releases officielles](https://github.com/jgraph/drawio-desktop/releases)
- [draw.io — travail hors ligne](https://www.drawio.com/docs/security/diagrams-offline/)
- [draw.io — formats et export](https://www.drawio.com/docs/manual/export/export-diagram/)
- [Guide complet — étape 4](/02-fiches-completes/debian/13/installation-deploiement/76-deploiement-draw-io-desktop-32-6-1-debian-13#4-creer-un-diagramme-technique-exploitable)
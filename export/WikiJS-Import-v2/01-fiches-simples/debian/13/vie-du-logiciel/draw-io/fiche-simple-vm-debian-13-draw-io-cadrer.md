---
title: "Fiche Simple - VM Debian 13 draw io Cadrer"
description: "Confirmer la version, le périmètre hors ligne et les règles de données avant installation."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "drawio", "desktop", "cadrage", "offline"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_draw_io_Cadrer.md

- **Environnement** : draw.io Desktop sur poste Debian 13
- **OS / Version** : Debian 13 Trixie amd64; draw.io Desktop 32.6.1
- **Catégorie** : documentation / cadrage
- **Tags** : `debian13`, `drawio`, `desktop`, `cadrage`, `offline`

---

## Problème précis à résoudre

Confirmer la version, le périmètre hors ligne et les règles de données avant installation.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'architecture de la machine :
   ```bash
   dpkg --print-architecture
   cat /etc/os-release | head -3
   ```
   👉 Explication : le paquet officiel visé est amd64 pour Debian 13.

2. Relever la dernière release stable sur la page officielle (version utilisée : 32.6.1) :
   ```bash
   curl -fsSL https://api.github.com/repos/jgraph/drawio-desktop/releases/latest | grep -E '"tag_name"'
   ```
   👉 Explication : on confirme que la version correspond à celle validée.

3. Noter par écrit : pas d'intégration Cloud, de plugin tiers ni de collaboration en ligne; aucun secret dans les dessins.
   👉 Explication : la version Desktop sert à créer des diagrammes locaux, hors ligne.

## 2. Production — Contrôles

Pour un environnement sensible, télécharger sur un poste connecté approuvé puis transférer l'artefact vérifié.

## 3. Production — Sécurité

- Pas de mots de passe, tokens ni données non classifiées dans un dessin.

## Validation et retour arrière

- **Validation** : architecture amd64 confirmée et version retenue notée.
- **Retour arrière** : aucun changement à annuler.

## Si le problème n'est pas résolu

- [draw.io Desktop — releases officielles](https://github.com/jgraph/drawio-desktop/releases)
- [draw.io — travail hors ligne](https://www.drawio.com/docs/security/diagrams-offline/)
- [draw.io — formats et export](https://www.drawio.com/docs/manual/export/export-diagram/)
- [Guide complet — étape 1](/02-fiches-completes/debian/13/installation-deploiement/76-deploiement-draw-io-desktop-32-6-1-debian-13#1-choix-et-perimetre)
---
title: "Fiche Simple - VM Debian 13 draw io Maj Depannage"
description: "Mettre à jour en sécurité et traiter une dépendance manquante."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "drawio", "mise-a-jour", "depannage"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_draw_io_Maj_Depannage.md

- **Environnement** : draw.io Desktop sur poste Debian 13
- **OS / Version** : Debian 13 Trixie amd64; draw.io Desktop 32.6.1
- **Catégorie** : documentation / maintenance
- **Tags** : `debian13`, `drawio`, `mise-a-jour`, `depannage`

---

## Problème précis à résoudre

Mettre à jour en sécurité et traiter une dépendance manquante.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder les diagrammes avant mise à jour :
   ```bash
   cp -a "$HOME/Documents/schema-exemple" "$HOME/Documents/schema-exemple.sauvegarde"
   ```
   👉 Explication : la copie protège les fichiers (chemin d'exemple à remplacer).

2. Contrôler la version installée puis la nouvelle release avec son digest, puis installer le .deb approuvé :
   ```bash
   apt-cache policy draw.io
   sudo apt install ./drawio-amd64-NOUVELLE_VERSION.deb
   ```
   👉 Explication : remplacer `NOUVELLE_VERSION` par la version validée (fichier vérifié comme à l'étape de téléchargement).

3. Si APT signale une dépendance manquante :
   ```bash
   sudo apt --fix-broken install
   dpkg --print-architecture
   ```
   👉 Explication : on confirme Debian 13 amd64 et on laisse APT résoudre; pas de paquets d'autres distributions.

4. Ouvrir une copie d'un diagramme représentatif avant de supprimer l'ancienne version.
   👉 Explication : un problème sur un diagramme précis se traite sur une copie, l'original reste préservé.

## 2. Production — Contrôles

Contrôler la page des releases et le digest de chaque nouvelle version.

## 3. Production — Sécurité

- Ne pas ouvrir le fichier original en cas de doute, travailler sur copie.

## Validation et retour arrière

- **Validation** : la nouvelle version ouvre et exporte une copie.
- **Retour arrière** : réinstaller le .deb précédent conservé et restaurer la sauvegarde.

## Si le problème n'est pas résolu

- [draw.io Desktop — releases officielles](https://github.com/jgraph/drawio-desktop/releases)
- [draw.io — travail hors ligne](https://www.drawio.com/docs/security/diagrams-offline/)
- [draw.io — formats et export](https://www.drawio.com/docs/manual/export/export-diagram/)
- [Guide complet — étape 6](/02-fiches-completes/debian/13/installation-deploiement/76-deploiement-draw-io-desktop-32-6-1-debian-13#6-mises-a-jour-et-depannage)
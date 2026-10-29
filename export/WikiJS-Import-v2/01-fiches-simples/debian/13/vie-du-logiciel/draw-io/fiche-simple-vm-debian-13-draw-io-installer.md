---
title: "Fiche Simple - VM Debian 13 draw io Installer"
description: "Installer le paquet vérifié avec APT, qui résout ses dépendances."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "drawio", "apt", "deb", "installation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_draw_io_Installer.md

- **Environnement** : draw.io Desktop sur poste Debian 13
- **OS / Version** : Debian 13 Trixie amd64; draw.io Desktop 32.6.1
- **Catégorie** : documentation / installation
- **Tags** : `debian13`, `drawio`, `apt`, `deb`, `installation`

---

## Problème précis à résoudre

Installer le paquet vérifié avec APT, qui résout ses dépendances.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler architecture et métadonnées :
   ```bash
   cd "$HOME/drawio-install"
   dpkg --print-architecture
   dpkg-deb --info drawio-amd64-32.6.1.deb
   ```
   👉 Explication : l'architecture doit être amd64 et le paquet nommé `draw.io`.

2. Installer :
   ```bash
   sudo apt install ./drawio-amd64-32.6.1.deb
   ```
   👉 Explication : APT installe le .deb et ses dépendances Debian.

3. Lancer draw.io depuis le menu graphique, créer un fichier de test dans un dossier utilisateur approuvé, le fermer puis le rouvrir.
   👉 Explication : on vérifie le lancement et l'enregistrement local, hors ligne.

## 2. Production — Contrôles

Valider d'abord sur un poste pilote avant déploiement.

## 3. Production — Sécurité

- Ne pas installer de dépendances venant d'autres distributions pour contourner une erreur.

## Validation et retour arrière

- **Validation** : l'application se lance et rouvre le fichier de test.
- **Retour arrière** : `sudo apt remove draw.io`.

## Si le problème n'est pas résolu

- [draw.io Desktop — releases officielles](https://github.com/jgraph/drawio-desktop/releases)
- [draw.io — travail hors ligne](https://www.drawio.com/docs/security/diagrams-offline/)
- [draw.io — formats et export](https://www.drawio.com/docs/manual/export/export-diagram/)
- [Guide complet — étape 3](/02-fiches-completes/debian/13/installation-deploiement/76-deploiement-draw-io-desktop-32-6-1-debian-13#3-installer-lapplication)
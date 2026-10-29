---
title: "Fiche Simple - VM Debian 13 Bash Shell Installer"
description: "Installer Bash depuis les dépôts Debian approuvés."
published: true
date: 2026-10-29T20:47:59Z
tags: ["debian13", "bash", "shell", "scripting", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:47:59Z
dateModified: 2026-10-29T20:47:59Z
---

# Fiche_Simple_-_VM_Debian_13_Bash_Shell_Installer

- **Environnement** : VM Debian 13 de laboratoire, compte utilisateur non privilégié
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting
- **Tags** : `debian13`, `bash`, `shell`, `scripting`, `securite`
---

## Problème précis à résoudre

Installer Bash depuis les dépôts Debian approuvés.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier candidat APT
   ```bash
   sudo apt update
   apt-cache policy bash
   ```
   👉 Explication : le paquet doit venir de la source Debian approuvée.

2. Installer le paquet
   ```bash
   sudo apt install bash shellcheck
   ```
   👉 Explication : respecter le contrôle de changement et ne pas ajouter de dépôt tiers.

3. Vérifier version et chemin
   ```bash
   bash --version
   command -v bash
   ```
   👉 Explication : confirmer version et chemin.

## 2. Production — Contrôles

Tester dépendances et version sur une machine pilote; gérer le paquet par APT.

## 3. Production — Sécurité

- Ne pas utiliser de binaire non vérifié.
- Ne pas exécuter les commandes en root sans justification.
- Suivre les mises à jour de sécurité Debian.

## Validation et retour arrière

- **Validation** : Le binaire attendu est présent et sa provenance est approuvée.
- **Retour arrière** : Réinstaller un paquet supporté depuis APT et restaurer la configuration antérieure.

## Si le problème n'est pas résolu

- [GNU Bash — manuel](https://www.gnu.org/software/bash/manual/)
- [Debian — paquet bash](https://packages.debian.org/trixie/bash)
- [ShellCheck — wiki](https://www.shellcheck.net/wiki/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-prerequis-limites>)
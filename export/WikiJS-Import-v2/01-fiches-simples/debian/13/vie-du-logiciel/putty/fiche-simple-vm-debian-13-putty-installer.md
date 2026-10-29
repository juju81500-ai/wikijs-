---
title: "Fiche Simple - VM Debian 13 PuTTY Installer"
description: "Installer les outils PuTTY en ligne de commande sur Debian 13."
published: true
date: 2026-10-29T21:24:09Z
tags: ["putty", "putty-tools", "plink", "puttygen", "ssh", "installation", "apt"]
editor: markdown
dateCreated: 2026-10-29T21:24:09Z
dateModified: 2026-10-29T21:24:09Z
---

# Fiche_Simple_-_VM_Debian_13_PuTTY_Installer

- **Environnement** : VM Debian 13 (Trixie), poste d'administration en ligne de commande
- **OS / Version** : Debian 13 (Trixie) — paquet putty-tools
- **Catégorie** : outils d'administration / SSH
- **Tags** : `putty`, `putty-tools`, `plink`, `puttygen`, `ssh`, `installation`, `apt`

---

## Problème précis à résoudre

Installer les outils PuTTY en ligne de commande sur Debian 13.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le paquet :
   ```bash
   sudo apt update
   sudo apt install putty-tools
   ```
   👉 Explication : `apt` installe `/usr/bin/plink`, `/usr/bin/pscp`, `/usr/bin/psftp`, `/usr/bin/puttygen`, `/usr/bin/psusan`.
2. Contrôler l'installation :
   ```bash
   command -v plink puttygen
   plink -V
   puttygen --version
   ```
   👉 Explication : les commandes doivent retourner un chemin et une version.
3. Lire l'aide :
   ```bash
   man puttygen
   man plink
   ```
   👉 Explication : les pages de manuel sont installées par le paquet.

## 2. Production — Contrôles

- Installation sur un poste d'administration, pas sur un serveur exposé inutilement.

## 3. Production — Sécurité

- Ne pas installer de binaires PuTTY téléchargés hors des dépôts sans vérifier leur signature.

## Validation et retour arrière

- **Validation** : `plink -V` affiche une version. **Retour arrière** : `sudo apt remove putty-tools`.

## Si le problème n'est pas résolu

- [Fiche d'entrée PuTTY](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-putty)
- [Debian — paquet putty-tools](https://packages.debian.org/trixie/putty-tools)
- [Documentation officielle PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)
---
title: "Fiche Simple - VM Debian 13 Wireshark Analyse Installer"
description: "Installer Wireshark, son interface et TShark depuis Debian."
published: true
date: 2026-10-29T20:14:10Z
tags: ["wireshark", "debian13", "tshark", "apt"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Wireshark_Analyse_Installer.md

- **Environnement** : Poste Debian 13 amd64
- **OS / Version** : Debian 13 Trixie amd64; paquet Wireshark des dépôts Debian
- **Catégorie** : analyse reseau / installation
- **Tags** : `wireshark`, `debian13`, `tshark`, `apt`

---

## Problème précis à résoudre

Installer Wireshark, son interface et TShark depuis Debian.

## 1. Hors-Production (Lab / Test / POC)

1. Installer :
   ```bash
   sudo apt update
   sudo apt install -y wireshark wireshark-qt tshark
   ```
   👉 Explication : on installe l'interface Qt et l'outil en ligne de commande.

2. À la question « Should non-superusers be able to capture packets? », répondre **No** pour une simple analyse de fichiers.
   👉 Explication : un utilisateur normal peut lire les fichiers sans privilège de capture.

3. Contrôler les versions :
   ```bash
   wireshark --version
   tshark --version
   ```
   👉 Explication : on vérifie l'installation.

## 2. Production — Contrôles

Suivre les mises à jour de sécurité Debian, car les dissectors analysent des données potentiellement hostiles.

## 3. Production — Sécurité

- Pas de dépôt tiers sans revue de compatibilité et de signature.

## Validation et retour arrière

- **Validation** : `wireshark --version` et `tshark --version` répondent.
- **Retour arrière** : `sudo apt remove wireshark wireshark-qt tshark`.

## Si le problème n'est pas résolu

- [Wireshark — installation depuis Debian](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallUnixInstallBins.html)
- [Wireshark — téléchargements](https://www.wireshark.org/download.html)
- [Guide complet Wireshark Debian 13](/02-fiches-completes/debian/13/installation-deploiement/83-installation-wireshark-debian-13-analyse-capture#2-installer-les-paquets-debian)
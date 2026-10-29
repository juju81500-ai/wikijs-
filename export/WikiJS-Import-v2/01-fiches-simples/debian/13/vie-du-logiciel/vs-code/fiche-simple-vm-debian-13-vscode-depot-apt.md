---
title: "Fiche Simple - VM Debian 13 VSCode Depot APT"
description: "Ajouter le dépôt Microsoft vérifié, avec sa clé limitée à ce dépôt."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "vscode", "apt", "signed-by", "gpg"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_VSCode_Depot_APT.md

- **Environnement** : Poste Debian 13 amd64, VS Code Stable installé via le dépôt APT Microsoft
- **OS / Version** : Debian 13 Trixie amd64; Visual Studio Code Stable 1.143.1
- **Catégorie** : éditeur / dépôt APT
- **Tags** : `debian13`, `vscode`, `apt`, `signed-by`, `gpg`

---

## Problème précis à résoudre

Ajouter le dépôt Microsoft vérifié, avec sa clé limitée à ce dépôt.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   sudo apt update
   sudo apt install -y ca-certificates curl gpg
   ```
   👉 Explication : installe les outils nécessaires au dépôt.

2. Exécuter :
   ```bash
   curl --fail --location --proto '=https' --tlsv1.2 -o /tmp/microsoft.asc https://packages.microsoft.com/keys/microsoft.asc
   gpg --show-keys --with-fingerprint /tmp/microsoft.asc
   ```
   👉 Explication : télécharge la clé officielle et affiche son empreinte pour contrôle.

3. Exécuter :
   ```bash
   gpg --dearmor --output /tmp/packages.microsoft.gpg /tmp/microsoft.asc
   sudo install -D -o root -g root -m 0644 /tmp/packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
   rm -f /tmp/microsoft.asc /tmp/packages.microsoft.gpg
   ```
   👉 Explication : convertit la clé en trousseau APT dédié puis supprime les fichiers temporaires.

4. Exécuter :
   ```bash
   printf '%s\n' 'deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main' | sudo tee /etc/apt/sources.list.d/vscode.list >/dev/null
   sudo apt update
   apt-cache policy code
   ```
   👉 Explication : déclare le dépôt avec `signed-by` et vérifie qu'une version Candidate vient du dépôt Microsoft.

## 2. Production — Contrôles

Si la clé, son origine ou la signature du dépôt ne peuvent pas être vérifiées, arrêter l'installation.

## 3. Production — Sécurité

- Ne pas utiliser `apt-key`.
- Ne pas ajouter de dépôt tiers.
- Le trousseau sert uniquement au dépôt VS Code.

## Validation et retour arrière

- **Validation** : `apt-cache policy code` montre le dépôt Microsoft et une version Candidate.
- **Retour arrière** : `sudo rm /etc/apt/sources.list.d/vscode.list /etc/apt/keyrings/packages.microsoft.gpg` puis `sudo apt update`.

## Si le problème n'est pas résolu

- [Visual Studio Code — installation Linux](https://code.visualstudio.com/docs/setup/linux)
- [Guide complet Déployer Visual Studio Code Stable 1.143.1 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13#2-installer-le-depot-apt-microsoft)
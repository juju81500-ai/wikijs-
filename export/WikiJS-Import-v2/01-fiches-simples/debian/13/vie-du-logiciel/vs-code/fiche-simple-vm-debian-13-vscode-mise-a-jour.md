---
title: "Fiche Simple - VM Debian 13 VSCode Mise a jour"
description: "Mettre à jour VS Code par APT et sauvegarder le profil."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "vscode", "apt", "maj", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_VSCode_Mise_a_jour.md

- **Environnement** : Poste Debian 13 amd64, VS Code Stable installé via le dépôt APT Microsoft
- **OS / Version** : Debian 13 Trixie amd64; Visual Studio Code Stable 1.143.1
- **Catégorie** : éditeur / maintenance
- **Tags** : `debian13`, `vscode`, `apt`, `maj`, `sauvegarde`

---

## Problème précis à résoudre

Mettre à jour VS Code par APT et sauvegarder le profil.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   apt-cache policy code
   sudo apt update
   sudo apt install --only-upgrade code
   code --version
   ```
   👉 Explication : consulte la version candidate, met à jour uniquement `code` et vérifie la version.

2. Avant de désactiver une extension ou de changer de version, noter version, extensions et journaux.
   👉 Explication : permet un diagnostic fiable.

3. Exécuter :
   ```bash
   cp -a ~/.config/Code/User ~/Code-User-sauvegarde
   ```
   👉 Explication : copie les réglages personnels (ou utiliser l'export de profil); contrôler que la copie ne contient aucun secret.

## 2. Production — Contrôles

Éviter de restaurer le répertoire de données d'une version plus récente dans une ancienne sans essai sur profil séparé.

## 3. Production — Sécurité

- Ne pas inclure de secrets dans la sauvegarde.
- Ne pas versionner la sauvegarde dans un dépôt partagé.

## Validation et retour arrière

- **Validation** : la version est à jour et le profil sauvegardé.
- **Retour arrière** : restaurer la copie `~/Code-User-sauvegarde` dans `~/.config/Code/User` après fermeture de VS Code.

## Si le problème n'est pas résolu

- [Visual Studio Code — installation Linux](https://code.visualstudio.com/docs/setup/linux)
- [Guide complet Déployer Visual Studio Code Stable 1.143.1 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13#7-mise-a-jour-sauvegarde-et-retour-arriere)
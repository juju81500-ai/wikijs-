---
title: "Fiche Simple - VM Debian 13 VSCode Recette"
description: "Valider l'installation de VS Code point par point."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "vscode", "apt", "recette"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_VSCode_Recette.md

- **Environnement** : Poste Debian 13 amd64, VS Code Stable installé via le dépôt APT Microsoft
- **OS / Version** : Debian 13 Trixie amd64; Visual Studio Code Stable 1.143.1
- **Catégorie** : éditeur / validation
- **Tags** : `debian13`, `vscode`, `apt`, `recette`

---

## Problème précis à résoudre

Valider l'installation de VS Code point par point.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   apt-cache policy code
   code --version
   ```
   👉 Explication : vérifie le dépôt Stable Microsoft avec `signed-by` et la version Stable.

2. Ouvrir VS Code en utilisateur, créer, modifier et enregistrer un fichier de test dans un dossier autorisé.
   👉 Explication : valide l'usage normal.

3. Ouvrir un dossier de test non approuvé et confirmer qu'il reste en Restricted Mode.
   👉 Explication : valide Workspace Trust.

4. Exécuter :
   ```bash
   code --list-extensions --show-versions
   ```
   👉 Explication : inventorie les extensions; contrôler éditeurs et signatures.

5. Tester la sauvegarde et la récupération du profil utilisateur sans secrets dans un dépôt partagé.
   👉 Explication : valide la reprise.

## 2. Production — Contrôles

Consigner les résultats de chaque point de la recette.

## 3. Production — Sécurité

- Aucun secret dans les sauvegardes de profil.
- Dossiers inconnus en Restricted Mode.

## Validation et retour arrière

- **Validation** : tous les points de la recette sont validés.
- **Retour arrière** : désinstaller `code` et supprimer le dépôt Microsoft si la recette échoue (`sudo apt remove code`).

## Si le problème n'est pas résolu

- [Visual Studio Code — installation Linux](https://code.visualstudio.com/docs/setup/linux)
- [Guide complet Déployer Visual Studio Code Stable 1.143.1 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13#8-verifications-de-reception)
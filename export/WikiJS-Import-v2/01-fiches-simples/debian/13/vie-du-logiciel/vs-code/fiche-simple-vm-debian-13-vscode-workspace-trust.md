---
title: "Fiche Simple - VM Debian 13 VSCode Workspace Trust"
description: "Éviter d'exécuter du code d'un dossier inconnu."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "vscode", "apt", "workspace-trust", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_VSCode_Workspace_Trust.md

- **Environnement** : Poste Debian 13 amd64, VS Code Stable installé via le dépôt APT Microsoft
- **OS / Version** : Debian 13 Trixie amd64; Visual Studio Code Stable 1.143.1
- **Catégorie** : éditeur / sécurité
- **Tags** : `debian13`, `vscode`, `apt`, `workspace-trust`, `securite`

---

## Problème précis à résoudre

Éviter d'exécuter du code d'un dossier inconnu.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir un dossier reçu non examiné et choisir de le laisser en **Restricted Mode**.
   👉 Explication : VS Code limite terminaux, tâches, débogueurs, réglages d'espace de travail et certaines extensions.

2. Relire les scripts, les tâches `.vscode`, les fichiers de configuration et les commandes de construction.
   👉 Explication : repère toute exécution non prévue.

3. Faire confiance au dossier seulement si sa provenance et son contenu sont évalués (**Manage > Trust**).
   👉 Explication : l'approbation active les fonctions restreintes.

## 2. Production — Contrôles

Ne jamais désactiver globalement Workspace Trust; il ne remplace pas une sandbox.

## 3. Production — Sécurité

- Les agents et tâches peuvent modifier des fichiers, lancer des commandes et faire des requêtes réseau.
- Une extension malveillante peut contourner le mode restreint.

## Validation et retour arrière

- **Validation** : un dossier de test non approuvé reste en Restricted Mode.
- **Retour arrière** : retirer la confiance du dossier (**Manage Workspace Trust**).

## Si le problème n'est pas résolu

- [Visual Studio Code — Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust)
- [Guide complet Déployer Visual Studio Code Stable 1.143.1 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13#5-utiliser-workspace-trust-pour-les-dossiers-inconnus)
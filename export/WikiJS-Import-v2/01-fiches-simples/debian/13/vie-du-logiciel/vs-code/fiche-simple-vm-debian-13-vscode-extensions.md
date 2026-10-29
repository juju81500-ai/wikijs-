---
title: "Fiche Simple - VM Debian 13 VSCode Extensions"
description: "Installer uniquement des extensions contrôlées."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "vscode", "apt", "extensions", "marketplace"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_VSCode_Extensions.md

- **Environnement** : Poste Debian 13 amd64, VS Code Stable installé via le dépôt APT Microsoft
- **OS / Version** : Debian 13 Trixie amd64; Visual Studio Code Stable 1.143.1
- **Catégorie** : éditeur / extensions
- **Tags** : `debian13`, `vscode`, `apt`, `extensions`, `marketplace`

---

## Problème précis à résoudre

Installer uniquement des extensions contrôlées.

## 1. Hors-Production (Lab / Test / POC)

1. Dans la vue Extensions, rechercher l'identifiant exact `publisher.extension`.
   👉 Explication : évite les extensions homonymes.

2. Examiner éditeur, identité vérifiée, licence, dépôt, dépendances, notes de version et maintenance, puis confirmer l'éditeur à l'installation.
   👉 Explication : les extensions ont les droits de l'utilisateur.

3. Conserver la vérification des signatures activée; ne pas contourner un avertissement sans analyse approuvée.
   👉 Explication : garantit l'origine de l'extension.

4. Exécuter :
   ```bash
   code --list-extensions --show-versions
   ```
   👉 Explication : inventorie les extensions installées et leurs versions.

## 2. Production — Contrôles

En environnement administré, établir une liste d'autorisation et un processus de revue des mises à jour.

## 3. Production — Sécurité

- Installer le minimum requis et supprimer les extensions inutiles.
- Une signature vérifiée ne garantit pas l'absence de risque.

## Validation et retour arrière

- **Validation** : la liste d'extensions est inventoriée et chaque éditeur contrôlé.
- **Retour arrière** : `code --uninstall-extension` suivi de l'identifiant exact (`publisher.extension`).

## Si le problème n'est pas résolu

- [Visual Studio Code — extensions et Marketplace](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)
- [Visual Studio Code — sécurité des extensions](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security)
- [Guide complet Déployer Visual Studio Code Stable 1.143.1 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13#6-installer-et-gerer-les-extensions)
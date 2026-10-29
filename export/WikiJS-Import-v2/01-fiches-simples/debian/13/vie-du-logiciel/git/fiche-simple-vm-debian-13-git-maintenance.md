---
title: "Fiche Simple - VM Debian 13 Git Maintenance"
description: "Garder Git à jour et détecter configurations ou identifiants indésirables."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "git", "maintenance", "configuration"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Git_Maintenance.md

- **Environnement** : Poste Debian 13, client Git
- **OS / Version** : Debian 13 Trixie amd64; paquet Git Debian
- **Catégorie** : gestion de versions / maintenance
- **Tags** : `debian13`, `git`, `maintenance`, `configuration`

---

## Problème précis à résoudre

Garder Git à jour et détecter configurations ou identifiants indésirables.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour Git via APT :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade git
   git --version
   ```
   👉 Explication : on vérifie la version après mise à jour.

2. Inventorier remotes et configuration avec leur origine :
   ```bash
   git remote -v
   git config --show-origin --list
   ```
   👉 Explication : aucune donnée d'authentification ne doit y figurer.

3. Contrôler l'état et les droits de `known_hosts` :
   ```bash
   git status --short --branch
   ls -l "$HOME/.ssh/known_hosts"
   ```
   👉 Explication : le fichier doit appartenir à l'utilisateur, non écrit par d'autres.

## 2. Production — Contrôles

Sauvegarder le travail non poussé : un commit local n'est pas une sauvegarde indépendante.

## 3. Production — Sécurité

- Connaître la procédure de révocation des clés et jetons.

## Validation et retour arrière

- **Validation** : aucun secret dans la configuration et version attendue.
- **Retour arrière** : réinstaller la version précédente d'APT si une mise à jour pose problème.

## Si le problème n'est pas résolu

- [Git — installer Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Git — configuration](https://git-scm.com/docs/git-config)
- [Git — remotes, fetch, pull et push](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Git — credentials](https://git-scm.com/docs/gitcredentials)
- [Guide complet — étape 7](/02-fiches-completes/debian/13/installation-deploiement/82-administration-git-client-debian-13#7-maintenance-et-verifications)
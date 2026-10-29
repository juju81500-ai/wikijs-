---
title: "Fiche Simple - VM Debian 13 Python Choisir Mode"
description: "Choisir entre paquet APT, venv par projet ou pipx."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "python", "pep668", "cadrage"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Python_Choisir_Mode.md

- **Environnement** : Python 3 sur Debian 13 avec venv et pipx
- **OS / Version** : Debian 13 amd64; Python fourni par Debian
- **Catégorie** : développement / cadrage
- **Tags** : `debian13`, `python`, `pep668`, `cadrage`

---

## Problème précis à résoudre

Choisir entre paquet APT, venv par projet ou pipx.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier que le Python système est géré par APT :
   ```bash
   dpkg -S $(readlink -f $(which python3))
   ```
   👉 Explication : Le paquet propriétaire doit être un paquet Debian.

2. Repérer la protection PEP 668 :
   ```bash
   ls /usr/lib/python3*/EXTERNALLY-MANAGED
   ```
   👉 Explication : Sa présence interdit `pip` global; c'est voulu.

## 2. Production — Contrôles

Application système : paquets Debian. Projet applicatif : `venv`. Outil CLI hors Debian : `pipx`. Ces environnements isolent les dépendances, pas les permissions.

## 3. Production — Sécurité

- Ne pas utiliser `sudo pip` ni `--break-system-packages`.
- Ne pas écrire dans le `site-packages` global.

## Validation et retour arrière

- **Validation** : mode choisi et consigné pour chaque usage.
- **Retour arrière** : aucune modification; rien à annuler.

## Si le problème n'est pas résolu

- [Debian Wiki — Python](https://wiki.debian.org/Python)
- [Python — module venv](https://docs.python.org/3/library/venv.html)
- [pipx — installation](https://pipx.pypa.io/stable/installation/)
- [Guide complet Python Debian 13](/02-fiches-completes/debian/13/installation-deploiement/81-administration-python-3-debian-13-venv-pipx#1-choisir-le-mode-dinstallation)
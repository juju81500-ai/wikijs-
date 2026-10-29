---
title: "Fiche Simple - VM Debian 13 Python Dependances"
description: "Garder des dépendances reproductibles et revues."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "python", "dependances", "tests", "audit"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Python_Dependances.md

- **Environnement** : Python 3 sur Debian 13 avec venv et pipx
- **OS / Version** : Debian 13 amd64; Python fourni par Debian
- **Catégorie** : développement / dépendances
- **Tags** : `debian13`, `python`, `dependances`, `tests`, `audit`

---

## Problème précis à résoudre

Garder des dépendances reproductibles et revues.

## 1. Hors-Production (Lab / Test / POC)

1. Enregistrer l'interpréteur et les versions résolues :
   ```bash
   .venv/bin/python --version
   .venv/bin/python -m pip freeze > requirements.lock
   ```
   👉 Explication : Le manifeste verrouillé permet de reconstruire l'environnement.

2. Recréer un environnement de test propre :
   ```bash
   python3 -m venv .venv-test
   .venv-test/bin/python -m pip install -r requirements.lock
   ```
   👉 Explication : Vérifie la reconstruction depuis zéro.

3. Lister les paquets obsolètes :
   ```bash
   .venv/bin/python -m pip list --outdated
   ```
   👉 Explication : Base pour décider des mises à jour après revue.

## 2. Production — Contrôles

Lancer les tests du projet et les scripts d'administration sur des données fictives; contrôler vulnérabilités et paquets abandonnés via le processus approuvé; retirer les paquets inutiles.

## 3. Production — Sécurité

- Comparer les changements sensibles de dépendances avant déploiement.
- Ne pas compter sur la copie de `.venv` pour le retour arrière.

## Validation et retour arrière

- **Validation** : environnement reconstruit et tests passés.
- **Retour arrière** : supprimer `.venv-test` et conserver la version déployée jusqu'à validation.

## Si le problème n'est pas résolu

- [Debian Wiki — Python](https://wiki.debian.org/Python)
- [Python — module venv](https://docs.python.org/3/library/venv.html)
- [pipx — installation](https://pipx.pypa.io/stable/installation/)
- [Guide complet Python Debian 13](/02-fiches-completes/debian/13/installation-deploiement/81-administration-python-3-debian-13-venv-pipx#5-controler-et-maintenir-les-dependances)
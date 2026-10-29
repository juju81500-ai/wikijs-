---
title: "Fiche Simple - VM Debian 13 Python Script Admin"
description: "Lancer un script Python d'administration sans élévation excessive."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "python", "systemd", "sudo", "secrets"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Python_Script_Admin.md

- **Environnement** : Python 3 sur Debian 13 avec venv et pipx
- **OS / Version** : Debian 13 amd64; Python fourni par Debian
- **Catégorie** : développement / droits minimaux
- **Tags** : `debian13`, `python`, `systemd`, `sudo`, `secrets`

---

## Problème précis à résoudre

Lancer un script Python d'administration sans élévation excessive.

## 1. Hors-Production (Lab / Test / POC)

1. Relire le script et ses dépendances avant exécution :
   ```bash
   less script_admin.py
   ```
   👉 Explication : Remplacer par votre script; un script lancé avec `sudo` hérite de privilèges étendus.

2. Lancer avec l'interpréteur de l'environnement, sous un compte non privilégié :
   ```bash
   .venv/bin/python script_admin.py
   ```
   👉 Explication : Évite `sudo` quand le droit n'est pas nécessaire.

3. Pour un service : définir `ExecStart` avec l'interpréteur `.venv`, `WorkingDirectory`, `User` et `Group` dans l'unité systemd, puis contrôler :
   ```bash
   systemd-analyze security nom-du-service.service
   ```
   👉 Explication : Remplacer `nom-du-service` par votre unité; note l'exposition du service.

## 2. Production — Contrôles

Préférer un compte de service dédié, des droits ciblés ou une opération APT documentée; limiter fichiers accessibles et capabilities.

## 3. Production — Sécurité

- Aucun mot de passe, token ou donnée personnelle dans arguments, journaux ou manifests.
- Injecter les secrets via le gestionnaire approuvé.

## Validation et retour arrière

- **Validation** : le script s'exécute avec le compte minimal prévu.
- **Retour arrière** : désactiver l'unité ou retirer le script du planificateur.

## Si le problème n'est pas résolu

- [Debian Wiki — Python](https://wiki.debian.org/Python)
- [Python — module venv](https://docs.python.org/3/library/venv.html)
- [pipx — installation](https://pipx.pypa.io/stable/installation/)
- [Guide complet Python Debian 13](/02-fiches-completes/debian/13/installation-deploiement/81-administration-python-3-debian-13-venv-pipx#6-executer-un-script-dadministration-avec-les-droits-minimaux)
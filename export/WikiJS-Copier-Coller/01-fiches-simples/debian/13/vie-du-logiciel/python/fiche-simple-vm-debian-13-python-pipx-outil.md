# Fiche_Simple_-_VM_Debian_13_Python_Pipx_Outil.md

- **Environnement** : Python 3 sur Debian 13 avec venv et pipx
- **OS / Version** : Debian 13 amd64; Python fourni par Debian
- **Catégorie** : développement / pipx

---

## Problème précis à résoudre

Installer un outil CLI Python isolé sans toucher au système.

## 1. Hors-Production (Lab / Test / POC)

1. Préparer le PATH utilisateur :
   ```bash
   pipx ensurepath
   ```
   👉 Explication : Ajoute `~/.local/bin`; ouvrir une nouvelle session ensuite.

2. Installer un outil approuvé (exemple `ruff`, à remplacer par l'outil validé) :
   ```bash
   pipx install ruff
   ```
   👉 Explication : Crée un environnement dédié à l'application.

3. Lister les outils installés :
   ```bash
   pipx list
   ```
   👉 Explication : Confirme l'installation et l'exécutable.

## 2. Production — Contrôles

Mettre à jour un outil après revue de version et essai, sans automatiser de mise à niveau non contrôlée.

## 3. Production — Sécurité

- pipx exécute le code du paquet avec les droits de l'utilisateur : inspecter provenance et permissions avant installation.
- L'isolation n'empêche ni l'accès aux fichiers ni le réseau.

## Validation et retour arrière

- **Validation** : l'outil figure dans `pipx list` et s'exécute.
- **Retour arrière** : `pipx uninstall ruff` (remplacer par l'outil installé).

## Si le problème n'est pas résolu

- [Debian Wiki — Python](https://wiki.debian.org/Python)
- [Python — module venv](https://docs.python.org/3/library/venv.html)
- [pipx — installation](https://pipx.pypa.io/stable/installation/)
- [Guide complet Python Debian 13](/02-fiches-completes/debian/13/installation-deploiement/81-administration-python-3-debian-13-venv-pipx#4-installer-un-outil-cli-isole-avec-pipx)
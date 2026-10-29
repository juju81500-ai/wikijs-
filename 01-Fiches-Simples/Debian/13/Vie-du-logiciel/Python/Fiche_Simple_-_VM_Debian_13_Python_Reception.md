# Fiche_Simple_-_VM_Debian_13_Python_Reception.md

- **Environnement** : Python 3 sur Debian 13 avec venv et pipx
- **OS / Version** : Debian 13 amd64; Python fourni par Debian
- **Catégorie** : développement / réception
- **Tags** : `debian13`, `python`, `validation`, `recette`

---

## Problème précis à résoudre

Valider que l'installation Python respecte les règles Debian.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les versions :
   ```bash
   python3 --version
   python3 -m pip --version
   pipx --version
   ```
   👉 Explication : Doivent correspondre à la configuration Debian approuvée.

2. Contrôler l'isolation du venv :
   ```bash
   .venv/bin/python -c 'import sys; print(sys.prefix != sys.base_prefix)'
   ```
   👉 Explication : Doit afficher `True`.

3. Vérifier l'absence de paquets pip globaux :
   ```bash
   python3 -m pip list --user 2>/dev/null; pip3 list 2>&1 | head -5
   ```
   👉 Explication : Aucun paquet ne doit venir de `sudo pip` ni de `--break-system-packages`.

4. Lister les outils pipx :
   ```bash
   pipx list
   ```
   👉 Explication : Doit refléter les outils approuvés.

## 2. Production — Contrôles

Consigner dépendances, provenance et reconstruction depuis un environnement propre.

## 3. Production — Sécurité

- Aucun paquet ajouté au Python système par `sudo pip`.

## Validation et retour arrière

- **Validation** : les quatre contrôles réussissent.
- **Retour arrière** : corriger l'écart constaté (recréer `.venv`, désinstaller l'outil pipx concerné).

## Si le problème n'est pas résolu

- [Debian Wiki — Python](https://wiki.debian.org/Python)
- [Python — module venv](https://docs.python.org/3/library/venv.html)
- [pipx — installation](https://pipx.pypa.io/stable/installation/)
- [Guide complet Python Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/81_Administration_Python_3_Debian_13_Venv_Pipx.md#7-verifications-de-reception)

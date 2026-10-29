# Fiche_Simple_-_VM_Debian_13_Python_Valider_Venv_Pipx.md

- **Environnement** : Python 3 Debian, `venv` par projet, `pipx` pour outil CLI
- **OS / Version** : Debian 13 Trixie amd64
- **Catégorie** : développement / automatisation

---

## Problème précis à résoudre

Confirmer qu'un projet ou outil Python utilise son environnement isolé et ne modifie pas les paquets système Debian.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les versions et la source des paquets :
   ```bash
   python3 --version
   python3 -m pip --version
   pipx --version
   apt-cache policy python3 pipx
   ```
   👉 Explication : confirme les versions installées et la version candidate Debian.

2. Dans un projet de test, créer l'environnement virtuel :
   ```bash
   python3 -m venv .venv
   ```
   👉 Explication : crée `.venv`, un environnement isolé du Python système.

3. Confirmer le chemin de l'interpréteur et la séparation des préfixes :
   ```bash
   .venv/bin/python -c 'import sys; print(sys.executable); print(sys.prefix != sys.base_prefix)'
   .venv/bin/python -m pip --version
   ```
   👉 Explication : la deuxième ligne affichée doit être `True` : on travaille bien dans l'environnement virtuel.

4. Installer les dépendances depuis le manifeste approuvé, puis vérifier :
   ```bash
   .venv/bin/python -m pip install -r requirements.txt
   .venv/bin/python -m pip list
   ```
   👉 Explication : les paquets sont installés dans `.venv` et non dans le système.

5. Pour un outil en ligne de commande séparé :
   ```bash
   pipx install NOM_OUTIL
   pipx list
   command -v NOM_OUTIL
   ```
   👉 Explication : `pipx` isole l'outil dans son propre environnement; remplacer `NOM_OUTIL` par l'outil approuvé.

## 2. Production — Contrôles

Consigner les versions Python, les sources APT/PyPI approuvées, le fichier de dépendances verrouillé, l'outil CLI et son propriétaire. Tester une reconstruction depuis un environnement vide avant déploiement.

## 3. Production — Sécurité

- Ne pas utiliser `sudo pip`, `pip install` global ou `--break-system-packages`.
- Une `venv` ou un environnement `pipx` isole les dépendances, pas les permissions ou le réseau du code.
- Examiner les projets et dépendances avant installation; limiter les droits des scripts, particulièrement avec `sudo` ou systemd.
- Ne pas versionner `.venv`, tokens ou secrets. Préserver les versions et manifestes nécessaires à la reconstruction.

## Validation et retour arrière

- **Validation** : préfixe virtuel distinct, pip installé dans `.venv`, CLI visible via pipx et aucun changement global effectué.
- **Retour arrière** : conserver le manifeste verrouillé; supprimer puis recréer uniquement la venv du projet de test. Ne pas modifier le Python système pour rétablir un projet.

## Si le problème n'est pas résolu

- [Python — venv](https://docs.python.org/3/library/venv.html)
- [Python Packaging User Guide — pip et venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [Guide complet Python 3 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/81-administration-python-3-debian-13-venv-pipx)
# Fiche_Simple_-_VM_Debian_13_Python_Installer_Outils.md

- **Environnement** : Python 3 sur Debian 13 avec venv et pipx
- **OS / Version** : Debian 13 amd64; Python fourni par Debian
- **Catégorie** : développement / installation

---

## Problème précis à résoudre

Installer Python, pip, venv et pipx depuis les dépôts Debian.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv pipx
   ```
   👉 Explication : Tous viennent des dépôts Debian configurés.

2. Contrôler la provenance APT :
   ```bash
   apt-cache policy python3 python3-pip python3-venv pipx
   ```
   👉 Explication : Consigner la version candidate.

3. Vérifier les versions installées :
   ```bash
   python3 --version
   python3 -m pip --version
   pipx --version
   ```
   👉 Explication : Confirme les trois outils.

## 2. Production — Contrôles

Ne pas mélanger de paquets Python d'une autre distribution ou d'un dépôt non approuvé.

## 3. Production — Sécurité

- Installer uniquement depuis des dépôts approuvés.

## Validation et retour arrière

- **Validation** : les trois commandes de version répondent.
- **Retour arrière** : `sudo apt remove python3-venv python3-pip pipx` (ne jamais retirer `python3` : le système en dépend).

## Si le problème n'est pas résolu

- [Debian Wiki — Python](https://wiki.debian.org/Python)
- [Python — module venv](https://docs.python.org/3/library/venv.html)
- [pipx — installation](https://pipx.pypa.io/stable/installation/)
- [Guide complet Python Debian 13](/02-fiches-completes/debian/13/installation-deploiement/81-administration-python-3-debian-13-venv-pipx#2-installer-python-et-les-outils-debian)
# Fiche_Simple_-_VM_Debian_13_Python_Venv_Projet.md

- **Environnement** : Python 3 sur Debian 13 avec venv et pipx
- **OS / Version** : Debian 13 amd64; Python fourni par Debian
- **Catégorie** : développement / venv
- **Tags** : `debian13`, `python`, `venv`, `requirements`

---

## Problème précis à résoudre

Isoler les dépendances d'un projet dans `.venv`.

## 1. Hors-Production (Lab / Test / POC)

1. Se placer à la racine du projet approuvé (remplacer le chemin) et créer l'environnement :
   ```bash
   cd /chemin/vers/le-projet
   python3 -m venv .venv
   ```
   👉 Explication : Crée `.venv` propre au projet.

2. Contrôler l'interpréteur et pip de l'environnement :
   ```bash
   .venv/bin/python --version
   .venv/bin/python -m pip --version
   ```
   👉 Explication : L'appel par chemin complet évite toute ambiguïté.

3. Installer les dépendances révisées du projet :
   ```bash
   .venv/bin/python -m pip install -r requirements.txt
   ```
   👉 Explication : Le fichier doit être fourni et revu avec le projet.

4. Activation optionnelle :
   ```bash
   source .venv/bin/activate
   python --version
   python -m pip list
   deactivate
   ```
   👉 Explication : Valide l'environnement; `deactivate` en sort.

5. Exclure l'environnement du suivi de versions :
   ```bash
   echo '.venv/' >> .gitignore
   ```
   👉 Explication : Un `.venv` ne se copie ni ne se déplace entre postes.

## 2. Production — Contrôles

Verrouiller versions directes et transitives, utiliser les empreintes si le processus le permet; recréer `.venv` après restauration, changement d'emplacement ou montée majeure de Python.

## 3. Production — Sécurité

- Contrôler éditeur, licence, dépendances et index avant d'installer un paquet.
- Ne pas installer un paquet par simple nom trouvé dans une recherche.

## Validation et retour arrière

- **Validation** : `sys.prefix` diffère de `sys.base_prefix` dans l'environnement.
- **Retour arrière** : supprimer `.venv` : `rm -r .venv`, puis le recréer.

## Si le problème n'est pas résolu

- [Debian Wiki — Python](https://wiki.debian.org/Python)
- [Python — module venv](https://docs.python.org/3/library/venv.html)
- [pipx — installation](https://pipx.pypa.io/stable/installation/)
- [Guide complet Python Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/81_Administration_Python_3_Debian_13_Venv_Pipx.md#3-creer-un-environnement-isole-pour-un-projet)

# Administrer Python 3 sur Debian 13 avec venv et pipx

- **OS / Version** : Debian 13 Trixie amd64; interpréteur Python fourni par Debian
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : paquet système, environnements `venv` par projet et outils CLI isolés avec `pipx`
- **Catégorie** : développement / automatisation / administration
- **Tags** : `python`, `debian13`, `venv`, `pipx`, `pip`, `pep668`, `dependances`

## 1. Choisir le mode d'installation

Fiche simple : [choisir le mode d'installation](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Python/Fiche_Simple_-_VM_Debian_13_Python_Choisir_Mode.md).

Sur Debian, APT possède et gère le Python système et les bibliothèques destinées aux applications du système. Installer les modules disponibles pour une application système avec les paquets Debian. Pour un projet applicatif, utiliser un environnement virtuel `venv` propre au projet. Pour un outil Python en ligne de commande qui ne fait pas partie des paquets Debian, utiliser `pipx`, qui crée un environnement isolé par application.

Ne pas installer de paquets avec `sudo pip`, ne pas écrire dans le `site-packages` global et ne pas contourner PEP 668 avec `--break-system-packages`. Ces contournements peuvent remplacer des modules gérés par APT et rendre l'interpréteur ou des utilitaires système incohérents. Les environnements `venv` et `pipx` ne sont pas des sandboxes : ils isolent les dépendances, pas les permissions d'exécution ou l'accès aux fichiers.

## 2. Installer Python et les outils Debian

Fiche simple : [installer Python et les outils Debian](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Python/Fiche_Simple_-_VM_Debian_13_Python_Installer_Outils.md).

Installer les paquets nécessaires depuis les dépôts Debian configurés et approuvés :

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv pipx
```

Consigner la version Candidate et vérifier la provenance APT avant installation en environnement géré :

```bash
apt-cache policy python3 python3-pip python3-venv pipx
python3 --version
python3 -m pip --version
pipx --version
```

Les numéros de version dépendent des mises à jour de sécurité et du dépôt Debian activé; ne pas mélanger de paquets Python système provenant d'une autre distribution ou d'un dépôt non approuvé.

## 3. Créer un environnement isolé pour un projet

Fiche simple : [créer un environnement isolé pour un projet](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Python/Fiche_Simple_-_VM_Debian_13_Python_Venv_Projet.md).

Depuis la racine d'un projet approuvé, créer un environnement dédié et installer les dépendances documentées par ce projet :

```bash
cd /chemin/vers/le-projet
python3 -m venv .venv
.venv/bin/python --version
.venv/bin/python -m pip --version
.venv/bin/python -m pip install -r requirements.txt
```

Le fichier `requirements.txt` doit être fourni et révisé avec le projet. Pour un déploiement reproductible, verrouiller les versions directes et transitives, et utiliser les empreintes des artefacts lorsque le processus de livraison le permet. Ne pas installer arbitrairement un paquet par nom saisi depuis un résultat de recherche; contrôler son éditeur, sa page projet, sa licence, ses dépendances et la source d'index approuvée.

L'activation est optionnelle; l'appel par chemin complet évite toute ambiguïté d'interpréteur :

```bash
source .venv/bin/activate
python --version
python -m pip list
deactivate
```

Ajouter `.venv/` au fichier d'exclusion du système de gestion de versions. Un environnement virtuel contient des chemins vers son interpréteur de base; ne pas le copier ou le déplacer entre postes. Le recréer à partir des dépendances verrouillées après restauration, mise à niveau majeure de Python ou changement d'emplacement.

## 4. Installer un outil CLI isolé avec pipx

Fiche simple : [installer un outil CLI isolé avec pipx](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Python/Fiche_Simple_-_VM_Debian_13_Python_Pipx_Outil.md).

`pipx` convient à une application CLI autonome, pas aux bibliothèques importées par un projet. Préparer le PATH utilisateur puis installer uniquement un outil connu et approuvé :

```bash
pipx ensurepath
pipx install <outil-cli-approuve>
pipx list
```

Ouvrir une nouvelle session de terminal si `~/.local/bin` vient d'être ajouté au PATH. `pipx` télécharge et exécute le code du paquet sous les droits de l'utilisateur courant; son environnement isolé n'empêche ni l'accès à ses fichiers ni les connexions réseau. Inspecter le projet, les permissions et la provenance avant installation. Mettre à jour un outil après revue de version et essai, plutôt que d'automatiser une mise à niveau non contrôlée.

## 5. Contrôler et maintenir les dépendances

Fiche simple : [contrôler et maintenir les dépendances](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Python/Fiche_Simple_-_VM_Debian_13_Python_Dependances.md).

Pour un projet, enregistrer l'interpréteur utilisé, le manifeste de dépendances, les versions résolues, l'index de paquets et la commande de test. Contrôler les dépendances vulnérables et abandonnées via le processus approuvé de l'organisation; retirer les paquets non utilisés.

Après une mise à jour Python ou des dépendances :

1. Recréer un environnement de test avec le manifeste verrouillé.
2. Lancer les tests du projet et vérifier les commandes ou scripts d'administration sur des données fictives.
3. Comparer les versions et changements sensibles des dépendances avant le déploiement.
4. Préserver l'ancien environnement ou la version déployée jusqu'à validation, mais ne pas compter sur le déplacement ou la copie de son répertoire `.venv` pour le retour arrière.

## 6. Exécuter un script d'administration avec les droits minimaux

Fiche simple : [exécuter un script d'administration avec les droits minimaux](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Python/Fiche_Simple_-_VM_Debian_13_Python_Script_Admin.md).

Examiner le code et les dépendances avant exécution; un script Python lancé avec `sudo` hérite de privilèges étendus. Préférer un compte de service dédié, des droits ciblés ou une opération APT documentée plutôt que d'élever l'ensemble du processus Python. Pour une tâche système, définir explicitement l'interpréteur de `.venv` ou le Python système approuvé dans l'unité systemd, définir un `WorkingDirectory` sûr et limiter `User`, `Group`, fichiers accessibles et capabilities.

Ne pas placer de mots de passe, tokens ou données personnelles dans les arguments, les exemples, les journaux ou les manifests partagés. Injecter les secrets par le gestionnaire de secrets approuvé et éviter leur sortie vers stdout/stderr. Une venv ne valide pas le code et n'isole pas un script malveillant de l'utilisateur qui l'exécute.

## 7. Vérifications de réception

Fiche simple : [vérifications de réception](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Python/Fiche_Simple_-_VM_Debian_13_Python_Reception.md).

- `python3 --version`, `python3 -m pip --version` et `pipx --version` retournent les versions installées par la configuration Debian approuvée.
- Un `venv` fraîchement créé utilise un `sys.prefix` distinct de `sys.base_prefix` et son `python -m pip` installe uniquement dans `.venv`.
- L'outil CLI installé avec `pipx` apparaît dans `pipx list` et son exécutable est accessible au compte utilisateur prévu.
- Aucun paquet n'a été ajouté au Python système par `sudo pip` ou `--break-system-packages`.
- Les dépendances et leur provenance sont révisables, et une reconstruction/test depuis un environnement propre est consignée.

## Sources

- [Debian Wiki — Python et paquets système](https://wiki.debian.org/Python)
- [Python — module venv, création et fonctionnement](https://docs.python.org/3/library/venv.html)
- [Python Packaging User Guide — pip et environnements virtuels](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
- [Python Packaging User Guide — spécification des environnements gérés par l'OS](https://packaging.python.org/en/latest/specifications/externally-managed-environments/)
- [pipx — installation et fonctionnement](https://pipx.pypa.io/stable/installation/)

Les commandes n'ont pas été exécutées sur une machine Debian 13 dans cette fiche. Vérifier les versions candidates, les paquets disponibles et la reconstruction du projet sur un poste pilote.
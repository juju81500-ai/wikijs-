# Fiche_Simple_-_VM_Debian_13_VSCode_Installer.md

- **Environnement** : Poste Debian 13 amd64, VS Code Stable installé via le dépôt APT Microsoft
- **OS / Version** : Debian 13 Trixie amd64; Visual Studio Code Stable 1.143.1
- **Catégorie** : éditeur / installation

---

## Problème précis à résoudre

Installer le paquet `code` et relever la version réelle.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   sudo apt install -y code
   code --version
   apt-cache policy code
   ```
   👉 Explication : installe VS Code; la première ligne de `code --version` est la version installée (1.143.1 au gel du guide).

2. Lancer VS Code depuis le menu ou avec `code`, sous le compte de l'utilisateur.
   👉 Explication : l'éditeur ne doit jamais être lancé avec `sudo`.

## 2. Production — Contrôles

Si une version Stable plus récente est fournie, lire ses notes de version et consigner le changement sans rétrograder.

## 3. Production — Sécurité

- Ne pas lancer l'éditeur avec `sudo`.

## Validation et retour arrière

- **Validation** : `code --version` renvoie une version Stable.
- **Retour arrière** : `sudo apt remove code`.

## Si le problème n'est pas résolu

- [Visual Studio Code — installation Linux](https://code.visualstudio.com/docs/setup/linux)
- [Guide complet Déployer Visual Studio Code Stable 1.143.1 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13#3-installer-et-verifier-vs-code)
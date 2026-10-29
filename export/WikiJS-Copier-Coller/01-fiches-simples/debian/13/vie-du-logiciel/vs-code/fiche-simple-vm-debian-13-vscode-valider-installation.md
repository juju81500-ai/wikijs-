# Fiche_Simple_-_VM_Debian_13_VSCode_Valider_Installation.md

- **Environnement** : Visual Studio Code Stable 1.143.1 via dépôt APT Microsoft sur Debian 13 amd64
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : éditeur de code / environnement de développement

---

## Problème précis à résoudre

Vérifier que VS Code Stable s'installe depuis le dépôt APT Microsoft attendu, s'ouvre sous un compte utilisateur standard et respecte les contrôles de confiance du workspace et des extensions.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer architecture, trousseau et source :
   ```bash
   dpkg --print-architecture
   ls -l /usr/share/keyrings/microsoft.gpg
   grep -rH 'packages.microsoft.com/repos/code' /etc/apt/sources.list.d/
   ```
   👉 Explication : `amd64`; la source doit porter `signed-by=` vers le trousseau Microsoft.

2. Vérifier, installer et contrôler :
   ```bash
   apt-cache policy code
   sudo apt update && sudo apt install code
   code --version
   ```
   👉 Explication : la version provient du dépôt Microsoft.

3. Lancer sans privilèges et tester :
   ```bash
   mkdir -p /tmp/vscode-test && cd /tmp/vscode-test
   code .
   ```
   👉 Explication : créer un fichier de test (**Fichier > Nouveau fichier**), puis fermer; ne jamais lancer avec `sudo`.

4. Ouvrir un dossier non approuvé : à l'invite, choisir **No, I don't trust the authors** (ou **Manage > Workspace Trust**).
   👉 Explication : le bandeau **Restricted Mode** doit apparaître; aucun terminal, tâche ni débogueur ne s'exécute.

5. Installer seulement une extension approuvée :
   ```bash
   code --install-extension EDITEUR.EXTENSION
   code --list-extensions --show-versions
   ```
   👉 Explication : remplacer par l'identifiant approuvé; vérifier l'éditeur dans la vue **Extensions**.

## 2. Production — Contrôles

Consigner la version Stable, l'origine APT, la liste d'extensions autorisées et la méthode de mise à jour. Pour un parc géré, définir les sources approuvées, extensions autorisées, profils, synchronisation et responsable du support.

## 3. Production — Sécurité

- Maintenir Workspace Trust activé; laisser les dépôts inconnus en Restricted Mode pendant leur revue.
- Traiter toute extension comme du code exécuté avec les droits de l'utilisateur; n'installer que le minimum requis.
- Ne pas désactiver la vérification des signatures et ne pas accepter une erreur d'intégrité sans analyse formelle.
- Ne pas lancer VS Code avec `sudo`; ne pas enregistrer secrets, tokens ou données sensibles dans les paramètres partagés du workspace.
- Sauvegarder les profils et paramètres utiles dans un emplacement contrôlé, sans données de session ou secrets non nécessaires.

## Validation et retour arrière

- **Validation** : dépôt APT/signature, version Stable, ouverture utilisateur, Restricted Mode, éditeur d'extension et inventaire vérifiés.
- **Retour arrière** : conserver la version et les extensions consignées; tester désactivation d'extension ou retour de version sur un profil séparé avant changement du poste utilisateur.

## Si le problème n'est pas résolu

- [Visual Studio Code — installation Linux](https://code.visualstudio.com/docs/setup/linux)
- [Visual Studio Code — Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust)
- [Visual Studio Code — sécurité des extensions](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security)
- [Guide complet VS Code Stable Debian 13](/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13)
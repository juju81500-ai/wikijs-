---
title: "Déployer Visual Studio Code Stable 1.143.1 sur Debian 13"
description: "Fiche simple : [cadrer version et périmètre](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/VS-Code/FicheSimple-VMDebian13VSCodeVersion.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["vscode", "visual-studio-code", "debian13", "apt", "workspace-trust", "extensions"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer Visual Studio Code Stable 1.143.1 sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64; Visual Studio Code Stable 1.143.1
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : paquet `.deb` Microsoft via dépôt APT officiel, configuration utilisateur et contrôles Workspace Trust/extensions
- **Catégorie** : éditeur de code / environnement de développement
- **Tags** : `vscode`, `visual-studio-code`, `debian13`, `apt`, `workspace-trust`, `extensions`

## 1. Version et périmètre

Fiche simple : [cadrer version et périmètre](/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-version).

Au 27 octobre 2026, le canal Stable de Visual Studio Code affiche la version 1.143.1. Le guide vise Debian 13 amd64 et utilise le dépôt APT officiel `packages.microsoft.com`; les versions ultérieures du canal Stable sont proposées par ce dépôt et sont mises à jour par APT. VS Code est le produit Microsoft, sous sa licence d'utilisation; il ne s'agit pas de la distribution communautaire Code - OSS.

Ce guide installe l'éditeur et couvre les contrôles de base pour travailler sur des dépôts. Les runtimes, compilateurs, serveurs, extensions propres à un langage, accès distants et fonctions Copilot sont hors périmètre; les installer seulement selon le besoin et les règles de l'organisation.

## 2. Installer le dépôt APT Microsoft

Fiche simple : [installer le dépôt APT Microsoft](/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-depot-apt).

Vérifier l'architecture et installer les outils nécessaires à la configuration du dépôt :

```bash
dpkg --print-architecture
sudo apt update
sudo apt install -y ca-certificates curl gpg
```

La sortie d'architecture doit être `amd64`. Télécharger la clé depuis le point de distribution Microsoft officiel, la convertir en trousseau APT et la limiter au dépôt VS Code avec `signed-by` :

```bash
curl --fail --location --proto '=https' --tlsv1.2 -o /tmp/microsoft.asc https://packages.microsoft.com/keys/microsoft.asc
gpg --show-keys --with-fingerprint /tmp/microsoft.asc
gpg --dearmor --output /tmp/packages.microsoft.gpg /tmp/microsoft.asc
sudo install -D -o root -g root -m 0644 /tmp/packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
rm -f /tmp/microsoft.asc /tmp/packages.microsoft.gpg
printf '%s\n' 'deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main' | sudo tee /etc/apt/sources.list.d/vscode.list >/dev/null
sudo apt update
apt-cache policy code
```

Avant de poursuivre, confirmer que `apt-cache policy code` affiche le dépôt Microsoft attendu et une version Candidate. Ne pas ajouter de dépôt tiers ni utiliser `apt-key`; si le fichier de clés, son origine ou la signature du dépôt ne peuvent pas être vérifiés, arrêter l'installation. Le trousseau est dédié au dépôt VS Code et ne doit pas servir à authentifier d'autres sources APT.

## 3. Installer et vérifier VS Code

Fiche simple : [installer et vérifier VS Code](/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-installer).

Installer le paquet stable et relever la version réellement fournie :

```bash
sudo apt install -y code
code --version
apt-cache policy code
```

La première ligne de `code --version` correspond à la version installée. Au gel de cette fiche, elle est `1.143.1`; si le dépôt fournit une version Stable plus récente, vérifier ses notes de version et consigner le changement plutôt que de rétrograder. Lancer VS Code depuis le menu graphique ou avec `code` sous le compte de l'utilisateur concerné; ne pas lancer l'éditeur avec `sudo`.

## 4. Première ouverture et configuration

Fiche simple : [première ouverture et configuration](/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-premiere-ouverture).

1. Ouvrir un dossier de travail utilisateur et vérifier le chemin dans la barre de titre.
2. Garder les réglages par défaut pour les mises à jour, les espaces de travail et les extensions, sauf politique organisationnelle différente.
3. Configurer les paramètres personnels dans le profil utilisateur. Ne placer ni secrets ni chemins contenant des identifiants dans les réglages versionnés du workspace.
4. Si plusieurs rôles ou projets nécessitent des extensions différentes, créer des profils séparés. Ne synchroniser les paramètres qu'avec un compte et un service autorisés.
5. Si un terminal intégré ou le lancement depuis un shell ne fonctionne pas, vérifier le PATH, le shell et les journaux de l'application avant de modifier les permissions.

## 5. Utiliser Workspace Trust pour les dossiers inconnus

Fiche simple : [utiliser Workspace Trust](/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-workspace-trust).

Lorsqu'un dépôt, une archive ou un dossier reçu n'a pas encore été examiné, le laisser en **Restricted Mode**. Dans ce mode, VS Code limite notamment les terminaux, tâches, débogueurs, réglages d'espace de travail, certaines extensions et agents. Parcourir d'abord les scripts, tâches `.vscode`, fichiers de configuration et commandes de construction; ne faire confiance au dossier que si sa provenance et son contenu ont été évalués.

Ne pas désactiver globalement Workspace Trust pour éviter les demandes. Il réduit le risque d'exécution accidentelle, mais ne constitue pas une sandbox et ne peut pas empêcher une extension malveillante de contourner le mode restreint. Garder à l'esprit que les agents et tâches peuvent modifier des fichiers, lancer des commandes et effectuer des requêtes réseau.

## 6. Installer et gérer les extensions

Fiche simple : [installer et gérer les extensions](/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-extensions).

Les extensions ont les mêmes droits que VS Code : elles peuvent lire et modifier les fichiers accessibles à l'utilisateur, accéder au réseau et lancer des processus. Pour chaque extension nécessaire :

1. Rechercher l'identifiant exact `publisher.extension` dans la vue Extensions.
2. Examiner l'éditeur, l'identité vérifiée éventuelle, la licence, le dépôt, les dépendances, les notes de version et l'activité de maintenance.
3. Confirmer l'éditeur au premier install si VS Code le demande; n'installer que le minimum requis et supprimer les extensions devenues inutiles.
4. Conserver la vérification des signatures activée. Si une signature ne peut être vérifiée, ne pas contourner l'avertissement sans analyse approuvée.
5. Contrôler la liste installée et ses versions avec `code --list-extensions --show-versions`. Les organisations peuvent gérer les extensions autorisées ou utiliser un Marketplace privé.

Le Marketplace analyse et signe les extensions, mais cela ne garantit pas qu'une extension soit adaptée à chaque contexte ni exempte de risque. Pour un environnement administré, établir une liste d'autorisation et un processus de revue des mises à jour.

## 7. Mise à jour, sauvegarde et retour arrière

Fiche simple : [mettre à jour, sauvegarder, revenir en arrière](/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-mise-a-jour).

Le dépôt APT Stable est configuré pour proposer les mises à jour de VS Code avec celles du système. Consulter la version candidate avant une opération de maintenance :

```bash
apt-cache policy code
sudo apt update
sudo apt install --only-upgrade code
code --version
```

En cas de régression, consigner la version installée, les extensions et les journaux avant de désactiver une extension ou de changer de version. Les profils et extensions sont propres à l'utilisateur; sauvegarder les réglages personnels utiles via l'export de profil ou une copie contrôlée de `~/.config/Code/User/`. Éviter de restaurer tout le répertoire de données d'une version plus récente dans une ancienne version sans sauvegarde et essai sur profil séparé.

## 8. Vérifications de réception

Fiche simple : [recette de réception](/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-recette).

- APT présente le dépôt Stable Microsoft avec le trousseau défini par `signed-by`.
- Le paquet `code` s'installe et la commande `code --version` renvoie une version Stable.
- VS Code s'ouvre sous le compte utilisateur et peut créer, modifier et enregistrer un fichier de test dans un dossier autorisé.
- Un dossier de test non approuvé reste en Restricted Mode jusqu'à revue explicite.
- La liste et les versions d'extensions sont inventoriables; les éditeurs et signatures ont été contrôlés pour celles retenues.
- La procédure de sauvegarde/récupération du profil utilisateur est testée sans inclure de secrets dans un dépôt partagé.

## Sources

- [Visual Studio Code — installation Linux, Debian/Ubuntu et mises à jour APT](https://code.visualstudio.com/docs/setup/linux)
- [Visual Studio Code — version Stable 1.143.1 et notes de mise à jour](https://code.visualstudio.com/updates)
- [Visual Studio Code — Workspace Trust et Restricted Mode](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust)
- [Visual Studio Code — Marketplace, extensions et vérification des signatures](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)
- [Visual Studio Code — sécurité d'exécution des extensions](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security)
- [Visual Studio Code — licence](https://code.visualstudio.com/License)

L'installation et les fonctions graphiques ne sont pas testées sur Debian 13 dans cette fiche. Valider le dépôt APT, l'ouverture graphique, Workspace Trust et une extension approuvée sur un poste pilote avant généralisation.
# Fiche_Simple_-_VM_Debian_13_Git_Identite.md

- **Environnement** : Poste Debian 13, client Git
- **OS / Version** : Debian 13 Trixie amd64; paquet Git Debian
- **Catégorie** : gestion de versions / configuration
- **Tags** : `debian13`, `git`, `config`, `identite`

---

## Problème précis à résoudre

Configurer nom et adresse de commit autorisés.

## 1. Hors-Production (Lab / Test / POC)

1. Définir l'identité (valeurs d'exemple à remplacer par les vôtres) :
   ```bash
   git config --global user.name "Nom Approuve"
   git config --global user.email "adresse-approuvee@example.invalid"
   git config --global init.defaultBranch main
   ```
   👉 Explication : l'adresse apparaît dans les commits; suivre la politique du dépôt (adresse dédiée ou masquée).

2. Vérifier l'origine de chaque valeur :
   ```bash
   git config --global --show-origin --get-regexp '^user\.(name|email)$|^init\.defaultbranch$'
   ```
   👉 Explication : on confirme la configuration effective.

3. Pour une identité propre à un projet, dans le dépôt concerné :
   ```bash
   git config --local user.email "adresse-projet@example.invalid"
   ```
   👉 Explication : le niveau local évite une identité erronée globale.

## 2. Production — Contrôles

Identités distinctes par client ou projet au niveau local.

## 3. Production — Sécurité

- Aucun secret dans la configuration Git ni dans l'URL distante.

## Validation et retour arrière

- **Validation** : la commande de vérification affiche l'identité attendue.
- **Retour arrière** : `git config --global --unset user.email` (ou `user.name`).

## Si le problème n'est pas résolu

- [Git — installer Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Git — configuration](https://git-scm.com/docs/git-config)
- [Git — remotes, fetch, pull et push](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Git — credentials](https://git-scm.com/docs/gitcredentials)
- [Guide complet — étape 3](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/82_Administration_Git_Client_Debian_13.md#3-definir-lidentite-de-commit)

# Fiche_Simple_-_VM_Debian_13_Bash_Shell_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 de laboratoire, compte utilisateur non privilégié
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting
- **Tags** : `debian13`, `bash`, `shell`, `scripting`, `securite`
---

## Problème précis à résoudre

Mettre à jour Bash via APT et rejouer les contrôles représentatifs.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter mises à jour et notes Debian
   ```bash
   sudo apt update
   apt list --upgradable bash
   ```
   👉 Explication : vérifier les avis de sécurité et dépôts.

2. Sauvegarder la configuration et relever versions
   ```bash
   cp -a ~/.bashrc ~/.bashrc.before-upgrade
   ```
   👉 Explication : conserver l’état courant.

3. Mettre à jour le paquet approuvé
   ```bash
   sudo apt install --only-upgrade bash
   ```
   👉 Explication : appliquer la fenêtre de changement prévue.

4. Répéter la recette
   ```bash
   bash --version | head -n 1
   bash -n CHEMIN_SCRIPT
   ```
   👉 Explication : retaper les validations avec le chemin à remplacer.

## 2. Production — Contrôles

Déployer d’abord sur pilote, conserver versions/configurations et ne pas rétrograder vers une version vulnérable.

## 3. Production — Sécurité

- Documenter versions et changements de comportement.
- Ne pas restaurer secrets dans des journaux ou fichiers non chiffrés.
- Appliquer avis Debian de sécurité.

## Validation et retour arrière

- **Validation** : Version mise à jour et recette passent.
- **Retour arrière** : Restaurer configuration et choisir un paquet supporté par APT après analyse de régression.

## Si le problème n'est pas résolu

- [GNU Bash — manuel](https://www.gnu.org/software/bash/manual/)
- [Debian — paquet bash](https://packages.debian.org/trixie/bash)
- [ShellCheck — wiki](https://www.shellcheck.net/wiki/)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_Bash_Shell_Prerequis_Limites.md>)

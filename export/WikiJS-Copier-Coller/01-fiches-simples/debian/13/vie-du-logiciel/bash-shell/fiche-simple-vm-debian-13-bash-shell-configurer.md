# Fiche_Simple_-_VM_Debian_13_Bash_Shell_Configurer

- **Environnement** : VM Debian 13 de laboratoire, compte utilisateur non privilégié
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Configurer Bash sans exposer de secrets ni affecter les sessions non interactives.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier configuration utilisateur et système
   ```bash
   cp -a ~/.bashrc ~/.bashrc.before
   nano ~/.bashrc
   ```
   👉 Explication : modifier le profil utilisateur et éviter d’y mettre des secrets.

2. Appliquer une configuration limitée
   ```bash
   export EDITOR="nano"
   export HISTCONTROL=ignoreboth
   ```
   👉 Explication : ne définir que des préférences non sensibles; adapter le profil selon type de shell.

3. Valider la configuration sans effet externe
   ```bash
   bash -n ~/.bashrc
   ```
   👉 Explication : contrôle syntaxique avant chargement.

## 2. Production — Contrôles

Gérer les paramètres par utilisateur ou configuration centrale contrôlée; conserver sauvegarde et documenter les exceptions.

## 3. Production — Sécurité

- Ne jamais conserver identifiants en clair dans l’historique ou config.
- Protéger permissions et environnement.
- Ne pas définir des réglages qui neutralisent TLS ou validation.

## Validation et retour arrière

- **Validation** : La configuration est chargée sans fuite ni effet hors périmètre.
- **Retour arrière** : Restaurer le fichier précédemment sauvegardé puis ouvrir une session propre.

## Si le problème n'est pas résolu

- [GNU Bash — manuel](https://www.gnu.org/software/bash/manual/)
- [Debian — paquet bash](https://packages.debian.org/trixie/bash)
- [ShellCheck — wiki](https://www.shellcheck.net/wiki/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-prerequis-limites>)
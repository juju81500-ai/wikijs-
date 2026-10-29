# Fiche_Simple_-_VM_Debian_13_Bash_Shell_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 de laboratoire, compte utilisateur non privilégié
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Préserver configuration et scripts associés à Bash; vérifier restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder fichiers de configuration non secrets
   ```bash
   install -m 0700 -d ~/.config/bash-backup
   cp -a ~/.bashrc ~/.config/bash-backup/bashrc
   ```
   👉 Explication : sauvegarder seulement la configuration non secrète.

2. Chiffrer et vérifier copie
   ```bash
   sha256sum ~/.config/bash-backup/bashrc
   ```
   👉 Explication : contrôler l’intégrité de copie; protéger le répertoire.

3. Restaurer sur une copie isolée
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.gnu.org/software/bash/manual/
   ```
   👉 Explication : ne pas copier une configuration testée sur des comptes de production sans revue. Détail à confirmer dans la documentation officielle avant application : Restaurer le fichier dans le compte de test et ouvrir une nouvelle session.

## 2. Production — Contrôles

Définir rétention, accès, chiffrement et test de restauration; ne pas sauvegarder les secrets en clair.

## 3. Production — Sécurité

- Ne pas traiter les fichiers secrets comme une sauvegarde ordinaire.
- Séparer sauvegarde et hôte de production.
- Tester la récupération avant dépendance.

## Validation et retour arrière

- **Validation** : Configuration de test est restaurée et les permissions attendues sont conservées.
- **Retour arrière** : Restaurer la copie connue et isoler la version suspecte.

## Si le problème n'est pas résolu

- [GNU Bash — manuel](https://www.gnu.org/software/bash/manual/)
- [Debian — paquet bash](https://packages.debian.org/trixie/bash)
- [ShellCheck — wiki](https://www.shellcheck.net/wiki/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/bash-shell/fiche-simple-vm-debian-13-bash-shell-prerequis-limites>)
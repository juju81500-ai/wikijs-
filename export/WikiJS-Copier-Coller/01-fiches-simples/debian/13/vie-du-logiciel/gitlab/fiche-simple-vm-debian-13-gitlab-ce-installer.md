# Fiche_Simple_-_VM_Debian_13_GitLab_CE_Installer

- **Environnement** : VM Debian 13 de préproduction; FQDN et ressources confirmés
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration

---

## Problème précis à résoudre

Installer GitLab CE depuis le dépôt officiel après examen du script de dépôt et épinglage de version.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis officiels
   ```bash
   sudo apt update
   sudo apt install -y curl ca-certificates openssh-server tzdata perl
   ```
   👉 Explication : vérifier qu’aucun service SSH en place n’est altéré sans accord.

2. Télécharger puis relire le script du dépôt CE
   ```bash
   curl -fsSLo /tmp/gitlab-ce-repo.sh https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh
   less /tmp/gitlab-ce-repo.sh
   ```
   👉 Explication : un script privilégié doit être relu, validé et conservé avec sa provenance.

3. Configurer le dépôt officiel et vérifier origine
   ```bash
   sudo bash /tmp/gitlab-ce-repo.sh
   sudo apt update
   apt-cache policy gitlab-ce
   ```
   👉 Explication : le candidat doit venir du dépôt GitLab CE approuvé.

4. Installer la version approuvée
   ```bash
   sudo EXTERNAL_URL="https://gitlab.example.com" apt install gitlab-ce=18.X.Y-ce.0
   ```
   👉 Explication : remplacer le FQDN et la version à remplacer; choisir une version de la matrice supportée.

5. Contrôler les composants
   ```bash
   sudo gitlab-ctl status
   sudo gitlab-rake gitlab:env:info
   ```
   👉 Explication : consigner versions et résultats avant configuration.

## 2. Production — Contrôles

Tester l’installation sur une copie de préproduction; épingler paquet et origine APT et appliquer un changement tracé.

## 3. Production — Sécurité

- Ne pas exécuter de script distant non relu en root.
- Ne pas désactiver APT Secure ni utiliser un dépôt tiers.
- Restreindre l’accès initial aux administrateurs et changer le secret initial via le flux officiel.

## Validation et retour arrière

- **Validation** : Les services sont actifs et le paquet installé vient du dépôt approuvé.
- **Retour arrière** : Restaurer l’instantané pilote; préserver les données avant toute désinstallation.

## Si le problème n'est pas résolu

- [GitLab — installation paquet](https://docs.gitlab.com/install/package/)
- [GitLab — configuration Omnibus](https://docs.gitlab.com/omnibus/settings/)
- [GitLab — backup/restore](https://docs.gitlab.com/omnibus/backup-restore/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-prerequis-limites>)
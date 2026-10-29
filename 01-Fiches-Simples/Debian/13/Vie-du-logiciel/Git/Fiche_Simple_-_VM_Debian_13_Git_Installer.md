# Fiche_Simple_-_VM_Debian_13_Git_Installer.md

- **Environnement** : Poste Debian 13, client Git
- **OS / Version** : Debian 13 Trixie amd64; paquet Git Debian
- **Catégorie** : gestion de versions / installation
- **Tags** : `debian13`, `git`, `apt`, `openssh`

---

## Problème précis à résoudre

Installer Git et OpenSSH depuis les dépôts Debian.

## 1. Hors-Production (Lab / Test / POC)

1. Installer :
   ```bash
   sudo apt update
   sudo apt install -y git openssh-client ca-certificates
   ```
   👉 Explication : les paquets viennent des dépôts Debian approuvés.

2. Contrôler la version et la source :
   ```bash
   git --version
   apt-cache policy git
   ```
   👉 Explication : consigner la version `Candidate` et la source.

## 2. Production — Contrôles

Préférer le paquet Debian aux scripts tiers ou compilations manuelles, sauf exigence approuvée.

## 3. Production — Sécurité

- Ne pas installer Git par script téléchargé.

## Validation et retour arrière

- **Validation** : `git --version` répond.
- **Retour arrière** : `sudo apt remove git`.

## Si le problème n'est pas résolu

- [Git — installer Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Git — configuration](https://git-scm.com/docs/git-config)
- [Git — remotes, fetch, pull et push](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Git — credentials](https://git-scm.com/docs/gitcredentials)
- [Guide complet — étape 2](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/82_Administration_Git_Client_Debian_13.md#2-installer-le-client-git)

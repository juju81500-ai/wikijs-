# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_23_Outils_D_Administration_Fondamentaux

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 23 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer la boîte à outils d'exploitation.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les outils courants :
   ```bash
   sudo dnf install -y vim-enhanced tmux curl wget rsync bind-utils net-tools lsof tcpdump bash-completion policycoreutils-python-utils
   ```
   👉 Explication : diagnostic réseau, édition, SELinux (`semanage`).

2. Installer les outils de performance :
   ```bash
   sudo dnf install -y htop iotop sysstat
   ```
   👉 Explication : observer CPU, mémoire et disques.

3. Contrôler la présence des commandes :
   ```bash
   command -v vim tmux semanage rsync
   ```
   👉 Explication : chaque commande doit répondre un chemin.

## 2. Production — Contrôles

Limiter la liste au nécessaire et la documenter.

## 3. Production — Sécurité

Retirer les outils d'attaque inutiles (compilateurs, scanners) sur la production.

## Validation et retour arrière

- **Validation** : Les commandes de la liste existent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)
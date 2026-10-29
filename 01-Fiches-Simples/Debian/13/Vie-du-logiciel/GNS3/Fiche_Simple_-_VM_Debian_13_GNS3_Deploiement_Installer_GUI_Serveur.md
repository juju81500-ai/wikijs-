# Fiche_Simple_-_VM_Debian_13_GNS3_Deploiement_Installer_GUI_Serveur.md

- **Environnement** : Poste Debian 13 avec dépendances installées
- **OS / Version** : Debian 13 Trixie amd64; GNS3 2.2.61 stable
- **Catégorie** : simulation reseau / installation
- **Tags** : `gns3`, `debian13`, `pipx`, `gns3-server`

---

## Problème précis à résoudre

Installer GNS3 GUI et serveur 2.2.61 par pipx.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les deux composants à la même version :
   ```bash
   pipx ensurepath
   pipx install gns3-server==2.2.61
   pipx install gns3-gui==2.2.61
   pipx inject gns3-gui gns3-server==2.2.61 PyQt6
   ```
   👉 Explication : `pipx` isole chaque outil sans toucher au Python système; client et serveur doivent avoir la même version.

2. Fermer puis rouvrir la session utilisateur.
   👉 Explication : pour que `~/.local/bin` soit dans le PATH.

3. Contrôler les exécutables :
   ```bash
   command -v gns3
   command -v gns3server
   gns3 --version
   gns3server --version
   ```
   👉 Explication : les deux doivent afficher 2.2.61.

## 2. Production — Contrôles

Documenter les versions GUI/serveur et mettre à niveau les deux ensemble.

## 3. Production — Sécurité

- Pas de PPA Ubuntu ni de `sudo pip`.
- Ne pas forcer une version non stable si une dépendance manque.

## Validation et retour arrière

- **Validation** : `gns3 --version` et `gns3server --version` affichent 2.2.61.
- **Retour arrière** : `pipx uninstall gns3-gui` puis `pipx uninstall gns3-server`.

## Si le problème n'est pas résolu

- [GNS3 — installation Linux](https://docs.gns3.com/docs/getting-started/installation/linux)
- [GNS3 — release 2.2.61](https://github.com/GNS3/gns3-gui/releases/tag/v2.2.61)
- [Guide complet GNS3 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/77_Deploiement_GNS3_2.2.61_Debian_13.md#3-installer-linterface-et-le-serveur-stables)

# Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Ubuntu 24.04 LTS de laboratoire, accès sudo, dépôt Microsoft officiel
- **OS / Version** : Ubuntu 24.04 LTS
- **Catégorie** : shell / scripting
- **Tags** : `ubuntu2404`, `powershell`, `pwsh`, `scripting`

---

## Problème précis à résoudre

Mettre à jour PowerShell 7 de façon contrôlée et savoir revenir à la version précédente.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder l'état avant mise à jour (voir la fiche Sauvegarder_Restaurer).
   👉 Explication : permet de restaurer profils et modules.

2. Lister la version installée et candidate, puis mettre à jour :
   ```bash
   apt-cache policy powershell
   sudo apt-get update
   sudo apt-get install --only-upgrade powershell
   ```
   👉 Explication : met à jour le seul paquet powershell.

3. Figer la version après validation :
   ```bash
   sudo apt-mark hold powershell
   ```
   👉 Explication : empêche une mise à jour non planifiée ; `unhold` pour la lever.

4. Retour arrière vers une version précédente (VERSION_APT à remplacer par une version listée par `apt-cache policy` ou `apt-cache madison powershell`) :
   ```bash
   sudo apt-get install powershell=VERSION_APT
   ```
   👉 Explication : possible seulement si la version est encore publiée dans le dépôt ; sinon réinstaller depuis le paquet `.deb` archivé.

5. Contrôler après mise à jour :
   ```bash
   pwsh -NoLogo -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
   ```
   👉 Explication : comparer à la version attendue ; rejouer la recette.

## 2. Production — Contrôles

Tester sur un pilote, lire les notes de version PowerShell, conserver le paquet précédent. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne mettre à jour que depuis le dépôt Microsoft approuvé.
- Ne pas mélanger Snap, APT et téléchargements manuels.

## Validation et retour arrière

- **Validation** : la version attendue est active et la recette est conforme.
- **Retour arrière** : rétrograder la version comme ci-dessus puis restaurer profils et modules.

## Si le problème n'est pas résolu

- [Notes de version PowerShell](https://github.com/PowerShell/PowerShell/releases)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Prerequis_Limites.md)

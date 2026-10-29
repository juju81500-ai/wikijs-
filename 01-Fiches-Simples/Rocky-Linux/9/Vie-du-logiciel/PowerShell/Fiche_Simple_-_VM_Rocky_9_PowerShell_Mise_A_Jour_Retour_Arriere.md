# Fiche_Simple_-_VM_Rocky_9_PowerShell_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Rocky Linux 9 de laboratoire, accès sudo, dépôt Microsoft pour RHEL 9
- **OS / Version** : Rocky Linux 9
- **Catégorie** : shell / scripting
- **Tags** : `rocky9`, `powershell`, `pwsh`, `scripting`

---

## Problème précis à résoudre

Mettre à jour PowerShell 7 de façon contrôlée et savoir revenir à la version précédente.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder l'état avant mise à jour (voir la fiche Sauvegarder_Restaurer).
   👉 Explication : permet de restaurer profils et modules.

2. Lister la version installée et disponible, puis mettre à jour :
   ```bash
   dnf list --showduplicates powershell
   sudo dnf upgrade powershell
   ```
   👉 Explication : met à jour le seul paquet powershell.

3. Retour arrière vers la version précédente :
   ```bash
   dnf history list powershell
   sudo dnf downgrade powershell
   ```
   👉 Explication : `dnf downgrade` installe une version antérieure disponible dans les dépôts ; sinon installer le RPM archivé.

4. Figer une version (extension versionlock, à installer au préalable) :
   ```bash
   sudo dnf install -y python3-dnf-plugin-versionlock
   sudo dnf versionlock add powershell
   ```
   👉 Explication : empêche les mises à jour automatiques non validées.

5. Contrôler après mise à jour :
   ```bash
   pwsh -NoLogo -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
   ```
   👉 Explication : comparer à la version attendue ; rejouer la recette.

## 2. Production — Contrôles

Tester sur un pilote, lire les notes de version PowerShell, conserver le paquet précédent. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne mettre à jour que depuis le dépôt Microsoft approuvé.
- Ne pas mélanger RPM manuels et dépôt.

## Validation et retour arrière

- **Validation** : la version attendue est active et la recette est conforme.
- **Retour arrière** : rétrograder la version comme ci-dessus puis restaurer profils et modules.

## Si le problème n'est pas résolu

- [Notes de version PowerShell](https://github.com/PowerShell/PowerShell/releases)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_VM_Rocky_9_PowerShell_Prerequis_Limites.md)

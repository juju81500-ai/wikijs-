# Fiche_Simple_-_Windows_Server_2022_PowerShell_Mise_A_Jour_Retour_Arriere

- **Environnement** : Windows Server 2022 de laboratoire (Desktop Experience ou Core), session administrateur
- **OS / Version** : Windows Server 2022
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Mettre à jour PowerShell 7 sur Windows Server 2022 et revenir à la version précédente.

## 1. Hors-Production (Lab / Test / POC)

1. Conserver le MSI de la version actuelle et sauvegarder (fiche Sauvegarder_Restaurer).
   👉 Explication : permet le retour arrière hors ligne.

2. Installer le MSI de la nouvelle version approuvée par-dessus (CHEMIN_MSI_NOUVEAU à remplacer ; contrôler hash et signature comme à l'installation) :
   ```powershell
   msiexec.exe /package CHEMIN_MSI_NOUVEAU /quiet ADD_PATH=1 REGISTER_MANIFEST=1
   ```
   👉 Explication : le MSI de la même ligne de produit applique une mise à niveau. Microsoft Update pour PowerShell est activable via `USE_MU`/`ENABLE_MU` : vérifier la politique de patch avant.

3. Contrôler la version :
   ```powershell
   & 'C:\Program Files\PowerShell\7\pwsh.exe' -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
   ```
   👉 Explication : rejouer la recette.

4. Retour arrière : GUI Paramètres > Applications > Applications installées > PowerShell > Désinstaller ; ligne de commande avec le MSI courant puis réinstallation de l'ancien (CHEMIN_MSI_COURANT et CHEMIN_MSI_ANCIEN à remplacer) :
   ```powershell
   msiexec.exe /x CHEMIN_MSI_COURANT /quiet
   msiexec.exe /package CHEMIN_MSI_ANCIEN /quiet ADD_PATH=1 REGISTER_MANIFEST=1
   ```
   👉 Explication : désinstaller ne touche pas Windows PowerShell 5.1.

## 2. Production — Contrôles

Tester sur un pilote, lire les notes de version et planifier une fenêtre de maintenance. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- N'utiliser que des MSI contrôlés (hash et signature).
- Ne pas laisser la mise à jour automatique activée sans validation.

## Validation et retour arrière

- **Validation** : la version attendue est active et la recette est conforme.
- **Retour arrière** : désinstaller la version fautive puis réinstaller l'ancien MSI archivé.

## Si le problème n'est pas résolu

- [Notes de version PowerShell](https://github.com/PowerShell/PowerShell/releases)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-prerequis-limites)
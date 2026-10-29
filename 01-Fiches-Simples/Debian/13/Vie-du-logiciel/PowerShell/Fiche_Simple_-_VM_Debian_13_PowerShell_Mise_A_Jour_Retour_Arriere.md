# Fiche_Simple_-_VM_Debian_13_PowerShell_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13 de laboratoire avec dépôts Microsoft officiels
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting
- **Tags** : `debian13`, `powershell`, `pwsh`, `scripting`, `securite`
---

## Problème précis à résoudre

Gérer version PowerShell et modules avec test de compatibilité avant déploiement.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter version et candidat
   ```bash
   pwsh -NoLogo -NoProfile -Command "$PSVersionTable.PSVersion.ToString()"
   sudo apt update
   apt-cache policy powershell
   ```
   👉 Explication : vérifier origine et notes de version.

2. Mettre à jour en pilote
   ```bash
   sudo apt install --only-upgrade powershell
   ```
   👉 Explication : faire le changement dans une fenêtre approuvée.

3. Rejouer les tests des modules/scripts
   ```powershell
   $PSVersionTable.PSVersion
   ./SCRIPT.ps1 -WhatIf
   ```
   👉 Explication : remplacer le script à remplacer; confirmer comportement sous version cible.

4. Préparer retour à version supportée
   ```text
   Navigateur > ouvrir la documentation officielle : https://learn.microsoft.com/powershell/scripting/install/install-debian
   ```
   👉 Explication : ne pas downgrader vers version vulnérable sans dérogation. Détail à confirmer dans la documentation officielle avant application : Conserver version/package approuvé et restaurer le profil/modules compatibles selon gestion APT.

## 2. Production — Contrôles

Pinner CLI/modules dans automatisation; tester puis déployer par anneaux.

## 3. Production — Sécurité

- Ne pas mélanger deux binaires dans le PATH des tâches.
- Ne pas revenir à un paquet vulnérable sans validation sécurité.
- Consigner incompatibilités modules.

## Validation et retour arrière

- **Validation** : Version cible, modules et tests prioritaires fonctionnent.
- **Retour arrière** : Restaurer version supportée et profil compatible selon gestion APT après analyse.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer Debian](https://learn.microsoft.com/powershell/scripting/install/install-debian)
- [Microsoft Learn — sécurité](https://learn.microsoft.com/powershell/scripting/security/security-features)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_PowerShell_Prerequis_Limites.md>)

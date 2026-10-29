# Fiche_Simple_-_VM_Debian_13_PowerShell_Valider

- **Environnement** : VM Debian 13 de laboratoire avec dépôts Microsoft officiels
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Valider version, module, code retour et effets d’un script sur une VM isolée.

## 1. Hors-Production (Lab / Test / POC)

1. Afficher plateforme et version
   ```powershell
   $PSVersionTable | Format-List PSEdition,PSVersion,OS,Platform
   ```
   👉 Explication : la plateforme doit correspondre aux scripts.

2. Importer module autorisé et inspecter commandes
   ```powershell
   Import-Module NOM_MODULE -ErrorAction Stop
   Get-Command -Module NOM_MODULE
   ```
   👉 Explication : remplacer le module à remplacer; n’importer aucun module non vérifié.

3. Exécuter test non destructif et relever code
   ```powershell
   pwsh -NoLogo -NoProfile -Command "./SCRIPT.ps1 -WhatIf; exit $LASTEXITCODE"
   ```
   👉 Explication : remplacer le script à remplacer; adapter si le script n’a pas d’option WhatIf.

4. Contrôler journal et processus sans exposer arguments sensibles
   ```bash
   journalctl --user -n 50 --no-pager
   ```
   👉 Explication : examiner uniquement logs sans secrets.

## 2. Production — Contrôles

Définir cas nominaux/erreur, délais, résultat et compatibilité de module; obtenir validation du propriétaire.

## 3. Production — Sécurité

- Utiliser données fictives et modules approuvés.
- Nettoyer artefacts et journaux de test.
- Ne pas exécuter des scripts inconnus « pour voir ».

## Validation et retour arrière

- **Validation** : Version, sortie, code retour et effets sont conformes aux tests documentés.
- **Retour arrière** : Désactiver tâche et restaurer l’état de laboratoire à partir du snapshot.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer Debian](https://learn.microsoft.com/powershell/scripting/install/install-debian)
- [Microsoft Learn — sécurité](https://learn.microsoft.com/powershell/scripting/security/security-features)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-prerequis-limites>)
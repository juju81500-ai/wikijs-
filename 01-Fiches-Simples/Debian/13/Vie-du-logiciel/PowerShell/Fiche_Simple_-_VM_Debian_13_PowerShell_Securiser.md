# Fiche_Simple_-_VM_Debian_13_PowerShell_Securiser

- **Environnement** : VM Debian 13 de laboratoire avec dépôts Microsoft officiels
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting
- **Tags** : `debian13`, `powershell`, `pwsh`, `scripting`, `securite`
---

## Problème précis à résoudre

Réduire privilèges et exposition de secrets lors des scripts PowerShell sous Linux.

## 1. Hors-Production (Lab / Test / POC)

1. Inspecter le script avant exécution
   ```powershell
   Get-Content ./SCRIPT.ps1
   ```
   👉 Explication : remplacer le chemin à remplacer; examiner écritures, appels réseau et commandes privilégiées.

2. Vérifier policy et permissions du fichier
   ```powershell
   Get-ExecutionPolicy -List
   Get-Item ./SCRIPT.ps1 | Format-List FullName,Length
   ```
   👉 Explication : ExecutionPolicy n’est pas une frontière de sécurité; compléter par ACL Linux et revue de code.

3. Tester compte et mode simulation
   ```bash
   id
   pwsh -NoLogo -NoProfile -File ./SCRIPT.ps1 -WhatIf
   ```
   👉 Explication : remplacer le chemin à remplacer; utiliser WhatIf uniquement si le script le prend en charge.

4. Ne pas exporter secrets dans les logs
   ```text
   Navigateur > ouvrir la documentation officielle : https://learn.microsoft.com/powershell/scripting/install/install-debian
   ```
   👉 Explication : ne pas afficher variables d’environnement contenant des credentials. Détail à confirmer dans la documentation officielle avant application : Utiliser un gestionnaire de secrets approuvé; masquer paramètres et sorties sensibles.

## 2. Production — Contrôles

Faire relire le code, limiter droits Unix, contrôler dépendances et journaliser les opérations sans secrets.

## 3. Production — Sécurité

- Ne pas traiter ExecutionPolicy comme protection contre du code malveillant.
- Ne pas utiliser sudo si compte dédié suffit.
- Révoquer tout credential exposé et auditer les runs concernés.

## Validation et retour arrière

- **Validation** : Le script est relu et testé sans privilèges inutiles; sortie et journaux ne contiennent aucun secret.
- **Retour arrière** : Arrêter tâches, révoquer credentials exposés et restaurer les fichiers modifiés.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer Debian](https://learn.microsoft.com/powershell/scripting/install/install-debian)
- [Microsoft Learn — sécurité](https://learn.microsoft.com/powershell/scripting/security/security-features)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_PowerShell_Prerequis_Limites.md>)

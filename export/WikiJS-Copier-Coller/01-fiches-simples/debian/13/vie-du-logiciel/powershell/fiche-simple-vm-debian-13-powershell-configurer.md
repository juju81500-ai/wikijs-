# Fiche_Simple_-_VM_Debian_13_PowerShell_Configurer

- **Environnement** : VM Debian 13 de laboratoire avec dépôts Microsoft officiels
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Configurer profils et sources de modules sans y stocker de secret.

## 1. Hors-Production (Lab / Test / POC)

1. Afficher profil et chemins de modules
   ```powershell
   pwsh -NoLogo -NoProfile -Command "$PROFILE | Format-List *; $env:PSModulePath"
   ```
   👉 Explication : noter les chemins utilisateur et système avant modification.

2. Créer profil utilisateur contrôlé
   ```powershell
   pwsh -NoLogo -NoProfile -Command "New-Item -ItemType File -Force -Path $PROFILE | Out-Null"
   ```
   👉 Explication : ne pas modifier profil global pour un test.

3. Auditer les dépôts PowerShell
   ```powershell
   Get-PSRepository | Format-Table Name,SourceLocation,InstallationPolicy
   ```
   👉 Explication : n’approuver que des dépôts vérifiés.

4. Valider un script sans le lancer
   ```powershell
   $e=$null; [System.Management.Automation.Language.Parser]::ParseFile((Resolve-Path ./SCRIPT.ps1),[ref]$null,[ref]$e) | Out-Null; $e
   ```
   👉 Explication : remplacer le fichier à remplacer; un contrôle syntaxique ne valide pas ses effets.

## 2. Production — Contrôles

Gérer versions, dépôts et profils avec droits minimaux; tester les scripts non interactifs et tâches planifiées.

## 3. Production — Sécurité

- Ne pas placer secrets dans `$PROFILE`.
- Ne pas faire confiance automatiquement à un dépôt de modules inconnu.
- Protéger les permissions du chemin des modules.

## Validation et retour arrière

- **Validation** : Profil charge sans erreur et modules viennent d’une source approuvée.
- **Retour arrière** : Restaurer profil et liste de modules avant la modification.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer Debian](https://learn.microsoft.com/powershell/scripting/install/install-debian)
- [Microsoft Learn — sécurité](https://learn.microsoft.com/powershell/scripting/security/security-features)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-prerequis-limites>)
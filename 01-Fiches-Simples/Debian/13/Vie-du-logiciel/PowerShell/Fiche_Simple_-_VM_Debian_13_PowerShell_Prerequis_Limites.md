# Fiche_Simple_-_VM_Debian_13_PowerShell_Prerequis_Limites

- **Environnement** : VM Debian 13 de laboratoire avec dépôts Microsoft officiels
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting
- **Tags** : `debian13`, `powershell`, `pwsh`, `scripting`, `securite`
---

## Problème précis à résoudre

Confirmer support Debian 13, architecture, scripts et modules avant installation de PowerShell 7.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier OS, architecture et présence du binaire
   ```bash
   cat /etc/os-release
   dpkg --print-architecture
   command -v pwsh || true
   ```
   👉 Explication : valider architecture et compatibilité dans la documentation Microsoft actuelle.

2. Inventorier scripts et modules
   ```bash
   grep -RIn --include="*.ps1" "^#Requires\|Import-Module" CHEMIN_PROJET
   ```
   👉 Explication : remplacer le chemin à remplacer; identifier les dépendances Windows-only.

3. Vérifier support et canal
   ```text
   Microsoft Learn > Install PowerShell on Debian : vérifier Debian 13, architecture et version stable.
   ```
   👉 Explication : arrêter si la documentation ne cite pas la combinaison exacte.

## 2. Production — Contrôles

Documenter compatibilité des scripts/modules et les dépendances avant migration.

## 3. Production — Sécurité

- Ne pas supposer qu’un module Windows fonctionne sur Linux.
- Exécuter sous compte non privilégié et source de confiance.
- Ne pas stocker secrets dans profil ou scripts.

## Validation et retour arrière

- **Validation** : Microsoft confirme le support de la plateforme et les modules requis sont identifiés.
- **Retour arrière** : Reporter si OS, architecture ou module n’est pas supporté.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer Debian](https://learn.microsoft.com/powershell/scripting/install/install-debian)
- [Microsoft Learn — sécurité](https://learn.microsoft.com/powershell/scripting/security/security-features)
- [Fiche connexe](<Fiche_Simple_-_VM_Debian_13_PowerShell_Installer.md>)

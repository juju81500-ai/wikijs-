# Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Configurer_Profils_Modules

- **Environnement** : VM Ubuntu 24.04 LTS de laboratoire, accès sudo, dépôt Microsoft officiel
- **OS / Version** : Ubuntu 24.04 LTS
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Configurer les profils PowerShell 7 et l'installation de modules (PSResourceGet / PowerShellGet) de façon maîtrisée.

## 1. Hors-Production (Lab / Test / POC)

1. Afficher les chemins de profils et le chemin des modules :
   ```bash
   pwsh -NoLogo -NoProfile -Command '$PROFILE | Select-Object *; $env:PSModulePath -split ":"'
   ```
   👉 Explication : sous Linux, le profil utilisateur est dans `~/.config/powershell/` ; le profil commun est dans `$PSHOME` (répertoire d'installation de pwsh).

2. Créer un profil utilisateur minimal, sans secret :
   ```bash
   mkdir -p ~/.config/powershell
   cat > ~/.config/powershell/Microsoft.PowerShell_profile.ps1 <<'EOP'
   $ErrorActionPreference = 'Stop'
   Set-PSReadLineOption -HistorySaveStyle SaveNothing
   EOP
   ```
   👉 Explication : un profil court et versionné ; `SaveNothing` évite d'enregistrer l'historique des commandes (option PSReadLine à adapter à votre politique).

3. Lister les modules disponibles et les dépôts configurés :
   ```bash
   pwsh -NoLogo -NoProfile -Command 'Get-Module -ListAvailable | Select-Object Name,Version; Get-PSResourceRepository'
   ```
   👉 Explication : PowerShell 7.4 et supérieur embarque PSResourceGet (`Install-PSResource`) ; avec une version plus ancienne, utiliser `Install-Module` de PowerShellGet.

4. Installer un module en version fixée, pour l'utilisateur courant (MODULE et VERSION sont à remplacer) :
   ```bash
   pwsh -NoLogo -NoProfile -Command 'Install-PSResource -Name MODULE -Version VERSION -Scope CurrentUser'
   ```
   👉 Explication : PSGallery n'est pas approuvé par défaut : une confirmation est demandée ; n'ajouter `-TrustRepository` qu'après validation du module.

5. Lister puis désinstaller un module si besoin :
   ```bash
   pwsh -NoLogo -NoProfile -Command 'Get-InstalledPSResource; Uninstall-PSResource -Name MODULE'
   ```
   👉 Explication : permet de contrôler l'inventaire installé.

## 2. Production — Contrôles

Utiliser un dépôt interne ou `Save-PSResource` pour distribuer des modules relus ; documenter les versions. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne pas marquer PSGallery comme approuvé globalement sans politique.
- Éviter `-Scope AllUsers` sans revue : il exige sudo et modifie le système.

## Validation et retour arrière

- **Validation** : les modules visés apparaissent dans `Get-InstalledPSResource` avec la version attendue.
- **Retour arrière** : désinstaller le module avec `Uninstall-PSResource` et restaurer le profil sauvegardé.

## Si le problème n'est pas résolu

- [Microsoft Learn — profils](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_profiles)
- [Microsoft Learn — PSResourceGet](https://learn.microsoft.com/powershell/gallery/powershellget/overview)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-prerequis-limites)
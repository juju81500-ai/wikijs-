# Fiche_Simple_-_Windows_Server_2022_PowerShell_Configurer_Profils_Modules

- **Environnement** : Windows Server 2022 de laboratoire (Desktop Experience ou Core), session administrateur
- **OS / Version** : Windows Server 2022
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Configurer les profils et les modules pour Windows PowerShell 5.1 et PowerShell 7 sur Windows Server 2022.

## 1. Hors-Production (Lab / Test / POC)

1. Afficher les profils et chemins de modules dans chaque version :
   ```powershell
   $PROFILE | Select-Object *
   $env:PSModulePath -split ';'
   ```
   👉 Explication : 5.1 utilise `Documents\WindowsPowerShell\` ; PowerShell 7 utilise `Documents\PowerShell\` et son répertoire d'installation pour le profil commun (`AllUsers*`). Lancer la commande dans chaque shell.

2. Créer un profil utilisateur PowerShell 7 minimal, sans secret :
   ```powershell
   New-Item -ItemType File -Path $PROFILE.CurrentUserAllHosts -Force
   Add-Content -Path $PROFILE.CurrentUserAllHosts -Value '$ErrorActionPreference = ''Stop'''
   ```
   👉 Explication : le profil s'exécute à chaque démarrage : le garder court et versionné.

3. Lister les modules disponibles :
   ```powershell
   Get-Module -ListAvailable | Select-Object Name,Version,ModuleBase
   ```
   👉 Explication : identifie les modules propres à 5.1 et ceux disponibles dans 7.

4. Charger un module Windows historique dans PowerShell 7 via la compatibilité (MODULE à remplacer) :
   ```powershell
   Import-Module -Name MODULE -UseWindowsPowerShell
   ```
   👉 Explication : exécute le module dans un processus Windows PowerShell 5.1 avec des objets désérialisés ; à valider par module.

5. Installer un module de la galerie en version fixée (MODULE et VERSION à remplacer) :
   ```powershell
   Install-PSResource -Name MODULE -Version VERSION -Scope CurrentUser   # PowerShell 7.4+
   Install-Module -Name MODULE -RequiredVersion VERSION -Scope CurrentUser   # PowerShellGet, Windows PowerShell 5.1
   ```
   👉 Explication : `Install-PSResource` (PSResourceGet) est livré avec PowerShell 7.4 et supérieur ; en 5.1 utiliser PowerShellGet. PSGallery reste non approuvé tant qu'on ne le décide pas.

6. Fonctionnalités Windows (module ServerManager) : GUI Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités ; ligne de commande :
   ```powershell
   Get-WindowsFeature | Where-Object Installed
   ```
   👉 Explication : à lancer dans Windows PowerShell 5.1 pour une compatibilité maximale.

## 2. Production — Contrôles

Utiliser un dépôt interne ou `Save-Module`/`Save-PSResource` pour distribuer des modules relus et versionnés. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne pas rendre PSGallery approuvé globalement sans politique.
- Pas de secret dans un profil.

## Validation et retour arrière

- **Validation** : profils chargés sans erreur et modules attendus présents dans les deux versions.
- **Retour arrière** : supprimer le profil créé et désinstaller le module (`Uninstall-PSResource`).

## Si le problème n'est pas résolu

- [Microsoft Learn — profils](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_profiles)
- [Microsoft Learn — PSResourceGet](https://learn.microsoft.com/powershell/gallery/powershellget/overview)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-prerequis-limites)
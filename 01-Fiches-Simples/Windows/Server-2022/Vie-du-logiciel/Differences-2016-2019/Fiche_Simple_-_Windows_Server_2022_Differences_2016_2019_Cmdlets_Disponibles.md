# Fiche_Simple_-_Windows_Server_2022_Differences_2016_2019_Cmdlets_Disponibles

- **Environnement** : Windows Server 2016 et 2019 (comparés à 2022), lab ou serveur de test
- **OS / Version** : Windows Server 2016 / 2019 (référence 2022)
- **Catégorie** : systèmes / différences de versions
- **Tags** : `windows-server`, `windows-server-2016`, `windows-server-2019`, `windows-server-2022`, `powershell`, `cmdlets`

---

## Problème précis à résoudre

Savoir quelles cmdlets et quelle version de PowerShell sont disponibles sur 2016 et 2019 avant d'exécuter un script écrit pour 2022.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la version de PowerShell :
   ```powershell
   $PSVersionTable.PSVersion
   ```
   👉 Explication : Windows PowerShell 5.1 est la version intégrée à Windows Server 2016, 2019 et 2022 ; PowerShell 7 est un produit distinct à installer.
2. Tester la présence d'une cmdlet avant de l'utiliser (remplacer `NOM_CMDLET` par la cmdlet visée) :
   ```powershell
   Get-Command -Name NOM_CMDLET -ErrorAction SilentlyContinue
   Get-Module -ListAvailable | Select-Object Name,Version
   ```
   👉 Explication : une absence signale un module manquant (fonctionnalité RSAT/rôle non installé) ou une cmdlet introduite après la version du serveur.
3. Installer les outils d'administration manquants :
   ```powershell
   Install-WindowsFeature -Name RSAT-AD-PowerShell
   ```
   👉 Explication : installe le module ActiveDirectory ; adapter le nom de la fonctionnalité (`Get-WindowsFeature RSAT*`).
4. Dans les scripts partagés, protéger les appels propres à 2022 par un test de version ou `Get-Command`.
   👉 Explication : évite qu'un script échoue sur 2016 ou 2019 sans message clair.

## 2. Production — Contrôles

- Maintenir une table « cmdlet → version minimale » pour les scripts d'exploitation et la valider sur chaque version cible.

## 3. Production — Sécurité

- Utiliser `Set-ExecutionPolicy` de façon limitée et signer les scripts de production ; ne pas désactiver la journalisation PowerShell.

## Validation et retour arrière

- **Validation** : le script s'exécute sur 2016, 2019 et 2022 sans erreur de commande inconnue. **Retour arrière** : retirer la fonctionnalité ajoutée avec `Uninstall-WindowsFeature`.

## Si le problème n'est pas résolu

- [Fiche d'entrée Windows Server 2016 / 2019 / 2022](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_Windows-Server-2016-2019-2022.md)
- [Microsoft Learn — Get-Command](https://learn.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/get-command)
- [Microsoft Learn — Install-WindowsFeature](https://learn.microsoft.com/fr-fr/powershell/module/servermanager/install-windowsfeature)

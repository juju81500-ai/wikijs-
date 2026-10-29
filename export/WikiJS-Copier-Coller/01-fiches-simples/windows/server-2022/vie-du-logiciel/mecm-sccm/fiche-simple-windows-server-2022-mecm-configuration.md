# Fiche_Simple_-_Windows_Server_2022_MECM_Configuration

- **Environnement** : Windows Server 2022, site primaire MECM/SCCM installé; console et module PowerShell ConfigurationManager
- **OS / Version** : Windows Server 2022; Configuration Manager : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC

---

## Problème précis à résoudre

Configurer le site installé : limites, groupes de limites, découverte, point de distribution et collection de test.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir le contexte du site (à remplacer) :
   ```powershell
   $CodeSite = "CODESITE"
   $Console = (Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\SMS\Setup")."UI Installation Directory"
   Import-Module "$Console\bin\ConfigurationManager.psd1"
   Set-Location "${CodeSite}:"
   ```
   👉 Explication : le module est installé avec la console (à vérifier sur la version publiée); le lecteur de site porte le code de site.

2. Créer une limite et un groupe de limites. GUI : `Administration > Configuration de la hiérarchie > Limites`, puis `Groupes de limites`.
   ```powershell
   New-CMBoundary -Name "LIMITE-LAB" -Type IPRange -Value "192.0.2.1-192.0.2.254"
   New-CMBoundaryGroup -Name "GROUPE-LIMITES-LAB"
   Add-CMBoundaryToGroup -BoundaryName "LIMITE-LAB" -BoundaryGroupName "GROUPE-LIMITES-LAB"
   ```
   👉 Explication : remplacer la plage d'exemple par celle des clients. Un client hors limite ne trouve pas de contenu.

3. Contrôler les méthodes de découverte. GUI : `Administration > Configuration de la hiérarchie > Méthodes de découverte`.
   ```powershell
   Get-CMDiscoveryMethod | Select-Object ItemName, Flag
   ```
   👉 Explication : activer la découverte de systèmes Active Directory sur l'OU `OU=ORDINATEURS,DC=DOMAINE,DC=LOCAL` (à remplacer) depuis la console; les paramètres sont à vérifier selon la version.

4. Contrôler le point de distribution. GUI : `Administration > Configuration du site > Serveurs et rôles système de site`.
   ```powershell
   Get-CMDistributionPoint | Select-Object NetworkOSPath
   ```
   👉 Explication : si rien n'est renvoyé, ajouter le rôle par l'assistant « Ajouter des rôles de système de site ».

5. Créer une collection de test. GUI : `Biens et conformité > Collections d'appareils > Créer`.
   ```powershell
   New-CMDeviceCollection -Name "COLLECTION-TEST" -LimitingCollectionName "All Systems"
   ```
   👉 Explication : on limite les premiers déploiements à quelques postes. `All Systems` est le nom anglais par défaut, à adapter selon la langue.

## 2. Production — Contrôles

Valider limites et groupes de limites avec l'équipe réseau. Ne déployer le client que sur une collection pilote.

## 3. Production — Sécurité

- Préférer l'authentification d'ordinateur; sinon un compte d'accès réseau dédié, sans droit interactif.
- Pas de premier déploiement sur `All Systems`.

## Validation et retour arrière

- **Validation** : `Get-CMBoundaryGroup -Name "GROUPE-LIMITES-LAB"` renvoie le groupe; la collection existe; le point de distribution est sain.
- **Retour arrière** : `Remove-CMBoundaryGroup -Name "GROUPE-LIMITES-LAB"`, `Remove-CMBoundary -Name "LIMITE-LAB"`, `Remove-CMDeviceCollection -Name "COLLECTION-TEST"` (confirmation demandée).

## Si le problème n'est pas résolu

- [Fiche d'entrée MECM/SCCM](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-microsoft-mecm-sccm)
- [Microsoft Learn — Groupes de limites](https://learn.microsoft.com/en-us/intune/configmgr/core/servers/deploy/configure/boundary-groups)
- [Microsoft Learn — Module PowerShell ConfigurationManager](https://learn.microsoft.com/en-us/powershell/module/configurationmanager/)
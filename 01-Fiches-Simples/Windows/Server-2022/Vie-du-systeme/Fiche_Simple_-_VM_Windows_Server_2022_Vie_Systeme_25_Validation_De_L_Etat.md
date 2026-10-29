# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-25`

---

## Problème précis à résoudre

Figer l'état initial du serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Gestionnaire de serveur > Serveur local** et relever l'état.
   ```powershell
   Get-ComputerInfo | Select-Object CsName, WindowsProductName, OsVersion, OsBuildNumber, CsDomain, TimeZone
   Get-Service | Where-Object Status -eq Running | Measure-Object
   ```
   👉 Explication : résume le système et le nombre de services démarrés.

2. Exporter l'inventaire des correctifs, services et rôles :
   ```powershell
   New-Item -ItemType Directory C:\Baseline -Force | Out-Null
   Get-HotFix | Export-Csv C:\Baseline\correctifs.csv -NoTypeInformation
   Get-Service | Export-Csv C:\Baseline\services.csv -NoTypeInformation
   Get-WindowsFeature | Where-Object Installed | Export-Csv C:\Baseline\roles.csv -NoTypeInformation
   ```
   👉 Explication : ces fichiers servent de référence pour détecter les dérives.

3. Prendre un point de contrôle de la VM (Hyper-V : **clic droit sur la VM > Point de contrôle**) :
   ```powershell
   Checkpoint-VM -Name NOM_VM -SnapshotName 'Baseline'
   ```
   👉 Explication : permet de revenir à l'état initial validé (à exécuter sur l'hôte).

## 2. Production — Contrôles

Conserver les exports avec la date dans le dossier du projet.

## 3. Production — Sécurité

Protéger les exports : ils décrivent la configuration du serveur.

## Validation et retour arrière

- **Validation** : Fichiers de baseline présents et point de contrôle créé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)

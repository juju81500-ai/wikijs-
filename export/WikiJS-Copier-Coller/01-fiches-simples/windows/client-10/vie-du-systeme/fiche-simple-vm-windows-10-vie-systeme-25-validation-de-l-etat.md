# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Figer l'état de référence du poste avant les durcissements.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter l'état général : **Paramètres > Système > À propos de**, ou commande.
   ```powershell
   Get-ComputerInfo | Select-Object CsName,WindowsProductName,WindowsVersion,OsBuildNumber,BiosVersion | Export-Csv "$env:USERPROFILE\baseline_systeme.csv" -NoTypeInformation
   ```
   👉 Explication : sauvegarde l'identité et la version du poste.

2. Exporter les logiciels, correctifs et services.
   ```powershell
   Get-HotFix | Export-Csv "$env:USERPROFILE\baseline_correctifs.csv" -NoTypeInformation
   Get-Service | Where-Object Status -eq Running | Export-Csv "$env:USERPROFILE\baseline_services.csv" -NoTypeInformation
   Get-NetTCPConnection -State Listen | Select-Object LocalAddress,LocalPort,OwningProcess | Export-Csv "$env:USERPROFILE\baseline_ports.csv" -NoTypeInformation
   ```
   👉 Explication : capture les correctifs, services et ports en écoute.

3. Exporter les stratégies appliquées.
   ```powershell
   gpresult /h "$env:USERPROFILE\baseline_gpo.html" /f
   ```
   👉 Explication : rapport HTML des GPO appliquées.

4. Ranger les fichiers dans le dossier du poste du CMDB, puis prendre un point de restauration ou snapshot : **Panneau de configuration > Système > Protection du système > Créer**.
   ```powershell
   Enable-ComputerRestore -Drive 'C:\'
   Checkpoint-Computer -Description 'Baseline' -RestorePointType MODIFY_SETTINGS
   ```
   👉 Explication : crée un point de restauration nommé « Baseline ».

## 2. Production — Contrôles

Baseline signée avant la mise en production et comparée régulièrement.

## 3. Production — Sécurité

Les exports peuvent contenir des informations sensibles : les stocker dans un espace à accès restreint.

## Validation et retour arrière

- **Validation** : Fichiers de baseline présents et point de restauration créé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-31`

---

## Problème précis à résoudre

Désactiver ce qui n'est pas nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les services démarrés (**services.msc**) et les rôles installés (**Gestionnaire de serveur > Gérer > Supprimer des rôles et fonctionnalités**) :
   ```powershell
   Get-Service | Where-Object {$_.Status -eq 'Running'} | Select-Object Name, DisplayName, StartType
   Get-WindowsFeature | Where-Object Installed
   ```
   👉 Explication : repère ce qui n'a pas d'utilité.

2. Désactiver un service inutile (remplacer `NOM_SERVICE`) :
   ```powershell
   Stop-Service NOM_SERVICE
   Set-Service NOM_SERVICE -StartupType Disabled
   ```
   👉 Explication : arrête et empêche le démarrage; tester avant d'appliquer en production.

3. Désactiver SMBv1 et vérifier les ports en écoute :
   ```powershell
   Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
   Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess | Sort-Object LocalPort
   ```
   👉 Explication : SMBv1 est obsolète et vulnérable; la liste des ports en écoute doit correspondre aux besoins.

## 2. Production — Contrôles

Documenter les services conservés et leur justification.

## 3. Production — Sécurité

Appliquer un référentiel (CIS Benchmark, base de référence Microsoft Security Compliance Toolkit).

## Validation et retour arrière

- **Validation** : Plus aucun service ni port inutile.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)

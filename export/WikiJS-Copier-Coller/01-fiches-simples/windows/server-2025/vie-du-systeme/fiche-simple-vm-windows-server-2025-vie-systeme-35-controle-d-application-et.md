# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_35_Controle_D_Application_Et

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Activer Microsoft Defender et le contrôle d'applications.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Sécurité Windows > Protection contre les virus et menaces** (ou **Gestionnaire de serveur > Rôles > Windows Defender**).
   ```powershell
   Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, AntivirusSignatureLastUpdated
   ```
   👉 Explication : doit montrer la protection en temps réel active et des signatures récentes.

2. Mettre à jour les signatures et lancer une analyse rapide :
   ```powershell
   Update-MpSignature
   Start-MpScan -ScanType QuickScan
   ```
   👉 Explication : actualise la protection et vérifie le système.

3. Appliquer des exclusions strictes si nécessaire (remplacer `CHEMIN`) :
   ```powershell
   Add-MpPreference -ExclusionPath 'CHEMIN'
   ```
   👉 Explication : à limiter aux chemins recommandés par l'éditeur d'une application.

## 2. Production — Contrôles

Compléter avec WDAC ou AppLocker pour n'autoriser que les applications approuvées.

## 3. Production — Sécurité

Ne pas désactiver Defender sans solution de remplacement validée par le RSSI.

## Validation et retour arrière

- **Validation** : `RealTimeProtectionEnabled` vaut `True` et la dernière analyse est propre.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
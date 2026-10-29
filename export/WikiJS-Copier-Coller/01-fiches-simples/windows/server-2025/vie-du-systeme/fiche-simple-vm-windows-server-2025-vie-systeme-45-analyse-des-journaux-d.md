# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_45_Analyse_Des_Journaux_D

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 45 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Repérer les erreurs au démarrage et en fonctionnement.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Observateur d'événements > Affichages personnalisés > Événements d'administration**.
   ```powershell
   Get-WinEvent -FilterHashtable @{LogName='System';Level=1,2;StartTime=(Get-Date).AddDays(-1)} -MaxEvents 50 | Select-Object TimeCreated, ProviderName, Id, Message
   ```
   👉 Explication : liste les erreurs critiques des dernières 24 heures.

2. Examiner le journal Application :
   ```powershell
   Get-WinEvent -FilterHashtable @{LogName='Application';Level=2} -MaxEvents 30 | Format-Table TimeCreated, ProviderName, Id -AutoSize
   ```
   👉 Explication : repère les erreurs applicatives.

3. Lancer la vérification des fichiers système en cas de doute :
   ```powershell
   sfc /scannow
   Dism /Online /Cleanup-Image /ScanHealth
   ```
   👉 Explication : contrôle et signale la corruption du système.

## 2. Production — Contrôles

Traiter ou justifier chaque erreur récurrente.

## 3. Production — Sécurité

Ne pas laisser de messages d'erreur contenant des informations sensibles dans des tickets publics.

## Validation et retour arrière

- **Validation** : Plus d'erreur critique non expliquée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
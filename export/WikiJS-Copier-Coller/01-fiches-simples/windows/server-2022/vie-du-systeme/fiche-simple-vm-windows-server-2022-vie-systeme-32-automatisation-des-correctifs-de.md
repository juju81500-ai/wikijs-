# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer automatiquement les correctifs selon une fenêtre définie.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Paramètres > Windows Update > Options avancées** ou la stratégie **Configurer les mises à jour automatiques** (**gpedit.msc > Composants Windows > Windows Update > Gérer l'expérience de l'utilisateur final**).
   ```powershell
   $k='HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU'
   New-Item $k -Force | Out-Null
   Set-ItemProperty $k NoAutoUpdate 0
   Set-ItemProperty $k AUOptions 4
   Set-ItemProperty $k ScheduledInstallDay 0
   Set-ItemProperty $k ScheduledInstallTime 3
   ```
   👉 Explication : télécharge et installe chaque jour à 3 h (`ScheduledInstallDay 0` = tous les jours).

2. Éviter les redémarrages inopinés sur les serveurs :
   ```powershell
   Set-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU' NoAutoRebootWithLoggedOnUsers 1
   ```
   👉 Explication : ne redémarre pas si une session est ouverte; planifier les redémarrages.

3. Vérifier le dernier correctif :
   ```powershell
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 3
   ```
   👉 Explication : confirme l'installation récente.

## 2. Production — Contrôles

Tester les correctifs sur un groupe pilote avant la production (anneaux WSUS).

## 3. Production — Sécurité

Ne jamais différer les correctifs critiques au-delà de la politique (ex. 14 jours).

## Validation et retour arrière

- **Validation** : Les correctifs récents sont installés dans la fenêtre prévue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
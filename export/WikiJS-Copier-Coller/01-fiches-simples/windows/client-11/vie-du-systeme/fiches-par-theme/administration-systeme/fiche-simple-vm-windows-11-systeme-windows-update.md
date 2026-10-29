# 📄 Fiche_Simple_-_VM_Windows_11_Systeme_Windows_Update

- **Environnement** : VM / Poste de travail (Windows 11)
- **OS / Version** : Windows 11 - Famille Windows Client
- **Catégorie** : Système & Services / Mises à jour

## 🎯 Problème précis à résoudre
Contrôler l'état de Windows Update sur un poste Windows 11, lancer une recherche de mises à jour, puis appliquer une politique de report et de redémarrage qui évite les interruptions de travail.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Contrôler le service Windows Update et les correctifs déjà installés :
   ```powershell
   Get-Service -Name wuauserv | Select-Object Name, Status, StartType
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10 HotFixID, Description, InstalledOn
   ```
   👉 Explication : Vérifie que le service est actif et liste les dix derniers correctifs installés.
2. Lancer une recherche de mises à jour et consulter son journal :
   ```powershell
   UsoClient.exe StartScan
   Get-WinEvent -LogName "Microsoft-Windows-WindowsUpdateClient/Operational" -MaxEvents 20 | Select-Object TimeCreated, Id, Message
   ```
   👉 Explication : Déclenche l'analyse via l'orchestrateur Windows Update, puis affiche les derniers événements du client pour diagnostiquer un échec éventuel.

**Équivalent interface graphique :**

- **Paramètres > Windows Update > Rechercher des mises à jour**, puis **Historique des mises à jour**.
  👉 Explication : équivalent de `UsoClient.exe StartScan` et de `Get-HotFix`.
- **Win + R** > `services.msc` > **Windows Update** (état et type de démarrage).
  👉 Explication : équivalent de `Get-Service wuauserv`.

## ⚡ 2. Production — Façon Simplifiée
1. Différer les mises à jour de qualité de 7 jours et les mises à jour de fonctionnalités de 30 jours :
   ```powershell
   $wu = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate"
   New-Item -Path $wu -Force | Out-Null
   Set-ItemProperty -Path $wu -Name "DeferQualityUpdates" -Value 1 -Type DWord
   Set-ItemProperty -Path $wu -Name "DeferQualityUpdatesPeriodInDays" -Value 7 -Type DWord
   Set-ItemProperty -Path $wu -Name "DeferFeatureUpdatesPeriodInDays" -Value 30 -Type DWord
   ```
   👉 Explication : Écrit les clés équivalentes à la stratégie « Gestion des mises à jour pour Windows ». En production, appliquer par GPO pour éviter les écarts entre postes.
2. Forcer une nouvelle analyse après application :
   ```powershell
   gpupdate /force
   UsoClient.exe StartScan
   ```
   👉 Explication : Recharge les stratégies puis relance la recherche de mises à jour pour prendre en compte le report.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Installer automatiquement les mises à jour à heure fixe, sans redémarrage pendant une session ouverte :
   ```powershell
   $au = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"
   New-Item -Path $au -Force | Out-Null
   Set-ItemProperty -Path $au -Name "AUOptions" -Value 4 -Type DWord
   Set-ItemProperty -Path $au -Name "ScheduledInstallTime" -Value 3 -Type DWord
   Set-ItemProperty -Path $au -Name "NoAutoRebootWithLoggedOnUsers" -Value 1 -Type DWord
   ```
   👉 Explication : AUOptions 4 télécharge et planifie l'installation ; ScheduledInstallTime 3 la place à 3 h du matin. Le redémarrage ne se produit pas tant qu'un utilisateur est connecté.
2. Contrôler que la politique est bien enregistrée sur le poste :
   ```powershell
   reg query "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"
   ```
   👉 Explication : Affiche les valeurs réellement présentes dans le registre, à comparer avec la GPO attendue.
3. Relever les événements d'installation pour contrôle de conformité :
   ```powershell
   Get-WinEvent -LogName "Microsoft-Windows-WindowsUpdateClient/Operational" -MaxEvents 50 | Where-Object { $_.Id -in 19, 20, 43 } | Select-Object TimeCreated, Id, Message
   ```
   👉 Explication : Les identifiants 19 et 20 signalent une installation réussie ou en échec, 43 le début d'une installation. Un échec répété doit être traité avant la remise en production.
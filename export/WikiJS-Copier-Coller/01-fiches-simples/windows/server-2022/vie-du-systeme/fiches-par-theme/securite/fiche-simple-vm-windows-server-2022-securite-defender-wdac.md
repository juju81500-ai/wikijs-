# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Securite_Defender_WDAC

- **Environnement** : VM (Windows Server 2022)
- **OS / Version** : Windows Server 2022 - Famille Windows Server
- **Catégorie** : Sécurité / Antivirus et contrôle d'applications

## 🎯 Problème précis à résoudre
Vérifier et renforcer Microsoft Defender Antivirus sur un serveur Windows Server 2022, puis mettre en place un contrôle des applications exécutables (WDAC ou AppLocker) en commençant par un mode audit qui ne bloque rien.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Contrôler l'état de Defender et l'âge des signatures :
   ```powershell
   Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, AntispywareSignatureLastUpdated
   ```
   👉 Explication : Confirme que le moteur, la protection temps réel et les signatures sont actifs et récents.
2. Mettre à jour les signatures puis lancer une analyse rapide :
   ```powershell
   Update-MpSignature
   Start-MpScan -ScanType QuickScan
   ```
   👉 Explication : Télécharge les dernières définitions de virus et analyse les zones les plus exposées du serveur.

**Équivalent interface graphique :**

- Rôle **Sécurité Windows** : **Protection contre les virus et menaces > Mises à jour de la protection**, puis **Options d'analyse > Analyse rapide**.
  👉 Explication : équivalent de `Update-MpSignature` et `Start-MpScan`.

## ⚡ 2. Production — Façon Simplifiée
1. Activer la protection contre les applications potentiellement indésirables, la télémétrie cloud et le niveau de blocage élevé :
   ```powershell
   Set-MpPreference -PUAProtection Enabled -MAPSReporting Advanced -CloudBlockLevel High
   ```
   👉 Explication : Bloque les logiciels indésirables connus et active la réputation dans le cloud Microsoft. Vérifier que la politique de confidentialité de l'organisation l'autorise.
2. Démarrer le service d'identité des applications, requis par AppLocker :
   ```powershell
   Set-Service -Name AppIDSvc -StartupType Automatic
   Start-Service -Name AppIDSvc
   ```
   👉 Explication : Sans le service AppIDSvc, les règles AppLocker ne sont jamais évaluées.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Activer la protection des dossiers contrôlés contre les rançongiciels :
   ```powershell
   Set-MpPreference -EnableControlledFolderAccess Enabled
   ```
   👉 Explication : Empêche les processus non autorisés de modifier les dossiers protégés. Ajouter les applications légitimes à la liste d'autorisation avant de passer en blocage.
2. Construire une politique WDAC en mode audit (journalisation seule) :
   ```powershell
   New-Item -ItemType Directory -Path "C:\WDAC" -Force | Out-Null
   New-CIPolicy -FilePath "C:\WDAC\PolicyAudit.xml" -ScanPath "C:\Program Files" -Level Publisher -Fallback Hash -UserPEs
   Set-RuleOption -FilePath "C:\WDAC\PolicyAudit.xml" -Option 3
   ```
   👉 Explication : Crée une politique basée sur les éditeurs signés, avec repli sur le hachage. L'option 3 active le mode audit : les exécutions non conformes sont journalisées sans être bloquées.
3. Vérifier l'état de Code Integrity et les événements d'audit avant tout passage en blocage :
   ```powershell
   Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard | Select-Object SecurityServicesConfigured, SecurityServicesRunning, UsermodeCodeIntegrityPolicyEnforcementStatus
   Get-WinEvent -LogName "Microsoft-Windows-CodeIntegrity/Operational" -MaxEvents 20 | Select-Object TimeCreated, Id, Message
   ```
   👉 Explication : Les événements 3076 signalent les exécutions qui seraient bloquées en mode applicatif. Les analyser et compléter la politique avant de retirer le mode audit.
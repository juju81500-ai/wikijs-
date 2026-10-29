# 📄 Fiche_Simple_-_VM_Windows_11_Securite_Defender_WDAC

- **Environnement** : VM / Poste de travail (Windows 11)
- **OS / Version** : Windows 11 - Famille Windows Client
- **Catégorie** : Sécurité / Antivirus et contrôle d'applications
- **Tags** : `[windows-11]`, `[defender]`, `[wdac]`, `[applocker]`, `[code-integrity]`, `[powershell]`

## 🎯 Problème précis à résoudre
Vérifier et durcir Microsoft Defender Antivirus sur un poste Windows 11, puis mettre en place un contrôle des applications (WDAC) en commençant par un mode audit qui journalise sans bloquer.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Contrôler l'état de Defender, la protection contre la falsification et l'âge des signatures :
   ```powershell
   Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled, IsTamperProtected, AntispywareSignatureLastUpdated
   ```
   👉 Explication : Confirme que la protection temps réel et la protection contre la falsification sont actives, et que les signatures sont récentes.
2. Mettre à jour les signatures puis lancer une analyse rapide :
   ```powershell
   Update-MpSignature
   Start-MpScan -ScanType QuickScan
   ```
   👉 Explication : Télécharge les dernières définitions et analyse les emplacements les plus exposés (téléchargements, dossiers de démarrage).

**Équivalent interface graphique :**

- **Sécurité Windows > Protection contre les virus et menaces > Mises à jour de la protection > Rechercher des mises à jour**, puis **Options d'analyse > Analyse rapide**.
  👉 Explication : équivalent de `Update-MpSignature` et `Start-MpScan`; **Paramètres de protection contre les virus > Protection contre les falsifications** doit être activée.

## ⚡ 2. Production — Façon Simplifiée
1. Activer la détection des applications indésirables, la télémétrie cloud et le blocage élevé :
   ```powershell
   Set-MpPreference -PUAProtection Enabled -MAPSReporting Advanced -CloudBlockLevel High
   ```
   👉 Explication : Bloque les logiciels indésirables et active la réputation cloud. Vérifier la conformité de la télémétrie avec la politique de confidentialité de l'entreprise.
2. Consulter les menaces détectées récemment :
   ```powershell
   Get-MpThreatDetection | Select-Object InitialDetectionTime, ThreatID, ProcessName, Resources
   ```
   👉 Explication : Liste les détections récentes pour repérer un poste qui revient régulièrement en alerte.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Activer la protection des dossiers contrôlés contre les rançongiciels :
   ```powershell
   Set-MpPreference -EnableControlledFolderAccess Enabled
   ```
   👉 Explication : Empêche les processus non autorisés de modifier les dossiers protégés (Documents, Bureau, Images). Ajouter les applications métier à la liste d'autorisation avant ce passage en blocage.
2. Construire une politique WDAC en mode audit (journalisation seule) :
   ```powershell
   New-Item -ItemType Directory -Path "C:\WDAC" -Force | Out-Null
   New-CIPolicy -FilePath "C:\WDAC\PolicyAudit.xml" -ScanPath "C:\Program Files" -Level Publisher -Fallback Hash -UserPEs
   Set-RuleOption -FilePath "C:\WDAC\PolicyAudit.xml" -Option 3
   ```
   👉 Explication : Crée une politique fondée sur les éditeurs signés, avec repli sur le hachage. L'option 3 active le mode audit : les exécutions non conformes sont journalisées sans blocage. Le module ConfigCI doit être disponible sur le poste.
3. Contrôler l'état de Code Integrity et les événements d'audit avant tout blocage :
   ```powershell
   Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard | Select-Object SecurityServicesConfigured, SecurityServicesRunning, UsermodeCodeIntegrityPolicyEnforcementStatus
   Get-WinEvent -LogName "Microsoft-Windows-CodeIntegrity/Operational" -MaxEvents 20 | Select-Object TimeCreated, Id, Message
   ```
   👉 Explication : Les événements 3076 signalent les exécutions qui seraient bloquées en mode applicatif. Compléter la politique à partir de ces événements avant de retirer le mode audit, puis redémarrer le poste pour l'appliquer.

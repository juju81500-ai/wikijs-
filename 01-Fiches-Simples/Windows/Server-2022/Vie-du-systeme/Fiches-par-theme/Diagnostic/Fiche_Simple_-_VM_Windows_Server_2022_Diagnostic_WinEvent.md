# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Diagnostic_WinEvent

- **Environnement** : VM (Windows Server 2022)
- **OS / Version** : Windows Server 2022 - Famille Windows Server
- **Catégorie** : Système & Services / Diagnostic et journaux
- **Tags** : `[windows-server-2022]`, `[get-winevent]`, `[event-log]`, `[diagnostic]`, `[powershell]`

## 🎯 Problème précis à résoudre
Identifier rapidement les erreurs et avertissements récents des journaux System et Application d'un serveur Windows Server 2022 avec `Get-WinEvent`, puis exporter les résultats pour analyse ou preuve.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Repérer les journaux les plus volumineux et leur taille maximale :
   ```powershell
   Get-WinEvent -ListLog System, Application, Security | Select-Object LogName, RecordCount, MaximumSizeInBytes, IsEnabled
   ```
   👉 Explication : Indique si un journal est proche de sa limite et s'il est actif.
2. Lister les erreurs et avertissements des dernières 24 heures :
   ```powershell
   Get-WinEvent -FilterHashtable @{ LogName = 'System', 'Application'; Level = 1, 2, 3; StartTime = (Get-Date).AddHours(-24) } -MaxEvents 50 -ErrorAction SilentlyContinue | Select-Object TimeCreated, LogName, Id, LevelDisplayName, ProviderName, Message
   ```
   👉 Explication : Niveau 1 = critique, 2 = erreur, 3 = avertissement. `-ErrorAction SilentlyContinue` évite l'erreur « Aucun événement » lorsque la période est calme.

**Équivalent interface graphique :**

- **Win + R** > `eventvwr.msc` > **Journaux Windows > Système / Application** > **Filtrer le journal actuel...** (niveaux Critique, Erreur, Avertissement, période « Dernières 24 heures »).
  👉 Explication : équivalent de `Get-WinEvent -FilterHashtable`; clic droit > **Propriétés** sur un journal pour sa taille maximale.

## ⚡ 2. Production — Façon Simplifiée
1. Rechercher un identifiant d'événement précis (ici les services arrêtés ou installés) :
   ```powershell
   Get-WinEvent -FilterHashtable @{ LogName = 'System'; Id = 7034, 7036, 7045 } -MaxEvents 30 -ErrorAction SilentlyContinue | Select-Object TimeCreated, Id, ProviderName, Message
   ```
   👉 Explication : 7034 = service arrêté de façon inattendue, 7036 = changement d'état d'un service, 7045 = nouveau service installé (à surveiller pour détecter une persistance).
2. Exporter les erreurs de la semaine au format CSV pour l'équipe d'exploitation :
   ```powershell
   New-Item -ItemType Directory -Path "C:\Diagnostic" -Force | Out-Null
   Get-WinEvent -FilterHashtable @{ LogName = 'System'; Level = 1, 2; StartTime = (Get-Date).AddDays(-7) } -ErrorAction SilentlyContinue | Select-Object TimeCreated, Id, ProviderName, Message | Export-Csv -Path "C:\Diagnostic\System_erreurs_7j.csv" -NoTypeInformation -Encoding UTF8
   ```
   👉 Explication : Produit un fichier CSV exploitable dans un tableur, avec la date, l'identifiant, la source et le message.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Exporter le journal System complet au format EVTX, avec son empreinte :
   ```powershell
   wevtutil epl System "C:\Diagnostic\System.evtx"
   Get-FileHash -Algorithm SHA256 -Path "C:\Diagnostic\System.evtx"
   ```
   👉 Explication : Conserve une copie intégrable à un dossier d'incident. L'empreinte SHA256 permet de prouver que le fichier n'a pas été modifié.
2. Relire l'export hors du serveur d'origine, sans toucher au journal en ligne :
   ```powershell
   Get-WinEvent -Path "C:\Diagnostic\System.evtx" -MaxEvents 100 | Select-Object TimeCreated, Id, LevelDisplayName, Message
   ```
   👉 Explication : Analyse l'export EVTX, ce qui permet de diagnostiquer sans modifier ni vider le journal source.

# Fiche_Simple_-_VM_Windows_11_PowerShell7_Commandes_Objets.md

- **Environnement** : VM ou poste Windows 11 de test; compte standard puis élévation uniquement si requise
- **OS / Version** : Windows 11 x64; PowerShell 7.6.9 Stable (LTS)
- **Catégorie** : administration / PowerShell

---

## Problème précis à résoudre

Utiliser les commandes et le pipeline pour examiner le poste en lecture seule.

## 1. Hors-Production (Lab / Test / POC)

1. Découvrir des commandes et lire l'aide :
   ```powershell
   Get-Command -Verb Get -Noun Service
   Get-Help Get-Service -Examples
   ```
   👉 Explication : on explore avant d'agir.

2. Filtrer des objets avant de les afficher :
   ```powershell
   Get-Service | Where-Object Status -eq 'Running' | Sort-Object DisplayName | Select-Object Status, Name, DisplayName
   Get-NetIPConfiguration
   ```
   👉 Explication : la sortie est faite d'objets; ne pas utiliser `Format-Table` avant un export ou une autre étape de pipeline.

3. Collecter l'inventaire minimal du poste :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-NetAdapter | Select-Object Name, Status, LinkSpeed
   Get-Service | Where-Object Status -eq 'Stopped' | Select-Object Name, DisplayName
   ```
   👉 Explication : commandes en lecture seule limitées aux propriétés utiles.

4. Lire les erreurs récentes du journal Système :
   ```powershell
   Get-WinEvent -FilterHashtable @{ LogName = 'System'; Level = 2; StartTime = (Get-Date).AddHours(-24) } -MaxEvents 50 |
       Select-Object TimeCreated, Id, ProviderName, LevelDisplayName, Message
   ```
   👉 Explication : les erreurs des dernières 24 h; certaines informations exigent des droits supplémentaires.

## 2. Production — Contrôles

Réduire le périmètre des collectes et protéger les exports.

## 3. Production — Sécurité

- Les journaux peuvent contenir identifiants ou noms internes : ne pas les copier dans un ticket public.

## Validation et retour arrière

- **Validation** : Les commandes renvoient les informations attendues sans modifier le poste.
- **Retour arrière** : Aucune modification; fermer la session.

## Si le problème n'est pas résolu

- [Microsoft Learn — Installer PowerShell 7 sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [PowerShell — publication v7.6.9](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9)
- [Guide complet PowerShell 7.6.9 Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11#4-prendre-en-main-les-commandes-et-objets)
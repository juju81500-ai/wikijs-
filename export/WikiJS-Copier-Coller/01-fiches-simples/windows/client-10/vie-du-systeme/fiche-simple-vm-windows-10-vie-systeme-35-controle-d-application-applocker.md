# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_35_Controle_D_Application_Applocker

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

N'autoriser que les applications approuvées.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir AppLocker : **Stratégie de sécurité locale (secpol.msc) > Stratégies de contrôle de l'application > AppLocker** (édition Entreprise, ou WDAC pour les autres éditions), puis **Créer les règles par défaut**.
   ```powershell
   Get-Service AppIDSvc | Select-Object Name,Status
   Set-Service AppIDSvc -StartupType Automatic
   Start-Service AppIDSvc
   ```
   👉 Explication : le service Identité de l'application est requis pour appliquer les règles.

2. Commencer en mode audit : **Propriétés d'AppLocker > Avancé > Règles : Auditer uniquement**.
   ```powershell
   Get-WinEvent -LogName 'Microsoft-Windows-AppLocker/EXE and DLL' -MaxEvents 20 | Select-Object TimeCreated,Id,Message
   ```
   👉 Explication : relève ce qui serait bloqué sans perturber les utilisateurs.

3. Exporter la stratégie testée et l'appliquer en mode forcé.
   ```powershell
   Get-AppLockerPolicy -Effective -Xml | Out-File "$env:USERPROFILE\applocker.xml"
   Set-AppLockerPolicy -XmlPolicy "$env:USERPROFILE\applocker.xml"
   ```
   👉 Explication : sauvegarde puis applique la stratégie.

4. Variante WDAC / Smart App Control : **Sécurité Windows > Contrôle des applications et du navigateur**.
   ```powershell
   Get-CimInstance -ClassName Win32_DeviceGuard -Namespace root\Microsoft\Windows\DeviceGuard
   ```
   👉 Explication : indique l'état de l'intégrité du code.

## 2. Production — Contrôles

Passer en application forcée seulement après une période d'audit complète sur un poste pilote.

## 3. Production — Sécurité

Consigner les exceptions; un contrôle d'application mal réglé bloque l'activité.

## Validation et retour arrière

- **Validation** : Les applications approuvées démarrent, les autres sont bloquées (événement 8004).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
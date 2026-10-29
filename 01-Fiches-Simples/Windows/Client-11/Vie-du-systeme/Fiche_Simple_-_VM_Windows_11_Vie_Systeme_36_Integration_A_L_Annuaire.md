# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-36`

---

## Problème précis à résoudre

Rattacher le poste à l'annuaire et à l'outil de gestion (GPO, Intune).

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'état d'appartenance : **Paramètres > Comptes > Accès Professionnel ou scolaire**.
   ```powershell
   dsregcmd /status | Select-String 'AzureAdJoined|DomainJoined|MdmUrl|TenantName'
   ```
   👉 Explication : affiche la jonction AD/Entra ID et l'inscription à la gestion des appareils (MDM).

2. Appliquer et contrôler les GPO : **Configuration ordinateur** et **Utilisateur**.
   ```powershell
   gpupdate /force
   gpresult /r
   gpresult /h "$env:USERPROFILE\gpo.html" /f
   ```
   👉 Explication : applique les stratégies et produit un rapport des GPO appliquées ou filtrées.

3. Pour Intune, forcer la synchronisation : **Paramètres > Comptes > Accès Professionnel ou scolaire > Informations > Synchroniser**.
   ```powershell
   Get-ScheduledTask -TaskName 'PushLaunch' -ErrorAction SilentlyContinue
   Get-WinEvent -LogName 'Microsoft-Windows-DeviceManagement-Enterprise-Diagnostics-Provider/Admin' -MaxEvents 10 | Select-Object TimeCreated,Id,Message
   ```
   👉 Explication : relève l'état de la synchronisation MDM.

4. Placer le poste dans la bonne unité d'organisation ou le bon groupe Intune.
   ```powershell
   Get-ADComputer 'NOM_POSTE' -Properties DistinguishedName | Select-Object DistinguishedName
   ```
   👉 Explication : confirme l'emplacement dans l'annuaire (module RSAT Active Directory requis).

## 2. Production — Contrôles

Le poste reçoit GPO et profils par groupe d'appareils; pas de configuration manuelle durable.

## 3. Production — Sécurité

Seuls les administrateurs de l'annuaire peuvent déplacer ou retirer un poste.

## Validation et retour arrière

- **Validation** : `gpresult` montre les GPO attendues et Intune affiche « Conforme ».
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)

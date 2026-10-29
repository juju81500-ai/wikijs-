---
title: "Fiche Simple - VM Windows 10 Vie Systeme 28 Gestion Fine Des Privileges"
description: "Faire respecter le moindre privilège avec le contrôle de compte d'utilisateur."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows10", "vie-du-systeme", "cycle-de-vie", "etape-28"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-28`

---

## Problème précis à résoudre

Faire respecter le moindre privilège avec le contrôle de compte d'utilisateur.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler UAC : **Paramètres > Comptes > Contrôle de compte d'utilisateur** (panneau de configuration `UserAccountControlSettings.exe`).
   ```powershell
   Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System | Select-Object EnableLUA,ConsentPromptBehaviorAdmin,PromptOnSecureDesktop
   ```
   👉 Explication : `EnableLUA = 1` : UAC actif; `ConsentPromptBehaviorAdmin = 2` : confirmation sur le bureau sécurisé.

2. Imposer les valeurs sûres par GPO : **Configuration ordinateur > Paramètres Windows > Paramètres de sécurité > Stratégies locales > Options de sécurité > Contrôle de compte d'utilisateur**.
   ```powershell
   Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System EnableLUA 1 -Type DWord
   Set-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System ConsentPromptBehaviorAdmin 2 -Type DWord
   ```
   👉 Explication : force UAC avec demande de consentement sur le bureau sécurisé (redémarrage requis).

3. Retirer les droits d'administrateur aux utilisateurs courants.
   ```powershell
   Get-LocalGroupMember -Group 'Administrateurs'
   Remove-LocalGroupMember -Group 'Administrateurs' -Member 'DOMAINE\UTILISATEUR'
   ```
   👉 Explication : ne laisse que les administrateurs prévus.

4. Utiliser le droit d'élévation à la demande : **clic droit > Exécuter en tant qu'administrateur**, ou Intune **Endpoint Privilege Management** si licencié.
   👉 Explication : limite l'usage permanent de droits élevés.

## 2. Production — Contrôles

Utilisateurs en compte standard; élévation ponctuelle et tracée.

## 3. Production — Sécurité

Ne jamais désactiver UAC (`EnableLUA 0`) en production.

## Validation et retour arrière

- **Validation** : `whoami /groups` d'un utilisateur ne montre pas Administrateurs.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
---
title: "Fiche Simple - VM Windows Server 2022 Securite Lockout Audit"
description: "Définir une politique de verrouillage de compte qui freine les attaques par force brute sans bloquer les utilisateurs légitimes, puis activer l'audit des verrouillages pour pouvoir les tracer."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-server-2022]", "[lockout]", "[audit]", "[auditpol]", "[active-directory]", "[powershell]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Securite_Lockout_Audit

- **Environnement** : VM (Windows Server 2022, contrôleur de domaine ou serveur membre)
- **OS / Version** : Windows Server 2022 - Famille Windows Server
- **Catégorie** : Sécurité / Authentification et audit
- **Tags** : `[windows-server-2022]`, `[lockout]`, `[audit]`, `[auditpol]`, `[active-directory]`, `[powershell]`

## 🎯 Problème précis à résoudre
Définir une politique de verrouillage de compte qui freine les attaques par force brute sans bloquer les utilisateurs légitimes, puis activer l'audit des verrouillages pour pouvoir les tracer.

> Le déverrouillage manuel d'un compte est traité dans la fiche ADDS dédiée. Cette fiche couvre la politique et l'audit.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lire la politique de verrouillage du domaine :
   ```powershell
   Get-ADDefaultDomainPasswordPolicy | Select-Object LockoutThreshold, LockoutDuration, LockoutObservationWindow
   ```
   👉 Explication : Affiche le nombre d'échecs autorisés, la durée de verrouillage et la fenêtre de comptage. Une valeur à 0 signifie qu'il n'y a aucun verrouillage.
2. Consulter la politique locale d'un serveur membre ou autonome :
   ```powershell
   net accounts
   ```
   👉 Explication : Montre la politique de verrouillage appliquée localement. Sur un contrôleur de domaine, la politique du domaine prévaut.
3. Appliquer une politique de test sur le domaine de laboratoire :
   ```powershell
   Set-ADDefaultDomainPasswordPolicy -Identity "<nom_domaine>" -LockoutThreshold 5 -LockoutDuration 00:30:00 -LockoutObservationWindow 00:30:00
   ```
   👉 Explication : Verrouille le compte après 5 échecs en 30 minutes, pour 30 minutes. Tester d'abord avec un compte de test.

**Équivalent interface graphique :**

- **Gestion de stratégie de groupe** (`gpmc.msc`) > **Default Domain Policy** > **Modifier** > **Configuration ordinateur > Stratégies > Paramètres Windows > Paramètres de sécurité > Stratégies de comptes > Stratégie de verrouillage du compte**.
  👉 Explication : équivalent de `Get-ADDefaultDomainPasswordPolicy`; pour un serveur local, `secpol.msc` > même chemin.

## ⚡ 2. Production — Façon Simplifiée
1. Appliquer la politique locale sur un serveur membre (valeurs en minutes) :
   ```powershell
   net accounts /lockoutthreshold:5 /lockoutduration:30 /lockoutwindow:30
   ```
   👉 Explication : Règle le seuil, la durée et la fenêtre de verrouillage. En domaine, ces valeurs doivent passer par la GPO « Stratégie de verrouillage du compte » du domaine.
2. Activer l'audit de la sous-catégorie « Verrouillage du compte » (identifiant indépendant de la langue) :
   ```powershell
   auditpol /set /subcategory:{0CCE9217-69AE-11D9-BED3-505054503030} /success:enable /failure:enable
   auditpol /get /subcategory:{0CCE9217-69AE-11D9-BED3-505054503030}
   ```
   👉 Explication : Génère les événements 4740 dans le journal Sécurité à chaque verrouillage, et vérifie que l'audit est actif.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Dimensionner le journal Sécurité pour conserver l'historique (1 Go) :
   ```powershell
   wevtutil sl Security /ms:1073741824
   ```
   👉 Explication : Évite que les événements de verrouillage soient écrasés avant d'être collectés par WEF ou un SIEM.
2. Vérifier les derniers verrouillages enregistrés :
   ```powershell
   Get-WinEvent -FilterHashtable @{ LogName = 'Security'; Id = 4740 } -MaxEvents 20 -ErrorAction SilentlyContinue | Select-Object TimeCreated, Message
   ```
   👉 Explication : Liste les 20 derniers verrouillages. Un volume anormal sur un même compte doit être investigué comme une tentative d'intrusion.
3. Exporter la politique de sécurité locale pour preuve de conformité :
   ```powershell
   New-Item -ItemType Directory -Path "C:\Audit" -Force | Out-Null
   secedit /export /cfg "C:\Audit\secpol.inf"
   Select-String -Path "C:\Audit\secpol.inf" -Pattern "LockoutBadCount|ResetLockoutCount|LockoutDuration"
   ```
   👉 Explication : Enregistre la configuration effective des paramètres de verrouillage, à archiver avec la fiche de production.
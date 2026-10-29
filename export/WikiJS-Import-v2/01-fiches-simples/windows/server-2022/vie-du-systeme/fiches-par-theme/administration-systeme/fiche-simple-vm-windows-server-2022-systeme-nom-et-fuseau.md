---
title: "Fiche Simple - VM Windows Server 2022 Systeme Nom Et Fuseau"
description: "Donner à un serveur Windows Server 2022 un nom d'hôte conforme à la convention de nommage (15 caractères maximum pour le nom NetBIOS), régler le fuseau horaire et vérifier que l'horloge suit bien ce fuseau et la source de temps du domaine."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-server-2022]", "[powershell]", "[rename-computer]", "[timezone]", "[w32tm]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Systeme_Nom_Et_Fuseau

- **Environnement** : VM (Windows Server 2022)
- **OS / Version** : Windows Server 2022 - Famille Windows Server
- **Catégorie** : Système & Services / Identité et configuration de base
- **Tags** : `[windows-server-2022]`, `[powershell]`, `[rename-computer]`, `[timezone]`, `[w32tm]`

## 🎯 Problème précis à résoudre
Donner à un serveur Windows Server 2022 un nom d'hôte conforme à la convention de nommage (15 caractères maximum pour le nom NetBIOS), régler le fuseau horaire et vérifier que l'horloge suit bien ce fuseau et la source de temps du domaine.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Contrôler le nom actuel, le fuseau horaire et l'appartenance au domaine :
   ```powershell
   Get-ComputerInfo -Property CsName, CsDomain, TimeZone
   ```
   👉 Explication : Affiche sans modification le nom NetBIOS, le domaine éventuel et le fuseau actif.
2. Rechercher l'identifiant exact du fuseau puis l'appliquer :
   ```powershell
   Get-TimeZone -ListAvailable | Where-Object { $_.Id -like "*Romance*" }
   Set-TimeZone -Id "Romance Standard Time"
   ```
   👉 Explication : Windows applique le fuseau par son identifiant (et non par « Europe/Paris »). Romance Standard Time correspond à Paris, Bruxelles et Madrid, avec changement d'heure.
3. Renommer le serveur et redémarrer pour appliquer le nouveau nom :
   ```powershell
   Rename-Computer -NewName "<nom_du_serveur>" -Restart
   ```
   👉 Explication : Remplace le nom NetBIOS (15 caractères maximum, sans espaces ni caractères spéciaux) puis redémarre la machine.

**Équivalent interface graphique :**

- **Gestionnaire de serveur > Serveur local > Nom de l'ordinateur** (ou `sysdm.cpl` > **Modifier...**), puis redémarrer.
  👉 Explication : équivalent de `Rename-Computer`.
- **Win + R** > `timedate.cpl` > **Modifier le fuseau horaire**.
  👉 Explication : équivalent de `Set-TimeZone`.

## ⚡ 2. Production — Façon Simplifiée
1. Renommer un serveur membre du domaine avec un compte habilité :
   ```powershell
   Rename-Computer -NewName "<nom_du_serveur>" -DomainCredential (Get-Credential "<nom_domaine>\<compte_admin>") -Restart
   ```
   👉 Explication : Demande les identifiants d'un compte autorisé à modifier l'objet ordinateur dans Active Directory, puis redémarre. Mettre à jour ensuite les enregistrements DNS et la supervision liés à l'ancien nom.
2. Vérifier la source de temps et l'écart d'horloge après application du fuseau :
   ```powershell
   w32tm /query /status
   ```
   👉 Explication : Confirme que le serveur est synchronisé et indique la source de temps utilisée, condition nécessaire à la validité des tickets Kerberos.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier qu'aucun objet ordinateur portant le futur nom n'existe déjà dans l'annuaire :
   ```powershell
   Get-ADComputer -Filter "Name -eq '<nom_du_serveur>'" -Properties DNSHostName, Enabled | Select-Object Name, DNSHostName, Enabled
   ```
   👉 Explication : Évite un conflit d'objet ou de nom DNS avant le renommage. Le module ActiveDirectory doit être disponible.
2. Contrôler le droit « Modifier le fuseau horaire » (SeTimeZonePrivilege) exporté dans la stratégie de sécurité locale :
   ```powershell
   New-Item -ItemType Directory -Path "C:\Audit" -Force | Out-Null
   secedit /export /cfg "C:\Audit\secpol.inf"
   Select-String -Path "C:\Audit\secpol.inf" -Pattern "SeTimeZonePrivilege"
   ```
   👉 Explication : Ce droit doit rester limité aux administrateurs. Si d'autres comptes y figurent, corriger la GPO « Attribution des droits utilisateur ».
3. Vérifier que le serveur de domaine (PDC émulateur) est bien la source de temps d'un membre du domaine :
   ```powershell
   w32tm /query /source
   ```
   👉 Explication : Pour un membre du domaine, la source doit pointer vers la hiérarchie temporelle du domaine, et non vers un serveur externe non prévu.
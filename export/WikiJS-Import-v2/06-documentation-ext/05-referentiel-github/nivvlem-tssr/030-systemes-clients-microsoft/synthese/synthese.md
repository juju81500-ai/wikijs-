---
title: "Synthèse – Systèmes Clients Microsoft"
description: "- Méthodes : ISO, USB bootable, WDS, image personnalisée (Sysprep + capture)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Synthèse – Systèmes Clients Microsoft

## 🔹 Notions essentielles

### 📄 Installation de Windows

- Méthodes : ISO, USB bootable, WDS, image personnalisée (Sysprep + capture)
- Systèmes de fichiers : NTFS (recommandé), exFAT (amovibles), ReFS (RAID)
- Partitionnement : `Diskpart`, `Gestion des disques`, `setup.exe /unattend` (installation silencieuse)

### 📂 Interactions avec le système

- Interfaces : graphique (GUI), invite de commandes (`cmd`), PowerShell
- Aide : `Get-Help`, `Get-Command`, `Start-Process`, `Get-Process`, `Get-Service`

### 🔢 Stockage

- Gestion : `diskmgmt.msc`, `Get-Partition`, `New-Partition`, `Format-Volume`
- Types : disques de base / dynamiques, volumes simples / fractionnés / agrégés

### 💼 Utilisateurs et groupes

- Comptes locaux / Microsoft / AD
- Gestion : `lusrmgr.msc`, `net user`, `net localgroup`
- Profils utilisateurs : `C:\Users`, `regedit > HKEY_USERS`

### 🔒 Sécurité NTFS & ACL

- Droits : Lecture, Écriture, Exécution, Contrôle total
- Outils : `icacls`, `Get-Acl`, `Set-Acl`
- Héritage, propriétaire, stratégies d'accès (lecture seule, refus prioritaire)

### 🌐 Réseau & Pare-feu

- Config : `ipconfig`, `netsh`, `Get-NetAdapter`, `New-NetIPAddress`
- Pare-feu : `wf.msc`, `Get-NetFirewallRule`, `New-NetFirewallRule`
- Profils : Public, Privé, Domaine

### 📦 Partage de ressources

- Partages de fichiers : `\NomMachine\Partage`, `net share`
- Sessions distantes : `mstsc`, `Enable-PSRemoting`, `Invoke-Command`
- Imprimantes locales / réseau : `control printers`, `pnputil`, `PrintManagement.msc`

### 📅 Maintenance

- Sauvegardes : `wbadmin`, `historique de fichiers`, `points de restauration`
- Outils : `sfc /scannow`, `DISM /Online /Cleanup-Image /RestoreHealth`
- Journalisation : `eventvwr.msc`, `Get-EventLog`

### ⛏ PowerShell avancé

- Pipeline : `|`, redirections : `>`, `>>`, `2>`
- Filtres : `Where-Object`, `Select-Object`, `Sort-Object`
- Fonctions : `function`, `param`, `return`
- Gestion d’erreurs : `Try / Catch / Finally`

### 🚧 Capture & déploiement

- Outils : `Sysprep`, `DISM`, `WinPE`, `WDS`
- Sysprep : `sysprep /oobe /generalize /shutdown`
- Clonage VMware : Full Clone post-Sysprep

### 🛂 Strats de groupe locales (LGPO)

- `gpedit.msc`, `secpol.msc`, `mmc`
- Ciblage par groupe d’utilisateurs : Non-administrateurs, Utilisateurs spécifiques
- Actions typiques : désactivation du panneau, verrouillage de l’interface, scripts à la connexion

---

## ✅ À retenir pour les révisions

- `diskpart`, `lusrmgr.msc`, `gpedit.msc`, `secpol.msc`, `icacls`, `netsh` : commandes incontournables
- **PowerShell** est préférable à `cmd` pour les scripts et automatisations
- Un compte **admin local activé** est indispensable avant tout Sysprep
- Les GPO locales sont puissantes mais **non centralisées**
- Toujours tester les modifications sur une **VM isolée** avant de les déployer en production

---

## 📌 Bonnes pratiques professionnelles

|Bonnes pratiques|Pourquoi ?|
|---|---|
|Toujours documenter les changements|Facilite le dépannage et la transmission d’infos|
|Travailler sur des snapshots ou VM clones|Permet des tests sans conséquences sur la prod|
|Automatiser les installations et paramètres|Gain de temps et homogénéité|
|Utiliser des images syspreppées à jour|Optimisation du déploiement|
|Sécuriser les comptes et droits NTFS|Réduction des risques d’accès non autorisés|
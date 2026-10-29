---
title: "Fiche Simple - VM Windows Server 2022 Vie Systeme 44 Audit D Exposition Reseau"
description: "Contrôler ce qu'un voisin voit du serveur."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windowsserver2022", "vie-du-systeme", "cycle-de-vie", "etape-44"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-44`

---

## Problème précis à résoudre

Contrôler ce qu'un voisin voit du serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis une machine du réseau, tester les ports (remplacer `IP_SERVEUR`) :
   ```powershell
   Test-NetConnection IP_SERVEUR -Port 3389
   Test-NetConnection IP_SERVEUR -Port 445
   Test-NetConnection IP_SERVEUR -Port 5985
   ```
   👉 Explication : teste RDP, SMB et WinRM; seuls les ports prévus doivent répondre.

2. Si autorisé, utiliser un scanner (nmap) depuis un poste d'audit :
   ```powershell
   nmap -sS -p- IP_SERVEUR
   ```
   👉 Explication : dresse la liste complète des ports ouverts; scan à n'effectuer qu'avec accord écrit.

3. Comparer avec les règles du pare-feu :
   ```powershell
   Get-NetFirewallRule -Enabled True -Direction Inbound | Select-Object DisplayName, Profile, Action
   ```
   👉 Explication : chaque règle doit avoir une justification.

## 2. Production — Contrôles

Refaire l'audit après chaque changement de règle.

## 3. Production — Sécurité

Ne scanner que des systèmes autorisés.

## Validation et retour arrière

- **Validation** : Les ports exposés sont conformes au dossier.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
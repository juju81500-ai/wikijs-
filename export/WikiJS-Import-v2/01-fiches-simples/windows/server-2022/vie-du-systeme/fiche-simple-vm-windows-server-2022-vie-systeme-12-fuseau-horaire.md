---
title: "Fiche Simple - VM Windows Server 2022 Vie Systeme 12 Fuseau Horaire"
description: "Régler le fuseau horaire pour des journaux cohérents."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windowsserver2022", "vie-du-systeme", "cycle-de-vie", "etape-12"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-12`

---

## Problème précis à résoudre

Régler le fuseau horaire pour des journaux cohérents.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Paramètres > Heure et langue > Date et heure > Fuseau horaire** (ou `timedate.cpl`).
   ```powershell
   Get-TimeZone
   Get-TimeZone -ListAvailable | Where-Object Id -like '*Romance*'
   ```
   👉 Explication : affiche le fuseau actuel et l'identifiant de l'Europe de l'Ouest.

2. Appliquer le fuseau de Paris :
   ```powershell
   Set-TimeZone -Id 'Romance Standard Time'
   ```
   👉 Explication : `Romance Standard Time` correspond à Paris, Bruxelles, Madrid; le changement est immédiat.

3. Contrôler l'heure :
   ```powershell
   Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz'
   ```
   👉 Explication : affiche l'heure locale avec le décalage UTC.

## 2. Production — Contrôles

Un fuseau unique pour tous les serveurs facilite la corrélation des journaux.

## 3. Production — Sécurité

Une heure fausse invalide Kerberos (écart maximal de 5 minutes) et les preuves d'audit.

## Validation et retour arrière

- **Validation** : Fuseau attendu et heure correcte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
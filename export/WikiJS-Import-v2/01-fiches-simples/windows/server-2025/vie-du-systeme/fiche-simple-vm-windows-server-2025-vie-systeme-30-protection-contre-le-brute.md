---
title: "Fiche Simple - VM Windows Server 2025 Vie Systeme 30 Protection Contre Le Brute"
description: "Limiter les tentatives de connexion répétées."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windowsserver2025", "vie-du-systeme", "cycle-de-vie", "etape-30"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

---

## Problème précis à résoudre

Limiter les tentatives de connexion répétées.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Stratégie de sécurité locale > Stratégies de comptes > Stratégie de verrouillage du compte**.
   ```powershell
   net accounts /lockoutthreshold:5 /lockoutduration:15 /lockoutwindow:15
   ```
   👉 Explication : verrouille le compte 15 minutes après 5 échecs en 15 minutes.

2. Contrôler la politique :
   ```powershell
   net accounts
   ```
   👉 Explication : affiche seuil, durée et fenêtre.

3. Repérer les échecs de connexion (événement 4625 dans **Observateur d'événements > Journaux Windows > Sécurité**) :
   ```powershell
   Get-WinEvent -FilterHashtable @{LogName='Security';Id=4625} -MaxEvents 20 | Select-Object TimeCreated, @{n='Message';e={$_.Message.Split("`n")[0]}}
   ```
   👉 Explication : liste les 20 derniers échecs; l'audit de connexion doit être activé.

## 2. Production — Contrôles

Alerter sur les rafales d'événements 4625 et 4740 (verrouillage).

## 3. Production — Sécurité

Un seuil trop bas permet un déni de service par verrouillage : choisir 5 à 10.

## Validation et retour arrière

- **Validation** : Après 5 échecs volontaires, le compte de test est verrouillé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
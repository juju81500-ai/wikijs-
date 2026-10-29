---
title: "Fiche Simple - VM Windows 10 Vie Systeme 12 Fuseau Horaire"
description: "Régler le fuseau horaire correct, Europe/Paris, et l'heure d'été automatique."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows10", "vie-du-systeme", "cycle-de-vie", "etape-12"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-12`

---

## Problème précis à résoudre

Régler le fuseau horaire correct, Europe/Paris, et l'heure d'été automatique.

## 1. Hors-Production (Lab / Test / POC)

1. Régler le fuseau : **Paramètres > Heure et langue > Date et heure > Fuseau horaire = (UTC+01:00) Bruxelles, Copenhague, Madrid, Paris**, avec **Ajuster automatiquement l'heure d'été** activé.
   ```powershell
   Set-TimeZone -Id 'Romance Standard Time'
   Get-TimeZone
   ```
   👉 Explication : `Romance Standard Time` est l'identifiant Windows du fuseau de Paris; `Get-TimeZone` confirme.

2. Lister les identifiants disponibles si un autre site est concerné.
   ```powershell
   Get-TimeZone -ListAvailable | Where-Object DisplayName -like '*Paris*'
   ```
   👉 Explication : retrouve l'identifiant exact du fuseau voulu.

3. Désactiver la définition automatique par localisation si la politique l'impose : **Paramètres > Confidentialité et sécurité > Localisation**.
   ```powershell
   Get-Service tzautoupdate | Select-Object Name,Status,StartType
   ```
   👉 Explication : le service `tzautoupdate` pilote le fuseau automatique; le désactiver évite des changements imprévus.

4. Contrôler l'heure.
   ```powershell
   Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz'
   w32tm /query /status
   ```
   👉 Explication : heure locale et état de la synchronisation.

## 2. Production — Contrôles

Fuseau identique sur tout le parc, appliqué par GPO ou Intune, avec l'heure du domaine comme source.

## 3. Production — Sécurité

Une heure fausse invalide Kerberos (écart supérieur à 5 min) et fausse les journaux d'audit.

## Validation et retour arrière

- **Validation** : `Get-TimeZone` retourne `Romance Standard Time`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
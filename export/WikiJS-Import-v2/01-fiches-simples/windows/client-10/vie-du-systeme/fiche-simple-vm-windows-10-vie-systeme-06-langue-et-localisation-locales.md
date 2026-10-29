---
title: "Fiche Simple - VM Windows 10 Vie Systeme 06 Langue Et Localisation Locales"
description: "Régler la langue d'affichage, le format régional et la localisation en français."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows10", "vie-du-systeme", "cycle-de-vie", "etape-06"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-06`

---

## Problème précis à résoudre

Régler la langue d'affichage, le format régional et la localisation en français.

## 1. Hors-Production (Lab / Test / POC)

1. Définir la langue : **Paramètres > Heure et langue > Langue et région > Langue d'affichage Windows**; ajouter le français (France) si besoin via **Ajouter une langue**.
   ```powershell
   Install-Language -Language fr-FR
   Set-WinUILanguageOverride -Language fr-FR
   Set-WinUserLanguageList -LanguageList fr-FR -Force
   ```
   👉 Explication : installe le pack de langue, force l'interface en français et fixe la liste des langues de l'utilisateur.

2. Définir le pays ou la région : **Paramètres > Heure et langue > Langue et région > Pays ou région = France**; régler aussi le format régional.
   ```powershell
   Set-WinHomeLocation -GeoId 84
   Set-Culture -CultureInfo fr-FR
   Set-WinSystemLocale -SystemLocale fr-FR
   ```
   👉 Explication : `GeoId 84` correspond à la France; la culture règle dates, nombres et devise; la locale système sert aux programmes non Unicode (redémarrage requis).

3. Appliquer les réglages aux écrans d'accueil et aux nouveaux comptes : **Panneau de configuration > Région > Administratif > Copier les paramètres**.
   ```powershell
   Copy-UserInternationalSettingsToSystem -WelcomeScreen $true -NewUser $true
   ```
   👉 Explication : reproduit les paramètres de langue sur l'écran de connexion et les futurs profils.

4. Vérifier le résultat.
   ```powershell
   Get-WinUserLanguageList
   Get-Culture
   Get-WinSystemLocale
   Get-WinHomeLocation
   ```
   👉 Explication : doit afficher `fr-FR` et la France.

## 2. Production — Contrôles

Imposer la langue et la région par GPO ou par profil Intune pour garder des postes homogènes.

## 3. Production — Sécurité

Ne rien installer comme pack de langue depuis une source non officielle; `Install-Language` utilise Windows Update.

## Validation et retour arrière

- **Validation** : `Get-Culture` retourne `fr-FR` après redémarrage.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
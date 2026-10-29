---
title: "Fiche Simple - VM Windows Server 2025 Vie Systeme 18 Table D Hotes Locale"
description: "Utiliser le fichier hosts de façon contrôlée."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windowsserver2025", "vie-du-systeme", "cycle-de-vie", "etape-18"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-18`

---

## Problème précis à résoudre

Utiliser le fichier hosts de façon contrôlée.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir en administrateur le fichier `C:\Windows\System32\drivers\etc\hosts` (Bloc-notes lancé **en tant qu'administrateur**).
   ```powershell
   Get-Content C:\Windows\System32\drivers\etc\hosts
   ```
   👉 Explication : affiche les entrées en vigueur (les lignes `#` sont des commentaires).

2. Ajouter une entrée temporaire (remplacer `IP` et `NOM_HOTE`) :
   ```powershell
   Add-Content C:\Windows\System32\drivers\etc\hosts "`nIP NOM_HOTE"
   ```
   👉 Explication : associe un nom à une adresse sans DNS; à réserver aux tests.

3. Vérifier la prise en compte :
   ```powershell
   Resolve-DnsName NOM_HOTE -DnsOnly:$false
   ipconfig /flushdns
   ```
   👉 Explication : le cache DNS est vidé et le nom résolu.

## 2. Production — Contrôles

Supprimer les entrées temporaires après les tests; le DNS reste la source de vérité.

## 3. Production — Sécurité

Surveiller le fichier : les logiciels malveillants le détournent pour rediriger des noms.

## Validation et retour arrière

- **Validation** : Entrée présente puis supprimée en fin de test.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
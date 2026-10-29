---
title: "Fiche Simple - VM Windows 11 PowerShell7 Profils Journalisation Secrets"
description: "Contrôler le profil PowerShell et la journalisation sans exposer de secret."
published: true
date: 2026-10-29T20:14:10Z
tags: ["windows-11", "powershell", "pwsh", "administration", "scripts", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_11_PowerShell7_Profils_Journalisation_Secrets.md

- **Environnement** : VM ou poste Windows 11 de test; compte standard puis élévation uniquement si requise
- **OS / Version** : Windows 11 x64; PowerShell 7.6.9 Stable (LTS)
- **Catégorie** : administration / PowerShell
- **Tags** : `windows-11`, `powershell`, `pwsh`, `administration`, `scripts`, `securite`

---

## Problème précis à résoudre

Contrôler le profil PowerShell et la journalisation sans exposer de secret.

## 1. Hors-Production (Lab / Test / POC)

1. Lire le chemin du profil et vérifier son existence :
   ```powershell
   $PROFILE
   Test-Path -LiteralPath $PROFILE
   ```
   👉 Explication : le profil est un script exécuté à chaque ouverture du shell; relire son contenu avant de le créer ou de l'utiliser.

2. N'écrire dans le profil ni mot de passe, ni jeton, ni clé privée.
   👉 Explication : un secret en clair dans un profil est lisible par tout processus du compte.

3. Activer le transcript uniquement si la politique l'exige, dans un emplacement protégé avec règles de rétention.
   👉 Explication : le transcript enregistre commandes et sorties, y compris des secrets affichés par erreur.

## 2. Production — Contrôles

Définir l'emplacement, la rétention et les accès aux transcripts.

## 3. Production — Sécurité

- Aucun secret dans le profil ni dans les journaux.
- Protéger les fichiers de transcript.

## Validation et retour arrière

- **Validation** : Le profil ne contient aucun secret et la journalisation respecte la politique.
- **Retour arrière** : Retirer du profil les lignes ajoutées et supprimer les transcripts non nécessaires selon la politique.

## Si le problème n'est pas résolu

- [Microsoft Learn — Installer PowerShell 7 sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [PowerShell — publication v7.6.9](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9)
- [Guide complet PowerShell 7.6.9 Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11#7-profils-journalisation-et-secrets)
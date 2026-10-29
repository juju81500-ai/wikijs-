---
title: "Fiche Simple - VM Windows Server 2025 Hardening Preparer Baseline"
description: "Inventorier l'existant et poser une baseline avant tout durcissement."
published: true
date: 2026-10-29T20:22:42Z
tags: ["windows-server-2025", "hardening", "smb", "ldap", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_VM_Windows_Server_2025_Hardening_Preparer_Baseline.md

- **Environnement** : Serveur membre ou contrôleur de domaine en laboratoire avant déploiement
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : sécurité / baseline
- **Tags** : `windows-server-2025`, `hardening`, `smb`, `ldap`, `securite`

---

## Problème précis à résoudre

Inventorier l'existant et poser une baseline avant tout durcissement.

## 1. Hors-Production (Lab / Test / POC)

1. Inventorier le serveur :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-WindowsFeature | Where-Object Installed
   ```
   👉 Explication : Relève la version du système et les rôles/fonctionnalités installés (lecture seule).

2. Inventorier clients, NAS, applications, mécanismes LDAP/SMB, outils de sauvegarde et dépendances d'authentification; déployer d'abord en laboratoire représentatif.
   👉 Explication : permet de prévoir les régressions de compatibilité.

3. Appliquer une baseline Microsoft adaptée au rôle, conserver un compte de secours testé et vérifier la restauration avant les changements de politique.
   👉 Explication : garantit un accès et un retour possibles.

## 2. Production — Contrôles

Ne désactiver aucune protection nouvelle sans analyse et dérogation formelle.

## 3. Production — Sécurité

- Compte de secours stocké dans un coffre et testé.

## Validation et retour arrière

- **Validation** : inventaire fait, baseline choisie, restauration vérifiée.
- **Retour arrière** : supprimer la baseline appliquée en lab ou restaurer la VM.

## Si le problème n'est pas résolu

- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Guide complet — étape 1](/02-fiches-completes/windows/server-2025/autres/31-hardening-windows-server-2025-production#1-preparer-la-baseline)
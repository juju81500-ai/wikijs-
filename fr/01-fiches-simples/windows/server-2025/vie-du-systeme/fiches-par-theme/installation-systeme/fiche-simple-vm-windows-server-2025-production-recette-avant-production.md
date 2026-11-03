---
title: "fiche-simple-vm-windows-server-2025-production-recette-avant-production"
description: "Valider le serveur avant sa mise en production."
published: true
date: 2026-11-03T09:36:14Z
tags: ["windows-server-2025", "installation", "production", "uefi", "openssh"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# fiche-simple-vm-windows-server-2025-production-recette-avant-production.md

- **Environnement** : Serveur physique ou [[Glossary:VM]] Windows Server 2025 administré par l'organisation
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : installation / déploiement
- **Tags** : `windows-server-2025`, `installation`, `production`, `uefi`, `openssh`

---

## Problème précis à résoudre

Valider le serveur avant sa mise en production.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier [[Glossary:DNS]], heure, connectivité depuis les réseaux autorisés, mises à jour, accès d'administration, supervision, sauvegarde/restauration et journaux.
   👉 Explication : on contrôle tous les points d'exploitation.

2. Contrôler les services et l'historique d'événements :
   ```powershell
   Get-Service | Where-Object Status -eq 'Stopped' | Select-Object -First 20 Name, DisplayName
   Get-WinEvent -FilterHashtable @{ LogName = 'System'; Level = 2; StartTime = (Get-Date).AddHours(-24) } -MaxEvents 20
   ```
   👉 Explication : aucune erreur inattendue ne doit subsister.

3. Tester un redémarrage planifié (**Démarrer > Alimentation > Redémarrer**) puis documenter version, édition, build, adresse, rôles, exceptions et propriétaire.
   👉 Explication : on prouve la reprise.

## 2. Production — Contrôles

Conserver la fiche de recette.

## 3. Production — Sécurité

- Ne pas mettre en production avec un écart non accepté.

## Validation et retour arrière

- **Validation** : Tous les points de recette sont validés.
- **Retour arrière** : Garder le serveur hors production jusqu'à correction.

## Si le problème n'est pas résolu

- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Microsoft Learn — Installation de Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server)
- [Guide complet déploiement Windows Server 2025](/fr/02-fiches-completes/windows/server-2025/installation-deploiement/30-deploiement-windows-server-2025-production#5-recette-avant-mise-en-production)
---
title: "Fiche Simple - Cloud Entra ID Connect Staging"
description: "Utiliser un serveur Entra Connect en mode staging pour tester la configuration sans exporter vers le tenant."
published: true
date: 2026-10-29T20:39:58Z
tags: ["entra-id", "entra-connect", "staging", "synchronisation", "bascule"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_Cloud_Entra_ID_Connect_Staging

- **Environnement** : Tenant Microsoft Entra ID (SaaS), poste d'administration avec PowerShell 7 et modules Microsoft.Graph ; second serveur Entra Connect
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer ; licences et fonctions à vérifier)
- **Catégorie** : systèmes, annuaires et services
- **Tags** : `entra-id`, `entra-connect`, `staging`, `synchronisation`, `bascule`

---

## Problème précis à résoudre

Utiliser un serveur Entra Connect en mode staging pour tester la configuration sans exporter vers le tenant.

## 1. Hors-Production (Lab / Test / POC)

1. Installer Entra Connect sur le second serveur ; dans l'assistant, cocher « Enable staging mode » à l'étape correspondante, en suivant la page Learn de staging.
   👉 Explication : le serveur importe et prépare les données sans les exporter vers Entra ID.

2. Contrôler que le serveur est bien en staging :
   ```powershell
   Import-Module ADSync
   Get-ADSyncScheduler | Select StagingModeEnabled,SyncCycleEnabled
   ```
   👉 Explication : `StagingModeEnabled` doit valoir True.

3. Lancer un cycle delta et comparer les résultats avec le serveur actif, via Synchronization Service Manager (Operations / Connectors / Search Connector Space).
   👉 Explication : aucune exportation ne doit être exécutée en staging.

4. Exporter la configuration du serveur actif : assistant Entra Connect → Configure → View or export current configuration.
   👉 Explication : sert à comparer les deux serveurs ; la configuration exportée ne remplace pas une sauvegarde complète et ne contient pas les secrets.

5. Pour une bascule planifiée : désactiver l'export sur l'ancien serveur actif, puis dans l'assistant du serveur staging choisir Configure staging mode et décocher le mode staging.
   👉 Explication : un seul serveur doit exporter à la fois ; suivre la page Learn « Staging server and disaster recovery ».

## 2. Production — Contrôles

Production : bascule en fenêtre de maintenance, comparaison des règles, fenêtres de supervision, suspension des changements d'annuaire non urgents.

## 3. Production — Sécurité

- Ne jamais laisser deux serveurs exporter simultanément.
- Limiter l'accès au serveur staging comme au serveur actif.
- Ne pas copier les bases ADSync entre serveurs sauf procédure Microsoft documentée.

## Validation et retour arrière

- **Validation** : après bascule, `Get-ADSyncScheduler` indique le serveur actif non staging ; un utilisateur pilote synchronise.
- **Retour arrière** : remettre l'ancien serveur en actif et le nouveau en staging (voir fiche Retour arrière).

## Si le problème n'est pas résolu

- [Serveur de staging Entra Connect](https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-sync-staging-server)
- [Documentation Microsoft Entra ID](https://learn.microsoft.com/entra/identity/)
- [Fiche d'entrée Microsoft Entra ID](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-microsoft-entra-id)
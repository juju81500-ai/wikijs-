---
title: "Fiche Simple - Cloud Entra ID Connect Retour Arriere"
description: "Préparer le retour arrière d'une modification de synchronisation hybride sans recette universelle de sauvegarde de l'état de synchronisation."
published: true
date: 2026-10-29T20:39:58Z
tags: ["entra-id", "entra-connect", "retour-arriere", "reprise", "synchronisation"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_Cloud_Entra_ID_Connect_Retour_Arriere

- **Environnement** : Tenant Microsoft Entra ID (SaaS), poste d'administration avec PowerShell 7 et modules Microsoft.Graph
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer ; licences et fonctions à vérifier)
- **Catégorie** : systèmes, annuaires et services
- **Tags** : `entra-id`, `entra-connect`, `retour-arriere`, `reprise`, `synchronisation`

---

## Problème précis à résoudre

Préparer le retour arrière d'une modification de synchronisation hybride sans recette universelle de sauvegarde de l'état de synchronisation.

## 1. Hors-Production (Lab / Test / POC)

1. Avant changement : exporter la configuration (assistant Entra Connect → View or export current configuration) et noter la version installée.
   👉 Explication : documentation de référence ; l'état de synchronisation lui-même n'a pas de sauvegarde universelle simple.

2. Prévoir une reconstruction : conserver le package d'installation validé et le plan de serveur staging, plutôt que s'appuyer sur la restauration d'une base ADSync.
   👉 Explication : la stratégie recommandée par Microsoft passe par un serveur staging et une réinstallation ; confirmer la page de reprise après sinistre.

3. Avant toute modification de filtrage ou de règles, garder le serveur staging à jour comme point de reprise.
   👉 Explication : limite le risque de suppression d'objets au cloud.

4. En cas d'anomalie : suspendre le cycle de synchronisation sur le serveur actif :
   ```powershell
   Import-Module ADSync
   Set-ADSyncScheduler -SyncCycleEnabled $false
   Get-ADSyncScheduler
   ```
   👉 Explication : arrête les nouveaux cycles ; ne corrige pas les exports déjà réalisés.

5. Reprendre après correction :
   ```powershell
   Set-ADSyncScheduler -SyncCycleEnabled $true
   ```
   👉 Explication : réactive le planificateur après vérification.

6. Vérifier les suppressions accidentelles dans Entra admin center → Entra ID → Users → Deleted users.
   👉 Explication : la corbeille permet une restauration pendant la période de conservation ; vérifier sa durée dans Learn.

## 2. Production — Contrôles

Production : seuil de suppression accidentelle compris, plan d'incident, contacts, validation par pilote, fenêtre de changement.

## 3. Production — Sécurité

- Ne jamais copier les secrets du connecteur ni les bases de synchronisation vers un support non protégé.
- Ne pas forcer de synchronisation complète pendant l'incident sans analyse.
- Tracer chaque réactivation du planificateur.

## Validation et retour arrière

- **Validation** : état normal `Get-ADSyncScheduler`, aucune suppression inattendue, pilote conforme.
- **Retour arrière** : bascule vers le serveur staging (fiche Staging) ou réinstallation depuis la configuration exportée.

## Si le problème n'est pas résolu

- [Documentation Entra Connect](https://learn.microsoft.com/entra/identity/hybrid/connect/whatis-azure-ad-connect)
- [Fiche Staging](/01-fiches-simples/transverses/cloud-saas/entra-id/fiche-simple-cloud-entra-id-connect-staging)
- [Documentation Microsoft Entra ID](https://learn.microsoft.com/entra/identity/)
- [Fiche d'entrée Microsoft Entra ID](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-microsoft-entra-id)
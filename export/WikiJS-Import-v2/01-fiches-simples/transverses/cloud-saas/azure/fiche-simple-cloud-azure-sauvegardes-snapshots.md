---
title: "Fiche Simple - Cloud Azure Sauvegardes Snapshots"
description: "Sauvegardes et snapshots dans Microsoft Azure en limitant les risques de sécurité, de disponibilité et de coût."
published: true
date: 2026-10-29T21:00:44Z
tags: ["azure", "sauvegardes_snapshots", "securite", "procedure"]
editor: markdown
dateCreated: 2026-10-29T21:00:44Z
dateModified: 2026-10-29T21:00:44Z
---

# Fiche_Simple_-_Cloud_Azure_Sauvegardes_Snapshots

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Azure CLI (az ; version publiée à vérifier)
- **Catégorie** : cloud public / sauvegardes et snapshots
- **Tags** : `azure`, `sauvegardes_snapshots`, `securite`, `procedure`

---

## Problème précis à résoudre

Sauvegardes et snapshots dans Microsoft Azure en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Recovery Services vaults → Create ; Backup → Backup goal ; Virtual machines → Disks → Create snapshot.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Azure CLI (az ; version publiée à vérifier)) :
   ```bash
   az backup vault list --resource-group GROUPE
az backup item list --resource-group GROUPE --vault-name NOM_VAULT --backup-management-type AzureIaasVM --workload-type VM
   ```
   👉 Explication : Définir RPO/RTO, politique de sauvegarde et rétention ; tester la restauration dans un groupe isolé. Un snapshot disque n’est pas à lui seul une sauvegarde applicative.
3. Console et CLI : comparer la configuration affichée avec l’état attendu, puis valider sur une ressource pilote non sensible.
   👉 Explication : les interfaces évoluent ; vérifier l’aide/version officielle et les quotas/licences avant généralisation.

## 2. Production — Contrôles

Définir RPO/RTO, cohérence applicative, périmètre, rétention, région secondaire et responsable. Contrôler les jobs échoués et le coût de stockage.

## 3. Production — Sécurité

Restreindre suppression/altération, chiffrer les sauvegardes et protéger leurs clés. Appliquer séparation des tâches et rétention légale.

## Validation et retour arrière

- **Validation** : Restauration isolée testée, intégrité confirmée et temps mesuré comparé au RTO.
- **Retour arrière** : Revenir à la dernière configuration approuvée ; préserver les sauvegardes et journaux. Ne supprimer la ressource de test qu’après validation des dépendances et du propriétaire.

## Si le problème n'est pas résolu

- [Microsoft Azure — documentation officielle](https://learn.microsoft.com/azure/backup/backup-overview)
- [Référence et bonnes pratiques](https://learn.microsoft.com/azure/virtual-machines/snapshot-copy-managed-disk)
- [Fiche d’entrée Microsoft Azure](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-microsoft-azure)
---
title: "Fiche Simple - VM Proxmox VE 8 Proxmox OpenStack Nettoyer Retour Arriere"
description: "Retirer un lab et révoquer les accès sans affecter l’hôte Proxmox ni les réseaux partagés."
published: true
date: 2026-10-29T20:49:11Z
tags: ["proxmox-ve", "openstack", "devstack", "nettoyage", "rollback"]
editor: markdown
dateCreated: 2026-10-29T20:49:11Z
dateModified: 2026-10-29T20:49:11Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Nettoyer_Retour_Arriere

- **Environnement** : VM OpenStack DevStack jetable sur Proxmox VE 8.x
- **OS / Version** : Ubuntu Server 24.04 LTS / DevStack
- **Catégorie** : cloud privé / nettoyage de lab
- **Tags** : `proxmox-ve`, `openstack`, `devstack`, `nettoyage`, `rollback`

---

## Problème précis à résoudre

Retirer un lab et révoquer les accès sans affecter l’hôte Proxmox ni les réseaux partagés.

## 1. Hors-Production (Lab / Test / POC)

1. Inventorier dans Horizon/CLI instances, volumes, images, réseaux, routeurs, règles et ressources; confirmer projet/propriétaires avant suppression.
   👉 Explication : suppressions irréversibles; aucun wildcard ou commande globale n’est donné.
2. Supprimer uniquement les ressources créées pour le POC, dans l’ordre des dépendances indiqué par documentation; vérifier les volumes/snapshots à conserver.
   👉 Explication : mauvaise identification détruit des données même en environnement partagé.
3. Révoquer les jetons de test et supprimer les fichiers secrets après accord du propriétaire.
   👉 Explication : supprimer le fichier ne remplace pas la révocation d’un secret exposé.
4. Dans Proxmox, arrêter puis supprimer la VM par son ID après double vérification ID/stockage/données; retirer ISO/bridge seulement s’ils étaient dédiés au POC et non utilisés ailleurs.
   👉 Explication : suppression de VM efface ses disques; bridge/datastore peuvent être partagés.

## 2. Production — Contrôles

- En production, suivre processus de changement, conservation/destruction de données, quotas, sauvegardes et journalisation.

## 3. Production — Sécurité

- Ne supprimer aucun bridge/datastore/image/compte partagé; révoquer immédiatement tout secret exposé et examiner ses usages.

## Validation et retour arrière

- **Validation** : ressources recensées puis retirées, jetons révoqués, hôtes/réseaux partagés inchangés. **Retour arrière** : suspendre après erreur; restaurer depuis sauvegarde validée/support, ne pas recréer à l’aveugle.

## Si le problème n'est pas résolu

- [Proxmox VE — Guide](https://pve.proxmox.com/pve-docs/)
- [Proxmox VE — API Viewer](https://pve.proxmox.com/pve-docs/api-viewer/index.html)
- [OpenStack — documentation](https://docs.openstack.org/)
- [DevStack — Quick Start](https://docs.openstack.org/devstack/latest/)
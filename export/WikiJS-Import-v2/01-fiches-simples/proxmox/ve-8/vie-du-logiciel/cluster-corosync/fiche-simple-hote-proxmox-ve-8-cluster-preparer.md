---
title: "Fiche Simple - Hote Proxmox VE 8 Cluster Preparer"
description: "Vérifier versions, noms, IP et résolution avant de créer le cluster."
published: true
date: 2026-10-29T20:14:10Z
tags: ["proxmox-ve", "pve8", "cluster", "corosync", "preparation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Preparer.md

- **Environnement** : Nœuds physiques dédiés, réseau Corosync faible latence
- **OS / Version** : Proxmox VE 8.x
- **Catégorie** : virtualisation / cluster
- **Tags** : `proxmox-ve`, `pve8`, `cluster`, `corosync`, `preparation`

---

## Problème précis à résoudre

Vérifier versions, noms, IP et résolution avant de créer le cluster.

## 1. Hors-Production (Lab / Test / POC)

1. Sur chaque nœud, vérifier la version Proxmox VE :
   ```bash
   pveversion -v
   ```
   👉 Explication : tous les nœuds doivent avoir des versions compatibles et à jour.

2. Vérifier le nom complet du nœud :
   ```bash
   hostname -f
   ```
   👉 Explication : le nom doit être stable et correspondre à l'IP fixe.

3. Vérifier la résolution des noms des nœuds (pve01 et pve02 sont des exemples à remplacer) :
   ```bash
   getent hosts pve01 pve02
   ```
   👉 Explication : une résolution directe stable est indispensable à Corosync.

4. Confirmer que le nœud à ajouter n'héberge aucune charge à conserver.
   👉 Explication : l'ajout peut remplacer sa configuration de cluster.

5. Vérifier sauvegardes, stockage partagé ou répliqué et fenêtre de maintenance.
   👉 Explication : un cluster ne remplace pas une sauvegarde.

## 2. Production — Contrôles

Prévoir un réseau Corosync dédié si possible, le quorum attendu et la fenêtre de maintenance.

## 3. Production — Sécurité

- Ne pas mélanger deux clusters existants.
- Garder un accès console aux nœuds.

## Validation et retour arrière

- **Validation** : Versions, noms et résolution sont cohérents sur tous les nœuds.
- **Retour arrière** : Aucune modification : rien à annuler.

## Si le problème n'est pas résolu

- [Proxmox VE — Cluster Manager](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Guide complet — préparer les nœuds](/02-fiches-completes/proxmox/ve-8/installation-deploiement/09-hyperviseur-proxmox-ve-8x-cluster-corosync#1-preparer-les-nuds)
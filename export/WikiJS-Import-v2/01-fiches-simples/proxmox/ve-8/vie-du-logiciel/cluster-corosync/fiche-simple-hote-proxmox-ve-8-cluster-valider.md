---
title: "Fiche Simple - Hote Proxmox VE 8 Cluster Valider"
description: "Vérifier le quorum, les liens Corosync et la cohérence des VM et du stockage."
published: true
date: 2026-10-29T20:14:10Z
tags: ["proxmox-ve", "pve8", "cluster", "corosync", "quorum", "ha"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Valider.md

- **Environnement** : Nœuds physiques dédiés, réseau Corosync faible latence
- **OS / Version** : Proxmox VE 8.x
- **Catégorie** : virtualisation / cluster
- **Tags** : `proxmox-ve`, `pve8`, `cluster`, `corosync`, `quorum`, `ha`

---

## Problème précis à résoudre

Vérifier le quorum, les liens Corosync et la cohérence des VM et du stockage.

## 1. Hors-Production (Lab / Test / POC)

1. Afficher les nœuds et l'état du quorum :
   ```bash
   pvecm nodes
   pvecm status
   ```
   👉 Explication : tous les nœuds et le quorum attendu doivent apparaître.

2. Contrôler les liens Corosync :
   ```bash
   corosync-cfgtool -s
   ```
   👉 Explication : chaque lien doit être connecté.

3. Arrêter proprement un nœud, vérifier que le quorum tient, puis le redémarrer.
   👉 Explication : on valide le comportement lors d'une panne contrôlée.

4. Confirmer que VM, conteneurs et stockage restent cohérents. Pour la HA, définir groupes, priorités et fencing selon la conception.
   👉 Explication : la HA doit être conçue avant d'être activée.

## 2. Production — Contrôles

Documenter le quorum attendu et la conception HA retenue.

## 3. Production — Sécurité

- Ne pas activer la HA sans fencing ou support matériel adapté.

## Validation et retour arrière

- **Validation** : Quorum conservé après arrêt contrôlé d'un nœud; VM et stockage cohérents.
- **Retour arrière** : Redémarrer le nœud arrêté et revérifier `pvecm status`.

## Si le problème n'est pas résolu

- [Proxmox VE — Cluster Manager](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Guide complet — valider quorum et stockage](/02-fiches-completes/proxmox/ve-8/installation-deploiement/09-hyperviseur-proxmox-ve-8x-cluster-corosync#3-valider-quorum-et-stockage)
---
title: "Mettre en place un cluster Proxmox VE 8.x"
description: "Fiche simple : [préparer les nœuds](../../../../01-Fiches-Simples/Proxmox/VE-8/Vie-du-logiciel/Cluster-Corosync/FicheSimple-HoteProxmoxVE8ClusterPreparer.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["proxmox-ve", "pve8", "cluster", "corosync", "ha"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Mettre en place un cluster Proxmox VE 8.x

- **Environnement** : Nœuds physiques dédiés, réseau Corosync faible latence
- **Tags** : `proxmox-ve`, `pve8`, `cluster`, `corosync`, `ha`

## 1. Préparer les nœuds

Fiche simple : [préparer les nœuds](/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-preparer).

Utiliser des versions Proxmox VE compatibles et à jour sur tous les nœuds, des noms/IP fixes, une résolution directe/inverse stable et un réseau Corosync dédié si possible. Vérifier le quorum attendu, le stockage partagé ou répliqué, les sauvegardes et la fenêtre de maintenance. Un cluster ne remplace pas une sauvegarde.

Un nœud ajouté ne doit pas déjà héberger de charges à conserver : l'ajout peut remplacer sa configuration de cluster. Ne pas mélanger deux clusters existants.

```bash
pveversion -v
hostname -f
getent hosts pve01 pve02
```

## 2. Créer le cluster

Fiche simple : [créer le cluster](/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-creer).

Sur un premier nœud uniquement, après sauvegarde de la configuration et validation du nom :

```bash
pvecm create NOM_CLUSTER
pvecm status
```

Sur un nœud vierge prêt à rejoindre, depuis sa console ou une connexion de secours :

```bash
pvecm add IP_DU_NOEUD_EXISTANT
pvecm status
```

Utiliser les paramètres Corosync et la méthode d'ajout de la version exacte, selon la documentation Proxmox. Ne pas lancer ces commandes sur des nœuds déjà utilisés en production sans plan de migration.

## 3. Valider quorum et stockage

Fiche simple : [valider quorum et stockage](/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-valider).

```bash
pvecm nodes
pvecm status
corosync-cfgtool -s
```

Vérifier le quorum après arrêt contrôlé d'un nœud, puis confirmer que les VM/CT et le stockage restent cohérents. Pour HA, définir les groupes, priorités et règles de fencing/support matériel selon la conception retenue.

## 4. Sécuriser l'administration

Fiche simple : [sécuriser l'administration](/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-securiser).

Restreindre l'interface Web/API et SSH au réseau d'administration, utiliser des comptes nominatifs et MFA, gérer les certificats, limiter les privilèges et centraliser les sauvegardes hors cluster. Ne pas appliquer de règles firewall sans garder un accès console.

## 5. Maintenance et incidents

Fiche simple : [maintenance et incidents](/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-maintenance).

Sauvegarder les invités avant mises à jour, suivre les notes officielles par version et mettre à jour un nœud à la fois seulement si la matrice le permet. En cas de perte de quorum, ne pas forcer arbitrairement le nombre de votes : préserver les données, isoler les nœuds et suivre la procédure Proxmox de récupération du quorum.
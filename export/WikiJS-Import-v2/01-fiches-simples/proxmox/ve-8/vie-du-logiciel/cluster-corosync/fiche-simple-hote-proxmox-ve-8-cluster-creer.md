---
title: "Fiche Simple - Hote Proxmox VE 8 Cluster Creer"
description: "Créer le cluster sur un premier nœud puis y joindre les autres."
published: true
date: 2026-10-29T20:14:10Z
tags: ["proxmox-ve", "pve8", "cluster", "corosync", "creation", "pvecm"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Creer.md

- **Environnement** : Nœuds physiques dédiés, réseau Corosync faible latence
- **OS / Version** : Proxmox VE 8.x
- **Catégorie** : virtualisation / cluster
- **Tags** : `proxmox-ve`, `pve8`, `cluster`, `corosync`, `creation`, `pvecm`

---

## Problème précis à résoudre

Créer le cluster sur un premier nœud puis y joindre les autres.

## 1. Hors-Production (Lab / Test / POC)

1. Sur le premier nœud uniquement : **Datacenter > Cluster > Create Cluster**, saisir le nom du cluster et choisir le lien réseau.
   👉 Explication : c'est l'équivalent graphique de `pvecm create`.

2. Ou en ligne de commande (`labcluster` est un nom d'exemple à remplacer) :
   ```bash
   pvecm create labcluster
   pvecm status
   ```
   👉 Explication : la commande initialise le cluster et affiche son état.

3. Sur un nœud vierge : **Datacenter > Cluster > Join Cluster**, coller les informations de jointure du premier nœud et saisir le mot de passe root à l'invite.
   👉 Explication : le mot de passe se saisit dans l'interface, jamais en argument.

4. Ou en ligne de commande depuis la console (192.0.2.11 est un exemple d'IP du nœud existant à remplacer) :
   ```bash
   pvecm add 192.0.2.11
   pvecm status
   ```
   👉 Explication : la commande demande le mot de passe en interactif puis rejoint le cluster.

## 2. Production — Contrôles

Utiliser la méthode d'ajout et les paramètres Corosync de la version exacte selon la documentation Proxmox.

## 3. Production — Sécurité

- Ne pas lancer ces commandes sur des nœuds en production sans plan de migration.
- Sauvegarder la configuration avant de créer le cluster.

## Validation et retour arrière

- **Validation** : `pvecm status` affiche tous les nœuds et le quorum.
- **Retour arrière** : Sur un lab, réinstaller le nœud ajouté; en production, suivre la procédure Proxmox de retrait de nœud.

## Si le problème n'est pas résolu

- [Proxmox VE — Cluster Manager](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Guide complet — créer le cluster](/02-fiches-completes/proxmox/ve-8/installation-deploiement/09-hyperviseur-proxmox-ve-8x-cluster-corosync#2-creer-le-cluster)
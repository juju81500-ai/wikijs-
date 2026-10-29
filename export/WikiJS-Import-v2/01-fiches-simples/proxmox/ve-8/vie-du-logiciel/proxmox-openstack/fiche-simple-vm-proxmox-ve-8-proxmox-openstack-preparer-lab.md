---
title: "Fiche Simple - VM Proxmox VE 8 Proxmox OpenStack Preparer Lab"
description: "Préparer une VM isolée pour DevStack avant d’installer les services ou d’autoriser du trafic externe."
published: true
date: 2026-10-29T20:49:11Z
tags: ["proxmox-ve", "pve8", "openstack", "prerequis", "reseau-isole"]
editor: markdown
dateCreated: 2026-10-29T20:49:11Z
dateModified: 2026-10-29T20:49:11Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Preparer_Lab

- **Environnement** : Nœud Proxmox VE 8.x de lab; VM OpenStack isolée et jetable
- **OS / Version** : Proxmox VE 8.x; Ubuntu Server 24.04 LTS pour DevStack
- **Catégorie** : cloud privé / préparation lab
- **Tags** : `proxmox-ve`, `pve8`, `openstack`, `prerequis`, `reseau-isole`

---

## Problème précis à résoudre

Préparer une VM isolée pour DevStack avant d’installer les services ou d’autoriser du trafic externe.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l’ISO Ubuntu Server 24.04 LTS depuis le site Ubuntu officiel et l’importer dans Proxmox via **Stockage > ISO Images > Upload**.
   👉 Explication : DevStack présente Ubuntu 24.04 Noble comme version la plus testée au moment consulté; cela ne certifie pas l’intégration Proxmox-OpenStack.
2. Dans Proxmox, sélectionner le nœud > **Create VM**; attacher l’ISO, créer un disque jetable et relier la VM à un bridge de lab sans uplink externe. Dimensionner selon ressources et recommandations DevStack actuelles.
   👉 Explication : besoins variables selon services; éviter surallocation sur hôte partagé.
3. Dans les options CPU, exposer les extensions de virtualisation imbriquée seulement après vérification de la documentation PVE. Dans Ubuntu, contrôler :
   ```bash
   grep -m1 -Eo 'vmx|svm' /proc/cpuinfo
   ```
   👉 Explication : résultat vide = extensions non visibles; nesting dépend du matériel. Ne pas changer une VM de production.
4. Installer Ubuntu minimal, mettre à jour, vérifier routes/adresses depuis la console et prendre un snapshot court avant DevStack.
   👉 Explication : snapshot n’est pas sauvegarde; DevStack modifie profondément le système.

## 2. Production — Contrôles

- Architecture jetable uniquement; DevStack n’est pas production. Confirmer les matrices de support des fournisseurs avant tout usage réel.

## 3. Production — Sécurité

- Bridge/VLAN isolé, sans réseau gestion/production ni IP publique; aucun port entrant Internet; ne pas réutiliser comptes/clefs SSH de production.

## Validation et retour arrière

- **Validation** : Ubuntu démarre, nesting visible si requis, routes confirment l’isolement. **Retour arrière** : restaurer ou supprimer la VM après vérification de son ID et des données.

## Si le problème n'est pas résolu

- [DevStack — Quick Start et distributions](https://docs.openstack.org/devstack/latest/)
- [DevStack — installation mono-machine](https://docs.openstack.org/devstack/latest/guides/single-machine.html)
- [Proxmox VE — documentation officielle](https://pve.proxmox.com/pve-docs/)
---
title: "Fiche Simple - VM Proxmox VE 8 Proxmox OpenStack Sauvegarder Restaurer Lab"
description: "Restaurer un lab OpenStack jetable sans confondre snapshot VM, sauvegarde indépendante et protection de production."
published: true
date: 2026-10-29T20:49:11Z
tags: ["proxmox", "openstack", "devstack", "sauvegarde", "restauration", "lab"]
editor: markdown
dateCreated: 2026-10-29T20:49:11Z
dateModified: 2026-10-29T20:49:11Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Sauvegarder_Restaurer_Lab

- **Environnement** : VM DevStack jetable sur Proxmox VE 8.x, environnement isolé
- **OS / Version** : Ubuntu Server 24.04 LTS pour le lab OpenStack; DevStack selon branche officiellement documentée
- **Catégorie** : cloud privé / sauvegarde de lab
- **Tags** : `proxmox`, `openstack`, `devstack`, `sauvegarde`, `restauration`, `lab`

---

## Problème précis à résoudre

Restaurer un lab OpenStack jetable sans confondre snapshot VM, sauvegarde indépendante et protection de production.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter proprement la VM DevStack depuis le système invité et vérifier dans la console qu’aucun test n’est en cours.
   👉 Explication : l’arrêt propre réduit le risque de capturer un état incohérent.
2. Dans l’interface Proxmox, ouvrir **Datacenter > Node > VM > Snapshots > Take Snapshot**, saisir `SNAPSHOT_LAB_AVANT_TEST` (à remplacer) et confirmer l’ID de VM.
   👉 Explication : le snapshot facilite un retour mais reste sur le stockage Proxmox; il n’est pas une sauvegarde indépendante.
3. Pour une copie indépendante, utiliser la tâche et le dépôt déjà administrés dans Proxmox VE ou Proxmox Backup Server, selon leur documentation de version.
   👉 Explication : ne pas inventer une cible ni supposer qu’un snapshot est répliqué hors site.
4. Restaurer un point de sauvegarde dans le lab sous un nouvel ID VM et sur un réseau isolé, en suivant l’assistant de l’outil utilisé.
   👉 Explication : le nouvel ID évite d’écraser la VM source; les étapes exactes dépendent de la version de PBS/PVE.
5. Vérifier l’accès local à Horizon et au catalogue, puis supprimer seulement la VM restaurée de test.
   👉 Explication : ce contrôle valide la récupération sans toucher à une plateforme réelle.

## 2. Production — Contrôles

- DevStack est jetable et n’est pas destiné aux données ou services de production.
- Une plateforme réelle exige une architecture et une procédure de sauvegarde supportées et validées séparément.

## 3. Production — Sécurité

- Isoler la VM et son réseau; ne pas exposer Horizon ni les API au réseau public.
- Protéger les sauvegardes et fichiers de configuration contenant des secrets.

## Validation et retour arrière

- **Validation** : restauration d’essai sur nouvel ID, réseau isolé et catalogue accessible.
- **Retour arrière** : retirer uniquement la VM restaurée de test et conserver la source jusqu’à approbation.

## Si le problème n'est pas résolu

- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [DevStack — Quick Start](https://docs.openstack.org/devstack/latest/)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-proxmox-openstack)
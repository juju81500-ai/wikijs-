---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 01 Definition Des Besoins Sizing"
description: "Dimensionner l'hôte Proxmox VE avant l'achat ou l'installation."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-01"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-01`

---

## Problème précis à résoudre

Dimensionner l'hôte Proxmox VE avant l'achat ou l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les VM et conteneurs à héberger avec leurs vCPU, RAM et disque (tableau dans le dossier projet). Sur un hôte existant, relever la charge :
   ```bash
   pvesh get /nodes/NOEUD/status --output-format json-pretty
   nproc
   free -h
   lsblk -o NAME,SIZE,TYPE,ROTA
   ```
   👉 Explication : `NOEUD` = nom du nœud (`hostname`). Donne CPU, RAM et type de disques (`ROTA=0` = SSD) pour comparer au besoin.

2. Calculer le total : somme des vCPU (ratio de sur-allocation 2:1 à 4:1 selon la charge), RAM des VM + 2 Go pour l'hôte (+ 1 Go par To de ZFS si ZFS est utilisé).
   👉 Explication : la RAM ne se sur-alloue pas sans risque (OOM killer); ZFS consomme du cache ARC.

3. Prévoir réseau et stockage : 2 cartes pour la gestion et le trafic VM, 1 réseau dédié pour le stockage/cluster, disques SSD/NVMe pour les VM, disque séparé ou PBS pour les sauvegardes.
   👉 Explication : un hôte à 1 seule carte réseau mélange gestion, stockage et sauvegarde : à éviter en production.

## 2. Production — Contrôles

Ajouter 20 à 30 % de marge; prévoir la perte d'un nœud (capacité N+1) si un cluster est prévu (3 nœuds minimum pour le quorum).

## 3. Production — Sécurité

Choisir du matériel compatible (liste de compatibilité du constructeur) avec alimentation et réseau redondants.

## Validation et retour arrière

- **Validation** : Tableau de sizing validé par le propriétaire du service et conservé avec le dossier.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
---
title: "Fiche Simple - LXC Alpine Sauvegarde Reprise Production"
description: "Reprendre le service depuis une sauvegarde après validation, sans écritures concurrentes ni conflit d'identité réseau."
published: true
date: 2026-10-29T20:14:10Z
tags: ["alpine", "proxmox", "pbs", "lxc", "reprise", "rpo", "rto"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_LXC_Alpine_Sauvegarde_Reprise_Production.md

- **Environnement** : incident de production; CT source et point PBS identifiés
- **OS / Version** : Proxmox VE, PBS et Alpine maintenus
- **Catégorie** : sauvegarde LXC / reprise
- **Tags** : `alpine`, `proxmox`, `pbs`, `lxc`, `reprise`, `rpo`, `rto`

---

## Problème précis à résoudre

Reprendre le service depuis une sauvegarde après validation, sans écritures concurrentes ni conflit d'identité réseau.

## 1. Hors-Production (Lab / Test / POC)

1. Geler les écritures sur l'ancien service :
   ```sh
   rc-service SERVICE stop
   ```
   👉 Explication : déclarer l'incident; remplacer `SERVICE`.

2. Choisir le point de sauvegarde et restaurer en isolation :
   ```bash
   pvesm list STOCKAGE_PBS --vmid CTID
   pct restore 9001 STOCKAGE_PBS:backup/ct/CTID/DATE --storage STOCKAGE_DISQUE
   ```
   👉 Explication : noter ID source et destination; valider avant la bascule.

3. Éteindre ou isoler l'ancien CT :
   ```bash
   pct shutdown CTID
   ```
   👉 Explication : avant de réutiliser IP, DNS ou tâches planifiées.

4. Basculer l'adresse/DNS/VIP :
   ```bash
   pct set 9001 -net0 name=eth0,bridge=vmbr0,ip=IP/PREFIXE,gw=PASSERELLE
   pct start 9001
   ```
   👉 Explication : tester les clients puis surveiller.

## 2. Production — Contrôles

Activer la procédure d'incident et faire approuver point de reprise, gel d'écriture, bascule réseau, propriétaire applicatif et mesures RPO/RTO.

## 3. Production — Sécurité

- Ne pas basculer une restauration non validée.
- Ne pas réutiliser une IP, une tâche ou une identité tant que l'ancien CT peut être actif.
- Ne pas effectuer de bascule DNS/VIP hors du plan de changement approuvé.
- Tracer accès, décisions et actions selon la procédure de crise.

## Validation et retour arrière

- **Validation** : clients testés, données cohérentes, ancien CT isolé et durée/RPO/RTO réels documentés.
- **Retour arrière** : rétablir l'ancien service seulement après confirmation qu'il n'y a pas d'écritures concurrentes.

## Si le problème n'est pas résolu

- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Guide complet sauvegarde/restauration LXC Alpine](/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production#5-reprise-en-production)
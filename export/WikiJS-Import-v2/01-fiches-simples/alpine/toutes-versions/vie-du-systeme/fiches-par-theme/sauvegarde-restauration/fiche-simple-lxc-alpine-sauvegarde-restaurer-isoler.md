---
title: "Fiche Simple - LXC Alpine Sauvegarde Restaurer Isoler"
description: "Prouver qu'un point de sauvegarde restaure correctement le CT sans créer de conflit d'adresse ou lancer deux instances actives."
published: true
date: 2026-10-29T20:14:10Z
tags: ["alpine", "proxmox", "pbs", "lxc", "restore", "isolation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_LXC_Alpine_Sauvegarde_Restaurer_Isoler.md

- **Environnement** : PVE/PBS; restauration vers un CTID temporaire et un réseau isolé
- **OS / Version** : Alpine Linux, version maintenue utilisée par le CT source
- **Catégorie** : sauvegarde LXC / restauration test
- **Tags** : `alpine`, `proxmox`, `pbs`, `lxc`, `restore`, `isolation`

---

## Problème précis à résoudre

Prouver qu'un point de sauvegarde restaure correctement le CT sans créer de conflit d'adresse ou lancer deux instances actives.

## 1. Hors-Production (Lab / Test / POC)

1. Restaurer vers un ID temporaire : **Stockage PBS > Content > point de sauvegarde > Restore** (CT ID temporaire), ou :
   ```bash
   pct restore 9001 STOCKAGE_PBS:backup/ct/CTID/DATE --storage STOCKAGE_DISQUE --unprivileged 1
   ```
   👉 Explication : remplacer ID, chemin du point de sauvegarde et stockage; ne jamais utiliser l'ID du CT en production.

2. Isoler le réseau avant démarrage :
   ```bash
   pct set 9001 -net0 name=eth0,bridge=vmbr_isole,ip=192.0.2.250/24
   pct start 9001
   ```
   👉 Explication : bridge isolé ou IP de test distincte, pour éviter tout conflit avec l'original.

3. Vérifier dans Alpine :
   ```sh
   cat /etc/alpine-release
   ip -br addr
   ip route
   rc-status
   ```
   👉 Explication : puis contrôler volumes, propriétaires, secrets, journaux et fonction applicative (lecture/écriture métier; restauration applicative cohérente pour une base).

## 2. Production — Contrôles

Faire valider point de restauration, CTID, réseau isolé, données, résultats, RPO/RTO mesurés et responsable avant toute bascule.

## 3. Production — Sécurité

- Ne jamais connecter la copie de test au réseau actif avec la même IP que l'original.
- Ne pas faire tourner simultanément des tâches planifiées ou traitements en double.
- Protéger données et secrets restaurés selon leur classification.
- Ne pas écraser le CT source lors d'un test de restauration.

## Validation et retour arrière

- **Validation** : CT démarre isolé, volumes et application sont vérifiés, et aucune identité réseau ne chevauche la production.
- **Retour arrière** : arrêter et garder isolé le CT de test; conserver la source intacte.

## Si le problème n'est pas résolu

- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [Proxmox VE — vzdump](https://pve.proxmox.com/pve-docs/vzdump.1.html)
- [Guide complet sauvegarde/restauration LXC Alpine](/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production#4-tester-une-restauration-isolee)
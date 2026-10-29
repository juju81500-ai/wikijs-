---
title: "Fiche Simple - Hote Proxmox Backup Server Preparer Infrastructure"
description: "Dimensionner et préparer l'environnement avant d'installer PBS."
published: true
date: 2026-10-29T20:14:10Z
tags: ["proxmox-backup-server", "pbs3", "proxmox", "sauvegarde", "restauration"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_Hote_Proxmox_Backup_Server_Preparer_Infrastructure.md

- **Environnement** : Serveur de sauvegarde Proxmox Backup Server dédié, séparé du cluster protégé
- **OS / Version** : Proxmox Backup Server 3.x (appliquer une version encore supportée) avec Proxmox VE
- **Catégorie** : sauvegarde / restauration
- **Tags** : `proxmox-backup-server`, `pbs3`, `proxmox`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Dimensionner et préparer l'environnement avant d'installer PBS.

## 1. Hors-Production (Lab / Test / POC)

1. Estimer le stockage selon données, rétention, taux de changement et fenêtre de sauvegarde.
   👉 Explication : la déduplication n'est ni une réplication ni une sauvegarde indépendante.

2. Séparer datastore et système si possible; prévoir une copie hors site ou hors ligne.
   👉 Explication : protège contre la perte du serveur.

3. Vérifier DNS, NTP et compatibilité des versions PVE/PBS. Sur un hôte PVE existant :
   ```bash
   pveversion
   timedatectl status
   ```
   👉 Explication : affiche la version PVE et l'état de l'heure.

4. Appliquer une version PBS encore supportée et lire les notes de mise à jour actuelles.
   👉 Explication : les références `3.x` sont historiques.

5. Protéger le serveur et le réseau d'administration.
   👉 Explication : PBS contient l'ensemble des sauvegardes.

## 2. Production — Contrôles

Valider capacité, copie hors site et règles réseau avant l'installation.

## 3. Production — Sécurité

- Réseau d'administration dédié et filtré.

## Validation et retour arrière

- **Validation** : dimensionnement validé, versions compatibles et DNS/NTP corrects.
- **Retour arrière** : aucune modification n'est faite par cette fiche; rien à annuler.

## Si le problème n'est pas résolu

- [Proxmox — matrice de versions](https://pbs.proxmox.com/docs/installation.html)
- [Proxmox Backup Server — documentation](https://pbs.proxmox.com/docs/)
- [Guide complet](/02-fiches-completes/proxmox/toutes-versions/autres/12-proxmox-backup-server-3x-pbs-deduplication#1-preparer-linfrastructure)
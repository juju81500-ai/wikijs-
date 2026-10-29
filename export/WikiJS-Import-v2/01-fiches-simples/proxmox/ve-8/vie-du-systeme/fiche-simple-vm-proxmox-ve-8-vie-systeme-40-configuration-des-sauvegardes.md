---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 40 Configuration Des Sauvegardes"
description: "Planifier la sauvegarde des VM et de l'hôte vers Proxmox Backup Server."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-40"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_40_Configuration_Des_Sauvegardes

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 40 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-40`

---

## Problème précis à résoudre

Planifier la sauvegarde des VM et de l'hôte vers Proxmox Backup Server.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Datacenter > Storage > Add > Proxmox Backup Server** (serveur, datastore, utilisateur, empreinte) puis **Datacenter > Backup > Add** (sélection des VM, planning, rétention). En ligne de commande :
   ```bash
   pvesm add pbs PBS --server IP_PBS --datastore DATASTORE --username sauvegarde@pbs --password --fingerprint EMPREINTE
   pvesh create /cluster/backup --vmid 100,101 --storage PBS --schedule '02:00' --mode snapshot --prune-backups keep-daily=7,keep-weekly=4
   ```
   👉 Explication : `IP_PBS` = serveur PBS, `DATASTORE` = datastore, `EMPREINTE` = empreinte SHA-256 du certificat PBS; la commande demande le mot de passe; mode `snapshot` sans arrêt de la VM.

2. Lancer une sauvegarde immédiate :
   ```bash
   vzdump 100 --storage PBS --mode snapshot
   ```
   👉 Explication : `100` = VMID; vérifie le circuit complet.

3. Sauvegarder aussi la configuration de l'hôte (`/etc/pve`, `/etc/network`) par un script planifié vers un stockage distant.
   ```bash
   tar czf /mnt/sauvegarde/pve-config-$(date +%F).tgz /etc/pve /etc/network /etc/hosts
   ```
   👉 Explication : les sauvegardes de VM ne contiennent pas la configuration de l'hôte.

## 2. Production — Contrôles

Règle 3-2-1; chiffrer côté client PBS; copie hors site.

## 3. Production — Sécurité

Chiffrement des sauvegardes (clé conservée hors de l'hôte); compte PBS limité.

## Validation et retour arrière

- **Validation** : La sauvegarde apparaît dans PBS et la tâche se termine en `OK`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Hote Proxmox VE 8 Cluster Maintenance](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-maintenance>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
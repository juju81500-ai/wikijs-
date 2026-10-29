---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 13 Partitionnement Et Systemes De"
description: "Choisir le disque d'installation et créer le datastore."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-13"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-13`

---

## Problème précis à résoudre

Choisir le disque d'installation et créer le datastore.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : choisir le disque système (M.2/SD/SSD de 32 Go minimum, idéalement un volume RAID1). Le reste du disque peut servir de datastore VMFS.
   👉 Explication : ESXi partitionne le disque automatiquement (boot, système, scratch, VMFS).

2. Host Client : **Stockage > Datastores > Nouveau datastore > Créer un datastore VMFS**. En ligne de commande :
   ```sh
   esxcli storage core device list | grep -E 'Display Name|Size'
   esxcli storage filesystem list
   vmkfstools -V
   ```
   👉 Explication : repérer le disque (`naa.XXXX`) puis le formater; le Host Client est plus sûr pour la création.

3. Prévoir un disque séparé pour les VM, distinct du disque d'amorçage.
   👉 Explication : évite un datastore saturé qui bloque l'hôte.

## 2. Production — Contrôles

Documenter les datastores (nom, taille, usage).

## 3. Production — Sécurité

Ne pas dépasser 80 % d'occupation.

## Validation et retour arrière

- **Validation** : `esxcli storage filesystem list` montre le datastore monté.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
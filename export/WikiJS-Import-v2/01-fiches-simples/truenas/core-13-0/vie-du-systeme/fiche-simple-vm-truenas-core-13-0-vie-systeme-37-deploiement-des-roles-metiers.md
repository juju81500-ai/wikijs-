---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 37 Deploiement Des Roles Metiers"
description: "Créer pool et partages."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-37"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-37`

---

## Problème précis à résoudre

Créer pool et partages.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le pool : GUI Stockage > Pools > Ajouter (nom, disposition, disques).
   ```sh
   zpool create -o ashift=12 POOL raidz2 da1 da2 da3 da4 da5 da6
   zpool status POOL
   ```
   👉 Explication : RAIDZ2 sur six disques ; da1 à da6 sont les disques de données (créer par GUI en pratique).

2. Créer un dataset et un zvol : GUI Stockage > Pools > Ajouter un jeu de données / Ajouter un zvol.
   ```sh
   zfs create POOL/DONNEES
   zfs create -V 100G POOL/VOL_ISCSI
   ```
   👉 Explication : dataset de fichiers et volume bloc pour iSCSI.

3. Créer le partage : GUI Partage > Windows Shares (SMB) > Ajouter ; Unix Shares (NFS) ; Block Shares (iSCSI).
   ```sh
   midclt call sharing.smb.create '{"path": "/mnt/POOL/DONNEES", "name": "DONNEES"}'
   service samba_server status
   ```
   👉 Explication : publie le dataset en SMB.

## 2. Production — Contrôles

Un dataset par usage avec quotas.

## 3. Production — Sécurité

Ne pas partager la racine du pool.

## Validation et retour arrière

- **Validation** : Le partage est accessible depuis un client.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 40 Configuration Des Sauvegardes"
description: "Sauvegarder les VM et la configuration de l'hôte."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-40"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_40_Configuration_Des_Sauvegardes

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 40 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-40`

---

## Problème précis à résoudre

Sauvegarder les VM et la configuration de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Configuration de l'hôte : sauvegarde de configuration (`configBundle`) :
   ```sh
   vim-cmd hostsvc/firmware/sync_config
   vim-cmd hostsvc/firmware/backup_config
   ```
   👉 Explication : affiche l'URL de téléchargement de l'archive; la copier hors de l'hôte.

2. Sauvegarde des VM : utiliser Veeam Backup & Replication (console Veeam : **Inventory > Add Server > VMware vSphere**, puis **Home > Backup Job > Virtual machine**), ou un snapshot ponctuel :
   ```sh
   vim-cmd vmsvc/snapshot.create VMID AVANT_CHANGEMENT 'avant maintenance' 0 0
   vim-cmd vmsvc/snapshot.get VMID
   ```
   👉 Explication : `VMID` = numéro de la VM; le snapshot n'est pas une sauvegarde et ne doit pas rester plus de quelques jours.

3. Restaurer la configuration en cas de besoin :
   ```sh
   vim-cmd hostsvc/firmware/restore_config /tmp/configBundle.tgz
   ```
   👉 Explication : l'hôte redémarre; le build doit être identique à celui de la sauvegarde.

## 2. Production — Contrôles

Règle 3-2-1; Veeam avec vCenter (accès aux API de sauvegarde).

## 3. Production — Sécurité

Compte de sauvegarde en rôle minimal; sauvegardes chiffrées.

## Validation et retour arrière

- **Validation** : La tâche de sauvegarde se termine en succès et l'archive de configuration est hors de l'hôte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
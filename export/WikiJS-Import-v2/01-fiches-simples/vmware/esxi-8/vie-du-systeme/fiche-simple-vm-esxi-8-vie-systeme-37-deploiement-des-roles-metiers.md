---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 37 Deploiement Des Roles Metiers"
description: "Créer réseaux, datastores et premières VM."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-37"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-37`

---

## Problème précis à résoudre

Créer réseaux, datastores et premières VM.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un groupe de ports (Host Client : **Réseau > Groupes de ports > Ajouter un groupe de ports**) :
   ```sh
   esxcli network vswitch standard portgroup add -p NOM_GP -v vSwitch0
   esxcli network vswitch standard portgroup set -p NOM_GP --vlan-id ID_VLAN
   ```
   👉 Explication : `NOM_GP` = nom du groupe de ports; `ID_VLAN` = VLAN.

2. Créer une VM (Host Client : **Machines virtuelles > Créer/enregistrer une VM**) et la lister :
   ```sh
   vim-cmd vmsvc/getallvms
   vim-cmd vmsvc/power.getstate VMID
   ```
   👉 Explication : `VMID` = numéro de la VM; la création se fait de préférence par le Host Client ou vCenter.

3. Ajouter l'hôte à vCenter pour les fonctions avancées (vMotion, HA, DRS) (vSphere Client : **Centre de données > Ajouter un hôte**).
   👉 Explication : vCenter est nécessaire pour la gestion de plusieurs hôtes.

## 2. Production — Contrôles

Réserver une convention de nommage pour VM et groupes de ports.

## 3. Production — Sécurité

Isoler les VM par VLAN.

## Validation et retour arrière

- **Validation** : Une VM de test démarre.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
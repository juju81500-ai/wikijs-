---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 05 Configuration Materielle Firmware"
description: "Préparer BIOS et contrôleurs pour ZFS."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-05"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_05_Configuration_Materielle_Firmware

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 05 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-05`

---

## Problème précis à résoudre

Préparer BIOS et contrôleurs pour ZFS.

## 1. Hors-Production (Lab / Test / POC)

1. Activer UEFI ou BIOS selon le support, mettre à jour BIOS et BMC.
   👉 Explication : menu BIOS/UEFI > Boot.

2. Passer le contrôleur en mode HBA/IT, sans RAID matériel :
   ```sh
   pciconf -lv | grep -i -B3 -E 'sas|raid'
   sas2flash -listall
   ```
   👉 Explication : ZFS doit voir les disques bruts ; `sas2flash` ou `sas3flash` selon le contrôleur LSI.

3. Vérifier les disques et leurs numéros de série :
   ```sh
   camcontrol devlist
   geom disk list | grep -E 'Name|ident'
   ```
   👉 Explication : le numéro de série sert au remplacement.

## 2. Production — Contrôles

Ne jamais utiliser de RAID matériel avec ZFS ; mettre à jour le firmware en maintenance.

## 3. Production — Sécurité

Protéger BIOS et BMC par mot de passe, BMC sur VLAN d'administration.

## Validation et retour arrière

- **Validation** : Tous les disques sont visibles sans RAID.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
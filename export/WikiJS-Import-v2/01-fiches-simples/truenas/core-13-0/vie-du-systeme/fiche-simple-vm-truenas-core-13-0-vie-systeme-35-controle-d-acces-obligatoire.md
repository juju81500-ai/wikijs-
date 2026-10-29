---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 35 Controle D Acces Obligatoire"
description: "Contrôle d'accès obligatoire : sans objet sur FreeBSD."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-35"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_35_Controle_D_Acces_Obligatoire

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-35`

---

## Problème précis à résoudre

Contrôle d'accès obligatoire : sans objet sur FreeBSD.

## 1. Hors-Production (Lab / Test / POC)

1. Constater l'absence de SELinux et AppArmor :
   ```sh
   uname -sr
   getenforce 2>&1
   ```
   👉 Explication : la commande est inconnue sous FreeBSD : normal.

2. Utiliser les ACL ZFS et l'isolation par dataset : GUI Stockage > Pools > Modifier les permissions.
   ```sh
   zfs get acltype POOL/DATASET
   ```
   👉 Explication : les ACL contrôlent l'accès.

## 2. Production — Contrôles

Documenter que le MAC n'est pas applicable.

## 3. Production — Sécurité

Compenser par ACL strictes.

## Validation et retour arrière

- **Validation** : ACL conformes.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
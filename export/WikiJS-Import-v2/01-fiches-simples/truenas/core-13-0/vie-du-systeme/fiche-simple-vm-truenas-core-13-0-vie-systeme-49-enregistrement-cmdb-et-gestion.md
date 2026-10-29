---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 49 Enregistrement Cmdb Et Gestion"
description: "Inventorier le NAS."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-49"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-49`

---

## Problème précis à résoudre

Inventorier le NAS.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les informations :
   ```sh
   midclt call system.info | grep -E 'hostname|version|serial|physmem'
   midclt call disk.query | grep -E 'serial|model'
   ```
   👉 Explication : version, mémoire et disques.

2. Saisir en CMDB : nom, IP, version, pools, partages, propriétaire, support, fin de vie de CORE.
   👉 Explication : permet l'astreinte et le suivi.

## 2. Production — Contrôles

Revue annuelle des accès.

## 3. Production — Sécurité

Retirer les anciens administrateurs.

## Validation et retour arrière

- **Validation** : NAS présent en CMDB.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
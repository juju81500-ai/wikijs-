---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 49 Enregistrement Cmdb Et Gestion"
description: "Inventorier le NAS."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-49"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-49`

---

## Problème précis à résoudre

Inventorier le NAS.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les informations à saisir :
   ```bash
   sudo midclt call system.info | python3 -m json.tool | grep -E 'hostname|version|serial|physmem'
   sudo midclt call disk.query | grep -E 'serial|model'
   ```
   👉 Explication : version, mémoire et disques avec leur numéro de série.

2. Saisir dans la CMDB : nom, IP, version, pools, partages, propriétaire, contrat de support, date de mise à jour.
   👉 Explication : permet l'astreinte et le suivi du cycle de vie.

## 2. Production — Contrôles

Revue annuelle des accès et des partages.

## 3. Production — Sécurité

Retirer les comptes d'anciens administrateurs.

## Validation et retour arrière

- **Validation** : NAS présent dans la CMDB.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
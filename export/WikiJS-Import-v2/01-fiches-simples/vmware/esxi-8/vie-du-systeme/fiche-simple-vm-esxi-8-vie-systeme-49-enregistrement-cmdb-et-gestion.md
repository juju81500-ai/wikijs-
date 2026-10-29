---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 49 Enregistrement Cmdb Et Gestion"
description: "Inscrire l'hôte dans l'inventaire et revoir les accès."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-49"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-49`

---

## Problème précis à résoudre

Inscrire l'hôte dans l'inventaire et revoir les accès.

## 1. Hors-Production (Lab / Test / POC)

1. Collecter les informations à enregistrer :
   ```sh
   esxcli system hostname get
   esxcli system version get
   esxcli hardware platform get
   esxcli network ip interface ipv4 get
   ```
   👉 Explication : nom, version, numéro de série et IP : à saisir dans la CMDB.

2. Lister les comptes et droits :
   ```sh
   esxcli system account list
   esxcli system permission list
   ```
   👉 Explication : à comparer à la liste des personnes autorisées.

3. Associer l'hôte à un responsable, une criticité et un contrat de support.
   👉 Explication : permet d'escalader en cas d'incident.

## 2. Production — Contrôles

Revue des accès au moins trimestrielle.

## 3. Production — Sécurité

Supprimer les comptes inutilisés (`esxcli system account remove -i ADMIN1`).

## Validation et retour arrière

- **Validation** : La fiche CMDB existe et correspond à l'hôte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 33 Securisation Des Systemes De"
description: "Protéger les datastores et les accès."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-33"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-33`

---

## Problème précis à résoudre

Protéger les datastores et les accès.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les datastores et leurs types :
   ```sh
   esxcli storage filesystem list
   esxcli storage nfs list
   ```
   👉 Explication : contrôler les montages NFS (préférer NFSv4.1 avec Kerberos).

2. Monter un datastore NFS restreint (Host Client : **Stockage > Datastores > Nouveau datastore > Monter un datastore NFS**) :
   ```sh
   esxcli storage nfs41 add -H IP_NFS -s /EXPORT -v NOM_DS
   ```
   👉 Explication : `IP_NFS` = serveur NFS; `/EXPORT` = chemin; `NOM_DS` = nom du datastore.

3. Limiter l'export côté serveur aux IP des hôtes ESXi uniquement.
   👉 Explication : empêche l'accès non autorisé au stockage.

## 2. Production — Contrôles

Documenter qui accède à chaque datastore.

## 3. Production — Sécurité

Isoler le réseau de stockage dans un VLAN dédié.

## Validation et retour arrière

- **Validation** : Les datastores sont montés et accessibles.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
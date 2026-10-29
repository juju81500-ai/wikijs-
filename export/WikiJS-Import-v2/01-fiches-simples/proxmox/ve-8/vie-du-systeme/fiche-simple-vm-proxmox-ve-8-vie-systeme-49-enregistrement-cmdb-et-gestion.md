---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 49 Enregistrement Cmdb Et Gestion"
description: "Inscrire l'hôte dans l'inventaire et revoir les accès."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-49"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-49`

---

## Problème précis à résoudre

Inscrire l'hôte dans l'inventaire et revoir les accès.

## 1. Hors-Production (Lab / Test / POC)

1. Collecter les informations à enregistrer :
   ```bash
   hostname -f
   pveversion
   dmidecode -s system-serial-number
   ip -br a
   ```
   👉 Explication : nom, version, numéro de série et IP : à saisir dans la CMDB.

2. Lister les comptes et droits Proxmox (GUI : **Datacenter > Permissions**) :
   ```bash
   pveum user list
   pveum acl list
   pveum user token list ADMIN1@pve
   ```
   👉 Explication : à comparer à la liste des personnes autorisées.

3. Associer l'hôte à un responsable, une criticité et un contrat de support (abonnement).
   👉 Explication : permet d'escalader en cas d'incident.

## 2. Production — Contrôles

Revue des accès au moins trimestrielle.

## 3. Production — Sécurité

Supprimer les comptes inutilisés (`pveum user delete`).

## Validation et retour arrière

- **Validation** : La fiche CMDB existe et correspond à l'hôte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
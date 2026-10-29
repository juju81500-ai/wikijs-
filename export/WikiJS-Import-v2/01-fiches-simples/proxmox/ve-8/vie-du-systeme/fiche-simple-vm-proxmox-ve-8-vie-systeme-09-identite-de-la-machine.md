---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 09 Identite De La Machine"
description: "Nommer l'hôte avec un FQDN résolvable (obligatoire sous Proxmox)."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-09"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Nommer l'hôte avec un FQDN résolvable (obligatoire sous Proxmox).

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : champ **Hostname (FQDN)** (par exemple `pve01.domaine.local`).
   👉 Explication : le FQDN doit se résoudre vers l'IP de gestion, sinon les services Proxmox échouent.

2. Après installation, contrôler :
   ```bash
   hostname -f
   getent hosts $(hostname -f)
   cat /etc/hosts
   ```
   👉 Explication : le FQDN doit pointer vers `IP_HOTE`, pas vers 127.0.1.1.

3. Ne pas renommer un nœud après sa création : réinstaller si le nom est faux (GUI : l'interface ne permet pas de renommer).
   👉 Explication : le nom est inscrit dans `/etc/pve` et dans le cluster.

## 2. Production — Contrôles

Nom conforme à la convention de nommage et déclaré dans le DNS (A et PTR).

## 3. Production — Sécurité

Un nom explicite simplifie l'audit.

## Validation et retour arrière

- **Validation** : `hostname -f` renvoie le FQDN attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Hote Proxmox VE 8 Cluster Preparer](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-preparer>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 32 Automatisation Des Correctifs De"
description: "Être averti des mises à jour sans les installer automatiquement."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-32"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-32`

---

## Problème précis à résoudre

Être averti des mises à jour sans les installer automatiquement.

## 1. Hors-Production (Lab / Test / POC)

1. Proxmox envoie un e-mail quand des mises à jour existent (GUI : **Datacenter > Notifications** ou **Nœud > System > Notifications**). Contrôler la messagerie :
   ```bash
   echo test | mail -s 'test pve' ADMIN_MAIL
   mailq
   ```
   👉 Explication : `ADMIN_MAIL` = adresse reçue par l'équipe; configure Postfix en relais si nécessaire.

2. Lister les mises à jour disponibles :
   ```bash
   apt update
   apt list --upgradable
   ```
   👉 Explication : liste ce qui est à installer.

3. Ne pas activer `unattended-upgrades` sur un hôte de cluster : planifier les mises à jour nœud par nœud en fenêtre de maintenance.
   👉 Explication : une mise à jour automatique peut redémarrer des services ou casser un cluster.

## 2. Production — Contrôles

Fenêtre mensuelle de maintenance avec migration des VM.

## 3. Production — Sécurité

Suivre les bulletins de sécurité Proxmox et Debian.

## Validation et retour arrière

- **Validation** : L'e-mail de notification est reçu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
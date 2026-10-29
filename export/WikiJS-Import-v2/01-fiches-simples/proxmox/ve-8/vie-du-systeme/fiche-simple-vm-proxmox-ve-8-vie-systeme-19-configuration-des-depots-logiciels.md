---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 19 Configuration Des Depots Logiciels"
description: "Choisir les dépôts Enterprise ou No-Subscription."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-19"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-19`

---

## Problème précis à résoudre

Choisir les dépôts Enterprise ou No-Subscription.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Nœud > Updates > Repositories** : désactiver `pve-enterprise` si pas d'abonnement, puis **Add > No-Subscription**. En ligne de commande (Debian 12 = `bookworm`) :
   ```bash
   cat /etc/apt/sources.list.d/pve-enterprise.list
   echo 'deb http://download.proxmox.com/debian/pve bookworm pve-no-subscription' > /etc/apt/sources.list.d/pve-no-subscription.list
   apt update
   ```
   👉 Explication : sans abonnement, le dépôt Enterprise renvoie une erreur 401; le dépôt No-Subscription convient au lab.

2. Contrôler les sources actives :
   ```bash
   apt-cache policy | grep -i proxmox
   ```
   👉 Explication : affiche les dépôts Proxmox actifs.

3. En production, souscrire à l'abonnement et utiliser le dépôt Enterprise (GUI : **Nœud > Subscription > Upload Subscription Key**).
   👉 Explication : dépôt plus testé et support officiel.

## 2. Production — Contrôles

Dépôt Enterprise pour la production; No-Subscription pour le lab.

## 3. Production — Sécurité

N'ajouter aucun dépôt tiers non validé.

## Validation et retour arrière

- **Validation** : `apt update` sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
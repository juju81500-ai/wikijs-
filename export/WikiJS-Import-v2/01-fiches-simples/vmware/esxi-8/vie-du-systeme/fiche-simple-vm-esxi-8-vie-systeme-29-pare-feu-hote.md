---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 29 Pare Feu Hote"
description: "Filtrer l'accès aux services de l'hôte."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-29"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-29`

---

## Problème précis à résoudre

Filtrer l'accès aux services de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Réseau > Règles de pare-feu** (ou **Gérer > Sécurité > Pare-feu**). En ligne de commande :
   ```sh
   esxcli network firewall get
   esxcli network firewall ruleset list
   esxcli network firewall ruleset allowedip add -r sshServer -i RESEAU_ADMIN
   ```
   👉 Explication : `RESEAU_ADMIN` = réseau d'administration (CIDR); limite SSH à ces adresses.

2. Désactiver les ensembles de règles inutiles :
   ```sh
   esxcli network firewall ruleset set -r ntpClient -e true
   esxcli network firewall ruleset set -r NOM_REGLE -e false
   ```
   👉 Explication : `NOM_REGLE` = ensemble non nécessaire.

3. Activer le pare-feu s'il est désactivé :
   ```sh
   esxcli network firewall set --enabled true
   ```
   👉 Explication : le pare-feu doit rester `Enabled: true`.

## 2. Production — Contrôles

Autoriser seulement vCenter, NTP, DNS et SSH temporaire.

## 3. Production — Sécurité

Politique par défaut : refuser en entrée.

## Validation et retour arrière

- **Validation** : Le Host Client n'est joignable que depuis le réseau d'administration.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
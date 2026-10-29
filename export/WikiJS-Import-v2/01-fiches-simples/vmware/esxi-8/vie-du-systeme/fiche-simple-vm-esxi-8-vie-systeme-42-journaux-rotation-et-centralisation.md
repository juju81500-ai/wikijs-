---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 42 Journaux Rotation Et Centralisation"
description: "Conserver et centraliser les journaux."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-42"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_42_Journaux_Rotation_Et_Centralisation

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-42`

---

## Problème précis à résoudre

Conserver et centraliser les journaux.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Gérer > Système > Syslog avancé**. En ligne de commande (remplacer `IP_SYSLOG`) :
   ```sh
   esxcli system syslog config set --loghost='tcp://IP_SYSLOG:514' --logdir=/vmfs/volumes/DATASTORE/logs --default-rotate=20 --default-size=1024
   esxcli system syslog reload
   esxcli network firewall ruleset set -r syslog -e true
   ```
   👉 Explication : envoie les journaux au serveur central et les conserve sur un datastore (le disque de démarrage est volatil).

2. Contrôler la configuration :
   ```sh
   esxcli system syslog config get
   ls /var/log/
   ```
   👉 Explication : principaux journaux : `hostd.log`, `vmkernel.log`, `vpxa.log`, `auth.log`.

3. Consulter les événements (Host Client : **Hôte > Surveiller > Journaux**).
   ```sh
   tail -50 /var/log/hostd.log
   ```
   👉 Explication : dernières lignes du journal de gestion.

## 2. Production — Contrôles

Conserver les journaux selon la politique (90 jours minimum).

## 3. Production — Sécurité

Journaux en lecture seule pour les non-administrateurs.

## Validation et retour arrière

- **Validation** : Les événements de l'hôte arrivent sur le serveur central.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
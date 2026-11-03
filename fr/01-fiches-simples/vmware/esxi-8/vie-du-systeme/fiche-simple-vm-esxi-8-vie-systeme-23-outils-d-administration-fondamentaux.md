---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 23 Outils D Administration Fondamentaux"
description: "Disposer des outils de diagnostic de base."
published: true
date: 2026-11-03T14:22:28Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-23"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_23_Outils_D_Administration_Fondamentaux

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 23 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-23`

---

## Problème précis à résoudre

Disposer des outils de diagnostic de base.

## 1. Hors-Production (Lab / Test / POC)

1. Activer [[Glossary:SSH]] le temps de l'intervention (Host Client : **Gérer > Services > TSM-SSH > Démarrer**; ESXi Shell : **TSM**) :
   ```sh
   vim-cmd hostsvc/enable_ssh
   vim-cmd hostsvc/start_ssh
   esxcli system services list 2>/dev/null | head
   ```
   👉 Explication : SSH est désactivé par défaut; ne l'activer que pendant les interventions.

2. Utiliser les outils intégrés :
   ```sh
   esxtop
   esxcli --help
   vim-cmd vmsvc/getallvms
   esxcfg-nics -l
   esxcfg-vmknic -l
   ```
   👉 Explication : `esxtop` mesure [[Glossary:CPU]]/RAM/disque/réseau; `esxcfg-*` listent cartes et interfaces.

3. Arrêter SSH après l'intervention :
   ```sh
   vim-cmd hostsvc/stop_ssh
   vim-cmd hostsvc/disable_ssh
   ```
   👉 Explication : réduit l'exposition.

## 2. Production — Contrôles

Procédure d'activation temporaire de SSH documentée.

## 3. Production — Sécurité

SSH activé = alerte attendue; le refermer dès que possible.

## Validation et retour arrière

- **Validation** : `vim-cmd vmsvc/getallvms` liste les [[Glossary:VM]].
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire VMware ESXi 8](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
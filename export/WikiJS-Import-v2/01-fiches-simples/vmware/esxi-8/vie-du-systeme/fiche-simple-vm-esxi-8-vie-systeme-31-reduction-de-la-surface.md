---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 31 Reduction De La Surface"
description: "Désactiver ce qui n'est pas utile."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-31"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-31`

---

## Problème précis à résoudre

Désactiver ce qui n'est pas utile.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les services en écoute et leur état (Host Client : **Gérer > Services**) :
   ```sh
   esxcli network ip connection list | grep LISTEN
   chkconfig --list 2>/dev/null | head -30
   ```
   👉 Explication : identifie les ports ouverts.

2. Arrêter les services inutiles (SLP, SNMP si non utilisé) :
   ```sh
   /etc/init.d/slpd stop
   chkconfig slpd off
   esxcli system snmp set --enable false
   ```
   👉 Explication : SLP est vulnérable et rarement utile; SNMP seulement s'il est supervisé.

3. Désactiver le MOB et les accès invités non nécessaires (voir étape 24).
   👉 Explication : moins d'interfaces exposées.

## 2. Production — Contrôles

Liste des services autorisés documentée.

## 3. Production — Sécurité

Chaque service ouvert doit avoir un propriétaire.

## Validation et retour arrière

- **Validation** : Seuls les services attendus sont démarrés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
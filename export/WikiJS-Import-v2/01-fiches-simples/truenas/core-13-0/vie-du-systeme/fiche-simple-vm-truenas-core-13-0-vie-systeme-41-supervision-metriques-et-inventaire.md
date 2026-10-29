---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 41 Supervision Metriques Et Inventaire"
description: "Surveiller l'état du NAS."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-41"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 41 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-41`

---

## Problème précis à résoudre

Surveiller l'état du NAS.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Tableau de bord, Rapports (CPU, ARC, réseau, disques) et Alertes.
   ```sh
   zpool status -x
   zpool list -o name,size,alloc,free,cap,health
   ```
   👉 Explication : état et occupation.

2. SNMP : Services > SNMP.
   ```sh
   midclt call service.update snmp '{"enable": true}'
   snmpwalk -v2c -c COMMUNAUTE ADRESSE_NAS 1.3.6.1.2.1.1
   ```
   👉 Explication : COMMUNAUTE est la chaîne de lecture.

3. E-mail d'alertes : Système > E-mail.
   ```sh
   midclt call mail.config | head
   ```
   👉 Explication : SMTP configuré.

## 2. Production — Contrôles

Alerter à 70 % d'occupation et à toute erreur disque.

## 3. Production — Sécurité

SNMPv3 de préférence ; pas de `public`.

## Validation et retour arrière

- **Validation** : Les métriques remontent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
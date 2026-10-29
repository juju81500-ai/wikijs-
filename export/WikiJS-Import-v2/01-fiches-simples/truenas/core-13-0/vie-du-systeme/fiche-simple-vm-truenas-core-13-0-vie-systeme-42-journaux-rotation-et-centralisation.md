---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 42 Journaux Rotation Et Centralisation"
description: "Conserver et centraliser les journaux."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-42"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_42_Journaux_Rotation_Et_Centralisation

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-42`

---

## Problème précis à résoudre

Conserver et centraliser les journaux.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Avancé > Serveur Syslog.
   ```sh
   midclt call system.advanced.update '{"syslogserver": "SERVEUR_LOG", "syslog_transport": "TLS"}'
   ```
   👉 Explication : SERVEUR_LOG est le collecteur central.

2. Consulter :
   ```sh
   tail -n 50 /var/log/messages
   tail -n 50 /var/log/middlewared.log
   ```
   👉 Explication : événements récents.

## 2. Production — Contrôles

Conserver 90 jours minimum.

## 3. Production — Sécurité

Chiffrer le transport ; limiter l'accès.

## Validation et retour arrière

- **Validation** : Les événements arrivent au collecteur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
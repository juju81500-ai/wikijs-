---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 22 Synchronisation Horaire Ntp"
description: "Garder l'heure exacte (indispensable pour Kerberos et AD)."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-22"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-22`

---

## Problème précis à résoudre

Garder l'heure exacte (indispensable pour Kerberos et AD).

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Général > Serveurs NTP > Ajouter (serveur interne ou pool).
   ```bash
   sudo midclt call system.ntpserver.create '{"address": "SERVEUR_NTP", "prefer": true}'
   ```
   👉 Explication : SERVEUR_NTP est le serveur de temps interne.

2. Vérifier la synchronisation :
   ```bash
   chronyc sources -v
   timedatectl
   ```
   👉 Explication : une source marquée `*` et `System clock synchronized: yes`.

## 2. Production — Contrôles

Au moins deux sources de temps.

## 3. Production — Sécurité

Limiter l'accès NTP aux réseaux internes.

## Validation et retour arrière

- **Validation** : `chronyc sources` montre une source sélectionnée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 17 Resolution De Noms Client"
description: "Configurer les serveurs DNS."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-17"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-17`

---

## Problème précis à résoudre

Configurer les serveurs DNS.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Réseau > Configuration globale > Serveur DNS 1 à 3.
   ```sh
   midclt call network.configuration.update '{"nameserver1": "DNS1", "nameserver2": "DNS2"}'
   ```
   👉 Explication : DNS1 et DNS2 sont les serveurs internes.

2. Tester :
   ```sh
   host truenas.com
   cat /etc/resolv.conf
   ```
   👉 Explication : résolution fonctionnelle.

## 2. Production — Contrôles

Deux DNS internes.

## 3. Production — Sécurité

Ne pas éditer `/etc/resolv.conf` à la main.

## Validation et retour arrière

- **Validation** : `host` répond.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
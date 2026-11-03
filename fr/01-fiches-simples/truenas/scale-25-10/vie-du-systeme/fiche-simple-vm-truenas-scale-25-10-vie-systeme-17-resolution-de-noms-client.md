---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 17 Resolution De Noms Client"
description: "Configurer les serveurs [[Glossary:DNS]]."
published: true
date: 2026-11-03T14:22:28Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-17"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-17`

---

## Problème précis à résoudre

Configurer les serveurs [[Glossary:DNS]].

## 1. Hors-Production (Lab / Test / POC)

1. [[Glossary:GUI]] : Réseau > Paramètres globaux > Serveurs DNS 1 à 3.
   ```bash
   sudo midclt call network.configuration.update '{"nameserver1": "DNS1", "nameserver2": "DNS2"}'
   ```
   👉 Explication : DNS1 et DNS2 sont les serveurs internes.

2. Tester :
   ```bash
   getent hosts truenas.com
   cat /etc/resolv.conf
   ```
   👉 Explication : résolution réussie ; le fichier est géré par TrueNAS.

## 2. Production — Contrôles

Deux DNS internes, jamais un seul.

## 3. Production — Sécurité

Ne pas éditer `/etc/resolv.conf` à la main.

## Validation et retour arrière

- **Validation** : `getent hosts` renvoie une adresse.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/fr/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 08 Configuration Reseau D Installation"
description: "Donner une adresse au NAS pour atteindre l'interface web."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-08"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-08`

---

## Problème précis à résoudre

Donner une adresse au NAS pour atteindre l'interface web.

## 1. Hors-Production (Lab / Test / POC)

1. Au premier démarrage, le menu de la console propose `1) Configure Network Interfaces` ; saisir adresse, masque, passerelle.
   👉 Explication : ou laisser DHCP puis fixer l'adresse à l'étape 16.

2. Contrôler :
   ```sh
   ifconfig
   netstat -rn
   ```
   👉 Explication : adresse et route par défaut.

3. Tester :
   ```sh
   ping -c 3 PASSERELLE
   ```
   👉 Explication : PASSERELLE est l'adresse du routeur.

## 2. Production — Contrôles

Utiliser une adresse fixe réservée.

## 3. Production — Sécurité

Réseau d'administration séparé du réseau de données.

## Validation et retour arrière

- **Validation** : L'interface web répond sur http://ADRESSE_NAS.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
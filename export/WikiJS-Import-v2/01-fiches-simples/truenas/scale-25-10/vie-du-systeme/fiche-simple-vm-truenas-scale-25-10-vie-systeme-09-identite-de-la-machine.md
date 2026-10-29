---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 09 Identite De La Machine"
description: "Nommer le NAS de façon cohérente avec le DNS."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-09"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Nommer le NAS de façon cohérente avec le DNS.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Réseau > Paramètres globaux > Nom d'hôte, Nom de domaine.
   ```bash
   sudo midclt call network.configuration.update '{"hostname": "NOM_NAS", "domain": "EXEMPLE.LOCAL"}'
   ```
   👉 Explication : NOM_NAS suit la convention de nommage ; EXEMPLE.LOCAL est le domaine interne.

2. Vérifier :
   ```bash
   hostname
   hostname -f
   ```
   👉 Explication : affiche le nom court puis le nom complet.

## 2. Production — Contrôles

Créer l'enregistrement DNS A et PTR correspondant.

## 3. Production — Sécurité

Ne pas utiliser de nom révélant le contenu des données.

## Validation et retour arrière

- **Validation** : `hostname -f` renvoie le FQDN attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
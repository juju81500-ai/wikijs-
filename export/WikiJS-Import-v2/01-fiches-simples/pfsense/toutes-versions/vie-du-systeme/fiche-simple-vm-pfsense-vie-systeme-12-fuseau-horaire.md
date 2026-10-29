---
title: "Fiche Simple - VM pfSense Vie Systeme 12 Fuseau Horaire"
description: "Régler le fuseau pour des journaux datés correctement."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-12"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-12`

---

## Problème précis à résoudre

Régler le fuseau pour des journaux datés correctement.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'assistant (étape 2) ou System > General Setup > Timezone, choisir `Europe/Paris`, puis Save.
   👉 Explication : tous les journaux et tâches planifiées utilisent ce fuseau.

2. Contrôler en shell :
   ```sh
   date
   grep '<timezone>' /cf/conf/config.xml
   ```
   👉 Explication : doit afficher l'heure locale et `Europe/Paris`.

## 2. Production — Contrôles

Utiliser le même fuseau (ou UTC) sur tous les équipements pour la corrélation.

## 3. Production — Sécurité

Un fuseau erroné fausse les journaux utilisés comme preuve.

## Validation et retour arrière

- **Validation** : `date` affiche l'heure locale correcte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
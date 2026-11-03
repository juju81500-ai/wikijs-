---
title: "Fiche Simple - VM OPNsense Vie Systeme 09 Identite De La Machine"
description: "Donner un nom et un domaine cohérents au pare-feu."
published: true
date: 2026-11-03T14:22:28Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-09"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : Pare-feu OPNsense ([[Glossary:VM]] ou matériel)
- **OS / Version** : OPNsense; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Donner un nom et un domaine cohérents au pare-feu.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Système > Paramètres > Général et renseigner Nom d'hôte (ex. `fw01`) et Domaine (ex. `exemple.lan`), puis Enregistrer.
   👉 Explication : le nom complet devient `fw01.exemple.lan` ([[Glossary:FQDN]]).

2. Ou en console (option 8) : contrôler le nom appliqué :
   ```sh
   hostname
   grep -E '<hostname>|<domain>' /conf/config.xml
   ```
   👉 Explication : affiche le nom court et le domaine stockés dans la configuration.

3. Créer l'enregistrement [[Glossary:DNS]] correspondant dans l'annuaire DNS interne.
   👉 Explication : permet d'administrer le pare-feu par son nom.

## 2. Production — Contrôles

Respecter la convention de nommage de l'entreprise et la déclarer dans la [[Glossary:CMDB]].

## 3. Production — Sécurité

Ne pas utiliser un domaine public que l'on ne possède pas.

## Validation et retour arrière

- **Validation** : `hostname` renvoie le nom attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire OPNsense](/fr/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)
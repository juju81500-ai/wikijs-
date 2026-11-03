---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 09 Identite De La Machine"
description: "Nommer le [[Glossary:NAS]] de façon cohérente avec le [[Glossary:DNS]]."
published: true
date: 2026-11-03T14:22:28Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-09"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Nommer le [[Glossary:NAS]] de façon cohérente avec le [[Glossary:DNS]].

## 1. Hors-Production (Lab / Test / POC)

1. [[Glossary:GUI]] : Réseau > Configuration globale > Nom d'hôte et Domaine.
   ```sh
   midclt call network.configuration.update '{"hostname": "NOM_NAS", "domain": "EXEMPLE.LOCAL"}'
   ```
   👉 Explication : NOM_NAS suit la convention ; EXEMPLE.LOCAL est le domaine interne.

2. Vérifier :
   ```sh
   hostname
   ```
   👉 Explication : nom enregistré.

## 2. Production — Contrôles

Créer les enregistrements DNS A et PTR.

## 3. Production — Sécurité

Pas de nom révélant le contenu.

## Validation et retour arrière

- **Validation** : `hostname` renvoie le [[Glossary:FQDN]] attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/fr/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
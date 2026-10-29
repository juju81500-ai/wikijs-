---
title: "Fiche Simple - VM OPNsense Vie Systeme 25 Validation De L Etat"
description: "Capturer l'état de référence du pare-feu neuf."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-25"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-25`

---

## Problème précis à résoudre

Capturer l'état de référence du pare-feu neuf.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter la configuration : Système > Configuration > Sauvegardes > Télécharger la configuration (cocher le chiffrement).
   👉 Explication : fichier `config-FW01-DATE.xml` qui sert de référence.

2. Relever les informations de référence en shell :
   ```sh
   opnsense-version -v
   sysctl hw.ncpu hw.physmem
   ifconfig -l
   pfctl -si | head -5
   sha256 /conf/config.xml
   ```
   👉 Explication : versions, ressources, interfaces, état du pare-feu et empreinte de la configuration.

## 2. Production — Contrôles

Archiver la baseline avec le dossier du projet.

## 3. Production — Sécurité

Chiffrer le fichier de configuration car il contient des secrets.

## Validation et retour arrière

- **Validation** : Baseline enregistrée et configuration exportée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)
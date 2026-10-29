---
title: "Fiche Simple - VM OPNsense Vie Systeme 19 Configuration Des Depots Logiciels"
description: "Choisir le miroir et la branche des mises à jour."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-19"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-19`

---

## Problème précis à résoudre

Choisir le miroir et la branche des mises à jour.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Système > Micrologiciel > Paramètres : choisir le Miroir (ex. `OPNsense (Paris)`) et la Variante (`OPNsense` communautaire ou `OPNsense Business`).
   👉 Explication : le miroir proche accélère les téléchargements; la variante définit la branche.

2. Contrôler la configuration du dépôt :
   ```sh
   opnsense-version
   cat /usr/local/etc/pkg/repos/OPNsense.conf
   ```
   👉 Explication : affiche la version installée et l'URL du dépôt utilisé.

## 2. Production — Contrôles

Utiliser un miroir interne ou un proxy pour les parcs importants.

## 3. Production — Sécurité

Rester en HTTPS; ne pas activer les dépôts de développement en production.

## Validation et retour arrière

- **Validation** : Le dépôt est joignable (Vérifier les mises à jour sans erreur).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)
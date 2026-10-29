---
title: "Fiche Simple - VM OPNsense Vie Systeme 42 Journaux Rotation Et Centralisation"
description: "Centraliser et conserver les journaux."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-42"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_42_Journaux_Rotation_Et_Centralisation

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-42`

---

## Problème précis à résoudre

Centraliser et conserver les journaux.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Système > Paramètres > Journalisation > Distant, ajouter la destination `IP_SYSLOG` (port 514 UDP/TCP ou TLS) et choisir les applications.
   👉 Explication : `IP_SYSLOG` est le serveur de journaux; les événements sont envoyés en temps réel.

2. Régler la rétention locale dans Système > Journaux > Paramètres (nombre de fichiers, taille) et consulter Système > Journaux > Fichiers.
   👉 Explication : évite de remplir le disque.

3. Contrôler en shell :
   ```sh
   ls -lh /var/log | head
   clog /var/log/filter/latest.log | tail -5
   ```
   👉 Explication : liste les journaux et affiche les dernières lignes du pare-feu.

## 2. Production — Contrôles

Conserver les journaux selon la politique de rétention (12 mois pour la traçabilité).

## 3. Production — Sécurité

Journaliser les règles de blocage et protéger le serveur de journaux.

## Validation et retour arrière

- **Validation** : Les événements arrivent sur le serveur `IP_SYSLOG`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Appliance OPNsense Supervision Syslog](</01-fiches-simples/opnsense/toutes-versions/vie-du-logiciel/supervision/fiche-simple-appliance-opnsense-supervision-syslog>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)
---
title: "Fiche Simple - VM pfSense Vie Systeme 23 Outils D Administration Fondamentaux"
description: "Disposer des outils d'exploitation de base."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-23"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_23_Outils_D_Administration_Fondamentaux

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 23 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-23`

---

## Problème précis à résoudre

Disposer des outils d'exploitation de base.

## 1. Hors-Production (Lab / Test / POC)

1. Utiliser Diagnostics > Ping, Traceroute, Packet Capture, States, Command Prompt (ou console option 8 : Shell).
   👉 Explication : ces outils couvrent la plupart des diagnostics sans paquet supplémentaire.

2. Vérifier les commandes essentielles :
   ```sh
   which tcpdump pfctl drill sockstat netstat
   tcpdump -ni vtnet0 -c 5
   ```
   👉 Explication : confirme la présence des outils et capture 5 paquets sur l'interface `vtnet0`.

## 2. Production — Contrôles

Documenter les commandes de diagnostic standard dans le runbook.

## 3. Production — Sécurité

Les captures contiennent des données sensibles : les supprimer après usage.

## Validation et retour arrière

- **Validation** : Les outils répondent et la capture fonctionne.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
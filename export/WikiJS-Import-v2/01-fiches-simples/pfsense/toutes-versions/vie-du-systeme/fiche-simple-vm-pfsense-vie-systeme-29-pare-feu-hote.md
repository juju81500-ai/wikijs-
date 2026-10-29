---
title: "Fiche Simple - VM pfSense Vie Systeme 29 Pare Feu Hote"
description: "Appliquer une politique de filtrage cohérente sur les interfaces."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-29"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-29`

---

## Problème précis à résoudre

Appliquer une politique de filtrage cohérente sur les interfaces.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Firewall > Rules > LAN > Add : Action `Pass`, Protocol TCP/UDP, Source `LAN subnets`, Destination `any`, Destination Port 80/443/53, Save puis Apply Changes.
   👉 Explication : pfSense bloque par défaut tout ce qui n'est pas autorisé; chaque flux est ouvert explicitement.

2. Firewall > Rules > WAN : garder le blocage par défaut et cocher « Block private networks » et « Block bogon networks » dans Interfaces > WAN.
   👉 Explication : empêche les paquets usurpés depuis Internet.

3. Contrôler les règles actives :
   ```sh
   pfctl -sr | head -30
   pfctl -si | head
   ```
   👉 Explication : liste les règles chargées dans pf et ses statistiques.

## 2. Production — Contrôles

Documenter chaque règle (Description) et son demandeur; utiliser des alias (Firewall > Aliases).

## 3. Production — Sécurité

Principe du refus par défaut; aucune règle `any any`.

## Validation et retour arrière

- **Validation** : `pfctl -sr` montre les règles attendues et le trafic autorisé passe.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
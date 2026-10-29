---
title: "Fiche Simple - VM OPNsense Vie Systeme 29 Pare Feu Hote"
description: "Appliquer une politique de filtrage cohérente sur les interfaces."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-29"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-29`

---

## Problème précis à résoudre

Appliquer une politique de filtrage cohérente sur les interfaces.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Pare-feu > Règles > LAN et créer une règle `Passer` : Protocole TCP/UDP, Source `réseau LAN`, Destination `any`, Ports 80/443/53, puis Enregistrer et Appliquer les modifications.
   👉 Explication : OPNsense bloque par défaut tout ce qui n'est pas autorisé; chaque flux est autorisé explicitement.

2. Pare-feu > Règles > WAN : conserver la règle de blocage par défaut (« Bloquer les réseaux privés » et « Bloquer les réseaux bogon » activés dans l'interface WAN).
   👉 Explication : empêche les paquets spoofés depuis Internet.

3. Contrôler les règles actives :
   ```sh
   pfctl -sr | head -30
   pfctl -si | head
   ```
   👉 Explication : liste les règles chargées dans pf et les statistiques.

## 2. Production — Contrôles

Documenter chaque règle (description) et son demandeur; nommer les alias.

## 3. Production — Sécurité

Principe du refus par défaut; aucune règle `any any`.

## Validation et retour arrière

- **Validation** : `pfctl -sr` montre les règles attendues et le trafic autorisé passe.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)
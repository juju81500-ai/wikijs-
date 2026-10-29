---
title: "Fiche Simple - Appliance OPNsense CARP pfsync Preparer Basculement"
description: "Préparer deux appliances avant de configurer CARP et pfsync."
published: true
date: 2026-10-29T20:14:10Z
tags: ["opnsense", "carp", "pfsync", "ha", "firewall"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_Appliance_OPNsense_CARP_pfsync_Preparer_Basculement.md

- **Environnement** : Deux appliances OPNsense en haute disponibilité (CARP et pfsync)
- **OS / Version** : OPNsense (toutes versions compatibles entre les deux nœuds)
- **Catégorie** : pare-feu / haute disponibilité
- **Tags** : `opnsense`, `carp`, `pfsync`, `ha`, `firewall`

---

## Problème précis à résoudre

Préparer deux appliances avant de configurer CARP et pfsync.

## 1. Hors-Production (Lab / Test / POC)

1. Attribuer à chaque appliance une IP propre sur chaque interface : **Interfaces > [nom de l'interface]**, type IPv4 statique.
   👉 Explication : chaque nœud garde sa propre adresse en plus de la VIP partagée.

2. Prévoir une VIP CARP distincte par réseau, un réseau dédié à pfsync et un réseau de synchronisation de configuration.
   👉 Explication : évite de transporter l'état sur le WAN.

3. Vérifier que les commutateurs autorisent les adresses MAC virtuelles CARP et que les deux appliances ont une version compatible : **System > Firmware > Status**.
   👉 Explication : une incompatibilité casse la synchronisation.

4. Exporter et chiffrer les configurations actuelles : **System > Configuration > Backups > Download configuration** (cocher le chiffrement).
   👉 Explication : permet de revenir en arrière.

5. Garder un accès console local aux deux appliances.
   👉 Explication : une erreur de VIP ou de règle peut couper l'administration.

## 2. Production — Contrôles

Documenter adresses, VHID, réseaux dédiés et plan de maintenance.

## 3. Production — Sécurité

- Sauvegardes de configuration chiffrées et stockées hors des appliances.

## Validation et retour arrière

- **Validation** : plan d'adressage, versions compatibles et sauvegardes chiffrées disponibles.
- **Retour arrière** : aucune modification n'est faite par cette fiche; rien à annuler.

## Si le problème n'est pas résolu

- [OPNsense — sauvegarde](https://docs.opnsense.org/manual/backups.html)
- [OPNsense — haute disponibilité](https://docs.opnsense.org/manual/hacarp.html)
- [Guide complet](/02-fiches-completes/opnsense/toutes-versions/autres/10-pare-feu-appliance-opnsense-carp-pfsync-ha#1-preparer-le-basculement)
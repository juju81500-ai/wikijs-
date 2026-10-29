---
title: "Fiche Simple - VM pfSense Vie Systeme 34 Durcissement Du Noyau Et"
description: "Appliquer les paramètres réseau sûrs."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-34"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_34_Durcissement_Du_Noyau_Et

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 34 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-34`

---

## Problème précis à résoudre

Appliquer les paramètres réseau sûrs.

## 1. Hors-Production (Lab / Test / POC)

1. Dans System > Advanced > System Tunables, contrôler/ajouter : `net.inet.ip.redirect=0`, `net.inet.icmp.drop_redirect=1`, `net.inet.tcp.drop_synfin=1`, puis Save.
   👉 Explication : refuse les redirections ICMP et les paquets TCP anormaux.

2. Dans System > Advanced > Firewall & NAT : laisser la normalisation (Scrub) activée; vérifier que WAN a « Block private networks » et « Block bogon networks ».
   👉 Explication : réassemble les fragments et évite l'usurpation.

3. Contrôler les valeurs effectives :
   ```sh
   sysctl net.inet.ip.redirect net.inet.tcp.drop_synfin net.inet.ip.forwarding
   ```
   👉 Explication : affiche les valeurs du noyau; `forwarding` reste à 1 sur un routeur.

## 2. Production — Contrôles

Documenter chaque tunable modifié et sa justification.

## 3. Production — Sécurité

Éviter les tunables non compris; tester sur un lab.

## Validation et retour arrière

- **Validation** : Les valeurs `sysctl` correspondent à la cible.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
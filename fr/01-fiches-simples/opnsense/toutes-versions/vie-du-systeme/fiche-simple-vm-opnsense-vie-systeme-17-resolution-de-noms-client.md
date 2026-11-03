---
title: "Fiche Simple - VM OPNsense Vie Systeme 17 Resolution De Noms Client"
description: "Configurer les serveurs [[Glossary:DNS]] utilisés par le pare-feu et les clients."
published: true
date: 2026-11-03T14:22:28Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-17"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : Pare-feu OPNsense ([[Glossary:VM]] ou matériel)
- **OS / Version** : OPNsense; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-17`

---

## Problème précis à résoudre

Configurer les serveurs [[Glossary:DNS]] utilisés par le pare-feu et les clients.

## 1. Hors-Production (Lab / Test / POC)

1. Renseigner Système > Paramètres > Général > Serveurs DNS (ex. `IP_DNS1`, `IP_DNS2`) et décocher « Autoriser le remplacement par le [[Glossary:DHCP]] du [[Glossary:WAN]] » si les DNS sont imposés.
   👉 Explication : `IP_DNS1` et `IP_DNS2` sont les résolveurs internes ou publics choisis.

2. Activer le résolveur local dans Services > Unbound DNS > Général (Activer, interfaces [[Glossary:LAN]], [[Glossary:DNSSEC]]).
   👉 Explication : les clients interrogent le pare-feu qui résout ou relaie.

3. Tester en shell :
   ```sh
   drill exemple.fr @127.0.0.1
   cat /etc/resolv.conf
   ```
   👉 Explication : prouve la résolution par Unbound et affiche les serveurs configurés.

## 2. Production — Contrôles

Avoir deux résolveurs et documenter leur propriétaire.

## 3. Production — Sécurité

Activer DNSSEC et ne pas autoriser les requêtes DNS depuis le WAN.

## Validation et retour arrière

- **Validation** : `drill` renvoie une réponse `NOERROR`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire OPNsense](/fr/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)
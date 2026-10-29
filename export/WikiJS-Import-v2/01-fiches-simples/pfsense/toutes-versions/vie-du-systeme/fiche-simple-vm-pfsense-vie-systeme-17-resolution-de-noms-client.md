---
title: "Fiche Simple - VM pfSense Vie Systeme 17 Resolution De Noms Client"
description: "Configurer les serveurs DNS utilisés par le pare-feu et les clients."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-17"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-17`

---

## Problème précis à résoudre

Configurer les serveurs DNS utilisés par le pare-feu et les clients.

## 1. Hors-Production (Lab / Test / POC)

1. Renseigner System > General Setup > DNS Servers (`IP_DNS1`, `IP_DNS2`) et décocher « Allow DNS server list to be overridden by DHCP/PPP on WAN » si les DNS sont imposés.
   👉 Explication : `IP_DNS1` et `IP_DNS2` sont les résolveurs internes ou publics choisis.

2. Activer Services > DNS Resolver > General Settings (Enable DNS Resolver, DNSSEC, interfaces LAN).
   👉 Explication : les clients interrogent le pare-feu qui résout ou relaie (Unbound).

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

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
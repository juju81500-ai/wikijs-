---
title: "Fiche Simple - Appliance OPNsense Diagnostic Reseau Etat Appliance"
description: "Vérifier firmware, interfaces, passerelles et journaux autour de l'incident."
published: true
date: 2026-10-29T20:22:42Z
tags: ["opnsense", "diagnostic", "reseau", "firewall", "dns", "vpn"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_Appliance_OPNsense_Diagnostic_Reseau_Etat_Appliance.md

- **Environnement** : Appliance OPNsense seule ou paire CARP; accès console recommandé
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Catégorie** : pare-feu / diagnostic
- **Tags** : `opnsense`, `diagnostic`, `reseau`, `firewall`, `dns`, `vpn`

---

## Problème précis à résoudre

Vérifier firmware, interfaces, passerelles et journaux autour de l'incident.

## 1. Hors-Production (Lab / Test / POC)

1. **System > Firmware > Status** puis **Interfaces > Overview** et **System > Gateways > Dashboard**.
   👉 Explication : état du système, des liens et des passerelles.

2. Console ou **Interfaces > Diagnostics** : utiliser **Ping**, **DNS Lookup**, **Port Probe**, **Trace Route**, **Packet Capture** avec la bonne interface et la bonne adresse source.
   👉 Explication : le pare-feu peut avoir une route ou politique différente du client.

3. Équivalents en shell (menu console, option 8) :
   ```sh
   ifconfig
   netstat -rn
   ping -c 3 192.0.2.1
   ```
   👉 Explication : (dérivé) affiche interfaces, routes et teste une adresse d'exemple à remplacer.

4. Lire **System > Log Files > General** et **Firewall > Log Files > Live View** autour de l'heure concernée.
   👉 Explication : repère erreurs système et blocages.

## 2. Production — Contrôles

Lancer un audit de santé pour repérer fichiers ou dépendances altérés.

## 3. Production — Sécurité

- Capturer uniquement ce qui est nécessaire.

## Validation et retour arrière

- **Validation** : État de l'appliance noté.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [OPNsense — outils de diagnostic](https://docs.opnsense.org/manual/diagnostics_interfaces.html)
- [OPNsense — dépannage](https://docs.opnsense.org/troubleshooting.html)
- [Guide complet — 2. Contrôler l'état de l'appliance](/02-fiches-completes/opnsense/toutes-versions/diagnostic/35-diagnostic-reseau-opnsense-flux-dns-vpn#2-controler-letat-de-lappliance)
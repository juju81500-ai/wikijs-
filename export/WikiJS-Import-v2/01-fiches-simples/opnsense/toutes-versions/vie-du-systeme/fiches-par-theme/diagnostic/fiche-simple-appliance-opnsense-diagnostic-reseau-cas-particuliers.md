---
title: "Fiche Simple - Appliance OPNsense Diagnostic Reseau Cas Particuliers"
description: "Diagnostiquer les pannes spécifiques sans tout recréer."
published: true
date: 2026-10-29T20:22:42Z
tags: ["opnsense", "diagnostic", "reseau", "firewall", "dns", "vpn"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_Appliance_OPNsense_Diagnostic_Reseau_Cas_Particuliers.md

- **Environnement** : Appliance OPNsense seule ou paire CARP; accès console recommandé
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Catégorie** : pare-feu / cas particuliers
- **Tags** : `opnsense`, `diagnostic`, `reseau`, `firewall`, `dns`, `vpn`

---

## Problème précis à résoudre

Diagnostiquer les pannes spécifiques sans tout recréer.

## 1. Hors-Production (Lab / Test / POC)

1. DNS : comparer la résolution depuis le client et depuis OPNsense (**Interfaces > Diagnostics > DNS Lookup**). Équivalent shell (nom d'exemple à remplacer) :
   ```sh
   drill srv1.example.test
   ```
   👉 Explication : (dérivé) vérifie règles DNS, redirecteurs, DNSSEC et service choisi.

2. VPN : vérifier négociation, SA/phase, routes et sélecteurs (**VPN > IPsec > Status Overview** ou **VPN > WireGuard**).
   👉 Explication : avant de recréer un tunnel.

3. CARP/pfsync : contrôler VIP et lien de synchronisation sur les deux nœuds :
   ```sh
   ifconfig | grep -A1 carp
   ```
   👉 Explication : (dérivé) un seul nœud doit être MASTER pour une VIP donnée.

4. MTU : tester avec bit DF et tailles progressives (adresse d'exemple à remplacer) :
   ```sh
   ping -D -s 1472 -c 3 192.0.2.10
   ```
   👉 Explication : (dérivé) si le test échoue, réduire la taille pour trouver le MTU utilisable; ne pas réduire le MTU globalement.

## 2. Production — Contrôles

Isoler le segment concerné avant d'ajuster MTU ou VPN.

## 3. Production — Sécurité

- Éviter deux maîtres CARP actifs.

## Validation et retour arrière

- **Validation** : La cause (DNS, VPN, CARP ou MTU) est identifiée.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [OPNsense — outils de diagnostic](https://docs.opnsense.org/manual/diagnostics_interfaces.html)
- [OPNsense — dépannage](https://docs.opnsense.org/troubleshooting.html)
- [Guide complet — 4. Cas particuliers](/02-fiches-completes/opnsense/toutes-versions/diagnostic/35-diagnostic-reseau-opnsense-flux-dns-vpn#4-cas-particuliers)
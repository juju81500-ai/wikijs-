---
title: "Fiche Simple - VM OPNsense Vie Systeme 37 Deploiement Des Roles Metiers"
description: "Activer les rôles du pare-feu : DHCP, NAT, VPN."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-37"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-37`

---

## Problème précis à résoudre

Activer les rôles du pare-feu : DHCP, NAT, VPN.

## 1. Hors-Production (Lab / Test / POC)

1. DHCP : Services > Dnsmasq DNS & DHCP (ou Kea DHCPv4 / ISC DHCPv4) > LAN : activer, plage `IP_DEBUT` à `IP_FIN`, passerelle `IP_LAN`.
   👉 Explication : `IP_DEBUT` et `IP_FIN` délimitent la plage distribuée; en shell, vérifier le service.

2. NAT sortant : Pare-feu > NAT > Sortant, mode automatique ou hybride pour le LAN vers le WAN. Redirection de port : Pare-feu > NAT > Redirection de port.
   👉 Explication : traduit les adresses internes vers l'adresse WAN et publie un service si besoin.

3. VPN : VPN > WireGuard > Instances > Ajouter (port 51820), puis Pare-feu > Règles > WAN pour autoriser UDP 51820.
   👉 Explication : crée un accès distant chiffré; l'interface `wg0` apparaît ensuite.

4. Vérifier en shell :
   ```sh
   pfctl -sn | head
   wg show 2>/dev/null
   sockstat -4 -l | grep -E 'dnsmasq|kea|dhcpd'
   ```
   👉 Explication : affiche les règles NAT, les tunnels WireGuard et le serveur DHCP en écoute.

## 2. Production — Contrôles

Documenter chaque redirection de port et son propriétaire.

## 3. Production — Sécurité

Limiter la publication de services; préférer un VPN à une redirection directe.

## Validation et retour arrière

- **Validation** : Un client reçoit une adresse, sort sur Internet et le tunnel se monte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)
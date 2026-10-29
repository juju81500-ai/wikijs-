---
title: "Fiche Simple - VM Debian 13 Kea Controler Service"
description: "Vérifier sockets, journaux et attribution d'un bail depuis un client du VLAN isolé."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "kea", "dhcpv4", "isc", "reseau"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Kea_Controler_Service.md

- **Environnement** : VM Debian 13 serveur DHCPv4 sur un VLAN de test isolé
- **OS / Version** : Debian 13 Trixie x86-64; ISC Kea (canal stable)
- **Catégorie** : réseau / DHCP
- **Tags** : `debian13`, `kea`, `dhcpv4`, `isc`, `reseau`

---

## Problème précis à résoudre

Vérifier sockets, journaux et attribution d'un bail depuis un client du VLAN isolé.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la socket UDP/67 et les journaux du démarrage :
   ```bash
   sudo ss -lunp '( sport = :67 )'
   sudo journalctl -u isc-kea-dhcp4-server.service -b --no-pager
   ```
   👉 Explication : le daemon doit écouter sur UDP/67 sans erreur d'interface.

2. Depuis une VM cliente attachée au VLAN isolé, demander un bail et contrôler adresse, passerelle, DNS, domaine et renouvellement.
   👉 Explication : valide le service de bout en bout; ne jamais le faire sur un LAN partagé.

3. Contrôler le bail côté serveur dans le fichier persistant de baux Kea et la connectivité vers les services annoncés.
   👉 Explication : confirme que le bail est enregistré.

## 2. Production — Contrôles

Autoriser DHCP (UDP/67 serveur, UDP/68 client) selon les règles réseau et relais validés; tester depuis le réseau client réel avant de déclarer le service disponible.

## 3. Production — Sécurité

- Kea peut utiliser des sockets bruts qui contournent le filtrage local classique; le contrôle doit se faire côté réseau.
- Ne pas lancer de client DHCP de test sur un LAN partagé.

## Validation et retour arrière

- **Validation** : Bail obtenu avec les bons paramètres et visible côté serveur.
- **Retour arrière** : Arrêter le service : `sudo systemctl stop isc-kea-dhcp4-server.service`.

## Si le problème n'est pas résolu

- [ISC Kea — Serveur DHCPv4](https://kea.readthedocs.io/en/latest/arm/dhcp4-srv.html)
- [ISC Kea — Sécurité](https://kea.readthedocs.io/en/latest/arm/security.html)
- [Guide complet Kea DHCPv4 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13#5-controler-le-service-sans-perturber-le-lan)
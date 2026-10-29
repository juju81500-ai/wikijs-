---
title: "Fiche Simple - VM Debian 13 ISC-DHCP-Server Configurer"
description: "Limiter dhcpd à l’interface et plage du lab."
published: true
date: 2026-10-29T21:07:31Z
tags: ["isc-dhcp", "serveur", "vie-du-logiciel", "configurer"]
editor: markdown
dateCreated: 2026-10-29T21:07:31Z
dateModified: 2026-10-29T21:07:31Z
---

# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Configurer

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Configurer
- **Tags** : `isc-dhcp`, `serveur`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Limiter dhcpd à l’interface et plage du lab.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer :
   ```bash
   ip -br addr
sudoedit /etc/default/isc-dhcp-server
sudoedit /etc/dhcp/dhcpd.conf
sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf
   ```
   👉 Explication : Définir `INTERFACESv4` et les options réseau exactes; valider syntaxe avant démarrage.


## 2. Production — Contrôles

Vérifier chevauchements, réservations, relais et VLAN avec l’équipe réseau.

## 3. Production — Sécurité

Une plage erronée peut perturber le VLAN; préparer arrêt d’urgence.

## Validation et retour arrière

- **Validation** : Syntaxe valide et écoute limitée à l’interface attendue.
- **Retour arrière** : Restaurer les fichiers sauvegardés puis valider la syntaxe.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-prerequis-limites)
- [Installer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-installer)
- [Sécuriser](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-securiser)
- [Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-mise-a-jour-retour-arriere)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)
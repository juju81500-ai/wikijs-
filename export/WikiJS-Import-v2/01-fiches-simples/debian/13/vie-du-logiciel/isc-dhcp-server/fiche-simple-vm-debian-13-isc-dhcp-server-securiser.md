---
title: "Fiche Simple - VM Debian 13 ISC-DHCP-Server Securiser"
description: "Restreindre DHCP UDP 67 et les accès d’administration."
published: true
date: 2026-10-29T21:07:31Z
tags: ["isc-dhcp", "serveur", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T21:07:31Z
dateModified: 2026-10-29T21:07:31Z
---

# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Securiser

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Sécuriser
- **Tags** : `isc-dhcp`, `serveur`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Restreindre DHCP UDP 67 et les accès d’administration.

## 1. Hors-Production (Lab / Test / POC)

1. Sécuriser :
   ```bash
   grep -E "^INTERFACESv4" /etc/default/isc-dhcp-server
sudo ss -lunp | grep ":67" || true
sudo ufw allow from ADMIN_CIDR to any port 22 proto tcp
sudo ufw allow in on INTERFACE_LAB to any port 67 proto udp
sudo ufw status numbered
   ```
   👉 Explication : `ADMIN_CIDR` et `INTERFACE_LAB` sont des placeholders à remplacer; vérifier SSH avant activation.


## 2. Production — Contrôles

Filtrer par VLAN/interface et ACL réseau; valider les relais indépendamment.

## 3. Production — Sécurité

EOL upstream : limiter exposition, protéger journaux/baux et migrer Kea.

## Validation et retour arrière

- **Validation** : Seuls segments autorisés reçoivent une offre DHCP.
- **Retour arrière** : Retirer règles ajoutées en préservant l’accès admin.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-prerequis-limites)
- [Installer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-installer)
- [Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-configurer)
- [Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-mise-a-jour-retour-arriere)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)
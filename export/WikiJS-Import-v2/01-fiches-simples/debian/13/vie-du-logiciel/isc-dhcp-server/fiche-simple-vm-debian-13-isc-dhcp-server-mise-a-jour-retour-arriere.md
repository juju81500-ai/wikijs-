---
title: "Fiche Simple - VM Debian 13 ISC-DHCP-Server Mise A Jour Retour Arriere"
description: "Contrôler mises à jour Debian et accélérer le remplacement par Kea."
published: true
date: 2026-10-29T21:07:31Z
tags: ["isc-dhcp", "serveur", "vie-du-logiciel", "mise_a_jour_retour_arriere"]
editor: markdown
dateCreated: 2026-10-29T21:07:31Z
dateModified: 2026-10-29T21:07:31Z
---

# Fiche_Simple_-_VM_Debian_13_ISC-DHCP-Server_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13; ISC DHCP déprécié, usage transitoire
- **OS / Version** : Debian 13
- **Catégorie** : Vie du logiciel / ISC-DHCP-Server — Mise à jour et retour arrière
- **Tags** : `isc-dhcp`, `serveur`, `vie-du-logiciel`, `mise_a_jour_retour_arriere`

---

## Problème précis à résoudre

Contrôler mises à jour Debian et accélérer le remplacement par Kea.

## 1. Hors-Production (Lab / Test / POC)

1. Mise à jour et retour arrière :
   ```bash
   sudo apt update
apt-cache policy isc-dhcp-server
apt list --upgradable 2>/dev/null | grep isc-dhcp || true
sudo dhcpd -t -cf /etc/dhcp/dhcpd.conf
   ```
   👉 Explication : Paquet présent ne signifie pas maintenance upstream; archive de config avant migration.


## 2. Production — Contrôles

Prioriser migration Kea et tester plage, réservations/options en lab.

## 3. Production — Sécurité

Appliquer seulement mises à jour Debian disponibles; réduire usage du logiciel EOL.

## Validation et retour arrière

- **Validation** : Plan de migration/repli testé et approuvé.
- **Retour arrière** : Réactiver ISC uniquement après arrêt Kea et validation du propriétaire DHCP.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-prerequis-limites)
- [Installer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-installer)
- [Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-configurer)
- [Sécuriser](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-securiser)
- [Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/isc-dhcp-server/fiche-simple-vm-debian-13-isc-dhcp-server-sauvegarder-restaurer)
- [Documentation officielle](https://www.isc.org/blogs/isc-dhcp-eol/)
---
title: "Fiche Simple - VM Debian 13 Kea Configurer"
description: "Écrire une configuration DHCPv4 autonome avec baux persistants (memfile)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "kea", "dhcpv4", "isc", "reseau"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Kea_Configurer.md

- **Environnement** : VM Debian 13 serveur DHCPv4 sur un VLAN de test isolé
- **OS / Version** : Debian 13 Trixie x86-64; ISC Kea (canal stable)
- **Catégorie** : réseau / DHCP
- **Tags** : `debian13`, `kea`, `dhcpv4`, `isc`, `reseau`

---

## Problème précis à résoudre

Écrire une configuration DHCPv4 autonome avec baux persistants (memfile).

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration d'origine :
   ```bash
   sudo cp -a /etc/kea/kea-dhcp4.conf /etc/kea/kea-dhcp4.conf.orig
   ```
   👉 Explication : permet un retour arrière immédiat.

2. Écrire la configuration (interface, plage, adresses d'exemple à remplacer par les valeurs du VLAN) :
   ```bash
   sudo tee /etc/kea/kea-dhcp4.conf >/dev/null <<'EOF'
   {
     "Dhcp4": {
       "interfaces-config": { "interfaces": [ "ens18" ] },
       "lease-database": { "type": "memfile", "persist": true, "name": "kea-leases4.csv" },
       "valid-lifetime": 3600,
       "renew-timer": 900,
       "rebind-timer": 1800,
       "authoritative": true,
       "subnet4": [
         {
           "id": 1,
           "subnet": "192.0.2.0/24",
           "pools": [ { "pool": "192.0.2.100 - 192.0.2.199" } ],
           "option-data": [
             { "name": "routers", "data": "192.0.2.1" },
             { "name": "domain-name-servers", "data": "192.0.2.53" },
             { "name": "domain-name", "data": "lab.example.test" }
           ]
         }
       ]
     }
   }
   EOF
   ```
   👉 Explication : définit un sous-réseau, un pool `.100-.199`, la passerelle, le DNS et le domaine; `persist: true` conserve les baux.

3. Si les requêtes arrivent par un relais, ajouter `relay.ip-addresses` avec l'adresse du relais et revoir l'interface d'écoute.
   👉 Explication : sans cela le serveur ne répond pas aux requêtes relayées.

## 2. Production — Contrôles

Revue de la configuration par un second administrateur : absence de chevauchement, options correctes, interface d'écoute limitée.

## 3. Production — Sécurité

- Ne pas configurer de pool sur une interface qui ne dessert pas ce réseau.
- Restreindre les droits du fichier de configuration (secrets SQL en clair).

## Validation et retour arrière

- **Validation** : Le fichier est valide JSON et validé à l'étape suivante par `kea-dhcp4 -t`.
- **Retour arrière** : `sudo cp -a /etc/kea/kea-dhcp4.conf.orig /etc/kea/kea-dhcp4.conf`.

## Si le problème n'est pas résolu

- [ISC Kea — Serveur DHCPv4](https://kea.readthedocs.io/en/latest/arm/dhcp4-srv.html)
- [Guide complet Kea DHCPv4 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13#3-definir-une-configuration-minimale)
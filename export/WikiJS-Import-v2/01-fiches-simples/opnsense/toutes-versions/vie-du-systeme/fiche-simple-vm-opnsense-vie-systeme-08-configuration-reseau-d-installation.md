---
title: "Fiche Simple - VM OPNsense Vie Systeme 08 Configuration Reseau D Installation"
description: "Affecter les interfaces WAN et LAN pour que la console et l'interface web soient joignables."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-08"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-08`

---

## Problème précis à résoudre

Affecter les interfaces WAN et LAN pour que la console et l'interface web soient joignables.

## 1. Hors-Production (Lab / Test / POC)

1. À l'invite de la console, taper `n` pour passer les VLAN, puis saisir le nom des interfaces (ex. `vtnet0` pour WAN, `vtnet1` pour LAN), ou depuis le menu console choisir l'option 1.
   👉 Explication : l'option 1 « Assign interfaces » associe les cartes physiques aux rôles WAN et LAN.

2. Définir les adresses : option 2 « Set interface IP address » (LAN : `192.168.1.1/24` par défaut, WAN en DHCP). Vérifier en shell (option 8) :
   ```sh
   ifconfig -a | grep -E '^[a-z]|inet '
   netstat -rn | head
   ```
   👉 Explication : affiche les interfaces, leurs adresses et la route par défaut.

3. Depuis un poste du LAN, ouvrir `https://IP_LAN` (par défaut `https://192.168.1.1`), `IP_LAN` étant l'adresse du pare-feu côté LAN.
   👉 Explication : le certificat est auto-signé; accepter l'exception pour la première connexion.

## 2. Production — Contrôles

Prévoir un réseau d'administration distinct et documenter les affectations interface/rôle.

## 3. Production — Sécurité

Ne jamais exposer l'interface web sur le WAN; la règle d'anti-verrouillage doit rester sur LAN.

## Validation et retour arrière

- **Validation** : L'interface web répond sur l'IP LAN et le WAN reçoit une adresse.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)
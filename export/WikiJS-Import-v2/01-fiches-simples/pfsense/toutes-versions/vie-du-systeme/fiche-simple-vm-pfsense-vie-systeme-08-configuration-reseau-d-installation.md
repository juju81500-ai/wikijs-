---
title: "Fiche Simple - VM pfSense Vie Systeme 08 Configuration Reseau D Installation"
description: "Affecter les interfaces WAN et LAN pour joindre la console et l'interface web."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-08"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-08`

---

## Problème précis à résoudre

Affecter les interfaces WAN et LAN pour joindre la console et l'interface web.

## 1. Hors-Production (Lab / Test / POC)

1. À la fin de l'installation, répondre `n` à la question VLAN, puis saisir les noms d'interfaces (ex. `vtnet0` pour WAN, `vtnet1` pour LAN); ou depuis le menu console choisir l'option 1 « Assign Interfaces ».
   👉 Explication : l'option 1 associe les cartes physiques aux rôles WAN et LAN.

2. Définir les adresses : option 2 « Set interface(s) IP address » (LAN par défaut `192.168.1.1/24`, WAN en DHCP). Vérifier en shell (option 8) :
   ```sh
   ifconfig -a | grep -E '^[a-z]|inet '
   netstat -rn | head
   ```
   👉 Explication : affiche les interfaces, leurs adresses et la route par défaut.

3. Depuis un poste du LAN, ouvrir `https://IP_LAN` (par défaut `https://192.168.1.1`) puis se connecter.
   👉 Explication : `IP_LAN` est l'adresse du pare-feu côté LAN; le certificat est auto-signé.

## 2. Production — Contrôles

Prévoir un réseau d'administration distinct et documenter les affectations.

## 3. Production — Sécurité

Ne jamais exposer l'interface web sur le WAN; garder la règle d'anti-verrouillage sur le LAN.

## Validation et retour arrière

- **Validation** : L'interface web répond sur l'IP LAN et le WAN reçoit une adresse.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
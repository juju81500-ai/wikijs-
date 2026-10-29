---
title: "Fiche Simple - VM pfSense Vie Systeme 16 Adressage Ip Fixe Definitif"
description: "Fixer les adresses définitives des interfaces."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-16"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-16`

---

## Problème précis à résoudre

Fixer les adresses définitives des interfaces.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Interfaces > LAN : IPv4 Configuration Type = `Static IPv4`, IPv4 Address `IP_LAN/24` (ex. `10.0.0.1/24`), Save puis Apply Changes.
   👉 Explication : `IP_LAN` est l'adresse du pare-feu sur le réseau interne.

2. Interfaces > WAN : `DHCP` ou `Static IPv4`, avec une passerelle `IP_PASSERELLE` (fournie par le FAI) ajoutée via Add a new gateway.
   👉 Explication : définit la sortie vers Internet.

3. Contrôler en shell :
   ```sh
   ifconfig vtnet0
   netstat -rn | grep default
   ping -c 3 IP_PASSERELLE
   ```
   👉 Explication : vérifie l'adresse, la route par défaut et la joignabilité de la passerelle.

## 2. Production — Contrôles

Réserver les adresses dans le plan d'adressage (IPAM).

## 3. Production — Sécurité

Changer l'adresse LAN peut couper la session d'administration : garder la console.

## Validation et retour arrière

- **Validation** : Adresses conformes au plan et passerelle joignable.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
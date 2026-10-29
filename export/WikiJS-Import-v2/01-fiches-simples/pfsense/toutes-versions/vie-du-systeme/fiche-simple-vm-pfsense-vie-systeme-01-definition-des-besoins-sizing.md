---
title: "Fiche Simple - VM pfSense Vie Systeme 01 Definition Des Besoins Sizing"
description: "Dimensionner le pare-feu avant de créer la VM ou d'acheter le matériel."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-01"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-01`

---

## Problème précis à résoudre

Dimensionner le pare-feu avant de créer la VM ou d'acheter le matériel.

## 1. Hors-Production (Lab / Test / POC)

1. Relever le débit WAN, le nombre de clients, de tunnels VPN et les paquets activés (Snort/Suricata, pfBlockerNG) :
   👉 Explication : le débit avec inspection et chiffrement VPN dimensionne le CPU; les paquets additionnels consomment de la RAM.

2. Sur un pfSense existant, relever les ressources : Status > Dashboard (widget System Information) ou, en shell (console option 8 ou SSH) :
   ```sh
   sysctl hw.ncpu hw.physmem
   df -h /
   zpool list 2>/dev/null
   vmstat 1 3
   ```
   👉 Explication : nombre de CPU, RAM et disque; `zpool list` n'est utile qu'avec ZFS.

3. Compter les interfaces (WAN, LAN, DMZ, HA) et choisir des cartes réseau compatibles FreeBSD (Intel de préférence).
   👉 Explication : une carte non reconnue ne peut pas être affectée à l'installation.

4. Noter vCPU (2 minimum), RAM (2 Go minimum, 4 Go avec paquets), disque (8 Go minimum, 20 Go conseillés), interfaces et débit cible dans le dossier du projet.
   👉 Explication : ce tableau sert de référence pour l'hyperviseur et pour la recette.

## 2. Production — Contrôles

Ajouter 30 % de marge de débit; prévoir un second nœud si le pare-feu est un point unique de défaillance.

## 3. Production — Sécurité

Prévoir des interfaces physiques ou des VLAN distincts pour WAN, LAN et DMZ.

## Validation et retour arrière

- **Validation** : Tableau de sizing (CPU, RAM, disque, interfaces, débit) signé et conservé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
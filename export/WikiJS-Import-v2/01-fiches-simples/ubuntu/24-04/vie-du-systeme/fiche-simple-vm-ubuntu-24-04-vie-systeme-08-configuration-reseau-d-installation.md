---
title: "Fiche Simple - VM Ubuntu 24.04 Vie Systeme 08 Configuration Reseau D Installation"
description: "Disposer d'un réseau pendant l'installation."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2404", "vie-du-systeme", "cycle-de-vie", "etape-08"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-08`

---

## Problème précis à résoudre

Disposer d'un réseau pendant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Dans le programme d'installation (Subiquity), écran **Network connections** : laisser le DHCP ou choisir **Edit IPv4 > Manual** pour une IP statique temporaire. Après démarrage, contrôler :
   ```bash
   ip -br address
   ip route
   ping -c 2 archive.ubuntu.com
   ```
   👉 Explication : vérifie l'adresse, la passerelle et l'accès aux dépôts; l'installateur génère un fichier Netplan dans `/etc/netplan/`.

## 2. Production — Contrôles

Utiliser un VLAN d'installation si le réseau de production n'a pas de DHCP.

## 3. Production — Sécurité

Ne pas exposer une machine non durcie sur Internet.

## Validation et retour arrière

- **Validation** : `ping` vers `archive.ubuntu.com` réussit.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
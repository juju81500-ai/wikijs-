---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 08 Configuration Reseau D Installation"
description: "Donner à l'hôte une adresse IP de gestion temporaire."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-08"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-08`

---

## Problème précis à résoudre

Donner à l'hôte une adresse IP de gestion temporaire.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur, ESXi utilise DHCP par défaut. Après démarrage, configurer depuis la DCUI : **F2 > Configure Management Network > IPv4 Configuration**.
   👉 Explication : saisir l'IP, le masque et la passerelle pour accéder au Host Client.

2. Équivalent en ligne de commande (remplacer les placeholders) :
   ```sh
   esxcli network ip interface ipv4 set -i vmk0 -t static -I IP_HOTE -N 255.255.255.0
   esxcli network ip route ipv4 add -n default -g IP_GW
   ```
   👉 Explication : `IP_HOTE` = IP de gestion; `IP_GW` = passerelle; `vmk0` = interface de gestion.

3. Contrôler :
   ```sh
   esxcli network ip interface ipv4 get
   vmkping -I vmk0 IP_GW
   ```
   👉 Explication : `vmkping` teste depuis la pile de gestion.

## 2. Production — Contrôles

Réseau de gestion isolé (VLAN d'administration).

## 3. Production — Sécurité

Ne pas exposer le Host Client sur Internet.

## Validation et retour arrière

- **Validation** : `vmkping` vers la passerelle réussit.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)
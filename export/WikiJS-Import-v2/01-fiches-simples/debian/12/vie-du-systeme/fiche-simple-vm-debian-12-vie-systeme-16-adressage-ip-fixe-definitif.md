---
title: "Fiche Simple - VM Debian 12 Vie Systeme 16 Adressage Ip Fixe Definitif"
description: "Fixer l'IP du serveur."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-16"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-16`

---

## Problème précis à résoudre

Fixer l'IP du serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Éditer `/etc/network/interfaces` (ifupdown, par défaut sous Debian 12 ; remplacer interface et valeurs) :
   ```bash
   sudoedit /etc/network/interfaces
   ```
   👉 Explication : exemple : `iface ens18 inet static`, `address 192.0.2.10/24`, `gateway 192.0.2.1`.

2. Appliquer en gardant la console ouverte, puis tester :
   ```bash
   sudo systemctl restart networking
   ip -br address
   ip route
   ping -c 2 192.0.2.1
   ```
   👉 Explication : recharge le réseau; l'IP et la route par défaut doivent apparaître.

## 2. Production — Contrôles

Réserver l'adresse dans l'IPAM (étape 49).

## 3. Production — Sécurité

Valider depuis la console : une erreur coupe l'accès SSH.

## Validation et retour arrière

- **Validation** : Le serveur répond sur la nouvelle IP.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)
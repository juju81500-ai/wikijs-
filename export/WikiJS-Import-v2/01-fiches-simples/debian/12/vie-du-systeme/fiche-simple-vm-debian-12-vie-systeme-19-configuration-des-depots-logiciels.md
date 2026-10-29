---
title: "Fiche Simple - VM Debian 12 Vie Systeme 19 Configuration Des Depots Logiciels"
description: "Définir les sources APT."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-19"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-19`

---

## Problème précis à résoudre

Définir les sources APT.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les sources (Debian 12 « bookworm ») :
   ```bash
   cat /etc/apt/sources.list
   ls /etc/apt/sources.list.d/
   apt-cache policy | head -20
   ```
   👉 Explication : doit lister `bookworm`, `bookworm-updates` et `bookworm-security`.

2. Exemple de `/etc/apt/sources.list` :
   ```bash
   sudo tee /etc/apt/sources.list >/dev/null <<'EOT'
   deb http://deb.debian.org/debian bookworm main
   deb http://deb.debian.org/debian bookworm-updates main
   deb http://security.debian.org/debian-security bookworm-security main
   EOT
   sudo apt update
   ```
   👉 Explication : remplace les sources par les dépôts officiels puis rafraîchit l'index.

## 2. Production — Contrôles

Utiliser un miroir ou proxy interne si le parc est important.

## 3. Production — Sécurité

Toute source tierce doit avoir sa clé dans `/etc/apt/keyrings/` (jamais `apt-key`).

## Validation et retour arrière

- **Validation** : `apt update` sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)
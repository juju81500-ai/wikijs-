---
title: "Fiche Simple - VM Debian 13 Vie Systeme 19 Configuration Des Depots Logiciels"
description: "Définir les sources APT."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian13", "vie-du-systeme", "cycle-de-vie", "etape-19"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-19`

---

## Problème précis à résoudre

Définir les sources APT.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les sources (Debian 13 « bookworm ») :
   ```bash
   cat /etc/apt/sources.list.d/debian.sources
   ls /etc/apt/sources.list /etc/apt/sources.list.d/
   apt-cache policy | head -20
   ```
   👉 Explication : Debian 13 installe les sources au format deb822 dans `debian.sources`; doit lister `trixie`, `trixie-updates` et `trixie-security`.

2. Exemple de `/etc/apt/sources.list.d/debian.sources` (format deb822) :
   ```bash
   sudo tee /etc/apt/sources.list.d/debian.sources >/dev/null <<'EOT'
   Types: deb
   URIs: http://deb.debian.org/debian
   Suites: trixie trixie-updates
   Components: main
   Signed-By: /usr/share/keyrings/debian-archive-keyring.pgp

   Types: deb
   URIs: http://security.debian.org/debian-security
   Suites: trixie-security
   Components: main
   Signed-By: /usr/share/keyrings/debian-archive-keyring.pgp
   EOT
   sudo apt update
   ```
   👉 Explication : remplace les sources par les dépôts officiels puis rafraîchit l'index.

3. Si un ancien `/etc/apt/sources.list` (format une ligne) subsiste, le convertir :
   ```bash
   sudo apt modernize-sources
   sudo apt update
   ```
   👉 Explication : APT 3.0 convertit les fichiers `.list` en `.sources` et garde une copie `.bak`; vérifier le résultat avant de supprimer la copie.

## 2. Production — Contrôles

Utiliser un miroir ou proxy interne si le parc est important.

## 3. Production — Sécurité

Toute source tierce doit avoir sa clé dans `/etc/apt/keyrings/` (jamais `apt-key`).

## Validation et retour arrière

- **Validation** : `apt update` sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)
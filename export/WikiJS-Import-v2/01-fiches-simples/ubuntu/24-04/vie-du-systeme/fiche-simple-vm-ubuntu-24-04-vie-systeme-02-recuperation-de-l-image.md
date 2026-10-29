---
title: "Fiche Simple - VM Ubuntu 24.04 Vie Systeme 02 Recuperation De L Image"
description: "Obtenir l'image officielle d'Ubuntu Server 24.04 LTS."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2404", "vie-du-systeme", "cycle-de-vie", "etape-02"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-02`

---

## Problème précis à résoudre

Obtenir l'image officielle d'Ubuntu Server 24.04 LTS.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO « live server », les sommes de contrôle et leur signature depuis releases.ubuntu.com (version 24.04 « noble » ; remplacer `24.04.X` par le nom exact de l'ISO publié sur la page) :
   ```bash
   mkdir -p ~/iso && cd ~/iso
   curl -fLO https://releases.ubuntu.com/24.04/ubuntu-24.04.X-live-server-amd64.iso
   curl -fLO https://releases.ubuntu.com/24.04/SHA256SUMS
   curl -fLO https://releases.ubuntu.com/24.04/SHA256SUMS.gpg
   ```
   👉 Explication : récupère l'image, sa somme de contrôle et la signature; vérifier le nom exact sur https://releases.ubuntu.com/24.04/ (architecture `arm64` : image `ubuntu-24.04.X-live-server-arm64.iso`, hébergée sur cdimage.ubuntu.com si absente de releases).

2. Ranger l'image dans le stockage ISO de l'hyperviseur (Proxmox : **Datacenter > Stockage > ISO Images > Upload**).
   👉 Explication : l'image devient sélectionnable à la création de la VM.

## 2. Production — Contrôles

Utiliser uniquement les sources officielles ou le miroir interne approuvé.

## 3. Production — Sécurité

Ne jamais utiliser une image tierce non vérifiée.

## Validation et retour arrière

- **Validation** : Fichier `.iso` présent et taille cohérente (`ls -lh`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
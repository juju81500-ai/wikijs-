---
title: "Fiche Simple - VM Ubuntu 24.04 Vie Systeme 12 Fuseau Horaire"
description: "Régler le fuseau."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2404", "vie-du-systeme", "cycle-de-vie", "etape-12"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-12`

---

## Problème précis à résoudre

Régler le fuseau.

## 1. Hors-Production (Lab / Test / POC)

1. Lister puis fixer le fuseau :
   ```bash
   timedatectl list-timezones | grep Europe/Paris
   sudo timedatectl set-timezone Europe/Paris
   timedatectl
   ```
   👉 Explication : règle le fuseau; l'horloge matérielle doit rester en UTC (`RTC in local TZ: no`).

## 2. Production — Contrôles

Utiliser UTC pour les serveurs d'une zone multi-site.

## 3. Production — Sécurité

Une heure fausse invalide certificats et journaux.

## Validation et retour arrière

- **Validation** : `timedatectl` affiche le bon fuseau.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
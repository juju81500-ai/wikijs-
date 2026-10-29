---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 31 Reduction De La Surface"
description: "Désactiver les services inutiles."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-31"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-31`

---

## Problème précis à résoudre

Désactiver les services inutiles.

## 1. Hors-Production (Lab / Test / POC)

1. Lister et désactiver (remplacer `SERVICE`) :
   ```bash
   systemctl list-unit-files --state=enabled
   sudo systemctl disable --now SERVICE
   sudo systemctl mask SERVICE
   ```
   👉 Explication : `mask` empêche aussi un démarrage indirect.

2. Lister les ports en écoute :
   ```bash
   sudo ss -tulpn
   ```
   👉 Explication : chaque port ouvert doit être justifié.

## 2. Production — Contrôles

Documenter chaque service conservé.

## 3. Production — Sécurité

Valider qu'aucune dépendance n'est cassée avant `mask`.

## Validation et retour arrière

- **Validation** : `ss -tulpn` ne montre que les ports prévus.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
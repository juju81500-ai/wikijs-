---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 40 Configuration Des Sauvegardes"
description: "Sauvegarder données et configuration."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-40"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_40_Configuration_Des_Sauvegardes

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 40 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-40`

---

## Problème précis à résoudre

Sauvegarder données et configuration.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarde fichier avec Borg (remplacer dépôt et chemins) :
   ```bash
   sudo apt install borgbackup
   export BORG_REPO=ssh://sauvegarde@srv-bkp/./depot
   borg create --stats ::{hostname}-{now} /etc /srv
   ```
   👉 Explication : crée une archive dédupliquée; la phrase secrète est lue depuis `BORG_PASSCOMMAND` ou saisie.

2. Copie hors site avec rclone :
   ```bash
   sudo apt install rclone
   rclone sync /srv/sauvegardes remote:bucket --dry-run
   ```
   👉 Explication : `--dry-run` simule avant le vrai transfert.

## 2. Production — Contrôles

Règle 3-2-1 : trois copies, deux supports, une hors site.

## 3. Production — Sécurité

Chiffrer et protéger les clés de sauvegarde séparément.

## Validation et retour arrière

- **Validation** : Restauration testée à l'étape 48.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
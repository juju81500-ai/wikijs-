---
title: "Fiche Simple - VM Debian 12 Vie Systeme 33 Securisation Des Systemes De"
description: "Restreindre les montages."
published: true
date: 2026-11-03T09:36:13Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-33"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : [[Glossary:VM]] Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-33`

---

## Problème précis à résoudre

Restreindre les montages.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler et éditer `/etc/fstab` :
   ```bash
   findmnt -no TARGET,OPTIONS /tmp /var/tmp /dev/shm
   sudoedit /etc/fstab
   ```
   👉 Explication : ajouter `nodev,nosuid,noexec` à `/tmp`, `/var/tmp`, `/dev/shm`.

2. Tester sans redémarrer :
   ```bash
   sudo mount -o remount /tmp
   sudo findmnt --verify
   ```
   👉 Explication : applique et vérifie `fstab`.

## 2. Production — Contrôles

Garder `/var/tmp` exécutable si une application l'exige.

## 3. Production — Sécurité

Une erreur dans `fstab` peut bloquer le démarrage : snapshot avant.

## Validation et retour arrière

- **Validation** : `findmnt --verify` sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Debian 12](/fr/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)
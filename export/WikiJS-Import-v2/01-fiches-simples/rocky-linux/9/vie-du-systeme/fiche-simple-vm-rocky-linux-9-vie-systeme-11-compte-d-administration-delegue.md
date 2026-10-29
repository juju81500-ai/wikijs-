---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 11 Compte D Administration Delegue"
description: "Créer un administrateur nominatif."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-11"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-11`

---

## Problème précis à résoudre

Créer un administrateur nominatif.

## 1. Hors-Production (Lab / Test / POC)

1. Créer l'utilisateur (remplacer `ADMIN1`) :
   ```bash
   sudo useradd -m -G wheel -s /bin/bash ADMIN1
   sudo passwd ADMIN1
   ```
   👉 Explication : le groupe `wheel` donne les droits sudo sur Rocky.

2. Contrôler les groupes :
   ```bash
   id ADMIN1
   ```
   👉 Explication : doit afficher `wheel`.

3. Tester sudo avec ce compte :
   ```bash
   su - ADMIN1 -c 'sudo -l'
   ```
   👉 Explication : liste les commandes autorisées.

## 2. Production — Contrôles

Un compte nominatif par administrateur, jamais de compte partagé.

## 3. Production — Sécurité

Imposer un mot de passe robuste et l'authentification par clé.

## Validation et retour arrière

- **Validation** : `sudo -l` fonctionne pour le compte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)
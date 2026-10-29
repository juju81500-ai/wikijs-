---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 18 Table D Hotes Locale"
description: "Compléter /etc/hosts si besoin."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-18"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-18`

---

## Problème précis à résoudre

Compléter `/etc/hosts` si besoin.

## 1. Hors-Production (Lab / Test / POC)

1. Éditer prudemment :
   ```bash
   sudoedit /etc/hosts
   getent hosts srv01
   ```
   👉 Explication : ajouter `192.0.2.10 srv01.exemple.lan srv01`; `getent` confirme la résolution.

## 2. Production — Contrôles

Utiliser le DNS plutôt que `/etc/hosts` pour tout hôte partagé.

## 3. Production — Sécurité

Un `/etc/hosts` modifié peut rediriger du trafic : surveiller ce fichier.

## Validation et retour arrière

- **Validation** : `getent hosts` renvoie l'entrée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
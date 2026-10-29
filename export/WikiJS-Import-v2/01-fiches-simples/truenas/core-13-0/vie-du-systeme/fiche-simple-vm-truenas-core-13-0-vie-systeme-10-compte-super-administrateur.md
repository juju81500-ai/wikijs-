---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 10 Compte Super Administrateur"
description: "Sécuriser le compte root."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-10"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-10`

---

## Problème précis à résoudre

Sécuriser le compte root.

## 1. Hors-Production (Lab / Test / POC)

1. Lors de l'installation, définir le mot de passe root (ne jamais le laisser vide). Changer : Compte > Utilisateurs > root > Modifier.
   ```sh
   midclt call user.query '[["username","=","root"]]' | head
   ```
   👉 Explication : vérifie le compte sans afficher le mot de passe.

2. Désactiver la connexion root SSH par mot de passe (étape 27).
   👉 Explication : root reste utilisable à la console et via la GUI.

## 2. Production — Contrôles

Mot de passe dans le coffre de l'équipe.

## 3. Production — Sécurité

Mot de passe long et unique ; limiter les accès GUI par adresse.

## Validation et retour arrière

- **Validation** : Connexion GUI réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
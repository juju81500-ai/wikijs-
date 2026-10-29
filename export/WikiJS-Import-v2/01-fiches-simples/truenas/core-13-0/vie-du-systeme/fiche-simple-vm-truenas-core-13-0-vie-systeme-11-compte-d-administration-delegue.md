---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 11 Compte D Administration Delegue"
description: "Créer des comptes nominatifs."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-11"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-11`

---

## Problème précis à résoudre

Créer des comptes nominatifs.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Compte > Utilisateurs > Ajouter (nom, mot de passe, groupe `wheel` pour sudo).
   ```sh
   midclt call user.create '{"username":"ADMIN1","full_name":"Prénom Nom","password":"MOT_DE_PASSE","group_create":true,"sudo":true}'
   ```
   👉 Explication : ADMIN1 est le compte ; MOT_DE_PASSE à saisir sans le conserver dans l'historique.

2. Contrôler :
   ```sh
   midclt call user.query '[["username","=","ADMIN1"]]' | head
   ```
   👉 Explication : compte créé.

## 2. Production — Contrôles

Un compte par personne.

## 3. Production — Sécurité

Moindre privilège ; pas de compte partagé.

## Validation et retour arrière

- **Validation** : Connexion de ADMIN1 réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 38 Isolation Des Comptes De"
description: "Séparer les accès par application."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-38"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-38`

---

## Problème précis à résoudre

Séparer les accès par application.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Compte > Utilisateurs > Ajouter un compte sans shell.
   ```sh
   midclt call user.create '{"username":"SVC_SAUVEGARDE","full_name":"Service","password_disabled":true,"shell":"/usr/sbin/nologin","group_create":true}'
   ```
   👉 Explication : SVC_SAUVEGARDE est le compte de service.

2. Donner les droits sur le seul dataset : Modifier les permissions.
   ```sh
   zfs get mountpoint POOL/DATASET
   ```
   👉 Explication : limite l'accès.

## 2. Production — Contrôles

Un compte par application.

## 3. Production — Sécurité

Pas de compte de service administrateur.

## Validation et retour arrière

- **Validation** : Les comptes n'ont pas de shell.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
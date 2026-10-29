---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 36 Integration A L Annuaire"
description: "Joindre Active Directory ou LDAP."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-36"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-36`

---

## Problème précis à résoudre

Joindre Active Directory ou LDAP.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Services d'annuaire > Active Directory (domaine, compte de jonction).
   ```sh
   midclt call activedirectory.config | head -20
   ```
   👉 Explication : affiche la configuration.

2. Contrôler :
   ```sh
   midclt call activedirectory.get_state
   wbinfo -u | head
   ```
   👉 Explication : état de jonction et utilisateurs.

## 2. Production — Contrôles

Vérifier DNS et NTP d'abord (écart maximum : 5 minutes).

## 3. Production — Sécurité

Compte de jonction dédié à droits limités.

## Validation et retour arrière

- **Validation** : Les utilisateurs du domaine sont visibles.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
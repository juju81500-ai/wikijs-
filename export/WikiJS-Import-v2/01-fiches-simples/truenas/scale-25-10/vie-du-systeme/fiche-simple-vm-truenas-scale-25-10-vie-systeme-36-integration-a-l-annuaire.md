---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 36 Integration A L Annuaire"
description: "Joindre le NAS à Active Directory ou LDAP."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-36"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-36`

---

## Problème précis à résoudre

Joindre le NAS à Active Directory ou LDAP.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Identifiants > Services d'annuaire > Configurer Active Directory (domaine, compte de jonction).
   ```bash
   sudo midclt call activedirectory.config | python3 -m json.tool | head -20
   ```
   👉 Explication : affiche l'état de la jonction.

2. Contrôler :
   ```bash
   sudo midclt call directoryservices.status
   wbinfo -u | head
   ```
   👉 Explication : état du service d'annuaire et liste des utilisateurs du domaine.

## 2. Production — Contrôles

Vérifier d'abord DNS et NTP (écart d'horloge maximum : 5 minutes).

## 3. Production — Sécurité

Utiliser un compte de jonction dédié à droits limités.

## Validation et retour arrière

- **Validation** : Les utilisateurs du domaine sont visibles.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
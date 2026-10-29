---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 24 Personnalisation Et Bannieres"
description: "Afficher un avertissement légal."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-24"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-24`

---

## Problème précis à résoudre

Afficher un avertissement légal.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Services > SSH > Options > Texte de bannière (Paramètres supplémentaires).
   ```sh
   midclt call ssh.config | grep -i banner
   ```
   👉 Explication : affiche la valeur actuelle.

2. Texte conseillé : « Accès réservé aux personnes autorisées. Les actions sont journalisées. »
   👉 Explication : avertissement légal.

## 2. Production — Contrôles

Valider le texte avec le juridique.

## 3. Production — Sécurité

Pas de version ni d'organisation dans la bannière.

## Validation et retour arrière

- **Validation** : Bannière affichée à la connexion SSH.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)
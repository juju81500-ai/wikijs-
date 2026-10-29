---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 24 Personnalisation Et Bannieres"
description: "Afficher un avertissement légal et identifier le NAS."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-24"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_24_Personnalisation_Et_Bannieres

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 24 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-24`

---

## Problème précis à résoudre

Afficher un avertissement légal et identifier le NAS.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Général > Paramètres > Texte de bannière de connexion (ou Services > SSH > Paramètres avancés > Bannière).
   ```bash
   sudo midclt call ssh.config | grep -i banner
   ```
   👉 Explication : affiche la configuration SSH ; la bannière se saisit dans le champ prévu.

2. Texte conseillé : « Accès réservé aux personnes autorisées. Les actions sont journalisées. »
   👉 Explication : message d'avertissement légal.

## 2. Production — Contrôles

Valider le texte avec le service juridique.

## 3. Production — Sécurité

Ne pas indiquer de version ni de nom d'organisation dans la bannière.

## Validation et retour arrière

- **Validation** : La bannière s'affiche à la connexion SSH.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
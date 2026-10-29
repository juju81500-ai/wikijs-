---
title: "Fiche Simple - VM Debian 12 Vie Systeme 47 Test De Resilience Et"
description: "Valider relance et alerte."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-47"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-47`

---

## Problème précis à résoudre

Valider relance et alerte.

## 1. Hors-Production (Lab / Test / POC)

1. Forcer l'arrêt d'un service critique (remplacer `SERVICE`) :
   ```bash
   sudo systemctl edit SERVICE
   ```
   👉 Explication : ajouter `Restart=always` et `RestartSec=5`.

2. Simuler la panne :
   ```bash
   sudo systemctl kill -s KILL SERVICE
   sleep 8
   systemctl is-active SERVICE
   ```
   👉 Explication : le service doit repartir seul et l'alerte se déclencher.

## 2. Production — Contrôles

Prévenir l'équipe avant le test.

## 3. Production — Sécurité

Faire le test hors production d'abord.

## Validation et retour arrière

- **Validation** : Alerte reçue et service relancé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)
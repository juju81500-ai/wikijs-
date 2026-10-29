---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 20 Mise A Jour Initiale"
description: "Mettre le NAS à jour dès l'installation."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-20"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-20`

---

## Problème précis à résoudre

Mettre le NAS à jour dès l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Mise à jour > Rechercher les mises à jour > Télécharger puis Appliquer.
   ```bash
   sudo midclt call update.check_available | python3 -m json.tool
   ```
   👉 Explication : indique si une version est disponible.

2. Appliquer en ligne de commande :
   ```bash
   sudo midclt call update.update '{"reboot": true}' 
   ```
   👉 Explication : télécharge, installe et redémarre ; à lancer en fenêtre de maintenance.

3. Après redémarrage, vérifier la version :
   ```bash
   cat /etc/version
   sudo midclt call system.version
   ```
   👉 Explication : version SCALE installée.

## 2. Production — Contrôles

Sauvegarder la configuration avant (étape 40), puis planifier la mise à jour.

## 3. Production — Sécurité

Ne jamais couper l'alimentation pendant la mise à jour.

## Validation et retour arrière

- **Validation** : La version affichée est la cible.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
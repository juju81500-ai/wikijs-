---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 47 Test De Resilience Et"
description: "Valider qu'une panne déclenche une alerte."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-47"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_47_Test_De_Resilience_Et

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 47 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-47`

---

## Problème précis à résoudre

Valider qu'une panne déclenche une alerte.

## 1. Hors-Production (Lab / Test / POC)

1. Dans un lab, mettre un disque hors ligne : GUI Stockage > Gérer les périphériques > disque > Hors ligne.
   ```bash
   sudo zpool offline POOL sdX
   sudo zpool status POOL
   ```
   👉 Explication : le pool passe en DEGRADED ; une alerte doit arriver. N'exécuter qu'en lab.

2. Remettre le disque en ligne :
   ```bash
   sudo zpool online POOL sdX
   sudo zpool status POOL
   ```
   👉 Explication : resilver puis retour à ONLINE.

3. Tester l'envoi d'alerte : Système > Général > E-mail > Envoyer un e-mail test.
   ```bash
   sudo midclt call mail.send '{"subject":"Test","text":"Test d'alerte","to":["ADRESSE_MAIL"]}'
   ```
   👉 Explication : ADRESSE_MAIL est la boîte de l'équipe.

## 2. Production — Contrôles

Documenter le délai entre la panne et l'alerte.

## 3. Production — Sécurité

Ne jamais tester sur un pool de production sans redondance.

## Validation et retour arrière

- **Validation** : Alerte reçue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : TrueNAS SCALE 25.10 Supervision Alertes Pool](</01-fiches-simples/truenas/scale-25-10/vie-du-logiciel/supervision/fiche-simple-truenas-scale-25-10-supervision-alertes-pool>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
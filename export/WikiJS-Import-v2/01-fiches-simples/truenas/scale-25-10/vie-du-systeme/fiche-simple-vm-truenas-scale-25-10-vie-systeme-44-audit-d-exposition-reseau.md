---
title: "Fiche Simple - VM TrueNAS SCALE 25.10 Vie Systeme 44 Audit D Exposition Reseau"
description: "Vérifier ce qu'un poste distant voit."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenasscale2510", "vie-du-systeme", "cycle-de-vie", "etape-44"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_44_Audit_D_Exposition_Reseau

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 44 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-44`

---

## Problème précis à résoudre

Vérifier ce qu'un poste distant voit.

## 1. Hors-Production (Lab / Test / POC)

1. Depuis un autre poste du réseau :
   ```bash
   nmap -sS -p- -T4 ADRESSE_NAS
   ```
   👉 Explication : liste les ports vus de l'extérieur ; n'exécuter que sur un périmètre autorisé.

2. Tester les protocoles actifs :
   ```bash
   smbclient -L //ADRESSE_NAS -U ADMIN1
   showmount -e ADRESSE_NAS
   ```
   👉 Explication : liste des partages SMB et exports NFS visibles.

## 2. Production — Contrôles

Refaire l'audit après chaque changement de règles.

## 3. Production — Sécurité

Aucun port de stockage joignable depuis Internet.

## Validation et retour arrière

- **Validation** : Les résultats correspondent aux règles.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
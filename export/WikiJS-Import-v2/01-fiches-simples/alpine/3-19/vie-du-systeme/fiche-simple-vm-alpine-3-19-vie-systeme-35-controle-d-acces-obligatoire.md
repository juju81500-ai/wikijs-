---
title: "Fiche Simple - VM Alpine 3.19 Vie Systeme 35 Controle D Acces Obligatoire"
description: "Alpine n'active ni SELinux ni AppArmor par défaut; vérifier l'état et compenser."
published: true
date: 2026-10-29T20:22:10Z
tags: ["alpine319", "vie-du-systeme", "cycle-de-vie", "etape-35"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_35_Controle_D_Acces_Obligatoire

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-35`

---

## Problème précis à résoudre

Alpine n'active ni SELinux ni AppArmor par défaut; vérifier l'état et compenser.

## 1. Hors-Production (Lab / Test / POC)

1. Constater les modules de sécurité actifs :
   ```sh
   cat /sys/kernel/security/lsm 2>/dev/null || echo 'aucun module visible'
   cat /sys/module/apparmor/parameters/enabled 2>/dev/null
   ```
   👉 Explication : affiche la liste des modules de sécurité chargés dans le noyau.

2. Rechercher les paquets disponibles :
   ```sh
   apk search apparmor
   ```
   👉 Explication : indique ce qui est proposé en 3.19; l'activation demande d'ajouter `apparmor=1 security=apparmor` aux options noyau (`default_kernel_opts`, voir l'étape 15) et de tester.

3. Compenser par l'isolation : un compte de service par programme, et un système de fichiers en lecture seule pour les données statiques :
   ```sh
   ps -eo user,comm | sort | uniq -c | sort -rn | head
   ```
   👉 Explication : montre sous quel compte tourne chaque processus.

## 2. Production — Contrôles

Documenter que le contrôle d'accès obligatoire est absent et listé comme risque accepté.

## 3. Production — Sécurité

Ne jamais exécuter un service en `root` quand un compte dédié suffit (étape 38).

## Validation et retour arrière

- **Validation** : L'état des modules de sécurité est consigné.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)
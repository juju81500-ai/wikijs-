---
title: "LXC_Alpine_3.19_Systeme_Gestion-Services-OpenRC"
description: "Gérer le démarrage, l'arrêt, le redémarrage et le statut des services d'arrière-plan sous Alpine Linux avec le système d'initialisation ultraléger OpenRC."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[alpine-3.19]", "[openrc]", "[rc-service]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 LXC_Alpine_3.19_Systeme_Gestion-Services-OpenRC.md

- **Environnement** : Conteneur LXC / VM (Alpine Linux 3.19)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine
- **Catégorie** : Système / Gestionnaire de Services OpenRC
- **Tags** : `[alpine-3.19]`, `[openrc]`, `[rc-service]`, `[hardening]`

## 🎯 Problème précis à résoudre
Gérer le démarrage, l'arrêt, le redémarrage et le statut des services d'arrière-plan sous Alpine Linux avec le système d'initialisation ultraléger OpenRC.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Affichage du statut d'un service sous OpenRC :
   `rc-service sshd status`
   👉 Explication : Indique si le démon SSH est démarré ou arrêté.
2. Démarrage manuel temporaire d'un service :
   `rc-service sshd start`
   👉 Explication : Lance le service pour la session courante sans l'activer au boot.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ajout d'un service au niveau d'exécution standard (Runlevel `default`) :
   `rc-update add sshd default`
   👉 Explication : Configure OpenRC pour démarrer le service automatiquement lors du boot.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier les services actifs et les niveaux d'exécution configurés :
   ```sh
   rc-status -a
   rc-update show
   ```
   👉 Explication : Ne pas appliquer de `chmod -R` ou de `chown -R` à `/etc/init.d` ; les permissions des scripts sont gérées par les paquets.

2. N'activer au démarrage que les services requis par le rôle du conteneur, puis vérifier leur statut :
   ```sh
   rc-update add sshd default
   rc-service sshd status
   ```
   Remplacer `sshd` par le service choisi et retirer les services inutiles avec `rc-update del` après vérification des dépendances.
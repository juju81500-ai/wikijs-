---
title: "Fiche Simple - LXC Alpine 3.19 Systeme Fuseau Horaire"
description: "Configurer le fuseau horaire d'un conteneur Alpine Linux avec le paquet tzdata, en sachant que l'horloge système provient du noyau de l'hôte Proxmox."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[alpine3.19]", "[alpine]", "[lxc]", "[timezone]", "[tzdata]", "[ntp]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Fuseau_Horaire.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Système & Services / Date et heure
- **Tags** : `[alpine3.19]`, `[alpine]`, `[lxc]`, `[timezone]`, `[tzdata]`, `[ntp]`

## 🎯 Problème précis à résoudre
Configurer le fuseau horaire d'un conteneur Alpine Linux avec le paquet `tzdata`, en sachant que l'horloge système provient du noyau de l'hôte Proxmox.

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer la base de fuseaux horaires IANA :
   ```sh
   apk add tzdata
   ls /usr/share/zoneinfo/Europe/Paris
   ```
   👉 Explication : `tzdata` fournit les fichiers de fuseaux `/usr/share/zoneinfo/`; sans eux, aucun lien `/etc/localtime` valide ne peut être créé.

2. Afficher le fuseau actuel avant modification :
   ```sh
   date
   ls -l /etc/localtime
   cat /etc/timezone
   ```
   👉 Explication : `/etc/localtime` pointe vers le fuseau utilisé par les applications; `/etc/timezone` en garde le nom lisible.

3. Appliquer le fuseau `Europe/Paris` :
   ```sh
   ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime
   echo "Europe/Paris" > /etc/timezone
   date
   ```
   👉 Explication : Le lien symbolique change le fuseau appliqué par les processus lancés ensuite. Aucun redémarrage du conteneur n'est nécessaire.

---

## ⚡ 2. Production — Façon Simplifiée
1. Contrôler la synchronisation horaire de l'hôte Proxmox, car le conteneur utilise l'horloge du noyau de l'hôte :
   ```sh
   timedatectl status
   ```
   👉 Explication : À exécuter sur l'hôte Proxmox. Un conteneur ne règle pas l'heure matérielle; une dérive de l'hôte se répercute dans tous les CT.

2. Appliquer le fuseau dans le conteneur comme en laboratoire, puis vérifier :
   ```sh
   ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime
   echo "Europe/Paris" > /etc/timezone
   date
   ```
   👉 Explication : Le fuseau sert à l'affichage et aux journaux lisibles par un opérateur. Les paquets et le module `tzdata` restent installés, car les liens symboliques pointent vers ces fichiers.

---

## 🔒 3. Production — Façon Sécurisée
1. Conserver les horodatages transmis au SIEM et aux outils de corrélation en UTC pour éviter les ambiguïtés lors du passage à l'heure d'été :
   ```sh
   date -u
   ```
   👉 Explication : Le fuseau local ne doit pas modifier l'horodatage des événements de sécurité qui sont corrélés entre plusieurs machines.

2. Garder l'accès à la console Proxmox lors de la modification et noter le fuseau retenu dans la fiche serveur (étape 50 du cycle de vie).
---
title: "VM_Debian_13_Systeme_Creation-Swapfile-LVM"
description: "Créer et configurer un espace de mémoire virtuelle d'échange (Swap) sécurisé sous Debian 13, ajuster le paramètre swappiness et chiffrer l'espace swap au démarrage."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian13]", "[swap]", "[memory]", "[lvm]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_13_Systeme_Creation-Swapfile-LVM.md

- **Environnement** : VM (Debian 13)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Système & Mémoire / Fichier Swap & LVM
- **Tags** : `[debian13]`, `[swap]`, `[memory]`, `[lvm]`, `[hardening]`

## 🎯 Problème précis à résoudre
Créer et configurer un espace de mémoire virtuelle d'échange (Swap) sécurisé sous Debian 13, ajuster le paramètre `swappiness` et chiffrer l'espace swap au démarrage.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier la mémoire et l'espace du système de fichiers avant création :
   ```bash
   free -h
   df -h /
   swapon --show
   ```
2. Créer un nouveau fichier uniquement après confirmation qu'il n'existe pas déjà et qu'il y a assez d'espace :
   `sudo fallocate -l 2G /swapfile`
   👉 Explication : Si le système de fichiers ne prend pas en charge les extents requis, choisir une procédure adaptée ; ne pas utiliser une commande `dd` qui pourrait écraser un fichier existant.

3. Restreindre le fichier puis initialiser et activer le swap :
   `sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile`
   👉 Explication : Restreint l'accès au fichier, le structure en espace d'échange et l'active immédiatement en mémoire.

3. Vérification du statut de la mémoire swap :
   `swapon --show`
   👉 Explication : Affiche les espaces d'échange actifs et leur niveau de priorité.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder `/etc/fstab`, vérifier l'absence d'une entrée existante puis ajouter une seule ligne via `sudoedit` :
   ```text
   /swapfile none swap sw 0 0
   ```
   Valider avec `sudo findmnt --verify --verbose` avant redémarrage.

2. Optimisation du comportement d'échange dans `/etc/sysctl.d/99-swappiness.conf` :
   `echo -e "vm.swappiness = 10\nvm.vfs_cache_pressure = 50" > /etc/sysctl.d/99-swappiness.conf`
   👉 Explication : Réduit le recours au swap sur disque pour préserver les performances d'I/O et favoriser la RAM physique.

3. Appliquer les paramètres mémoire système :
   `sysctl --system`
   👉 Explication : Recharge immédiatement les variables noyau sans redémarrer le serveur.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Chiffrer le swap uniquement si le volume n'est pas déjà chiffré par la plateforme. Vérifier le périphérique réel et la configuration existante de `/etc/crypttab`; ne pas ajouter de ligne générique avec un nom de LV supposé.

2. Mise à jour de la table de montage `/etc/fstab` pour pointer vers le volume chiffré :
   Suivre la documentation Debian/LUKS pour le périphérique réel, sauvegarder les fichiers de configuration et valider `crypttab`/`fstab` avant redémarrage.
   👉 Si un swap chiffré temporaire est requis, suivre la documentation Debian/LUKS pour le périphérique réel, sauvegarder les fichiers de configuration et valider `crypttab`/`fstab` avant redémarrage.

3. Purge des résidus mémoire non chiffrés :
   Remplacement ou désactivation d'un swap existant : ne pas exécuter `swapoff -a` sur un système en charge. Le contenu peut ne pas tenir en RAM et provoquer un OOM. Désactiver un périphérique précis seulement après contrôle de `free -h` et pendant une fenêtre adaptée.
---
title: "VM_Debian_12_Stockage_Fstab-Options"
description: "Déclarer les montages persistants d'un serveur Debian 12 dans /etc/fstab par UUID, et appliquer les options nodev, nosuid et noexec sur les zones d'écriture publiques (/tmp, /var/tmp, /dev/shm) pour bloquer l'exécution de binaires déposés par un attaquant."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian12]", "[debian-family]", "[fstab]", "[mount]", "[uuid]", "[nodev]", "[nosuid]", "[noexec]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_12_Stockage_Fstab-Options.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Stockage & Système de fichiers / Montages sécurisés
- **Tags** : `[debian12]`, `[debian-family]`, `[fstab]`, `[mount]`, `[uuid]`, `[nodev]`, `[nosuid]`, `[noexec]`, `[hardening]`

## 🎯 Problème précis à résoudre
Déclarer les montages persistants d'un serveur Debian 12 dans `/etc/fstab` par UUID, et appliquer les options `nodev`, `nosuid` et `noexec` sur les zones d'écriture publiques (`/tmp`, `/var/tmp`, `/dev/shm`) pour bloquer l'exécution de binaires déposés par un attaquant.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Consultation des montages actuels :
   `findmnt -o TARGET,FSTYPE,OPTIONS /tmp /var/tmp /dev/shm`
   👉 Explication : Affiche le système de fichiers et les options réellement appliqués à chaque point de montage.
2. Relevé des identifiants UUID des partitions :
   `sudo blkid`
   👉 Explication : Liste les UUID à utiliser dans `/etc/fstab` à la place des noms de périphériques (`/dev/sdX`), plus stables après ajout de disques.
3. Lecture du fichier de montages :
   `cat /etc/fstab`
   👉 Explication : Montre les montages déclarés au démarrage ; vérifier qu'aucune ligne ne référence un périphérique absent.

---

## ⚡ 2. Production — Façon Simplifiée
1. Déclaration de `/tmp` en tmpfs durci :
   `sudoedit /etc/fstab`
   👉 Explication : Ajouter `tmpfs /tmp tmpfs defaults,nodev,nosuid,noexec,size=1G,mode=1777 0 0`, puis `tmpfs /dev/shm tmpfs defaults,nodev,nosuid,noexec 0 0`.
2. Application des montages :
   `sudo systemctl daemon-reload && sudo mount -a`
   👉 Explication : Recharge la configuration systemd puis monte tous les systèmes de fichiers déclarés ; une erreur ici indique une ligne `fstab` invalide.

---

## 🔒 3. Production — Façon Sécurisée (Partition de données dédiée)
1. Montage d'une partition de données par UUID avec options restrictives :
   `sudoedit /etc/fstab`
   👉 Explication : Ajouter `UUID=<uuid_partition_donnees> /srv/donnees ext4 defaults,nodev,nosuid,noexec 0 2`. Remplacer `<uuid_partition_donnees>` par la valeur relevée avec `sudo blkid -s UUID -o value /dev/<partition>`.
2. Validation complète du fichier fstab :
   `sudo findmnt --verify --verbose`
   👉 Explication : Contrôle la syntaxe et la cohérence de `/etc/fstab` avant tout redémarrage, pour éviter un boot bloqué en mode de secours.
3. Vérification des options appliquées :
   `findmnt -o TARGET,OPTIONS /srv/donnees /dev/shm`
   👉 Explication : Confirme la présence de `nodev`, `nosuid` et `noexec` sur les montages concernés.
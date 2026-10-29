---
title: "Fiche Simple - VM Debian 13 Stockage Creer RAID1 Mdadm"
description: "Créer un miroir logiciel RAID 1 avec deux partitions dédiées sous Debian, persister la configuration et surveiller l'état de synchronisation."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian13]", "[debian]", "[raid1]", "[mdadm]", "[stockage]", "[maintenance]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Debian_13_Stockage_Creer_RAID1_Mdadm.md

- **Environnement** : VM ou serveur Debian avec deux disques de données dédiés
- **OS / Version** : Debian 13 avec `mdadm`
- **Catégorie** : Stockage / Disponibilité
- **Tags** : `[debian13]`, `[debian]`, `[raid1]`, `[mdadm]`, `[stockage]`, `[maintenance]`

## 🎯 Problème précis à résoudre
Créer un miroir logiciel RAID 1 avec deux partitions dédiées sous Debian, persister la configuration et surveiller l'état de synchronisation.

> RAID améliore la disponibilité face à la panne d'un disque, mais ne remplace jamais une sauvegarde.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Installer l'outil et identifier deux partitions de même taille, vierges et dédiées à l'exercice :
   ```bash
   sudo apt update
   sudo apt install mdadm
   lsblk -o NAME,SIZE,FSTYPE,UUID,MOUNTPOINTS
   ```
   👉 Explication : `lsblk` permet de repérer les bonnes partitions avant toute écriture.

2. **La commande suivante écrase les métadonnées des partitions sélectionnées. Vérifier chaque périphérique avant de continuer.** Créer l'ensemble et suivre la synchronisation (remplacer `PARTITION1` et `PARTITION2`, par exemple `/dev/vdb1` et `/dev/vdc1`) :
   ```bash
   sudo mdadm --create --verbose /dev/md0 --level=1 --raid-devices=2 PARTITION1 PARTITION2
   cat /proc/mdstat
   sudo mdadm --detail /dev/md0
   ```
   👉 Explication : crée le miroir RAID 1 puis affiche l'avancement de la synchronisation et l'état `clean`.

3. Dans un lab vierge uniquement, créer un système de fichiers et le monter :
   ```bash
   sudo mkfs.ext4 /dev/md0
   sudo mkdir -p /srv/raid1
   sudo mount /dev/md0 /srv/raid1
   ```
   👉 Explication : rend le volume RAID utilisable; `mkfs` efface son contenu.

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder les données, identifier les disques par `lsblk`/`by-id`, et confirmer qu'aucune partition sélectionnée n'est montée ni utilisée.
2. Créer le miroir avec les partitions validées puis suivre sa synchronisation :
   ```bash
   sudo mdadm --create --verbose /dev/md0 --level=1 --raid-devices=2 /dev/<partition1> /dev/<partition2>
   watch cat /proc/mdstat
   sudo mdadm --detail /dev/md0
   ```
3. Enregistrer l'assemblage et régénérer l'initramfs :
   ```bash
   sudo mdadm --detail --scan | sudo tee -a /etc/mdadm/mdadm.conf
   sudo update-initramfs -u
   ```
4. Créer le système de fichiers seulement si le volume est neuf, puis monter par UUID et ajouter une entrée `/etc/fstab` validée avec `findmnt --verify`.
   👉 *Explication : ne pas recréer le système de fichiers lors d'une réutilisation d'un RAID contenant des données.*

## 🔒 3. Production — Façon Sécurisée
1. Utiliser des identifiants stables `/dev/disk/by-id` pour inventorier les disques et documenter leur numéro de série.
2. Ne pas débrancher un membre pendant la synchronisation; superviser les alertes et tester la procédure de remplacement sur du matériel de test.
3. Conserver une sauvegarde indépendante et vérifier régulièrement une restauration.

## ✅ Validation et retour arrière
- Confirmer l'état `clean` et deux membres actifs avec `mdadm --detail /dev/md0`, puis vérifier montage et écriture applicative.
- Une création incorrecte peut détruire des données; arrêter immédiatement les écritures et restaurer depuis une sauvegarde plutôt que recréer le tableau.
- Tester le démarrage après persistance dans une fenêtre de maintenance.
---
title: "Fiche Simple - VM pfSense Vie Systeme 04 Preparation Du Support D"
description: "Rendre l'image amorçable sur le matériel ou l'hyperviseur."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-04"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-04`

---

## Problème précis à résoudre

Rendre l'image amorçable sur le matériel ou l'hyperviseur.

## 1. Hors-Production (Lab / Test / POC)

1. Sur un matériel physique, identifier la clé USB puis y écrire l'image `Memstick` (remplacer `/dev/sdX`) :
   ```sh
   lsblk -o NAME,SIZE,MODEL,TRAN
   sudo dd if=pfSense-CE-memstick-VERSION-RELEASE-amd64.img of=/dev/sdX bs=4M status=progress oflag=sync
   ```
   👉 Explication : `/dev/sdX` est le disque entier de la clé (sans numéro de partition); une erreur effacerait un autre disque.

2. Sur un hyperviseur, attacher l'ISO comme lecteur CD-ROM de la VM (Proxmox : VM > Matériel > Lecteur CD/DVD > Utiliser un fichier ISO).
   👉 Explication : évite de créer une clé physique.

3. Pour un équipement sans écran, choisir l'image `Memstick Serial`.
   👉 Explication : l'installateur s'affiche sur le port série (115200 bauds).

## 2. Production — Contrôles

Utiliser le virtuel ou une image préparée pour les déploiements en série.

## 3. Production — Sécurité

Vérifier deux fois le périphérique cible avant `dd`.

## Validation et retour arrière

- **Validation** : L'écran de démarrage pfSense (menu de boot) apparaît.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
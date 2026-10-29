---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 20 Mise A Jour Initiale"
description: "Appliquer tous les correctifs."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-20"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-20`

---

## Problème précis à résoudre

Appliquer tous les correctifs.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour les métadonnées et les paquets :
   ```bash
   sudo dnf makecache
   sudo dnf -y upgrade
   ```
   👉 Explication : installe les correctifs publiés depuis l'ISO.

2. Vérifier si un redémarrage est requis :
   ```bash
   sudo dnf needs-restarting -r
   ```
   👉 Explication : code de sortie 1 = redémarrage nécessaire.

3. Redémarrer et contrôler le noyau :
   ```bash
   sudo reboot
   uname -r
   ```
   👉 Explication : valide l'activation du nouveau noyau.

## 2. Production — Contrôles

Prendre un snapshot avant la mise à jour et planifier la fenêtre.

## 3. Production — Sécurité

Les correctifs de sécurité doivent être appliqués avant toute exposition.

## Validation et retour arrière

- **Validation** : `dnf check-update` ne renvoie plus de paquet.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)
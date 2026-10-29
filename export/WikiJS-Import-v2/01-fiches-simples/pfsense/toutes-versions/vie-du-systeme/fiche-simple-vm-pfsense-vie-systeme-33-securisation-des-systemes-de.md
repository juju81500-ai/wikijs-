---
title: "Fiche Simple - VM pfSense Vie Systeme 33 Securisation Des Systemes De"
description: "Protéger la configuration et les points de restauration."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-33"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-33`

---

## Problème précis à résoudre

Protéger la configuration et les points de restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les droits du fichier de configuration :
   ```sh
   ls -l /cf/conf/config.xml
   ls -ld /cf/conf /cf/conf/backup
   ```
   👉 Explication : `config.xml` doit appartenir à `root` et ne pas être lisible par les autres.

2. Créer un environnement de démarrage ZFS : System > Boot Environments > Add, puis vérifier :
   ```sh
   bectl list
   zfs list -t snapshot | head
   ```
   👉 Explication : chaque environnement permet de revenir en arrière après une mise à jour.

## 2. Production — Contrôles

Limiter le nombre d'environnements conservés pour ne pas saturer le disque.

## 3. Production — Sécurité

Le fichier de configuration contient des secrets : droits stricts et sauvegardes chiffrées.

## Validation et retour arrière

- **Validation** : `config.xml` n'est accessible qu'à root.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
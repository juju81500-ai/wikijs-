---
title: "Fiche Simple - VM Ubuntu 24.04 Sauvegarde Test Restauration"
description: "Prouver qu'une sauvegarde BorgBackup d'un serveur Ubuntu Server 24.04 LTS est exploitable : lister les archives, restaurer un jeu de données dans un répertoire isolé et comparer les empreintes avec la source."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[borgbackup]", "[sauvegarde]", "[restauration]", "[pra]", "[sha256sum]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Sauvegarde_Test_Restauration

- **Environnement** : VM Ubuntu Server (dépôt de sauvegarde BorgBackup accessible)
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat) - BorgBackup 1.2.x depuis le dépôt Noble
- **Catégorie** : Sauvegarde / Validation PRA-DRP par restauration
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[borgbackup]`, `[sauvegarde]`, `[restauration]`, `[pra]`, `[sha256sum]`

## 🎯 Problème précis à résoudre
Prouver qu'une sauvegarde BorgBackup d'un serveur Ubuntu Server 24.04 LTS est exploitable : lister les archives, restaurer un jeu de données dans un répertoire isolé et comparer les empreintes avec la source.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer BorgBackup et lister les archives du dépôt de test :
   ```bash
   sudo apt update
   sudo apt install -y borgbackup
   borg list <chemin_depot_borg>
   ```
   👉 *Explication : `borg list` affiche le nom et la date de chaque archive. Le dépôt doit être initialisé avec `borg init` lors de la création initiale.*
2. Vérifier l'intégrité du dépôt de test :
   ```bash
   borg check --verify-data <chemin_depot_borg>
   ```
   👉 *Explication : `--verify-data` relit les données et contrôle leurs sommes ; l'opération est lente mais détecte la corruption silencieuse.*

## ⚡ 2. Production — Façon Simplifiée
1. Restaurer la dernière archive dans un répertoire isolé, jamais dans les chemins de production :
   ```bash
   sudo mkdir -p /srv/restauration-test
   sudo chmod 0700 /srv/restauration-test
   cd /srv/restauration-test && sudo borg extract <chemin_depot_borg>::<nom_archive>
   ```
   👉 *Explication : `borg extract` recrée l'arborescence de l'archive dans le répertoire courant. Le répertoire isolé évite d'écraser les données en service.*
2. Comparer les empreintes des fichiers restaurés avec la source :
   ```bash
   cd /srv/restauration-test && sudo find <chemin_des_donnees_restaurees> -type f -exec sha256sum {} + > /tmp/empreintes_restauration.txt
   wc -l /tmp/empreintes_restauration.txt
   ```
   👉 *Explication : Générer la même liste sur la source, puis comparer les deux fichiers avec `diff`. Toute différence signale une sauvegarde incomplète ou corrompue.*

## 🔒 3. Production — Façon Sécurisée
1. Mesurer le temps réel de restauration, qui est l'indicateur clé du PRA :
   ```bash
   time sudo borg extract <chemin_depot_borg>::<nom_archive> <chemin_des_donnees>
   ```
   👉 *Explication : Le temps mesuré doit être comparé au RTO (délai maximal de reprise) défini par le plan de reprise.*
2. Consigner le résultat dans le dossier d'exploitation : nom de l'archive, date du test, empreintes comparées, durée mesurée et opérateur.
   👉 *Explication : Une restauration non tracée ne prouve pas la capacité de reprise à l'audit.*

## ✅ Validation et retour arrière
- Le test est réussi si `diff` ne renvoie aucune différence entre les empreintes source et restaurées.
- Nettoyer l'environnement de test : `sudo rm -rf /srv/restauration-test /tmp/empreintes_restauration.txt`.
- Aucune restauration ne doit être réalisée sur les chemins de production sans procédure validée ; en cas de restauration réelle, sauvegarder d'abord l'état actuel.
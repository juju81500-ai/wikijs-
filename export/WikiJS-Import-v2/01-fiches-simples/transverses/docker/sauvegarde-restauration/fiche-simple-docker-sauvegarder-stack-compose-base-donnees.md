---
title: "Fiche Simple - Docker Sauvegarder Stack Compose Base Donnees"
description: "Créer une sauvegarde cohérente d'une application Compose avec base de données et fichiers persistants, puis vérifier sa restauration dans un projet isolé."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[docker]", "[compose]", "[postgresql]", "[sauvegarde]", "[restauration]", "[maintenance]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_Docker_Sauvegarder_Stack_Compose_Base_Donnees.md

- **Environnement** : Hôte Docker Linux avec une application Compose et une base PostgreSQL d'exemple
- **OS / Version** : Docker Engine, Compose v2; adapter les commandes à la base réellement utilisée
- **Catégorie** : Sauvegarde / Restauration / Conteneurs
- **Tags** : `[docker]`, `[compose]`, `[postgresql]`, `[sauvegarde]`, `[restauration]`, `[maintenance]`

## 🎯 Problème précis à résoudre
Créer une sauvegarde cohérente d'une application Compose avec base de données et fichiers persistants, puis vérifier sa restauration dans un projet isolé.

> Exemple PostgreSQL : pour MariaDB/MySQL, employer l'outil natif approprié et une méthode cohérente avec le moteur. Une archive de volume seule ne remplace pas un dump de base testé.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identifier les noms des services et volumes du projet :
   ```bash
   docker compose ps
   docker volume ls
   docker compose config --services
   ```
2. Préparer un dossier de sauvegarde restreint et arrêter les services applicatifs qui écrivent dans la base ou les fichiers partagés :
   ```bash
   install -d -m 0700 ./backup
   docker compose stop app
   ```
3. Effectuer un dump PostgreSQL depuis le service DB, puis arrêter la base avant l'archivage des volumes :
   ```bash
   docker compose exec -T db sh -c 'exec pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB"' > ./backup/database.sql
   docker compose stop db
   ```
   👉 *Explication : remplacer `app`, `db`, `POSTGRES_USER` et `POSTGRES_DB` par le modèle du projet; ne jamais mettre le mot de passe dans la ligne de commande.*

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder les fichiers Compose source et l'inventaire des volumes; protéger les variables et secrets à part dans un coffre sécurisé.
2. Une fois les écrivains arrêtés et le dump terminé, archiver chaque volume de données arrêté :
   ```bash
   docker run --rm -v <volume-app>:/source:ro -v "$PWD/backup:/backup" alpine:3.20 sh -c 'tar czf /backup/app-data.tar.gz -C /source .'
   docker run --rm -v <volume-db>:/source:ro -v "$PWD/backup:/backup" alpine:3.20 sh -c 'tar czf /backup/db-data.tar.gz -C /source .'
   ```
3. Redémarrer la pile après sauvegarde et vérifier les fichiers produits :
   ```bash
   docker compose start db app
   ls -lh ./backup
   ```
4. Pour tester une restauration, utiliser un projet isolé et des volumes vides, restaurer les fichiers, importer `database.sql`, puis démarrer l'application et vérifier son fonctionnement.
   👉 *Explication : ne jamais restaurer les archives sur les volumes de production pour un test.*

## 🔒 3. Production — Façon Sécurisée
1. Chiffrer les sauvegardes contenant des données personnelles ou secrets, les stocker hors de l'hôte et appliquer une rétention documentée.
2. Pour les bases très actives, choisir une méthode de sauvegarde adaptée à la cohérence attendue (dump logique, sauvegarde physique ou mécanisme du fournisseur).
3. Ne pas archiver un fichier `.env` en clair dans la sauvegarde; sauvegarder les références aux secrets et documenter leur récupération depuis le coffre.

## ✅ Validation et retour arrière
- Vérifier le code de sortie du dump, l'intégrité de l'archive et réaliser une restauration complète dans un environnement isolé.
- Vérifier les comptes, permissions, données et parcours applicatifs après restauration.
- Ne supprimer ni les volumes ni la sauvegarde source tant que la restauration n'a pas été validée.
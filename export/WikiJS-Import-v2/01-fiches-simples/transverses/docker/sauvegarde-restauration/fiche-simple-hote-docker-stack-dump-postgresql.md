---
title: "Fiche Simple - Hote Docker Stack Dump PostgreSQL"
description: "Produire un dump logique d'une base PostgreSQL de la stack."
published: true
date: 2026-10-29T19:42:02Z
tags: ["docker", "compose", "sauvegarde", "postgresql", "dump"]
editor: markdown
dateCreated: 2026-10-29T19:42:02Z
dateModified: 2026-10-29T19:42:02Z
---

# Fiche_Simple_-_Hote_Docker_Stack_Dump_PostgreSQL.md

- **Environnement** : Hôte Linux Docker avec stacks Compose et volumes persistants
- **OS / Version** : Distribution maintenue; Docker Engine et Compose v2
- **Catégorie** : conteneurs / sauvegarde-restauration
- **Tags** : `docker`, `compose`, `sauvegarde`, `postgresql`, `dump`

---

## Problème précis à résoudre

Produire un dump logique d'une base PostgreSQL de la stack.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un répertoire de sauvegarde protégé :
   ```bash
   sudo install -d -m 0700 /var/backups/docker/mon-projet
   ```
   👉 Explication : seul root peut lire les sauvegardes.

2. Lancer le dump (service `db`, compte `wikijs`, base `wiki` : exemples à adapter) :
   ```bash
   sudo sh -c 'cd /opt/docker/mon-projet && docker compose exec -T db pg_dump -U wikijs -d wiki -Fc > /var/backups/docker/mon-projet/wiki.dump'
   ```
   👉 Explication : le dump est écrit au format personnalisé; aucun mot de passe n'est passé en argument.

3. Vérifier la lisibilité du dump :
   ```bash
   pg_restore --list /var/backups/docker/mon-projet/wiki.dump | head
   ```
   👉 Explication : si la table des matières s'affiche, le dump est exploitable.

4. Contrôler le code retour et la taille :
   ```bash
   ls -l /var/backups/docker/mon-projet/wiki.dump
   ```
   👉 Explication : un fichier vide signale un échec.

5. Pour MariaDB/MySQL, utiliser `mariadb-dump`/`mysqldump` avec les options de cohérence et une authentification sécurisée.
   👉 Explication : la méthode dépend du moteur de base.

## 2. Production — Contrôles

Planifier le dump, surveiller le code retour et copier hors hôte.

## 3. Production — Sécurité

- Ne pas passer de mot de passe en argument de commande.
- Garder le répertoire de dump en `0700`.

## Validation et retour arrière

- **Validation** : `pg_restore --list` lit le dump sans erreur.
- **Retour arrière** : Supprimer le fichier de dump incomplet et relancer.

## Si le problème n'est pas résolu

- [Docker — Volumes et sauvegarde/restauration](https://docs.docker.com/engine/storage/volumes/)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet — sauvegarder une base PostgreSQL](/02-fiches-completes/transverses/docker/autres/37-sauvegarde-restauration-stacks-docker#3-sauvegarder-une-base-postgresql)
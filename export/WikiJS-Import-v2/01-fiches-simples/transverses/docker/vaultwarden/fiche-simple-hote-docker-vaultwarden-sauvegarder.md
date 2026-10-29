---
title: "Fiche Simple - Hote Docker Vaultwarden Sauvegarder"
description: "Produire une sauvegarde cohérente des données Vaultwarden et la copier hors hôte."
published: true
date: 2026-10-29T19:40:03Z
tags: ["docker", "vaultwarden", "sauvegarde", "sqlite"]
editor: markdown
dateCreated: 2026-10-29T19:40:03Z
dateModified: 2026-10-29T19:40:03Z
---

# Fiche_Simple_-_Hote_Docker_Vaultwarden_Sauvegarder.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose, Vaultwarden SQLite derrière un reverse proxy HTTPS
- **OS / Version** : Hôte Linux + Docker; image vaultwarden/server (tag à figer après validation)
- **Catégorie** : gestionnaire de mots de passe auto-hébergé
- **Tags** : `docker`, `vaultwarden`, `sauvegarde`, `sqlite`

---

## Problème précis à résoudre

Produire une sauvegarde cohérente des données Vaultwarden et la copier hors hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer la sauvegarde intégrée (ne pas copier le fichier SQLite actif) :
   ```bash
   docker exec -it vaultwarden /vaultwarden backup
   ```
   👉 Explication : la commande utilise l'API de sauvegarde SQLite et produit une copie cohérente.

2. Vérifier le fichier produit :
   ```bash
   ls -l vw-data
   ```
   👉 Explication : on repère l'emplacement du fichier de sauvegarde, à côté de `db.sqlite3`.

3. Copier hors hôte, sur un stockage chiffré, la sauvegarde ainsi que `attachments`, `sends`, `config.json` et les fichiers `rsa_key*`.
   👉 Explication : l'outil de copie peut être Restic ou Borg.

4. Ne pas se reposer sur des snapshots de système de fichiers ou de VM.
   👉 Explication : le projet les déconseille pour SQLite actif.

## 2. Production — Contrôles

Planifier la sauvegarde, tester sa restauration et définir une rétention.

## 3. Production — Sécurité

- Protéger les sauvegardes comme des secrets : elles contiennent des clés serveur.
- Chiffrer les copies hors hôte.

## Validation et retour arrière

- **Validation** : Le fichier de sauvegarde existe et sa copie hors hôte est lisible.
- **Retour arrière** : La sauvegarde ne modifie pas le service : supprimer le fichier produit si nécessaire.

## Si le problème n'est pas résolu

- [Vaultwarden — Using Docker Compose](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Vaultwarden — Backing up your vault](https://github.com/dani-garcia/vaultwarden/wiki/Backing-up-your-vault)
- [Guide — Sauvegarde de stacks Docker](/02-fiches-completes/transverses/docker/autres/37-sauvegarde-restauration-stacks-docker)
- [Guide complet — sauvegarder](/02-fiches-completes/transverses/docker/installation-deploiement/94-deploiement-vaultwarden-docker-compose#5-sauvegarder)
---
title: "Fiche Simple - VM Ubuntu 24.04 Graylog Installer MongoDB"
description: "Installer MongoDB 8.0 pour les métadonnées Graylog."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2404", "graylog", "datanode", "mongodb", "mongod"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Installer_MongoDB.md

- **Environnement** : Ubuntu Server 24.04: nœud Graylog + MongoDB et Data Node (laboratoire)
- **OS / Version** : Ubuntu Server 24.04 LTS; Graylog 7.2; MongoDB 8.0
- **Catégorie** : journaux / base de données
- **Tags** : `ubuntu2404`, `graylog`, `datanode`, `mongodb`, `mongod`

---

## Problème précis à résoudre

Installer MongoDB 8.0 pour les métadonnées Graylog.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer le dépôt MongoDB pour Ubuntu 24.04 (`noble`) puis installer `mongodb-org` :
   ```bash
   sudo apt update
   sudo apt install mongodb-org
   ```
   👉 Explication : suivre la procédure officielle MongoDB; vérifier la version avec la matrice Graylog.

2. Activer et démarrer le service :
   ```bash
   sudo systemctl enable --now mongod
   ```
   👉 Explication : démarrage au boot.

3. Contrôler l'état :
   ```bash
   sudo systemctl --no-pager status mongod
   ```
   👉 Explication : le service doit être actif et rester lié à l'interface locale.

## 2. Production — Contrôles

Activer l'authentification MongoDB et utiliser une URI authentifiée dans Data Node et Server.

## 3. Production — Sécurité

- Créer un compte de service limité à la base Graylog.
- Garder MongoDB lié à l'interface locale s'il est sur le même hôte.

## Validation et retour arrière

- **Validation** : `mongod` actif.
- **Retour arrière** : `sudo systemctl disable --now mongod`.

## Si le problème n'est pas résolu

- [Graylog 7.2 — installation Ubuntu](https://go2docs.graylog.org/current/downloading_and_installing_graylog/ubuntu_installation.htm)
- [Graylog — sécuriser l'environnement](https://go2docs.graylog.org/current/planning_your_deployment/secure_your_graylog_environment.htm)
- [MongoDB — installer sur Ubuntu](https://www.mongodb.com/docs/v8.0/tutorial/install-mongodb-on-ubuntu/)
- [Guide complet Graylog Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/49-deploiement-graylog-7-2-ubuntu-24-04#3-installer-mongodb-sur-le-nud-graylog)
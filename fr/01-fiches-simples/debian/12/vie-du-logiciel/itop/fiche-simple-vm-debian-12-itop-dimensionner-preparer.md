---
title: "fiche-simple-vm-debian-12-itop-dimensionner-preparer"
description: "Vérifier prérequis et ressources avant d'installer iTop."
published: true
date: 2026-11-03T14:22:28Z
tags: ["debian12", "itop", "itsm", "cmdb", "apache", "mariadb"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# fiche-simple-vm-debian-12-itop-dimensionner-preparer.md

- **Environnement** : [[Glossary:VM]] Linux dédiée avec Apache, PHP 8.2 ou 8.3 et MariaDB 10.11 (serveur [[Glossary:ITSM]]/CMDB)
- **OS / Version** : Debian 12 Bookworm (ou Ubuntu Server 24-04 [[Glossary:LTS]]); iTop Community 3.3.0
- **Catégorie** : ITSM / [[Glossary:CMDB]] / helpdesk
- **Tags** : `debian12`, `itop`, `itsm`, `cmdb`, `apache`, `mariadb`

---

## Problème précis à résoudre

Vérifier prérequis et ressources avant d'installer iTop.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les ressources de la VM :
   ```bash
   nproc
   free -h
   df -h /var
   ```
   👉 Explication : la recommandation éditeur (moins de 5 000 tickets/mois, 50 utilisateurs console, 200 000 CI) est 4 vCPU, 8 Go de [[Glossary:RAM]] et 20 Go pour la base.

2. Contrôler le système :
   ```bash
   cat /etc/os-release
   ```
   👉 Explication : iTop 3.3 recommande Debian 12 ou Ubuntu 24-04.

3. Préparer nom [[Glossary:DNS]], certificat [[Glossary:TLS]], [[Glossary:IP]] fixe, [[Glossary:SMTP]], compte de service et sauvegarde testée.
   👉 Explication : ces éléments doivent exister avant d'ouvrir l'application.

4. Vérifier le nom DNS prévu (remplacer `itsm.example.net` par le nom réel) :
   ```bash
   getent hosts itsm.example.net
   ```
   👉 Explication : le nom doit pointer vers la VM.

## 2. Production — Contrôles

Installer sur un hôte dédié avec sauvegarde testée; adapter les ressources au volume réel.

## 3. Production — Sécurité

- Ne pas exposer `/setup` à Internet après l'assistant.

## Validation et retour arrière

- **Validation** : ressources suffisantes, DNS résolu, prérequis (TLS, SMTP) prêts.
- **Retour arrière** : aucune modification n'est faite par cette fiche; rien à annuler.

## Si le problème n'est pas résolu

- [iTop — prérequis](https://www.itophub.io/wiki/page?id=latest:install:requirements)
- [iTop — installation et mise à niveau](https://www.itophub.io/wiki/page?id=latest:install:start)
- [Guide complet](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/40-deploiement-itop-3-3-debian12-ubuntu2404#1-dimensionner-et-preparer)
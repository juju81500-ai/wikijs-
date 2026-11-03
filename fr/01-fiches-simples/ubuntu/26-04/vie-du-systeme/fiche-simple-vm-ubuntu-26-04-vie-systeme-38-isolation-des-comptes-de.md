---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 38 Isolation Des Comptes De"
description: "Exécuter les services sans privilèges."
published: true
date: 2026-11-03T09:36:13Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-38"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : [[Glossary:VM]] Ubuntu Server 26-04 [[Glossary:LTS]]
- **OS / Version** : Ubuntu 26-04; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-38`

---

## Problème précis à résoudre

Exécuter les services sans privilèges.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte système sans shell (remplacer `svc-app`) :
   ```bash
   sudo useradd -r -s /usr/sbin/nologin -d /var/lib/svc-app svc-app
   id svc-app
   ```
   👉 Explication : compte non interactif réservé au service.

2. Appliquer dans l'unité systemd :
   ```bash
   sudo systemctl edit svc-app.service
   ```
   👉 Explication : ajouter `User=svc-app`, `NoNewPrivileges=yes`, `ProtectSystem=strict`.

## 2. Production — Contrôles

Un compte par service.

## 3. Production — Sécurité

Ne jamais donner de shell ni de sudo.

## Validation et retour arrière

- **Validation** : `ps -o user= -C svc-app` montre le compte dédié.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Ubuntu 26-04 LibreNMS Compte Service Code](/fr/01-fiches-simples/ubuntu/26-04/vie-du-logiciel/librenms/fiche-simple-vm-ubuntu-26-04-librenms-compte-service-code)
- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Ubuntu 26-04](/fr/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
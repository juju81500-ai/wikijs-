---
title: "Fiche Simple - VM Debian 13 Vie Systeme 38 Isolation Des Comptes De"
description: "Exécuter les services sans privilèges."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian13", "vie-du-systeme", "cycle-de-vie", "etape-38"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-38`

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

- [Fiche détaillée : VM Debian 13 Zeek Compte Service](</01-fiches-simples/debian/13/vie-du-logiciel/zeek/fiche-simple-vm-debian-13-zeek-compte-service>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)
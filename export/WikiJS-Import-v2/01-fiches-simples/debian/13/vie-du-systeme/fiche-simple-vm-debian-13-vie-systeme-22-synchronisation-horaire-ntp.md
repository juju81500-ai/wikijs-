---
title: "Fiche Simple - VM Debian 13 Vie Systeme 22 Synchronisation Horaire Ntp"
description: "Garder l'heure exacte."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian13", "vie-du-systeme", "cycle-de-vie", "etape-22"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-22`

---

## Problème précis à résoudre

Garder l'heure exacte.

## 1. Hors-Production (Lab / Test / POC)

1. Installer chrony :
   ```bash
   sudo apt install chrony
   sudoedit /etc/chrony/chrony.conf
   ```
   👉 Explication : ajouter `server ntp.exemple.lan iburst` (remplacer par le serveur interne).

2. Activer et contrôler :
   ```bash
   sudo systemctl enable --now chrony
   chronyc tracking
   chronyc sources -v
   ```
   👉 Explication : affiche le décalage et la source de temps.

## 2. Production — Contrôles

Deux sources internes, pas de dépendance directe à Internet.

## 3. Production — Sécurité

Autoriser seulement UDP 123 vers les serveurs de temps.

## Validation et retour arrière

- **Validation** : `chronyc tracking` : décalage faible, `Leap status: Normal`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)
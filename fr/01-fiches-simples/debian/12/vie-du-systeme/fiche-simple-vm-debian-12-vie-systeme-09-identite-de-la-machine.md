---
title: "Fiche Simple - VM Debian 12 Vie Systeme 09 Identite De La Machine"
description: "Nommer la machine."
published: true
date: 2026-11-03T09:36:13Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-09"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : [[Glossary:VM]] Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Nommer la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Définir le nom et vérifier (remplacer `srv01.exemple.lan`) :
   ```bash
   sudo hostnamectl set-hostname srv01.exemple.lan
   hostnamectl
   hostname -f
   ```
   👉 Explication : fixe le nom d'hôte; `hostname -f` doit renvoyer le [[Glossary:FQDN]].

2. Aligner `/etc/hosts` :
   ```bash
   grep -n 127.0.1.1 /etc/hosts
   ```
   👉 Explication : la ligne `127.0.1.1 srv01.exemple.lan srv01` doit exister.

## 2. Production — Contrôles

Respecter la convention de nommage de l'organisation et inscrire le nom au [[Glossary:DNS]].

## 3. Production — Sécurité

Éviter les noms qui révèlent le rôle ou la version.

## Validation et retour arrière

- **Validation** : `hostname -f` renvoie le FQDN attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Debian 12](/fr/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)
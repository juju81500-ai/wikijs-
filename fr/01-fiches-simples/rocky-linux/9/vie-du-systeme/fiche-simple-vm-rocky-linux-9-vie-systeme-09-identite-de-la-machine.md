---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 09 Identite De La Machine"
description: "Donner un nom stable et complet."
published: true
date: 2026-11-03T09:36:13Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-09"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : [[Glossary:VM]] Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Donner un nom stable et complet.

## 1. Hors-Production (Lab / Test / POC)

1. Définir le nom complet (remplacer `SRV01.EXEMPLE.LAN` par le [[Glossary:FQDN]] voulu) :
   ```bash
   sudo hostnamectl set-hostname SRV01.EXEMPLE.LAN
   ```
   👉 Explication : écrit `/etc/hostname`.

2. Contrôler :
   ```bash
   hostnamectl
   hostname -f
   ```
   👉 Explication : affiche le nom statique et le FQDN.

3. Déclarer le nom dans le [[Glossary:DNS]] et la [[Glossary:CMDB]].
   👉 Explication : le nom doit se résoudre depuis le réseau.

## 2. Production — Contrôles

Respecter la convention de nommage de l'entreprise.

## 3. Production — Sécurité

Ne pas exposer d'information sensible dans le nom.

## Validation et retour arrière

- **Validation** : `hostname -f` renvoie le FQDN attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Rocky Linux 9](/fr/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)
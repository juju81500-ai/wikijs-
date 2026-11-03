---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 42 Journaux Rotation Et Centralisation"
description: "Maîtriser et exporter les journaux."
published: true
date: 2026-11-03T09:36:13Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-42"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_42_Journaux_Rotation_Et_Centralisation

- **Environnement** : [[Glossary:VM]] Ubuntu Server 26-04 [[Glossary:LTS]]
- **OS / Version** : Ubuntu 26-04; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-42`

---

## Problème précis à résoudre

Maîtriser et exporter les journaux.

## 1. Hors-Production (Lab / Test / POC)

1. Limiter journald :
   ```bash
   sudo mkdir -p /etc/systemd/journald.conf.d
   printf '[Journal]\nSystemMaxUse=500M\nStorage=persistent\n' | sudo tee /etc/systemd/journald.conf.d/10-limite.conf
   sudo systemctl restart systemd-journald
   ```
   👉 Explication : journal persistant, 500 Mo maximum.

2. Envoyer à un collecteur avec rsyslog (remplacer l'hôte) :
   ```bash
   sudo apt install rsyslog
   echo '*.* @@collecteur.exemple.lan:514' | sudo tee /etc/rsyslog.d/90-forward.conf
   sudo systemctl restart rsyslog
   ```
   👉 Explication : `@@` = [[Glossary:TCP]]; utiliser [[Glossary:TLS]] selon la politique.

## 2. Production — Contrôles

Conserver selon la durée légale.

## 3. Production — Sécurité

Journaux protégés en écriture côté collecteur.

## Validation et retour arrière

- **Validation** : `journalctl --disk-usage` reste sous la limite.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Ubuntu 26-04](/fr/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
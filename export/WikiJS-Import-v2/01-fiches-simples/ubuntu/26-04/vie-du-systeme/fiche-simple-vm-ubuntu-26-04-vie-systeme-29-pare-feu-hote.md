---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 29 Pare Feu Hote"
description: "Filtrer les flux entrants avec UFW."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-29"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-29`

---

## Problème précis à résoudre

Filtrer les flux entrants avec UFW.

## 1. Hors-Production (Lab / Test / POC)

1. Définir la politique par défaut puis **autoriser SSH avant d'activer** (remplacer le réseau d'administration) :
   ```bash
   sudo ufw default deny incoming
   sudo ufw default allow outgoing
   sudo ufw allow from 192.0.2.0/24 to any port 22 proto tcp comment 'SSH admin'
   ```
   👉 Explication : trois règles enregistrées sans effet tant qu'UFW est inactif.

2. Activer puis contrôler :
   ```bash
   sudo ufw enable
   sudo ufw status verbose
   sudo ufw status numbered
   ```
   👉 Explication : active UFW au démarrage; ne jamais activer sans règle SSH testée depuis la console.

## 2. Production — Contrôles

Journaliser les refus (`sudo ufw logging on`) et conserver la console ouverte pendant l'application.

## 3. Production — Sécurité

Ne jamais appliquer `deny incoming` sans règle SSH testée.

## Validation et retour arrière

- **Validation** : `ufw status verbose` correspond au plan.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
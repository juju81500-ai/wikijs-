---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 22 Synchronisation Horaire Ntp"
description: "Garder l'heure exacte."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-22"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-22`

---

## Problème précis à résoudre

Garder l'heure exacte.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le client de temps en place (Ubuntu en fournit un par défaut) :
   ```bash
   timedatectl
   timedatectl timesync-status
   systemctl list-units --type=service | grep -Ei 'chrony|timesyncd|ntp'
   ```
   👉 Explication : `System clock synchronized: yes` attendu; la liste montre quel service de temps tourne (selon la version : `systemd-timesyncd` ou autre).

2. Installer chrony (remplace le client par défaut) et déclarer le serveur interne :
   ```bash
   sudo apt install chrony
   sudo tee /etc/chrony/sources.d/interne.sources >/dev/null <<'EOT'
   server ntp.exemple.lan iburst
   EOT
   sudo chronyc reload sources
   ```
   👉 Explication : remplacer `ntp.exemple.lan` par le serveur interne; `chrony` désactive le client précédent à l'installation.

3. Activer et contrôler :
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
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
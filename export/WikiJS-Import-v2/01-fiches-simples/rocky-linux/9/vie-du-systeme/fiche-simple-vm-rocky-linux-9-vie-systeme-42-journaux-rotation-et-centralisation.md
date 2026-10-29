---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 42 Journaux Rotation Et Centralisation"
description: "Conserver et centraliser les journaux."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-42"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_42_Journaux_Rotation_Et_Centralisation

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-42`

---

## Problème précis à résoudre

Conserver et centraliser les journaux.

## 1. Hors-Production (Lab / Test / POC)

1. Rendre journald persistant :
   ```bash
   sudo mkdir -p /var/log/journal
   sudo systemd-tmpfiles --create --prefix /var/log/journal
   sudo systemctl restart systemd-journald
   ```
   👉 Explication : conserve les journaux après redémarrage.

2. Limiter la taille :
   ```bash
   echo -e '[Journal]\nSystemMaxUse=500M' | sudo tee /etc/systemd/journald.conf.d/taille.conf
   sudo systemctl restart systemd-journald
   ```
   👉 Explication : évite de saturer `/var`.

3. Envoyer vers un serveur central avec rsyslog (adapter `LOG.EXEMPLE.LAN`) :
   ```bash
   echo '*.* @@LOG.EXEMPLE.LAN:514' | sudo tee /etc/rsyslog.d/90-central.conf
   sudo systemctl restart rsyslog
   ```
   👉 Explication : `@@` utilise TCP; préférer TLS en production.

## 2. Production — Contrôles

Conserver 90 jours minimum selon la politique.

## 3. Production — Sécurité

Protéger les journaux en écriture; ne pas y inscrire de secrets.

## Validation et retour arrière

- **Validation** : `journalctl --disk-usage` conforme et logs reçus au central.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)
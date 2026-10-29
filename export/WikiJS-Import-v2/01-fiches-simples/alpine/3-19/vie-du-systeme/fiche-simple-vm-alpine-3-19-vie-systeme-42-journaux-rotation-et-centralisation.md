---
title: "Fiche Simple - VM Alpine 3.19 Vie Systeme 42 Journaux Rotation Et Centralisation"
description: "Limiter la taille des journaux et les envoyer ailleurs."
published: true
date: 2026-10-29T20:22:10Z
tags: ["alpine319", "vie-du-systeme", "cycle-de-vie", "etape-42"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_42_Journaux_Rotation_Et_Centralisation

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-42`

---

## Problème précis à résoudre

Limiter la taille des journaux et les envoyer ailleurs.

## 1. Hors-Production (Lab / Test / POC)

1. Régler la rotation de `syslogd` (BusyBox) et l'envoi distant (remplacer `SERVEUR_LOG`) :
   ```sh
   doas sed -i 's|^SYSLOGD_OPTS=.*|SYSLOGD_OPTS="-t -s 1024 -b 7 -R SERVEUR_LOG:514"|' /etc/conf.d/syslog
   doas rc-service syslog restart
   ```
   👉 Explication : `-s 1024` fait tourner le fichier à 1 Mo, `-b 7` garde 7 anciens fichiers, `-R` envoie une copie au serveur distant.

2. Installer logrotate pour les journaux des services :
   ```sh
   doas apk add logrotate
   ls /etc/logrotate.d
   ```
   👉 Explication : `logrotate` est lancé par les tâches quotidiennes de `crond`.

3. Vérifier le journal :
   ```sh
   tail -n 20 /var/log/messages
   ```
   👉 Explication : montre les dernières lignes du journal du système.

## 2. Production — Contrôles

Fixer la durée de conservation selon la politique et la loi.

## 3. Production — Sécurité

Restreindre l'accès aux journaux (`root` et groupe d'audit).

## Validation et retour arrière

- **Validation** : La rotation fonctionne et le serveur distant reçoit les messages.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)
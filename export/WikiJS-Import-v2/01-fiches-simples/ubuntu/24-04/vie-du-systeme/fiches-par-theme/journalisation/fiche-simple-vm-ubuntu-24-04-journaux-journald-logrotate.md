---
title: "Fiche Simple - VM Ubuntu 24.04 Journaux Journald Logrotate"
description: "Rendre persistants les journaux systemd, borner leur taille et leur durée de conservation, et configurer la rotation des journaux d'une application dans /var/log sur Ubuntu Server 24.04 LTS, sans risquer de saturer le disque."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[journald]", "[journalctl]", "[logrotate]", "[logs]", "[retention]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Journaux_Journald_Logrotate

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat) - systemd 255, logrotate 3.21
- **Catégorie** : Journaux / Gestion, rotation et conservation
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[journald]`, `[journalctl]`, `[logrotate]`, `[logs]`, `[retention]`

## 🎯 Problème précis à résoudre
Rendre persistants les journaux systemd, borner leur taille et leur durée de conservation, et configurer la rotation des journaux d'une application dans `/var/log` sur Ubuntu Server 24.04 LTS, sans risquer de saturer le disque.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Mesurer l'espace occupé par les journaux systemd :
   ```bash
   journalctl --disk-usage
   ls -ld /var/log/journal
   ```
   👉 *Explication : Si `/var/log/journal` n'existe pas, les journaux sont volatils (en RAM) et disparaissent au redémarrage.*
2. Tester la rotation logrotate sans écrire de fichier :
   ```bash
   sudo logrotate -d /etc/logrotate.conf
   ```
   👉 *Explication : L'option `-d` (debug) simule la rotation et affiche les actions prévues, sans modifier les fichiers.*

## ⚡ 2. Production — Façon Simplifiée
1. Rendre les journaux persistants et limiter leur taille et leur durée :
   ```bash
   sudo mkdir -p /etc/systemd/journald.conf.d
   sudo tee /etc/systemd/journald.conf.d/99-retention.conf >/dev/null <<'EOF'
   [Journal]
   Storage=persistent
   SystemMaxUse=1G
   MaxRetentionSec=1month
   EOF
   sudo systemctl restart systemd-journald
   journalctl --disk-usage
   ```
   👉 *Explication : `Storage=persistent` crée l'espace persistant dans `/var/log/journal`. `SystemMaxUse` borne la taille totale ; `MaxRetentionSec` supprime les entrées plus anciennes qu'un mois.*
2. Créer la rotation d'un journal applicatif, par exemple `/var/log/<application>/*.log` :
   ```bash
   sudo install -o root -g root -m 0644 /dev/null /etc/logrotate.d/<application>
   sudo tee /etc/logrotate.d/<application> >/dev/null <<'EOF'
   /var/log/<application>/*.log {
       weekly
       rotate 8
       compress
       delaycompress
       missingok
       notifempty
       create 0640 <compte_service> adm
   }
   EOF
   sudo logrotate -d /etc/logrotate.d/<application>
   ```
   👉 *Explication : `create 0640` recrée le fichier avec les droits attendus après rotation. Le compte doit être celui qui écrit réellement dans le journal ; un mauvais propriétaire empêche l'application d'écrire.*

## 🔒 3. Production — Façon Sécurisée
1. Vérifier que la rotation force l'application à rouvrir ses fichiers, avec `postrotate` si le service l'exige :
   ```bash
   sudo logrotate -d /etc/logrotate.d/<application> 2>&1 | grep -i -E 'error|warning'
   ```
   👉 *Explication : Une rotation sans rechargement du service continue d'écrire dans l'ancien fichier, déplacé ; ajouter alors une directive `postrotate` appelant la commande de rechargement de l'application.*
2. Surveiller l'occupation et les erreurs de rotation :
   ```bash
   sudo systemctl status systemd-journald --no-pager
   sudo journalctl -u logrotate --since today --no-pager
   ```
   👉 *Explication : `logrotate` est déclenché par `logrotate.timer` ; ses erreurs apparaissent dans le journal de l'unité.*

## ✅ Validation et retour arrière
- Confirmer que `journalctl --disk-usage` reste sous `1G` après plusieurs jours.
- Forcer une rotation de test puis vérifier les fichiers `/var/log/<application>/` avec `sudo logrotate -f /etc/logrotate.d/<application>`.
- Retour arrière : `sudo rm /etc/systemd/journald.conf.d/99-retention.conf`, `sudo systemctl restart systemd-journald`, et `sudo rm /etc/logrotate.d/<application>`.
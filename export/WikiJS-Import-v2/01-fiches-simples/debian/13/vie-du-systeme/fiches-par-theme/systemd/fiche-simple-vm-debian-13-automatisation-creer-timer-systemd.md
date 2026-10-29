---
title: "Fiche Simple - VM Debian 13 Automatisation Creer Timer Systemd"
description: "Planifier une tâche récurrente avec une unité .timer systemd plutôt qu'un cron dispersé, et consulter ses exécutions dans journald."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian13]", "[debian]", "[systemd]", "[timer]", "[automatisation]", "[maintenance]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Debian_13_Automatisation_Creer_Timer_Systemd.md

- **Environnement** : VM ou serveur Debian 13
- **OS / Version** : Debian 13 avec systemd
- **Catégorie** : Automatisation / Services
- **Tags** : `[debian13]`, `[debian]`, `[systemd]`, `[timer]`, `[automatisation]`, `[maintenance]`

## 🎯 Problème précis à résoudre
Planifier une tâche récurrente avec une unité `.timer` systemd plutôt qu'un cron dispersé, et consulter ses exécutions dans journald.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Créer `/etc/systemd/system/lab-check.service` :
   ```ini
   [Unit]
   Description=Test de timer systemd

   [Service]
   Type=oneshot
   ExecStart=/usr/bin/logger -t lab-check Timer systemd execute
   ```
2. Créer `/etc/systemd/system/lab-check.timer` :
   ```ini
   [Unit]
   Description=Exécuter le test périodiquement

   [Timer]
   OnCalendar=*-*-* *:0/5:00
   Persistent=true

   [Install]
   WantedBy=timers.target
   ```
3. Vérifier le calendrier et activer le timer :
   ```bash
   sudo systemd-analyze verify /etc/systemd/system/lab-check.service /etc/systemd/system/lab-check.timer
   sudo systemctl daemon-reload
   sudo systemctl enable --now lab-check.timer
   systemctl list-timers lab-check.timer
   ```
   👉 *Explication : le service est lancé à la demande du timer; `Persistent=true` déclenche une exécution après démarrage si une échéance a été manquée.*

## ⚡ 2. Production — Façon Simplifiée
1. Remplacer `logger` par un script existant, exécutable et testé; utiliser des chemins absolus dans `ExecStart`.
2. Adapter `OnCalendar` au besoin, puis vérifier sa prochaine échéance :
   ```bash
   systemd-analyze calendar '*-*-* 02:15:00'
   sudo systemctl daemon-reload
   sudo systemctl enable --now mon-job.timer
   systemctl list-timers --all mon-job.timer
   ```
3. Lancer le service manuellement pour tester sans attendre le timer :
   ```bash
   sudo systemctl start mon-job.service
   sudo journalctl -u mon-job.service --since today --no-pager
   ```

## 🔒 3. Production — Façon Sécurisée
1. Exécuter le travail sous un compte dédié lorsque c'est possible et restreindre ses permissions aux seuls fichiers nécessaires.
2. Ne pas lancer un script téléchargé ou modifiable par un utilisateur non privilégié avec les droits root.
3. Ajouter des protections systemd seulement après validation de leurs effets sur le programme.

## ✅ Validation et retour arrière
- Vérifier le timer, son déclenchement et les journaux du service.
- Pour annuler, désactiver le `.timer`, puis sauvegarder et retirer les deux unités avant `systemctl daemon-reload`.
- Contrôler qu'aucune tâche cron doublon n'exécute déjà le même traitement.
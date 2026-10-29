---
title: "Fiche Simple - VM Ubuntu 26.04 LibreNMS Taches Journal"
description: "Activer les tâches planifiées, la commande lnms et la rotation des journaux."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2604", "librenms", "snmpv3", "nginx", "mariadb"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_LibreNMS_Taches_Journal.md

- **Environnement** : VM Ubuntu Server 26.04 dédiée à LibreNMS (Nginx, PHP-FPM, MariaDB, SNMP)
- **OS / Version** : Ubuntu Server 26.04 LTS; LibreNMS 26.10.2; PHP 8.5
- **Catégorie** : supervision / planification
- **Tags** : `ubuntu2604`, `librenms`, `snmpv3`, `nginx`, `mariadb`

---

## Problème précis à résoudre

Activer les tâches planifiées, la commande `lnms` et la rotation des journaux.

## 1. Hors-Production (Lab / Test / POC)

1. Installer `lnms` :
   ```bash
   sudo ln -s /opt/librenms/lnms /usr/bin/lnms
   sudo cp /opt/librenms/misc/lnms-completion.bash /etc/bash_completion.d/
   ```
   👉 Explication : Rend la commande `lnms` disponible avec complétion.

2. Planifier les tâches :
   ```bash
   sudo cp /opt/librenms/dist/librenms.cron /etc/cron.d/librenms
   sudo cp /opt/librenms/dist/librenms-scheduler.service \
     /opt/librenms/dist/librenms-scheduler.timer /etc/systemd/system/
   sudo systemctl enable --now librenms-scheduler.timer
   ```
   👉 Explication : Installe la planification cron et le timer systemd du scheduler.

3. Rotation des journaux :
   ```bash
   sudo cp /opt/librenms/misc/librenms.logrotate /etc/logrotate.d/librenms
   ```
   👉 Explication : Active la rotation des journaux.

## 2. Production — Contrôles

Vérifier que le timer apparaît dans `systemctl list-timers` et que les journaux sont rotatés.

## 3. Production — Sécurité

- Les tâches s'exécutent sous le compte `librenms`, pas root.

## Validation et retour arrière

- **Validation** : `systemctl status librenms-scheduler.timer` est actif.
- **Retour arrière** : `sudo systemctl disable --now librenms-scheduler.timer` puis supprimer `/etc/cron.d/librenms` et `/etc/logrotate.d/librenms`.

## Si le problème n'est pas résolu

- [LibreNMS — Installation](https://docs.librenms.org/Installation/Install-LibreNMS/)
- [Guide complet — étape 6](/02-fiches-completes/ubuntu/26-04/installation-deploiement/46-deploiement-librenms-26-10-2-ubuntu-26-04#6-programmer-les-taches-et-le-journal)
---
title: "Fiche Simple - VM Debian 12 iTop Activer Taches Planifiees"
description: "Activer cron.php pour SLA, notifications et tâches asynchrones sans mot de passe en ligne de commande."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "itop", "itsm", "cmdb", "apache", "mariadb"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_iTop_Activer_Taches_Planifiees.md

- **Environnement** : VM Linux dédiée avec Apache, PHP 8.2 ou 8.3 et MariaDB 10.11 (serveur ITSM/CMDB)
- **OS / Version** : Debian 12 Bookworm (ou Ubuntu Server 24.04 LTS); iTop Community 3.3.0
- **Catégorie** : ITSM / CMDB / helpdesk
- **Tags** : `debian12`, `itop`, `itsm`, `cmdb`, `apache`, `mariadb`

---

## Problème précis à résoudre

Activer `cron.php` pour SLA, notifications et tâches asynchrones sans mot de passe en ligne de commande.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'état des tâches avec le compte web :
   ```bash
   sudo -u www-data php /var/www/itop/webservices/cron.php --status_only=1
   ```
   👉 Explication : adapter le chemin si iTop est ailleurs.

2. Créer le fichier de paramètres hors du DocumentRoot :
   ```bash
   sudo install -d -o root -g www-data -m 0750 /etc/itop
   sudo install -o www-data -g www-data -m 0600 /dev/null /etc/itop/cron.params
   sudoedit /etc/itop/cron.params
   ```
   👉 Explication : le fichier n'est lisible que par le processus web.

3. Y inscrire un compte iTop dédié (remplacer SECRET_DEDIE par le secret réel, sans chevrons) :
   ```ini
   auth_user = itop-cron
   auth_pwd = SECRET_DEDIE
   ```
   👉 Explication : jamais le mot de passe dans la crontab.

4. Tester :
   ```bash
   sudo -u www-data /usr/bin/php /var/www/itop/webservices/cron.php --param_file=/etc/itop/cron.params --status_only=1
   ```
   👉 Explication : doit répondre sans erreur d'authentification.

5. Planifier chaque minute :
   ```bash
   sudoedit /etc/cron.d/itop
   ```
   👉 Explication : ouvre le fichier cron système.

6. Y ajouter la ligne :
   ```cron
   * * * * * www-data /usr/bin/php /var/www/itop/webservices/cron.php --param_file=/etc/itop/cron.params >> /var/log/itop-cron.log 2>&1
   ```
   👉 Explication : exécution par `www-data`, jamais root; prévoir la rotation de `/var/log/itop-cron.log`.

## 2. Production — Contrôles

Utiliser un compte iTop de privilèges minimaux dédié aux tâches d'arrière-plan et surveiller le journal cron.

## 3. Production — Sécurité

- `cron.params` hors DocumentRoot, mode 0600.
- Ne jamais mettre le mot de passe sur la ligne de commande.

## Validation et retour arrière

- **Validation** : la commande de statut s'exécute sans erreur et le journal `/var/log/itop-cron.log` se remplit.
- **Retour arrière** : supprimer `/etc/cron.d/itop` (`sudo rm /etc/cron.d/itop`) pour arrêter la planification.

## Si le problème n'est pas résolu

- [iTop — tâches planifiées](https://www.itophub.io/wiki/page?id=latest:admin:cron)
- [iTop — installation et mise à niveau](https://www.itophub.io/wiki/page?id=latest:install:start)
- [Guide complet](/02-fiches-completes/transverses/multi-os/installation-deploiement/40-deploiement-itop-3-3-debian12-ubuntu2404#6-activer-les-taches-planifiees)
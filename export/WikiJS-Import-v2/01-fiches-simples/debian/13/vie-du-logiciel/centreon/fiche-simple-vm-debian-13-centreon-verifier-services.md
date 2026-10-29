---
title: "Fiche Simple - VM Debian 13 Centreon Verifier Services"
description: "Contrôler que les services Centreon et la base tournent correctement."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "centreon", "supervision", "systemd", "journal"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Centreon_Verifier_Services.md

- **Environnement** : VM Debian 13 dédiée, serveur Centreon Central avec MariaDB locale
- **OS / Version** : Debian 13 Trixie; Centreon 26.10
- **Catégorie** : supervision / contrôle
- **Tags** : `debian13`, `centreon`, `supervision`, `systemd`, `journal`

---

## Problème précis à résoudre

Contrôler que les services Centreon et la base tournent correctement.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   sudo systemctl --no-pager status mariadb apache2 php8.4-fpm gorgoned cbd centengine
   ```
   👉 Explication : affiche l'état des services; adapter le nom du service PHP à la version installée par le dépôt Centreon.

2. Exécuter :
   ```bash
   sudo journalctl -b -p err --no-pager
   ```
   👉 Explication : liste les erreurs depuis le démarrage pour repérer un composant en défaut.

## 2. Production — Contrôles

Examiner les journaux des composants concernés; les services de trap SNMP peuvent rester inactifs s'ils ne sont pas utilisés.

## 3. Production — Sécurité

- Ne pas désactiver de service sans analyse.
- Ne pas copier les journaux contenant des secrets dans un ticket.

## Validation et retour arrière

- **Validation** : les services attendus sont actifs et aucune erreur bloquante n'apparaît.
- **Retour arrière** : aucune modification n'est faite; corriger le service en défaut puis le relancer.

## Si le problème n'est pas résolu

- [Centreon — installation unattended](https://docs.centreon.com/docs/installation/installation-of-a-central-server/unattended-install-central/)
- [Centreon — installation par paquets](https://docs.centreon.com/docs/installation/installation-of-a-central-server/using-packages/)
- [Guide complet Déployer Centreon 26.10 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/48-deploiement-centreon-26-10-debian-13#6-verifier-les-services)
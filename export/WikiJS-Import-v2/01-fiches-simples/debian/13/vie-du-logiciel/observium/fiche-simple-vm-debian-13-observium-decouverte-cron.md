---
title: "Fiche Simple - VM Debian 13 Observium Decouverte Cron"
description: "Lancer découverte et interrogation puis planifier le poller toutes les cinq minutes."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "observium", "poller", "discovery", "cron"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Observium_Decouverte_Cron.md

- **Environnement** : Observium Community sur Debian 13 (Apache/PHP, MariaDB, SNMPv3)
- **OS / Version** : Debian 13 Trixie x86-64; Observium Community
- **Catégorie** : supervision réseau / ordonnancement
- **Tags** : `debian13`, `observium`, `poller`, `discovery`, `cron`

---

## Problème précis à résoudre

Lancer découverte et interrogation puis planifier le poller toutes les cinq minutes.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer découverte et interrogation sur l'équipement pilote (nom d'exemple à remplacer par le nom ou l'identifiant dans Observium) :
   ```bash
   cd /opt/observium
   sudo ./discovery.php -h sw1.example.invalid
   sudo ./poller.php -h sw1.example.invalid
   ```
   👉 Explication : on confirme l'absence d'erreur SNMP, la création des RRD et la mise à jour des graphiques.

2. Créer `/etc/cron.d/observium` :
   ```bash
   sudoedit /etc/cron.d/observium
   ```
   👉 Explication : ce fichier de cron système contient un champ utilisateur.

3. Y placer ces lignes :
   ```bash
   */5 * * * * root /opt/observium/observium-wrapper poller >> /dev/null 2>&1
   */5 * * * * root /opt/observium/observium-wrapper discovery --host new >> /dev/null 2>&1
   33 */6 * * * root /opt/observium/observium-wrapper discovery >> /dev/null 2>&1
   ```
   👉 Explication : bloc à enregistrer dans le fichier : poller toutes les 5 minutes, découverte des nouveaux hôtes et découverte complète toutes les 6 heures; ne pas les copier dans `crontab -e`.

4. Attendre un cycle puis contrôler :
   ```bash
   sudo journalctl -u cron --since '15 minutes ago' --no-pager | tail
   sudo tail -n 20 /var/log/apache2/error.log
   ```
   👉 Explication : on vérifie l'exécution cron et l'absence d'erreurs PHP/Apache.

## 2. Production — Contrôles

Surveiller la fraîcheur des interrogations, erreurs SNMP, croissance MariaDB/RRD et espace disque.

## 3. Production — Sécurité

- Droits d'écriture web limités à `rrd` et `logs`.
- Ne pas élargir la découverte aux réseaux non autorisés.

## Validation et retour arrière

- **Validation** : le poller s'exécute toutes les cinq minutes et les graphiques de l'équipement progressent.
- **Retour arrière** : `sudo rm /etc/cron.d/observium` pour arrêter les tâches planifiées.

## Si le problème n'est pas résolu

- [Observium — installation Debian/Ubuntu](https://docs.observium.org/install_debian/)
- [Observium — prérequis logiciels](https://docs.observium.org/software_requirements/)
- [Observium — ajouter un équipement](https://docs.observium.org/add_device/)
- [Guide complet — étape 7](/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13#7-configurer-decouverte-interrogation-et-verification)
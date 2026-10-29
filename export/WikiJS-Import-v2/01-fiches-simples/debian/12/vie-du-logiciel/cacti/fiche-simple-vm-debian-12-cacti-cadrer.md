---
title: "Fiche Simple - VM Debian 12 Cacti Cadrer"
description: "Valider dimensionnement et prérequis avant d'installer Cacti 1.2.31."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "cacti", "snmp", "rrdtool", "mariadb"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_Cacti_Cadrer.md

- **Environnement** : VM Debian 12 dédiée (Apache, PHP, MariaDB, poller local)
- **OS / Version** : Debian 12 Bookworm; Cacti 1.2.31
- **Catégorie** : supervision / cadrage
- **Tags** : `debian12`, `cacti`, `snmp`, `rrdtool`, `mariadb`

---

## Problème précis à résoudre

Valider dimensionnement et prérequis avant d'installer Cacti 1.2.31.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les ressources de la VM :
   ```bash
   nproc
   free -h
   df -h /var
   ```
   👉 Explication : CPU, RAM et espace pour les fichiers RRD et la base doivent correspondre au nombre d'équipements et de graphes prévus.

2. Vérifier la version de Debian :
   ```bash
   cat /etc/os-release
   ```
   👉 Explication : confirme Debian 12 Bookworm.

3. Consulter la page des prérequis Cacti 1.2.31 (PHP, extensions, MariaDB, RRDtool, Composer) : https://docs.cacti.net/Requirements.md
   👉 Explication : on fige les versions de paquets sur ce que la release exige.

4. Préparer DNS, NTP, certificat TLS, stratégie de sauvegarde et un compte SNMP en lecture seule.
   👉 Explication : la collecte par polling impose une connectivité explicite vers les équipements autorisés.

## 2. Production — Contrôles

Choisir une release identifiée (pas de branche mobile) et vérifier sa provenance.

## 3. Production — Sécurité

- Ne pas utiliser un dépôt de branche mobile en production.
- Limiter UDP/161 aux sources nécessaires.

## Validation et retour arrière

- **Validation** : Dimensionnement, version et prérequis sont documentés.
- **Retour arrière** : Aucune installation n'est faite ici; rien à annuler.

## Si le problème n'est pas résolu

- [Cacti — documentation officielle](https://docs.cacti.net/)
- [Cacti — installation Ubuntu/Debian](https://docs.cacti.net/Installing-Under-Ubuntu-Debian.md)
- [Guide complet — 1. Cadrage et prérequis](/02-fiches-completes/debian/12/installation-deploiement/51-deploiement-cacti-1-2-31-debian-12#1-cadrage-et-prerequis)
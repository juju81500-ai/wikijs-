---
title: "fiche-simple-vm-debian-13-centreon-initialiser-supervision"
description: "Exporter la configuration et superviser d'abord localhost puis un hôte pilote."
published: true
date: 2026-11-03T14:22:28Z
tags: ["debian13", "centreon", "supervision", "poller", "snmp"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# fiche-simple-vm-debian-13-centreon-initialiser-supervision.md

- **Environnement** : [[Glossary:VM]] Debian 13 dédiée, serveur Centreon Central avec MariaDB locale
- **OS / Version** : Debian 13 Trixie; Centreon 26.10
- **Catégorie** : supervision / hôtes
- **Tags** : `debian13`, `centreon`, `supervision`, `poller`, `snmp`

---

## Problème précis à résoudre

Exporter la configuration et superviser d'abord localhost puis un hôte pilote.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Configuration > Pollers**, exporter la configuration du Central en cochant **Move Export Files**.
   👉 Explication : applique la configuration générée aux services de collecte.

2. Redémarrer les services de collecte/gestion nécessaires selon la procédure Centreon.
   👉 Explication : prend en compte la nouvelle configuration.

3. Contrôler les données et journaux de `localhost`, puis ajouter un hôte pilote autorisé.
   👉 Explication : valide la chaîne complète avant d'ajouter d'autres cibles.

4. Pour les équipements, utiliser SNMPv3 authPriv en lecture seule quand c'est possible.
   👉 Explication : évite les communautés publiques en clair.

## 2. Production — Contrôles

Limiter [[Glossary:UDP]]/161 aux pollers; les identifiants de supervision doivent être distincts des comptes d'administration.

## 3. Production — Sécurité

- Pas de communauté [[Glossary:SNMP]] publique.
- Comptes de supervision en lecture seule.
- Pas de cibles non autorisées.

## Validation et retour arrière

- **Validation** : localhost et l'hôte pilote apparaissent avec des données.
- **Retour arrière** : retirer l'hôte pilote de la configuration et ré-exporter.

## Si le problème n'est pas résolu

- [Centreon — installation Web et post-installation](https://docs.centreon.com/docs/installation/web-and-post-installation/)
- [Guide complet Déployer Centreon 26.10 sur Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/48-deploiement-centreon-26-10-debian-13#5-initialiser-la-supervision)
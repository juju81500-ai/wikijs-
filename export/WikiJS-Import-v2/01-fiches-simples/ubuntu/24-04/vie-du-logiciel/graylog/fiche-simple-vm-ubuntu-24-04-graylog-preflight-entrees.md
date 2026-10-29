---
title: "Fiche Simple - VM Ubuntu 24.04 Graylog Preflight Entrees"
description: "Terminer l'assistant initial et créer un premier input de test."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2404", "graylog", "datanode", "mongodb", "preflight", "syslog"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Preflight_Entrees.md

- **Environnement** : Ubuntu Server 24.04: nœud Graylog + MongoDB et Data Node (laboratoire)
- **OS / Version** : Ubuntu Server 24.04 LTS; Graylog 7.2; MongoDB 8.0
- **Catégorie** : journaux / entrées
- **Tags** : `ubuntu2404`, `graylog`, `datanode`, `mongodb`, `preflight`, `syslog`

---

## Problème précis à résoudre

Terminer l'assistant initial et créer un premier input de test.

## 1. Hors-Production (Lab / Test / POC)

1. Retrouver le mot de passe temporaire du preflight dans le journal initial :
   ```bash
   sudo journalctl -u graylog-server -b --no-pager | grep -i -A2 preflight
   ```
   👉 Explication : il est utilisé une seule fois pour l'assistant.

2. Ouvrir l'interface depuis le réseau d'administration (URL d'exemple à remplacer) et terminer le preflight : **http://192.0.2.10:9000 > Preflight**
   👉 Explication : l'assistant configure le Data Node; supprimer ensuite toute note du mot de passe temporaire.

3. Créer un input pour un flux de test autorisé : **System > Inputs > Select input > Syslog TCP/TLS > Launch new input**
   👉 Explication : ouvrir un seul hôte source, avec TLS pour les données sensibles; documenter port, format et règle de pare-feu.

## 2. Production — Contrôles

Documenter le port, le format, la source et la règle de pare-feu de chaque input.

## 3. Production — Sécurité

- Ne pas créer un listener ouvert à toutes les interfaces sans filtrage réseau.

## Validation et retour arrière

- **Validation** : preflight terminé et input de test en état Running.
- **Retour arrière** : **System > Inputs > Stop input / Delete input** pour retirer l'input de test.

## Si le problème n'est pas résolu

- [Graylog 7.2 — installation Ubuntu](https://go2docs.graylog.org/current/downloading_and_installing_graylog/ubuntu_installation.htm)
- [Graylog — sécuriser l'environnement](https://go2docs.graylog.org/current/planning_your_deployment/secure_your_graylog_environment.htm)
- [Guide complet Graylog Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/49-deploiement-graylog-7-2-ubuntu-24-04#6-terminer-le-preflight-et-activer-les-entrees)
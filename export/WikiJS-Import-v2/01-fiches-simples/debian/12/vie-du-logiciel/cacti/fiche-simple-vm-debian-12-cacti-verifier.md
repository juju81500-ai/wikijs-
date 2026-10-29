---
title: "Fiche Simple - VM Debian 12 Cacti Verifier"
description: "Contrôler services, base et collecte."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "cacti", "snmp", "rrdtool", "mariadb"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_Cacti_Verifier.md

- **Environnement** : VM Debian 12 dédiée (Apache, PHP, MariaDB, poller local)
- **OS / Version** : Debian 12 Bookworm; Cacti 1.2.31
- **Catégorie** : supervision / validation
- **Tags** : `debian12`, `cacti`, `snmp`, `rrdtool`, `mariadb`

---

## Problème précis à résoudre

Contrôler services, base et collecte.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les services et le journal Apache :
   ```bash
   sudo systemctl --no-pager status apache2 mariadb
   sudo journalctl -u apache2 -b --no-pager
   ```
   👉 Explication : les services doivent être `active (running)` et sans erreur.

2. Vérifier la base :
   ```bash
   sudo mariadb -e 'SHOW DATABASES LIKE "cacti";'
   ```
   👉 Explication : confirme que la base existe.

3. Dans Cacti, vérifier l'état du poller, les logs de collecte et la création des graphes.
   👉 Explication : la date de dernière collecte doit être récente.

4. Comparer les compteurs d'interface avec l'équipement source.
   👉 Explication : valide l'exactitude des données.

## 2. Production — Contrôles

Mettre en place une alerte si le poller ne s'exécute plus.

## 3. Production — Sécurité

- Contrôler que seuls les réseaux d'administration atteignent l'interface.

## Validation et retour arrière

- **Validation** : Services actifs, graphes alimentés et valeurs cohérentes.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [Cacti — documentation officielle](https://docs.cacti.net/)
- [Cacti — installation Ubuntu/Debian](https://docs.cacti.net/Installing-Under-Ubuntu-Debian.md)
- [Guide complet — 6. Vérifier](/02-fiches-completes/debian/12/installation-deploiement/51-deploiement-cacti-1-2-31-debian-12#6-verifier)
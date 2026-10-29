---
title: "Fiche Simple - VM Debian 13 Elastic Stack Cadrer"
description: "Vérifier que la VM et le réseau conviennent avant d'installer Elasticsearch et Kibana."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "elastic", "cadrage", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Elastic_Stack_Cadrer.md

- **Environnement** : Elasticsearch et Kibana sur Debian 13, nœud unique
- **OS / Version** : Debian 13; Elasticsearch et Kibana 9.5.x
- **Catégorie** : journalisation / cadrage
- **Tags** : `debian13`, `elastic`, `cadrage`, `securite`

---

## Problème précis à résoudre

Vérifier que la VM et le réseau conviennent avant d'installer Elasticsearch et Kibana.

## 1. Hors-Production (Lab / Test / POC)

1. Relever le système et les ressources :
   ```bash
   lsb_release -ds
   free -h
   nproc
   ```
   👉 Explication : Contrôle Debian 13 et mémoire/CPU disponibles pour la JVM d'Elasticsearch.

2. Relever l'espace disque disponible pour les index :
   ```bash
   df -h /var/lib
   ```
   👉 Explication : Les index grossissent avec le volume de logs; prévoir la capacité avant installation.

3. Vérifier que les ports Elastic ne sont pas déjà utilisés :
   ```bash
   sudo ss -tlnp | grep -E ':(9200|9300|5601)\b' || echo "ports libres"
   ```
   👉 Explication : 9200 (API), 9300 (transport) et 5601 (Kibana) doivent être libres et ne jamais être exposés sur Internet.

## 2. Production — Contrôles

Concevoir séparément rôles master/data/ingest, haute disponibilité, snapshots, capacité et rétention selon le débit de logs.

## 3. Production — Sécurité

- Ne pas exposer 9200 ni 9300 sur Internet.
- Placer Kibana derrière un proxy TLS ou limiter son accès aux administrateurs.
- Les deux composants doivent rester à la même version 9.5.x.

## Validation et retour arrière

- **Validation** : nœud unique dimensionné, ports libres, versions et architecture décidées.
- **Retour arrière** : aucune modification n'a été faite; rien à annuler.

## Si le problème n'est pas résolu

- [Elastic — paquet Debian Elasticsearch](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-debian-package)
- [Elastic — paquet Debian Kibana](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana-with-debian-package)
- [Guide complet Elastic_Stack Debian 13](/02-fiches-completes/debian/13/installation-deploiement/50-deploiement-elastic-stack-9-5-debian-13#1-cadrage)
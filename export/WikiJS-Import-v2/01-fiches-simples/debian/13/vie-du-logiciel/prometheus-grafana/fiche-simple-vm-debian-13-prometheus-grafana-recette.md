---
title: "Fiche Simple - VM Debian 13 Prometheus Grafana Recette"
description: "Confirmer l'état des services et des cibles avant de considérer la collecte opérationnelle."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "prometheus", "grafana", "health", "targets"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Prometheus_Grafana_Recette.md

- **Environnement** : serveur Prometheus/Grafana pilote et Node Exporter local
- **OS / Version** : Debian 13; Prometheus 3.15.1 et Grafana OSS
- **Catégorie** : supervision / recette
- **Tags** : `debian13`, `prometheus`, `grafana`, `health`, `targets`

---

## Problème précis à résoudre

Confirmer l'état des services et des cibles avant de considérer la collecte opérationnelle.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'état des services :
   ```bash
   sudo systemctl --no-pager status prometheus grafana-server
   ```
   👉 Explication : les deux services doivent être `active (running)`.

2. Contrôler la disponibilité de Prometheus :
   ```bash
   curl -fsS http://127.0.0.1:9090/-/ready
   ```
   👉 Explication : une réponse HTTP 200 confirme que le serveur accepte les requêtes.

3. Examiner l'état des cibles :
   ```bash
   curl -fsS http://127.0.0.1:9090/api/v1/targets | python3 -m json.tool | grep -E '"(job|health)"'
   ```
   👉 Explication : les jobs `prometheus` et `node` doivent avoir `"health": "up"`.

4. Interface Grafana : ouvrir **Explore**, choisir la datasource Prometheus et exécuter `up`, puis `node_memory_MemAvailable_bytes` et `node_filesystem_avail_bytes`.
   👉 Explication : des valeurs apparaissent pour la mémoire et le disque; vérifier aussi l'heure affichée avec le fuseau attendu.

5. Interface Prometheus ou Grafana : ouvrir **Status > Targets** (Prometheus) et confirmer qu'aucune cible hors périmètre n'est listée.
   👉 Explication : toute cible inattendue doit être retirée de `prometheus.yml`.

## 2. Production — Contrôles

Définir sondes de disponibilité, alertes opérationnelles, seuils, rotation d'astreinte et revue régulière des cibles non disponibles.

## 3. Production — Sécurité

- Les endpoints et sorties API peuvent révéler les cibles internes; restreindre l'accès.
- Ne pas publier des résultats contenant des noms d'hôtes sensibles.
- Ne pas assimiler un endpoint `UP` à une supervision complète ou à une détection d'incident.
- Ne pas ignorer silencieusement les cibles qui échouent.

## Validation et retour arrière

- **Validation** : services actifs, targets attendues `UP`, données visibles et absence de cible imprévue.
- **Retour arrière** : isoler le job de test en modifiant la configuration validée, puis recharger après `promtool check config`.

## Si le problème n'est pas résolu

- [Prometheus — expression browser et API](https://prometheus.io/docs/prometheus/latest/querying/api/)
- [Prometheus — Node Exporter](https://prometheus.io/docs/guides/node-exporter/)
- [Guide complet Prometheus/Grafana Debian 13](/02-fiches-completes/debian/13/installation-deploiement/45-deploiement-prometheus-grafana-debian-13#6-recette)
---
title: "Fiche Simple - VM Debian 13 K3s Cadrer"
description: "Définir une topologie K3s cohérente avant installation : nombre de serveurs et d'agents, datastore, réseaux, CNI, stockage, ingress, sauvegarde et accès API."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "k3s", "kubernetes", "cadrage", "architecture"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_K3s_Cadrer.md

- **Environnement** : VM ou cluster Debian dédié; cibles et réseaux autorisés
- **OS / Version** : Debian 13; version K3s à confirmer dans la matrice officielle
- **Catégorie** : Kubernetes / K3s / cadrage
- **Tags** : `debian13`, `k3s`, `kubernetes`, `cadrage`, `architecture`

---

## Problème précis à résoudre

Définir une topologie K3s cohérente avant installation : nombre de serveurs et d'agents, datastore, réseaux, CNI, stockage, ingress, sauvegarde et accès API.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'état des hôtes pilotes :
   ```bash
   cat /etc/os-release | grep -E '^(PRETTY_NAME|VERSION_ID)='
   nproc; free -h; df -h /var/lib
   timedatectl show -p NTPSynchronized --value
   ```
   👉 Explication : on confirme la version de Debian, les ressources disponibles et l'heure synchronisée.

2. Vérifier les adresses et la résolution de noms :
   ```bash
   ip -br addr
   ip route
   getent hosts $(hostname -f)
   ```
   👉 Explication : les adresses des nœuds doivent être fixes et ne pas chevaucher les réseaux pods/services (K3s utilise `10.42.0.0/16` et `10.43.0.0/16` par défaut).

3. Vérifier les ports de l'API et des composants avant installation :
   ```bash
   sudo ss -tlnp | grep -E ':(6443|10250)\b' || echo "ports libres"
   ```
   👉 Explication : `6443` (API) et `10250` (kubelet) doivent être libres; pour la HA avec etcd intégré, prévoir aussi `2379-2380` entre serveurs.

4. Consigner les décisions dans un document : version K3s, nombre de serveurs, datastore, CNI, ingress, stockage.
   👉 Explication : sans choix écrits, le guide complet ne peut pas être appliqué de façon reproductible.

## 2. Production — Contrôles

- Faire approuver le schéma, les capacités et les dépendances avant toute installation.
- Documenter la version exacte, les composants activés, les ports, les noms DNS et le plan de mise à jour.
- Prévoir la haute disponibilité uniquement si le datastore et le nombre de serveurs respectent la documentation K3s.
- Vérifier la supervision, les sauvegardes testées et les procédures de restauration.

## 3. Production — Sécurité

- Réserver l'API Kubernetes aux réseaux d'administration autorisés.
- Traiter le token K3s et les kubeconfigs comme des secrets; ne pas les déposer dans un dépôt.
- Limiter les ports inter-nœuds aux flux documentés et filtrer les interfaces d'administration.
- Exclure les données sensibles et secrets des manifests de test.

## Validation et retour arrière

- **Validation** : architecture, compatibilités, flux, sauvegarde et critères de reprise sont approuvés.
- **Arrêt** : ne pas installer si les versions, les réseaux ou le modèle de datastore ne sont pas confirmés.

## Si le problème n'est pas résolu

- [K3s — exigences d'installation](https://docs.k3s.io/installation/requirements)
- [K3s — options de configuration](https://docs.k3s.io/installation/configuration)
- [Guide complet K3s Debian 13](/02-fiches-completes/debian/13/installation-deploiement/14-orchestration-cluster-k3s-kubernetes-debian-13#1-concevoir-le-cluster)
---
title: "Fiche Simple - VM Debian 13 Minikube Demarrer"
description: "Démarrer un cluster mono-nœud avec le driver Docker et des ressources explicites."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "minikube", "docker", "kubernetes", "lab"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Minikube_Demarrer.md

- **Environnement** : VM Debian 13 de laboratoire avec Docker Engine, Minikube mono-nœud
- **OS / Version** : Debian 13 Trixie; Minikube (driver Docker)
- **Catégorie** : conteneurs / Kubernetes de laboratoire
- **Tags** : `debian13`, `minikube`, `docker`, `kubernetes`, `lab`

---

## Problème précis à résoudre

Démarrer un cluster mono-nœud avec le driver Docker et des ressources explicites.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer avec ressources explicites (`2` CPU et `4096` Mo sont des valeurs d'exemple à adapter) :
   ```bash
   minikube start --driver=docker --cpus=2 --memory=4096
   ```
   👉 Explication : dimensionne le nœud au lieu de se fier aux valeurs par défaut.

2. Pour fixer la version de Kubernetes, lister d'abord les options acceptées :
   ```bash
   minikube start --help | grep -i kubernetes-version
   ```
   👉 Explication : ajouter ensuite `--kubernetes-version=` avec la version contrôlée.

3. Garder Docker comme driver par défaut :
   ```bash
   minikube config set driver docker
   ```
   👉 Explication : évite de répéter `--driver`.

4. Isoler un environnement avec un profil (`lab1` est un nom d'exemple) :
   ```bash
   minikube start --profile lab1 --driver=docker --cpus=2 --memory=4096
   ```
   👉 Explication : chaque profil est un cluster séparé.

## 2. Production — Contrôles

Documenter profil, ressources et version de Kubernetes.

## 3. Production — Sécurité

- Ne pas publier l'API sur un réseau non maîtrisé.

## Validation et retour arrière

- **Validation** : `minikube status` indique `Running`.
- **Retour arrière** : `minikube stop` ou `minikube delete` (profil concerné).

## Si le problème n'est pas résolu

- [Minikube — Get Started](https://minikube.sigs.k8s.io/docs/start/)
- [Minikube — driver Docker](https://minikube.sigs.k8s.io/docs/drivers/docker/)
- [Guide complet Minikube Docker Debian 13](/02-fiches-completes/debian/13/installation-deploiement/88-deploiement-minikube-docker-driver-debian-13#4-demarrer-le-cluster)
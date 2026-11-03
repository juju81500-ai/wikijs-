---
title: "fiche-simple-vm-debian-13-minikube-prerequis"
description: "Vérifier Docker, le compte non-root et les ressources avant d'installer Minikube."
published: true
date: 2026-11-03T14:22:28Z
tags: ["debian13", "minikube", "docker", "kubernetes", "lab"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# fiche-simple-vm-debian-13-minikube-prerequis.md

- **Environnement** : [[Glossary:VM]] Debian 13 de laboratoire avec Docker Engine, Minikube mono-nœud
- **OS / Version** : Debian 13 Trixie; Minikube (driver Docker)
- **Catégorie** : conteneurs / Kubernetes de laboratoire
- **Tags** : `debian13`, `minikube`, `docker`, `kubernetes`, `lab`

---

## Problème précis à résoudre

Vérifier Docker, le compte non-root et les ressources avant d'installer Minikube.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version de Docker (18.09 minimum, 20.10 ou plus recommandée) :
   ```bash
   docker version
   docker info --format '{{.ServerVersion}}'
   ```
   👉 Explication : Docker Engine doit être installé selon la documentation officielle.

2. Vérifier que le compte non-root accède à Docker :
   ```bash
   id
   docker ps
   ```
   👉 Explication : l'appartenance au groupe `docker` équivaut à root sur l'hôte : n'utiliser qu'une VM de laboratoire dédiée.

3. Contrôler [[Glossary:CPU]], mémoire et disque :
   ```bash
   nproc
   free -h
   df -h /
   ```
   👉 Explication : on dimensionnera explicitement `--cpus` et `--memory` au démarrage.

4. Vérifier l'accès sortant vers le registre d'images (ou le miroir interne) :
   ```bash
   curl -sI https://registry-1.docker.io/v2/ | head -n 1
   ```
   👉 Explication : un code [[Glossary:HTTP]] (même 401) confirme que le registre est joignable.

## 2. Production — Contrôles

Limites connues : un seul nœud, pas de tolérance de panne; options de sécurité du runtime Docker non supportées pouvant bloquer le démarrage.

## 3. Production — Sécurité

- Utiliser une VM de laboratoire dédiée.
- Appliquer le durcissement de l'hôte décrit dans le guide 32.

## Validation et retour arrière

- **Validation** : Docker répond et ressources et accès registre confirmés.
- **Retour arrière** : Aucune modification n'est faite à cette étape.

## Si le problème n'est pas résolu

- [Docker — installer Docker Engine sur Debian](https://docs.docker.com/engine/install/debian/)
- [Minikube — driver Docker](https://minikube.sigs.k8s.io/docs/drivers/docker/)
- [Guide complet Minikube Docker Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/88-deploiement-minikube-docker-driver-debian-13#1-prerequis)
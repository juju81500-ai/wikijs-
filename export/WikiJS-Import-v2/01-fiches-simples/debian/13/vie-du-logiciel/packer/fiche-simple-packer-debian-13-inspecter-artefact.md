---
title: "Fiche simple — Inspecter un artefact Packer avant promotion"
description: "Vérifier le contenu et la traçabilité d'une image construite avant toute proposition de publication."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "packer", "docker", "artefact", "inspection"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche simple — Inspecter un artefact Packer avant promotion

- **Environnement** : image locale générée par un pilote Packer
- **OS / Version** : Debian 13; Packer et Docker
- **Catégorie** : automatisation / validation d'image
- **Tags** : `debian13`, `packer`, `docker`, `artefact`, `inspection`

---

## Problème précis à résoudre

Vérifier le contenu et la traçabilité d'une image construite avant toute proposition de publication.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les images et repérer l'identifiant :
   ```bash
   docker image ls
   IMAGE_ID=IDENTIFIANT_AFFICHE_PAR_PACKER
   ```
   👉 Explication : remplacer par l'identifiant exact copié de la sortie Packer.

2. Inspecter les métadonnées :
   ```bash
   docker image inspect "$IMAGE_ID" --format 'user={{.Config.User}} ports={{.Config.ExposedPorts}} env={{.Config.Env}}'
   ```
   👉 Explication : contrôler utilisateur par défaut, ports et variables (aucun secret résiduel).

3. Vérifier le marqueur de test :
   ```bash
   docker run --rm --entrypoint cat "$IMAGE_ID" /etc/packer-pilot
   ```
   👉 Explication : doit afficher `Image Packer de laboratoire`.

4. Lister les paquets installés :
   ```bash
   docker run --rm --entrypoint dpkg "$IMAGE_ID" -l | wc -l
   ```
   👉 Explication : la réussite de `packer build` n'est pas une approbation; analyser aussi les vulnérabilités avec l'outil de l'organisation avant promotion.

## 2. Production — Contrôles

Pour une chaîne d’images de production, approuver le builder, les images de base immuables, les plugins verrouillés, les provisioners, le contrôle des secrets, les scans, la traçabilité et les approbations avant publication. Le pilote Docker local ne constitue pas une chaîne de production.

## 3. Production — Sécurité

- L’accès au socket Docker équivaut généralement à des privilèges root; réserver le pilote aux opérateurs autorisés.
- Ne jamais intégrer de secret dans HCL, les variables commitées, les journaux ou les couches d’image.
- Ne pas publier l’image vers un registre ni exécuter de build sur un démon partagé sans approbation.
- Verrouiller et réviser les plugins et sources; rejeter tout artefact dont la provenance ou le contenu est incertain.

## Validation et retour arrière

- **Validation** : contenu attesté, provenance traçable, contrôles approuvés et responsable de promotion identifié.
- **Rejet** : ne pas promouvoir un artefact dont la base, le template, le plugin ou la provenance sont inconnus.

## Si le problème n'est pas résolu

- [HashiCorp — tutoriel de build Docker](https://developer.hashicorp.com/packer/tutorials/docker-get-started/docker-get-started-build-image)
- [Guide complet Packer Debian 13](/02-fiches-completes/debian/13/installation-deploiement/126-administration-packer-debian-13#6-inspecter-et-promouvoir-lartefact)
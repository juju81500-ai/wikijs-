---
title: "Packer : builders VM et cloud, publication d'images"
description: "- Périmètre : création d'images dorées via builders VM (par exemple QEMU, VirtualBox, VMware, vSphere, Proxmox) et cloud (par exemple AWS, Azure, GCP, OpenStack), puis publication."
published: true
date: 2026-11-03T09:36:14Z
tags: ["packer", "image", "qemu", "vsphere", "aws", "golden-image"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Packer : builders VM et cloud, publication d'images

- **Environnement** : Poste ou runner CI Linux/Windows/macOS avec HashiCorp Packer, en complément du [pilote Packer sur Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/126-administration-packer-debian-13)
- **Tags** : `packer`, `image`, `qemu`, `vsphere`, `aws`, `golden-image`
- **Statut de validation** : **Verdict : Non testé sur plateforme cible.** Les procédures ci-dessous sont issues de la méthode documentaire et doivent être rejouées en laboratoire avant toute production.

## 1. Périmètre et prérequis

- Périmètre : création d'images dorées via builders [[Glossary:VM]] (par exemple [[Glossary:QEMU]], VirtualBox, VMware, vSphere, Proxmox) et cloud (par exemple AWS, Azure, GCP, OpenStack), puis publication.
- Prérequis : compte de service à droits minimaux, réseau vers l'hyperviseur/cloud, source d'ISO/image de base vérifiée (somme de contrôle officielle), secrets hors du dépôt (variables d'environnement, coffre-fort).
- Les plugins sont distincts de Packer : chaque builder est un plugin d'intégration.

## 2. Exigences de version et licence

- **Version de Packer et des plugins à figer avant déploiement** (contrainte `required_plugins` avec versions explicites).
- Vérifier la licence actuelle de Packer (changement de licence de l'éditeur) et les conditions de redistribution des images ; licences OS des images (ex. [[Glossary:RHEL]], Windows) à respecter.
- Les frais cloud (stockage d'images, instances temporaires) sont à anticiper.

## 3. Procédure

1. Installer Packer depuis le dépôt/paquet officiel et vérifier la version : `packer version`.
2. Écrire un modèle HCL2 avec un bloc `packer { required_plugins { ... } }`, une `source` du builder retenu, un `build` avec provisioners (shell/ansible) et un post-processor si nécessaire.
3. Initialiser et valider :
```bash
packer init .
packer fmt -check .
packer validate .
```
4. Construire d'abord en laboratoire, avec variables et journalisation :
```bash
PACKER_LOG=1 packer build -var-file=lab.pkrvars.hcl .
```
5. Après build : vérifier l'image dans la plateforme (liste de templates ou d'AMI), la démarrer, contrôler paquets, utilisateurs, clés [[Glossary:SSH]], services.
6. Durcir : supprimer clés, historiques, comptes de build temporaires, secrets, identifiants machine (`machine-id`) avant finalisation.
7. Publier : taguer l'image (nom, version, date, commit), restreindre les droits de partage (privé par défaut) et enregistrer le manifeste (`manifest` post-processor).

## 4. Vérifications

- `validate` sans erreur ; image démarre et passe une suite de tests (Goss/InSpec ou script).
- Aucune donnée sensible dans l'image ni dans les journaux.
- Somme de contrôle et métadonnées enregistrées.

## 5. Rollback et risques

- Supprimer les ressources temporaires d'un build échoué (instances, volumes, réseaux) : contrôler le tableau de bord cloud pour éviter les coûts.
- Ne jamais écraser un tag d'image utilisé en production : publier une nouvelle version et basculer par étape, garder la précédente.
- Ne pas partager l'image publiquement par défaut.
- Un build exécuté avec un compte trop privilégié peut modifier ou supprimer des ressources : appliquer le moindre privilège.

## 6. Documentation officielle

- <https://developer.hashicorp.com/packer/docs>
- <https://developer.hashicorp.com/packer/integrations>
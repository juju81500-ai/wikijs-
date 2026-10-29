---
title: "Fiche simple — Installer Packer depuis le dépôt officiel"
description: "Installer le binaire Packer de l'éditeur via APT, après vérification de la provenance du dépôt et de sa clé."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "packer", "hashicorp", "apt", "signature"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche simple — Installer Packer depuis le dépôt officiel

- **Environnement** : Debian 13 Trixie, dépôts APT approuvés
- **OS / Version** : Debian 13; HashiCorp Packer
- **Catégorie** : automatisation / installation
- **Tags** : `debian13`, `packer`, `hashicorp`, `apt`, `signature`

---

## Problème précis à résoudre

Installer le binaire Packer de l'éditeur via APT, après vérification de la provenance du dépôt et de sa clé.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger la clé APT et afficher son empreinte :
   ```bash
   cd /tmp
   curl --fail --silent --show-error --location https://apt.releases.hashicorp.com/gpg -o hashicorp-archive-keyring.asc
   gpg --show-keys --with-fingerprint ./hashicorp-archive-keyring.asc
   ```
   👉 Explication : comparer l'empreinte avec la documentation officielle HashiCorp avant d'aller plus loin.

2. Installer la clé et configurer le dépôt (seulement si l'empreinte correspond) :
   ```bash
   gpg --dearmor < ./hashicorp-archive-keyring.asc | sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg >/dev/null
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com trixie main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
   ```
   👉 Explication : `signed-by` limite la confiance de cette clé à ce dépôt.

3. Installer :
   ```bash
   sudo apt update
   apt-cache policy packer
   sudo apt install packer
   ```
   👉 Explication : relever la version candidate et son origine avant d'installer.

4. Vérifier :
   ```bash
   packer version
   ```
   👉 Explication : consigner la version; ne jamais désactiver APT Secure ni utiliser un binaire de miroir inconnu.

## 2. Production — Contrôles

Pour une chaîne d’images de production, approuver le builder, les images de base immuables, les plugins verrouillés, les provisioners, le contrôle des secrets, les scans, la traçabilité et les approbations avant publication. Le pilote Docker local ne constitue pas une chaîne de production.

## 3. Production — Sécurité

- L’accès au socket Docker équivaut généralement à des privilèges root; réserver le pilote aux opérateurs autorisés.
- Ne jamais intégrer de secret dans HCL, les variables commitées, les journaux ou les couches d’image.
- Ne pas publier l’image vers un registre ni exécuter de build sur un démon partagé sans approbation.
- Verrouiller et réviser les plugins et sources; rejeter tout artefact dont la provenance ou le contenu est incertain.

## Validation et retour arrière

- **Validation** : version attendue affichée et paquet issu du dépôt vérifié.
- **Retour arrière** : arrêter si empreinte ou origine diffère; ne pas exécuter un binaire provenant d'une source non vérifiée.

## Si le problème n'est pas résolu

- [HashiCorp — installation Packer](https://developer.hashicorp.com/packer/install)
- [Guide complet Packer Debian 13](/02-fiches-completes/debian/13/installation-deploiement/126-administration-packer-debian-13#2-installer-packer-depuis-le-depot-officiel)
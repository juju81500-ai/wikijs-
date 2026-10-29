---
title: "Fiche Simple - VM Debian 13 OpenTofu Droits Minimaux"
description: "Préparer un répertoire et un compte à privilèges minimaux pour le projet OpenTofu."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "opentofu", "permissions", "secrets", "iac"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_OpenTofu_Droits_Minimaux.md

- **Environnement** : compte utilisateur dédié, répertoire de projet isolé
- **OS / Version** : Debian 13; OpenTofu 1.13.x
- **Catégorie** : infrastructure as code / permissions
- **Tags** : `debian13`, `opentofu`, `permissions`, `secrets`, `iac`

---

## Problème précis à résoudre

Préparer un répertoire et un compte à privilèges minimaux pour le projet OpenTofu.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un compte de service sans `sudo` :
   ```bash
   sudo adduser --disabled-password --gecos "" iac
   id iac
   ```
   👉 Explication : `id` ne doit pas montrer les groupes `sudo` ou `root`.

2. Créer le répertoire de travail dédié :
   ```bash
   sudo -u iac mkdir -p /home/iac/iac/pilote
   sudo chmod 0700 /home/iac/iac
   ls -ld /home/iac/iac/pilote
   ```
   👉 Explication : seul le compte `iac` peut lire l'état et les plans.

3. Fournir les futurs identifiants par variables d'environnement, jamais dans les `.tf` :
   ```bash
   sudo -u iac bash -c 'grep -rE "(password|secret|token)\s*=" /home/iac/iac || echo "aucun secret dans les fichiers"'
   ```
   👉 Explication : la commande contrôle l'absence de secrets en clair; utiliser un gestionnaire de secrets pour les fournisseurs.

4. Vérifier qu'OpenTofu ne tourne pas en root :
   ```bash
   sudo -u iac tofu version
   ```
   👉 Explication : toutes les commandes `tofu` sont exécutées avec ce compte.

## 2. Production — Contrôles

Définir propriétaire du projet, rôles, accès au backend et à l'état, rotation des secrets, contrôle de version et revue par pair.

## 3. Production — Sécurité

- Ne jamais exécuter `tofu` en root.
- Ne pas écrire de secret dans les fichiers `.tf`, `.tfvars` versionnés ou l'historique shell.
- Traiter `terraform.tfstate` et les plans comme des fichiers sensibles.
- Restreindre les permissions du répertoire au compte et au groupe autorisés.

## Validation et retour arrière

- **Validation** : `id`, propriétaire et permissions du répertoire sont conformes; aucun secret en clair n'est présent.
- **Retour arrière** : ne pas déplacer ou supprimer un état existant sans copie approuvée et vérification de son propriétaire.

## Si le problème n'est pas résolu

- [OpenTofu — état](https://opentofu.org/docs/language/state/)
- [OpenTofu — gestion des données sensibles](https://opentofu.org/docs/language/state/sensitive-data/)
- [Guide complet OpenTofu Debian 13](/02-fiches-completes/debian/13/installation-deploiement/120-deploiement-opentofu-1-13-debian-13#3-compte-et-repertoire-de-travail-a-droits-minimaux)
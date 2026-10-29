---
title: "Fiche simple — Nettoyer un pilote Packer et préparer le retour arrière"
description: "Retirer uniquement l'image de test inutilisée et pouvoir revenir à un template/plugin connu."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "packer", "docker", "nettoyage", "rollback"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche simple — Nettoyer un pilote Packer et préparer le retour arrière

- **Environnement** : démon Docker de laboratoire; image de test identifiée
- **OS / Version** : Debian 13; Packer et Docker
- **Catégorie** : automatisation / nettoyage et retour arrière
- **Tags** : `debian13`, `packer`, `docker`, `nettoyage`, `rollback`

---

## Problème précis à résoudre

Retirer uniquement l'image de test inutilisée et pouvoir revenir à un template/plugin connu.

## 1. Hors-Production (Lab / Test / POC)

1. Conserver template, lock file, version de Packer, journaux utiles et résultat approuvé :
   ```bash
   cd ~/packer-lab
   packer version > packer-version.txt
   ls -la
   ```
   👉 Explication : ces éléments permettent de rejouer ou d'auditer le pilote.

2. Vérifier qu'aucun conteneur n'utilise l'image :
   ```bash
   IMAGE_ID=IDENTIFIANT_EXACT
   docker ps -a --filter ancestor="$IMAGE_ID"
   ```
   👉 Explication : la liste doit être vide.

3. Supprimer l'image de pilote :
   ```bash
   docker image rm "$IMAGE_ID"
   ```
   👉 Explication : jamais de `prune` ni de suppression globale sur un démon partagé.

4. Retour arrière après mise à niveau : restaurer template et lock file puis réinstaller la version précédente :
   ```bash
   apt-cache madison packer
   sudo apt install packer=VERSION_PRECEDENTE
   ```
   👉 Explication : remplacer `VERSION_PRECEDENTE` par une version listée.

## 2. Production — Contrôles

Pour une chaîne d’images de production, approuver le builder, les images de base immuables, les plugins verrouillés, les provisioners, le contrôle des secrets, les scans, la traçabilité et les approbations avant publication. Le pilote Docker local ne constitue pas une chaîne de production.

## 3. Production — Sécurité

- L’accès au socket Docker équivaut généralement à des privilèges root; réserver le pilote aux opérateurs autorisés.
- Ne jamais intégrer de secret dans HCL, les variables commitées, les journaux ou les couches d’image.
- Ne pas publier l’image vers un registre ni exécuter de build sur un démon partagé sans approbation.
- Verrouiller et réviser les plugins et sources; rejeter tout artefact dont la provenance ou le contenu est incertain.

## Validation et retour arrière

- **Validation** : image pilote retirée seulement si non utilisée; sources du build antérieur conservées.
- **Sécurité** : la suppression d'image est irréversible si aucune autre copie n'existe; confirmer l'identité et la sauvegarde avant action.

## Si le problème n'est pas résolu

- [Docker — gérer les images](https://docs.docker.com/engine/manage-resources/pruning/)
- [HashiCorp — commande build](https://developer.hashicorp.com/packer/docs/commands/build)
- [Guide complet Packer Debian 13](/02-fiches-completes/debian/13/installation-deploiement/126-administration-packer-debian-13#7-nettoyer-et-revenir-a-letat-initial)
---
title: "Fiche Simple - VM Debian 13 GNS3 Deploiement Verifier Perimetre"
description: "Contrôler que le laboratoire reste isolé et sain."
published: true
date: 2026-10-29T20:14:10Z
tags: ["gns3", "debian13", "recette", "isolation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_GNS3_Deploiement_Verifier_Perimetre.md

- **Environnement** : Poste Debian 13 avec projet GNS3
- **OS / Version** : Debian 13 Trixie amd64; GNS3 2.2.61 stable
- **Catégorie** : simulation reseau / recette
- **Tags** : `gns3`, `debian13`, `recette`, `isolation`

---

## Problème précis à résoudre

Contrôler que le laboratoire reste isolé et sain.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le serveur local :
   ```bash
   pgrep -a gns3server
   ```
   👉 Explication : le serveur doit tourner en local (processus visible).

2. Contrôler les ressources libvirt :
   ```bash
   virsh list --all
   ```
   👉 Explication : aucune machine inattendue ne doit apparaître.

3. Dans le projet, vérifier visuellement qu'aucun lien ne va vers une interface physique, un pont de production ou un réseau tiers.
   👉 Explication : un lab doit rester fermé.

4. Rechercher d'éventuels secrets dans les fichiers du projet (répertoire à adapter) :
   ```bash
   grep -rIil -e password -e secret "$HOME/GNS3/projects"
   ```
   👉 Explication : on repère les secrets réutilisables à retirer.

## 2. Production — Contrôles

Faire relire et documenter les hypothèses avant de réutiliser un diagramme.

## 3. Production — Sécurité

- Un résultat d'émulation ne valide pas un équipement réel.
- Pas de secret réutilisable dans les projets.

## Validation et retour arrière

- **Validation** : Projet sain, isolé, sans secret.
- **Retour arrière** : Supprimer le lien ou le nœud fautif dans le projet.

## Si le problème n'est pas résolu

- [GNS3 — installation Linux](https://docs.gns3.com/docs/getting-started/installation/linux)
- [GNS3 — registre des appliances](https://github.com/GNS3/gns3-registry)
- [Guide complet GNS3 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/77-deploiement-gns3-2-2-61-debian-13#6-verifier-les-projets-et-le-perimetre-reseau)
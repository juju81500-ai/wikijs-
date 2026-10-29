---
title: "Fiche Simple - VM Ubuntu Ceph Limites Validation"
description: "Connaître les limites du guide avant d'utiliser la procédure."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2204", "ceph", "tentacle", "cephadm"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_Ceph_Limites_Validation.md

- **Environnement** : Cluster Ceph de laboratoire à trois nœuds (ceph01, ceph02, ceph03) géré par cephadm
- **OS / Version** : Ubuntu Server 22.04 LTS; Ceph Tentacle 20.2.4
- **Catégorie** : stockage / cluster Ceph
- **Tags** : `ubuntu2204`, `ceph`, `tentacle`, `cephadm`

---

## Problème précis à résoudre

Connaître les limites du guide avant d'utiliser la procédure.

## 1. Hors-Production (Lab / Test / POC)

1. Lire la limite : le guide cible Ceph Tentacle 20.2.4 et Ubuntu 22.04.
   👉 Explication : Ubuntu 22.04 est listé par Ceph comme plateforme testée.

2. Considérer adresses et disques comme des exemples de lab.
   👉 Explication : ils doivent être remplacés par votre plan réel.

3. Retenir qu'aucune commande de cluster n'a été exécutée dans ce workspace.
   👉 Explication : installation, placement CRUSH, OSD et restauration doivent être testés sur des VM et disques vierges dédiés.

4. Vérifier la version installée :
   ```bash
   ceph -v
   ```
   👉 Explication : confirme que la version correspond à celle du guide.

## 2. Production — Contrôles

Exiger un test complet en lab, y compris restauration, avant toute mise en production.

## 3. Production — Sécurité

- Ne pas tester sur du matériel ou des disques contenant des données.

## Validation et retour arrière

- **Validation** : les écarts de version ou de plateforme sont identifiés et documentés.
- **Retour arrière** : sans objet: fiche d'information.

## Si le problème n'est pas résolu

- [Ceph — versions actives](https://docs.ceph.com/en/tentacle/releases/)
- [Ceph Tentacle — cephadm](https://docs.ceph.com/en/tentacle/cephadm/install/)
- [Guide complet](/02-fiches-completes/ubuntu/22-04/installation-deploiement/67-deploiement-ceph-tentacle-20-2-4-ubuntu-22-04#9-limites-de-validation)
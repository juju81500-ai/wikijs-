---
title: "Fiche Simple - VM Ubuntu Ceph Ajouter Noeuds Monitors"
description: "Ajouter ceph02 et ceph03 au cluster et étendre les Monitors à trois hôtes."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2204", "ceph", "tentacle", "cephadm"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_Ceph_Ajouter_Noeuds_Monitors.md

- **Environnement** : Cluster Ceph de laboratoire à trois nœuds (ceph01, ceph02, ceph03) géré par cephadm
- **OS / Version** : Ubuntu Server 22.04 LTS; Ceph Tentacle 20.2.4
- **Catégorie** : stockage / cluster Ceph
- **Tags** : `ubuntu2204`, `ceph`, `tentacle`, `cephadm`

---

## Problème précis à résoudre

Ajouter `ceph02` et `ceph03` au cluster et étendre les Monitors à trois hôtes.

## 1. Hors-Production (Lab / Test / POC)

1. Installer la clé SSH publique du cluster sur les deux autres nœuds :
   ```bash
   sudo ssh-copy-id -f -i /etc/ceph/ceph.pub root@ceph02
   sudo ssh-copy-id -f -i /etc/ceph/ceph.pub root@ceph03
   ```
   👉 Explication : autorise cephadm à gérer ces hôtes; l'accès root/sudo sans interaction doit avoir été approuvé.

2. Ajouter les hôtes avec leur adresse publique (exemples à adapter) :
   ```bash
   sudo ceph orch host add ceph02 10.20.0.12
   sudo ceph orch host add ceph03 10.20.0.13
   ```
   👉 Explication : enregistre les nœuds dans l'orchestrateur.

3. Vérifier les hôtes :
   ```bash
   sudo ceph cephadm check-host ceph02
   sudo ceph cephadm check-host ceph03
   sudo ceph orch host ls --detail
   ```
   👉 Explication : confirme que prérequis et inventaire sont corrects.

4. Prévisualiser le placement des MON :
   ```bash
   sudo ceph orch apply mon --placement="ceph01,ceph02,ceph03" --dry-run
   ```
   👉 Explication : `--dry-run` montre ce qui serait fait sans rien appliquer.

5. Appliquer le même placement puis contrôler le quorum :
   ```bash
   sudo ceph orch apply mon --placement="ceph01,ceph02,ceph03"
   sudo ceph quorum_status --format json-pretty
   ```
   👉 Explication : trois MON sur des hôtes distincts tolèrent la perte d'un nœud.

## 2. Production — Contrôles

Valider l'accès SSH, la liste des hôtes et le quorum avant toute étape suivante; ne retirer aucun MON tant que le quorum n'est pas confirmé.

## 3. Production — Sécurité

- Limiter la clé `/etc/ceph/ceph.pub` aux hôtes du cluster.
- Un nombre impair de MON répartis sur des hôtes distincts est nécessaire.

## Validation et retour arrière

- **Validation** : `sudo ceph quorum_status` liste trois MON et `ceph orch host ls` trois hôtes.
- **Retour arrière** : restaurer le placement précédent avec `ceph orch apply mon` et retirer l'hôte ajouté (`sudo ceph orch host rm ceph03`) sans `--force`, après confirmation du quorum.

## Si le problème n'est pas résolu

- [Ceph — hôtes](https://docs.ceph.com/en/tentacle/cephadm/host-management/)
- [Ceph — service MON](https://docs.ceph.com/en/tentacle/cephadm/services/mon/)
- [Ceph Tentacle — cephadm](https://docs.ceph.com/en/tentacle/cephadm/install/)
- [Guide complet](/02-fiches-completes/ubuntu/22-04/installation-deploiement/67-deploiement-ceph-tentacle-20-2-4-ubuntu-22-04#4-ajouter-les-nuds-et-les-monitors)
---
title: "Fiche Simple - VM Ubuntu Ceph Preparer Noeuds"
description: "Préparer chaque hôte (paquets, NTP, conteneurs, pare-feu) avant l'installation de cephadm."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2204", "ceph", "tentacle", "cephadm"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_Ceph_Preparer_Noeuds.md

- **Environnement** : Cluster Ceph de laboratoire à trois nœuds (ceph01, ceph02, ceph03) géré par cephadm
- **OS / Version** : Ubuntu Server 22.04 LTS; Ceph Tentacle 20.2.4
- **Catégorie** : stockage / cluster Ceph
- **Tags** : `ubuntu2204`, `ceph`, `tentacle`, `cephadm`

---

## Problème précis à résoudre

Préparer chaque hôte (paquets, NTP, conteneurs, pare-feu) avant l'installation de cephadm.

## 1. Hors-Production (Lab / Test / POC)

1. Sur chaque nœud, contrôler l'état de base :
   ```bash
   hostnamectl
   timedatectl status
   ip -br address
   ip route
   getent hosts ceph01 ceph02 ceph03
   ```
   👉 Explication : vérifie nom, heure, adresses et résolutions réciproques.

2. Mettre à jour le système :
   ```bash
   sudo apt update
   sudo apt full-upgrade
   ```
   👉 Explication : applique les correctifs avant de construire le cluster.

3. Installer les dépendances requises par cephadm :
   ```bash
   sudo apt install chrony lvm2 podman
   ```
   👉 Explication : Chrony synchronise l'heure (indispensable à Ceph), LVM2 et Podman sont utilisés par cephadm.

4. Activer la synchronisation d'heure :
   ```bash
   sudo systemctl enable --now chrony
   ```
   👉 Explication : démarre Chrony et l'active au boot.

5. Redémarrer si le noyau ou des bibliothèques critiques ont changé, puis revérifier :
   ```bash
   timedatectl status
   ```
   👉 Explication : l'horloge doit être synchronisée avant de continuer.

6. Préparer le filtrage entre nœuds : autoriser les ports Monitor 3300/TCP et 6789/TCP et la plage 6800-7568/TCP, uniquement entre les sous-réseaux Ceph.
   👉 Explication : limite l'accès aux seuls pairs du cluster, sans exposition Internet.

7. Ne pas installer `ceph-osd` à la main sur les nœuds gérés par cephadm.
   👉 Explication : la documentation met en garde contre les conflits de gestion; cephadm prépare lui-même les dépendances.

## 2. Production — Contrôles

Documenter les adresses par nœud, la source NTP, les règles de pare-feu appliquées et le plan de redémarrage des hôtes.

## 3. Production — Sécurité

- Restreindre les ports Ceph aux interfaces et sous-réseaux Ceph.
- Ne pas lancer un `apt full-upgrade` non coordonné sur un cluster déjà en service.

## Validation et retour arrière

- **Validation** : Chrony synchronisé, noms résolus, paquets installés sur les trois nœuds.
- **Retour arrière** : désinstaller les paquets ajoutés (`sudo apt remove chrony lvm2 podman`) seulement si aucun service Ceph n'est encore déployé; supprimer les règles de pare-feu ajoutées.

## Si le problème n'est pas résolu

- [Ceph — cephadm prérequis](https://docs.ceph.com/en/tentacle/cephadm/install/)
- [Ceph Tentacle — cephadm](https://docs.ceph.com/en/tentacle/cephadm/install/)
- [Guide complet](/02-fiches-completes/ubuntu/22-04/installation-deploiement/67-deploiement-ceph-tentacle-20-2-4-ubuntu-22-04#2-preparer-les-nuds)
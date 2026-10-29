---
title: "Fiche Simple - VM Ubuntu Ceph Cadrer Perimetre"
description: "Définir ce que le cluster de test couvre (ou non) et réunir les prérequis avant de toucher aux nœuds."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2204", "ceph", "tentacle", "cephadm"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_Ceph_Cadrer_Perimetre.md

- **Environnement** : Cluster Ceph de laboratoire à trois nœuds (ceph01, ceph02, ceph03) géré par cephadm
- **OS / Version** : Ubuntu Server 22.04 LTS; Ceph Tentacle 20.2.4
- **Catégorie** : stockage / cluster Ceph
- **Tags** : `ubuntu2204`, `ceph`, `tentacle`, `cephadm`

---

## Problème précis à résoudre

Définir ce que le cluster de test couvre (ou non) et réunir les prérequis avant de toucher aux nœuds.

## 1. Hors-Production (Lab / Test / POC)

1. Noter le périmètre : trois nœuds `ceph01`, `ceph02`, `ceph03`, MON/MGR/OSD et un pool RBD pilote, sans CephFS, RGW ni iSCSI.
   👉 Explication : une VM mono-nœud n'est pas un cluster HA et ne prouve aucune résilience.

2. Vérifier sur chaque hôte son identité, ses adresses et ses routes :
   ```bash
   hostnamectl
   ip -br address
   ip route
   ```
   👉 Explication : contrôle que chaque nœud a le bon nom et les réseaux public et cluster prévus.

3. Vérifier que les noms se résolvent entre nœuds :
   ```bash
   getent hosts ceph01 ceph02 ceph03
   ```
   👉 Explication : chaque nom doit retourner l'adresse du plan de lab; sinon corriger DNS ou `/etc/hosts` avant la suite.

4. Lister les disques et repérer un disque de données vide par nœud :
   ```bash
   lsblk -o NAME,SIZE,MODEL,SERIAL,FSTYPE,MOUNTPOINTS
   ```
   👉 Explication : chaque nœud a besoin d'un disque système séparé et d'un disque de données inutilisé, dédié à Ceph.

5. Réserver des adresses RFC1918 de lab pour le réseau public et le réseau de réplication.
   👉 Explication : les adresses du guide (10.20.0.x, 10.30.0.x) sont des exemples à remplacer par votre plan; ne pas les copier tels quels.

## 2. Production — Contrôles

Valider avec le responsable : matériel (réseau 10 Gb/s ou plus, protection contre la perte d'alimentation), capacité, domaines de panne, plan d'adressage et fenêtre de maintenance. Un lab n'apporte pas cette preuve.

## 3. Production — Sécurité

- Ne jamais exposer le cluster à Internet; limiter les accès aux sous-réseaux Ceph.
- Ne pas réutiliser des disques contenant des données: l'ajout d'OSD les efface.

## Validation et retour arrière

- **Validation** : trois hôtes résolus, administrables par SSH et chacun avec un disque de données vierge identifié.
- **Retour arrière** : aucune modification n'est faite par cette fiche; rien à annuler.

## Si le problème n'est pas résolu

- [Ceph — OS recommandés](https://docs.ceph.com/en/tentacle/start/os-recommendations/)
- [Ceph — matériel et réseau](https://docs.ceph.com/en/tentacle/start/hardware-recommendations/)
- [Ceph Tentacle — cephadm](https://docs.ceph.com/en/tentacle/cephadm/install/)
- [Guide complet](/02-fiches-completes/ubuntu/22-04/installation-deploiement/67-deploiement-ceph-tentacle-20-2-4-ubuntu-22-04#1-perimetre-et-prerequis)
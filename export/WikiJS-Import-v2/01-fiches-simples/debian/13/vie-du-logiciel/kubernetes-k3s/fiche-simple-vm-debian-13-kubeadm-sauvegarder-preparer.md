---
title: "Fiche Simple - VM Debian 13 Kubeadm Sauvegarder Preparer"
description: "Préserver l'état des nœuds et collecter les informations initiales avant modification."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "kubeadm", "snapshot", "fstab", "rollback"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Kubeadm_Sauvegarder_Preparer.md

- **Environnement** : nœuds Debian 13 de laboratoire avant installation Kubernetes
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Kubernetes / sauvegarde et prérequis système
- **Tags** : `debian13`, `kubeadm`, `snapshot`, `fstab`, `rollback`

---

## Problème précis à résoudre

Préserver l'état des nœuds et collecter les informations initiales avant modification.

## 1. Hors-Production (Lab / Test / POC)

1. Faire un snapshot de chaque VM : **Proxmox > VM > Snapshots > Take Snapshot** (ou l'outil de l'hyperviseur).
   👉 Explication : point de retour complet avant toute modification.

2. Sauvegarder les fichiers modifiés :
   ```bash
   sudo cp -a /etc/fstab /etc/fstab.$(date +%F).bak
   sudo cp -a /etc/sysctl.d /etc/sysctl.d.$(date +%F).bak
   sudo cp -a /etc/containerd /etc/containerd.$(date +%F).bak 2>/dev/null || true
   ```
   👉 Explication : le dernier échoue sans conséquence si containerd n'est pas encore installé.

3. Désactiver le swap et retirer l'entrée persistante :
   ```bash
   sudo swapoff -a
   sudo sed -i.bak '/\sswap\s/ s/^/#/' /etc/fstab
   swapon --show
   ```
   👉 Explication : la sortie doit être vide; relire `/etc/fstab` pour confirmer la mise en commentaire.

## 2. Production — Contrôles

Définir RPO/RTO, rétention et approbation des snapshots; vérifier l'espace et le périmètre des sauvegardes.

## 3. Production — Sécurité

- Traiter les copies de configuration comme potentiellement sensibles.
- Protéger les sauvegardes hors du cluster et limiter les comptes qui peuvent les lire.
- Ne pas écraser une sauvegarde précédente avant d'avoir vérifié la nouvelle.
- Ne pas supposer qu'un snapshot remplace une sauvegarde applicative/etcd cohérente.

## Validation et retour arrière

- **Validation** : snapshot répertorié et restaurable, fichiers de référence stockés dans un dépôt protégé.
- **Retour arrière** : restaurer le snapshot du nœud concerné et confirmer son identité réseau avant de le reconnecter.

## Si le problème n'est pas résolu

- [Kubernetes — installation kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
- [Guide complet kubeadm Debian 13](/02-fiches-completes/debian/13/installation-deploiement/89-deploiement-cluster-kubernetes-kubeadm-debian-13#2-sauvegarde-et-point-de-retour-initial)
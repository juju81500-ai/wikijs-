---
title: "Fiche Simple - VM Debian 13 Kubeadm Ajouter Workers"
description: "Joindre un worker autorisé au cluster avec un jeton d'enrôlement à durée et périmètre contrôlés."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "kubeadm", "worker", "join", "token"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Kubeadm_Ajouter_Workers.md

- **Environnement** : worker Debian 13 préparé avec containerd et kubelet/kubeadm compatibles
- **OS / Version** : Debian 13; Kubernetes kubeadm
- **Catégorie** : Kubernetes / enrôlement de nœud
- **Tags** : `debian13`, `kubeadm`, `worker`, `join`, `token`

---

## Problème précis à résoudre

Joindre un worker autorisé au cluster avec un jeton d'enrôlement à durée et périmètre contrôlés.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter sur chaque worker la commande `kubeadm join` affichée en fin d'initialisation :
   ```bash
   sudo kubeadm join DNS_OU_IP_API:6443 --token JETON --discovery-token-ca-cert-hash sha256:HASH
   ```
   👉 Explication : remplacer par les valeurs réelles; le jeton et le hash sont des secrets d'enrôlement, à ne pas coller dans un ticket ni un dépôt.

2. Si la commande est perdue ou expirée, en régénérer une sur le plan de contrôle :
   ```bash
   sudo kubeadm token create --print-join-command
   ```
   👉 Explication : les jetons expirent par défaut après 24 h.

3. Vérifier depuis le plan de contrôle :
   ```bash
   kubectl get nodes -o wide
   ```
   👉 Explication : les workers doivent apparaître puis passer `Ready`.

## 2. Production — Contrôles

Documenter approbation d'enrôlement, inventaire de nœuds, propriétaires, étiquettes, capacité et procédure de retrait du worker.

## 3. Production — Sécurité

- Traiter jeton et commande join comme secrets d'enrôlement.
- Ne pas les mettre dans un ticket, dépôt, historique partagé ou journal de CI.
- Ne pas joindre un nœud à un API endpoint non vérifié.
- Révoquer/régénérer les jetons exposés selon la procédure officielle.

## Validation et retour arrière

- **Validation** : worker visible dans le bon cluster et passe `Ready` après installation du CNI.
- **Retour arrière** : retirer le nœud selon la procédure kubeadm; ne pas exécuter de reset sur un nœud qui héberge des workloads sans plan.

## Si le problème n'est pas résolu

- [Kubernetes — créer un cluster kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
- [kubeadm — référence](https://kubernetes.io/docs/reference/setup-tools/kubeadm/)
- [Guide complet kubeadm Debian 13](/02-fiches-completes/debian/13/installation-deploiement/89-deploiement-cluster-kubernetes-kubeadm-debian-13#6-ajouter-les-workers)
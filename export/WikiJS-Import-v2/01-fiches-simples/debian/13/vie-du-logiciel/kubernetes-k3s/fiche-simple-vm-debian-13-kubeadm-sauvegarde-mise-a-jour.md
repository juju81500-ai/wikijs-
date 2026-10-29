---
title: "Fiche Simple - VM Debian 13 Kubeadm Sauvegarde Mise A Jour"
description: "Protéger l'état du cluster et organiser les mises à niveau/migrations selon la documentation de la version."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "kubeadm", "etcd", "backup", "upgrade"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Kubeadm_Sauvegarde_Mise_A_Jour.md

- **Environnement** : cluster kubeadm pilote, accès administrateur contrôlé
- **OS / Version** : Debian 13; kubeadm, etcd et Kubernetes
- **Catégorie** : Kubernetes / sauvegarde et maintenance
- **Tags** : `debian13`, `kubeadm`, `etcd`, `backup`, `upgrade`

---

## Problème précis à résoudre

Protéger l'état du cluster et organiser les mises à niveau/migrations selon la documentation de la version.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder `/etc/kubernetes` et un snapshot etcd :
   ```bash
   sudo apt-get install -y etcd-client
   sudo install -d -m 0700 /var/backups
   sudo tar czf /var/backups/k8s-pki-$(date +%F).tgz /etc/kubernetes
   sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/server.crt --key=/etc/kubernetes/pki/etcd/server.key snapshot save /var/backups/etcd-$(date +%F).db
   ```
   👉 Explication : contient des secrets; copier hors du nœud puis tester la restauration en environnement isolé (procédure officielle de restauration etcd).

2. Préparer une mise à niveau, une mineure à la fois :
   ```bash
   sudo kubeadm upgrade plan
   ```
   👉 Explication : plan de contrôle d'abord, puis workers avec `kubectl drain NOEUD --ignore-daemonsets` et `kubectl uncordon NOEUD`; lire les notes de version avant.

3. Retour arrière d'un nœud en échec d'installation :
   ```bash
   sudo kubeadm reset
   ```
   👉 Explication : destructif pour la configuration locale du nœud. Après une mise à niveau échouée, restaurer le snapshot de VM ou la sauvegarde etcd.

## 2. Production — Contrôles

Définir RPO/RTO, fréquence, chiffrement, conservation, ordre d'upgrade, fenêtre, supervision et critères de validation avant chaque mise à niveau.

## 3. Production — Sécurité

- Sauvegardes contiennent certificats, kubeconfigs et secrets; protéger leur accès et transfert.
- Ne pas tester une restauration sur le cluster actif.
- Ne pas appliquer de mise à niveau multi-mineure ou hors matrice de compatibilité.
- Ne pas exposer la clé etcd ou kubeconfig administrateur dans les scripts ou journaux.

## Validation et retour arrière

- **Validation** : snapshot etcd créé, copié hors hôte et restauration testée; compatibilités confirmées.
- **Retour arrière** : utiliser la procédure de restauration officielle et les snapshots compatibles; ne pas improviser sur un plan de contrôle unique.

## Si le problème n'est pas résolu

- [Kubernetes — sauvegarder etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
- [Kubernetes — mise à niveau kubeadm](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [Guide complet kubeadm Debian 13](/02-fiches-completes/debian/13/installation-deploiement/89-deploiement-cluster-kubernetes-kubeadm-debian-13#8-sauvegarde-mise-a-jour-et-retour-arriere)
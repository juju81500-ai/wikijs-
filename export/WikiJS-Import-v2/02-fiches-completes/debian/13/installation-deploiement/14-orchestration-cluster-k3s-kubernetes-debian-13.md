---
title: "Cluster Kubernetes léger avec K3s sur Debian"
description: "Fiche simple : [cadrer le cluster](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/FicheSimple-VMDebian13K3sCadrer.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["k3s", "kubernetes", "debian", "cluster", "containerd", "cni"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Cluster Kubernetes léger avec K3s sur Debian

- **Environnement** : Lab ou cluster multi-nœuds dimensionné
- **Tags** : `k3s`, `kubernetes`, `debian`, `cluster`, `containerd`, `cni`

## 1. Concevoir le cluster

Fiche simple : [cadrer le cluster](/01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-k3s-cadrer).

Choisir la version K3s supportée, le nombre de serveurs, le datastore (SQLite pour un nœud simple, etcd ou datastore externe pour HA selon la documentation), les adresses fixes, le CNI, le stockage et l'ingress. Définir les ports entre nœuds et les règles d'accès à l'API. Les versions Debian 13 et K3s retenues doivent apparaître dans leurs matrices de compatibilité.

Sauvegarder le datastore et protéger le token de cluster ; ce token permet de rejoindre le cluster et doit être traité comme un secret.

## 2. Installer un nœud de laboratoire

Fiche simple : [installer un nœud de laboratoire](/01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-k3s-installer-noeud-lab).

Récupérer la méthode d'installation depuis la documentation officielle K3s, vérifier la provenance et épingler une version stable au lieu de prendre automatiquement la dernière version. Pour un lab, le script officiel peut être téléchargé, examiné puis lancé avec les options adaptées ; ne pas ajouter d'options copiées sans comprendre leurs effets.

Après installation :

```bash
sudo systemctl --no-pager status k3s
sudo k3s kubectl get nodes -o wide
sudo k3s kubectl get pods -A
```

Ne pas publier le kubeconfig admin ; copier une version sécurisée uniquement vers un poste d'administration autorisé.

## 3. Ajouter des nœuds et applications

Fiche simple : [ajouter des nœuds et applications](/01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-k3s-ajouter-noeuds-applications).

Ajouter des agents avec l'adresse API, le token conservé dans un coffre et la même version majeure/mineure selon la politique de mise à niveau. Vérifier l'état `Ready` avant de déployer. Utiliser des manifests versionnés, des namespaces, des ressources requests/limits et des secrets gérés hors dépôt.

Déployer d'abord une application de test sans données importantes, puis vérifier résolution DNS, stockage persistant, exposition Ingress, certificats et politiques réseau.

## 4. Sécuriser et surveiller

Fiche simple : [sécuriser et surveiller](/01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-k3s-securiser-surveiller).

- Restreindre l'API Kubernetes aux réseaux d'administration.
- Appliquer RBAC minimal et séparer les comptes opérateur.
- Ne pas exposer les services via `NodePort` ou `LoadBalancer` sans filtrage amont.
- Surveiller capacité, certificats, événements, composants système et sauvegardes.
- Éviter les conteneurs privilégiés et les montages d'hôte non nécessaires.

## 5. Maintenance et reprise

Fiche simple : [maintenance et reprise](/01-fiches-simples/debian/13/vie-du-logiciel/kubernetes-k3s/fiche-simple-vm-debian-13-k3s-maintenance-reprise).

Avant toute mise à niveau, sauvegarder le datastore selon la procédure de la topologie, vérifier les snapshots persistants et consulter les notes K3s. Mettre à jour un serveur/agent à la fois dans l'ordre supporté et valider les workloads après chaque étape. Tester une restauration complète dans un environnement isolé. En cas de panne du control plane, ne pas réinitialiser les nœuds ni supprimer `/var/lib/rancher/k3s` avant d'avoir préservé les données.
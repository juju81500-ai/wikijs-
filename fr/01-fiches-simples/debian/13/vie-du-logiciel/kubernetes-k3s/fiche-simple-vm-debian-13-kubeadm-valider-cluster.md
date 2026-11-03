---
title: "fiche-simple-vm-debian-13-kubeadm-valider-cluster"
description: "Confirmer que nœuds, CNI, [[Glossary:DNS]] interne et déploiement de test fonctionnent avant d'accueillir des charges réelles."
published: true
date: 2026-11-03T14:22:28Z
tags: ["debian13", "kubeadm", "validation", "nodes", "cni", "dns"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# fiche-simple-vm-debian-13-kubeadm-valider-cluster.md

- **Environnement** : cluster pilote kubeadm, namespaces système et application de test
- **OS / Version** : Debian 13; Kubernetes choisi et CNI installé
- **Catégorie** : Kubernetes / validation
- **Tags** : `debian13`, `kubeadm`, `validation`, `nodes`, `cni`, `dns`

---

## Problème précis à résoudre

Confirmer que nœuds, CNI, [[Glossary:DNS]] interne et déploiement de test fonctionnent avant d'accueillir des charges réelles.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler nœuds et pods système :
   ```bash
   kubectl get nodes -o wide
   kubectl get pods -A
   ```
   👉 Explication : tous les nœuds `Ready`; pods système (dont DNS et CNI) `Running`.

2. Déployer un test :
   ```bash
   kubectl create deployment test-nginx --image=REGISTRE/IMAGE:VERSION
   kubectl rollout status deployment/test-nginx
   ```
   👉 Explication : remplacer par une image approuvée; le déploiement doit réussir.

3. Tester le DNS interne :
   ```bash
   kubectl run dns-test --rm -it --restart=Never --image=REGISTRE/IMAGE_BUSYBOX:VERSION -- nslookup kubernetes.default
   ```
   👉 Explication : doit résoudre `kubernetes.default.svc.cluster.local`.

4. Nettoyer :
   ```bash
   kubectl delete deployment test-nginx
   ```
   👉 Explication : aucun avertissement kubeadm ignoré sans justification.

## 2. Production — Contrôles

Faire approuver les sondes, capacity planning, observabilité, [[Glossary:RBAC]], politiques réseau, stockage et critères de disponibilité.

## 3. Production — Sécurité

- Ne pas déployer d'image `latest` ou d'origine inconnue.
- Ne pas ignorer les avertissements kubeadm sans justification documentée.
- Ne pas exposer `NodePort` ou `LoadBalancer` sans contrôle réseau amont.
- Protéger la sortie kubectl, qui peut révéler noms internes et topologie.

## Validation et retour arrière

- **Validation** : nœuds Ready, pods système sains, DNS/flux valides et test applicatif supprimé.
- **Retour arrière** : supprimer uniquement les ressources de test après contrôle du namespace et du nom.

## Si le problème n'est pas résolu

- [Kubernetes — diagnostic des pods](https://kubernetes.io/docs/tasks/debug/)
- [Kubernetes — réseau de cluster](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- [Guide complet kubeadm Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/89-deploiement-cluster-kubernetes-kubeadm-debian-13#7-validation)
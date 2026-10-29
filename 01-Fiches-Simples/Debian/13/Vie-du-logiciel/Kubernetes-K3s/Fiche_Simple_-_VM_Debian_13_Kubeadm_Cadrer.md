# Fiche_Simple_-_VM_Debian_13_Kubeadm_Cadrer.md

- **Environnement** : cluster de laboratoire Debian 13, un plan de contrôle et un worker ou plus
- **OS / Version** : Debian 13 Trixie; version mineure Kubernetes choisie depuis `pkgs.k8s.io`
- **Catégorie** : conteneurs / orchestration Kubernetes
- **Tags** : `debian13`, `kubernetes`, `kubeadm`, `cadrage`, `cluster`

---

## Problème précis à résoudre

Vérifier prérequis, réseau, CNI et capacité avant d'initialiser un cluster kubeadm.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler ressources et unicité sur chaque nœud :
   ```bash
   nproc; free -h
   hostnamectl --static
   ip link | grep ether
   sudo cat /sys/class/dmi/id/product_uuid
   uname -r
   ```
   👉 Explication : minimum 2 Go de RAM par machine et 2 CPU pour le plan de contrôle; nom d'hôte, MAC et `product_uuid` uniques.

2. Contrôler IP statique, routes et ports déjà utilisés :
   ```bash
   ip route show
   sudo ss -lnt
   ```
   👉 Explication : connectivité complète entre nœuds; les ports requis (6443, 10250…) doivent être libres et ouverts.

3. Vérifier le swap :
   ```bash
   swapon --show
   ```
   👉 Explication : kubelet refuse de démarrer avec du swap; une sortie vide est attendue (désactivation à l'étape suivante).

4. Consigner : nom DNS ou adresse du `--control-plane-endpoint`, CNI choisi et son CIDR de pods, snapshot de VM ou console hors bande.
   👉 Explication : ces choix précèdent `kubeadm init`.

## 2. Production — Contrôles

Faire approuver topologie, sous-réseaux, règles de filtrage, capacité, haute disponibilité, propriétaires et plan de maintenance.

## 3. Production — Sécurité

- Ne pas réutiliser une adresse, MAC ou UUID entre nœuds.
- Ne pas ouvrir tous les ports inter-nœuds par défaut; appliquer uniquement les flux documentés.
- Ne pas confondre Docker Engine avec un runtime CRI sans composant adapté.
- Ne pas lancer le cluster sur des systèmes sans sauvegarde ou console de récupération.

## Validation et retour arrière

- **Validation** : prérequis documentés, CNI et CIDR sélectionnés, snapshots et accès hors bande testés.
- **Arrêt** : ne pas initialiser si le CNI, le routage ou les ports requis ne sont pas définis.

## Si le problème n'est pas résolu

- [Kubernetes — ports et protocoles](https://kubernetes.io/docs/reference/networking/ports-and-protocols/)
- [Kubernetes — créer un cluster kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
- [Guide complet kubeadm Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/89_Deploiement_Cluster_Kubernetes_kubeadm_Debian_13.md#1-prerequis)

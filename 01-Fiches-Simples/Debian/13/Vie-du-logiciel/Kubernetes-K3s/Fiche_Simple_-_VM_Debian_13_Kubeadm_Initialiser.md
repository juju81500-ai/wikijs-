# Fiche_Simple_-_VM_Debian_13_Kubeadm_Initialiser.md

- **Environnement** : premier nœud de plan de contrôle Debian 13, CNI et CIDR déjà choisis
- **OS / Version** : Debian 13; kubeadm
- **Catégorie** : Kubernetes / plan de contrôle
- **Tags** : `debian13`, `kubeadm`, `control-plane`, `cni`, `kubeconfig`

---

## Problème précis à résoudre

Initialiser le plan de contrôle avec une adresse de terminaison et un CIDR de pods correspondant au CNI.

## 1. Hors-Production (Lab / Test / POC)

1. Initialiser le premier nœud avec votre plan d'adressage :
   ```bash
   sudo kubeadm init --control-plane-endpoint=DNS_OU_IP_API --pod-network-cidr=CIDR_DU_CNI
   ```
   👉 Explication : remplacer les deux valeurs; le kubelet redémarre en boucle jusqu'à l'initialisation (normal). Avec plusieurs interfaces, ajouter `--apiserver-advertise-address=IP` (elle entre dans les certificats).

2. Configurer kubectl pour l'utilisateur courant :
   ```bash
   mkdir -p $HOME/.kube
   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
   sudo chown $(id -u):$(id -g) $HOME/.kube/config
   ```
   👉 Explication : `admin.conf` donne un accès administrateur; ne jamais le copier sur un poste non maîtrisé ni le publier.

3. Installer le plugin réseau (manifest officiel du CNI retenu) :
   ```bash
   kubectl apply -f MANIFEST_OFFICIEL_DU_CNI.yaml
   ```
   👉 Explication : le guide ne choisit pas le CNI; prendre le manifest dans la documentation du plugin.

4. Contrôler :
   ```bash
   kubectl get nodes
   kubectl get pods -n kube-system
   ```
   👉 Explication : le nœud passe `Ready` quand le CNI est opérationnel.

## 2. Production — Contrôles

Faire approuver IP de l'API, DNS/load balancer, CIDR, CNI, certificats, contrôles d'accès et plan HA avant initialisation.

## 3. Production — Sécurité

- `admin.conf` confère des droits administrateur complets; ne pas le copier vers des postes non maîtrisés.
- Ne pas placer kubeconfig, certificats ou manifests sensibles dans un dépôt public.
- Ne pas changer le CIDR après initialisation sans plan de migration documenté.
- Ne pas exposer l'API Kubernetes aux réseaux non autorisés.

## Validation et retour arrière

- **Validation** : API répond, configuration kubectl fonctionne, CNI installé et composants système sains.
- **Retour arrière** : préserver snapshot et journaux; ne pas réinitialiser sans vérifier les conséquences sur l'état local.

## Si le problème n'est pas résolu

- [Kubernetes — créer un cluster kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
- [Kubernetes — configuration réseau](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
- [Guide complet kubeadm Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/89_Deploiement_Cluster_Kubernetes_kubeadm_Debian_13.md#5-initialiser-le-plan-de-controle)

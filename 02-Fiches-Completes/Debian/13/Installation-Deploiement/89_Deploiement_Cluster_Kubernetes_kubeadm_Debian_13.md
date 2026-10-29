# Déployer un cluster Kubernetes générique avec kubeadm sur Debian 13

- **OS / Version** : Debian 13 Trixie, Kubernetes via dépôts `pkgs.k8s.io` (la documentation consultée le 29 octobre 2026 est rédigée pour Kubernetes v1.37 ; confirmer la version avant usage)
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Cluster Kubernetes amont à un plan de contrôle et plusieurs nœuds de travail, runtime containerd. La haute disponibilité du plan de contrôle n'est pas détaillée ici. Alternatives : [K3s](14_Orchestration_Cluster_K3s_Kubernetes_Debian_13.md) pour une distribution allégée, [Minikube](88_Deploiement_Minikube_Docker_Driver_Debian_13.md) pour un lab mono-nœud.
- **Catégorie** : Conteneurs / Kubernetes
- **Tags** : `kubernetes`, `kubeadm`, `kubelet`, `containerd`, `debian13`, `cluster`, `cni`

## 1. Prérequis

Fiche simple : [cadrer le cluster kubeadm](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Cadrer.md).

- Au moins 2 machines (1 plan de contrôle, 1 ou plusieurs workers) : 2 Go de RAM minimum chacune et 2 CPU minimum pour le plan de contrôle, d'après la documentation officielle.
- Nom d'hôte, adresse MAC et `product_uuid` uniques ; adresses IP statiques ; connectivité complète entre nœuds ; ports requis ouverts (voir [ports et protocoles](https://kubernetes.io/docs/reference/networking/ports-and-protocols/)).
- Swap désactivé (kubelet refuse par défaut de démarrer avec du swap) : contrôler avec `swapon --show`, désactiver avec `sudo swapoff -a` et retirer l'entrée persistante de `/etc/fstab`.
- Un nom DNS ou une adresse de répartiteur pour `--control-plane-endpoint` si une évolution vers la haute disponibilité est possible (recommandé par la documentation).
- Choix d'un plugin réseau (CNI) et de ses prérequis (CIDR des pods, ports) avant `kubeadm init`.
- Console hors bande ou snapshot de VM avant de commencer.

```bash
uname -r
sudo cat /sys/class/dmi/id/product_uuid
ip link
ip route show
sudo ss -lnt
```

Limites : les commandes de dépôt dépendent de la version mineure choisie ; Docker Engine seul n'est pas un runtime CRI sans `cri-dockerd`; le guide ne choisit pas votre CNI et ne fournit pas de manifest CNI, à prendre dans la documentation du plugin retenu.

## 2. Sauvegarde et point de retour initial

Fiche simple : [préparer les sauvegardes et l'état initial](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Sauvegarder_Preparer.md).

Avant modification : snapshot de chaque VM et copie de `/etc/fstab`, `/etc/sysctl.d` et `/etc/containerd` s'ils existent.

```bash
sudo cp -a /etc/fstab /etc/fstab.$(date +%F).bak
```

## 3. Préparer chaque nœud et installer le runtime

Fiche simple : [installer et configurer containerd](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Installer_Runtime.md).

Activer le routage IPv4, requis par certains réseaux de cluster :

```bash
cat <<'CONF' | sudo tee /etc/sysctl.d/k8s.conf
net.ipv4.ip_forward = 1
CONF
sudo sysctl --system
sysctl net.ipv4.ip_forward
```

Installer containerd depuis les dépôts Debian, contrôler la version puis aligner le pilote cgroup sur `systemd` (kubelet et runtime doivent utiliser le même ; recommandé avec systemd et cgroup v2) :

```bash
apt-cache policy containerd
sudo apt-get update
sudo apt-get install -y containerd
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml
```

Dans `/etc/containerd/config.toml`, régler `SystemdCgroup = true` pour le runtime `runc`, en suivant la page officielle [Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/) correspondant à la version de containerd installée, puis :

```bash
sudo systemctl restart containerd
sudo systemctl --no-pager status containerd
```

## 4. Installer kubeadm, kubelet et kubectl

Fiche simple : [installer les paquets Kubernetes](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Installer_Paquets.md).

Reprise de la procédure officielle (remplacer `v1.37` par la mineure choisie après lecture de la documentation de cette version) :

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gpg
sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.37/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.37/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
sudo systemctl enable --now kubelet
```

Les paquets sont verrouillés car leur mise à niveau suit une procédure dédiée. Les dépôts historiques `apt.kubernetes.io` sont obsolètes : ne pas les utiliser. Il y a un dépôt par version mineure.

## 5. Initialiser le plan de contrôle

Fiche simple : [initialiser le plan de contrôle](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Initialiser.md).

Sur le premier nœud, avec les valeurs de votre plan d'adressage (CIDR spécifique au CNI retenu) :

```bash
sudo kubeadm init --control-plane-endpoint=<dns-ou-ip-api> --pod-network-cidr=<cidr-du-cni>
```

Le kubelet redémarre en boucle jusqu'à l'initialisation : comportement attendu. Si plusieurs interfaces existent, vérifier l'adresse annoncée (`--apiserver-advertise-address`) ; elle entre dans les certificats. Configurer ensuite `kubectl` pour un administrateur autorisé :

```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

`admin.conf` donne un accès administrateur au cluster : ne pas le copier sur des postes non maîtrisés ni le publier. Installer ensuite le plugin réseau choisi en appliquant le manifest officiel de ce plugin, puis contrôler.

## 6. Ajouter les workers

Fiche simple : [ajouter les workers](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Ajouter_Workers.md).

Utiliser la commande `kubeadm join` affichée en fin d'initialisation. Si elle est perdue ou expirée :

```bash
sudo kubeadm token create --print-join-command
```

Le jeton et le hash de CA sont des secrets d'enrôlement : ne pas les journaliser dans un ticket ou un dépôt.

## 7. Validation

Fiche simple : [valider le cluster](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Valider_Cluster.md).

```bash
kubectl get nodes -o wide
kubectl get pods -A
kubectl create deployment test-nginx --image=<registre>/<image>:<version>
kubectl rollout status deployment/test-nginx
kubectl delete deployment test-nginx
```

Critères : tous les nœuds `Ready`, pods système `Running` (dont DNS et CNI), résolution DNS interne et trafic inter-nœuds fonctionnels, pas d'avertissement kubeadm ignoré sans justification.

## 8. Sauvegarde, mise à jour et retour arrière

Fiche simple : [sauvegarder et préparer les mises à jour](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Sauvegarde_Mise_A_Jour.md).

- Sauvegarder régulièrement `/etc/kubernetes` (certificats et kubeconfigs, secrets) et un snapshot etcd :

```bash
sudo apt-get install -y etcd-client
sudo ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  snapshot save /var/backups/etcd-$(date +%F).db
```

- Copier ces sauvegardes hors du nœud ; tester la restauration dans un environnement isolé (procédure : documentation officielle de restauration etcd).
- Mise à niveau : suivre la documentation kubeadm de la version cible, une mineure à la fois, plan de contrôle d'abord (`kubeadm upgrade plan`), puis workers avec drain/uncordon. Lire les notes de version avant.
- Retour arrière d'un nœud en échec d'installation : `sudo kubeadm reset`, qui est destructif pour la configuration locale du nœud. Pour une mise à niveau échouée, restaurer le snapshot de VM ou la sauvegarde etcd selon la documentation, sans improviser sur un plan de contrôle unique.

## 9. Limites de sécurité et d'exploitation

Fiche simple : [contrôler le durcissement et l'exploitation](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Kubernetes-K3s/Fiche_Simple_-_VM_Debian_13_Kubeadm_Durcir.md).

Restreindre l'API aux réseaux d'administration, appliquer RBAC minimal, des politiques réseau, une gestion des secrets hors dépôt, et la rotation des certificats (`kubeadm certs check-expiration`). Ne pas exposer `NodePort` ou `LoadBalancer` sans filtrage amont. Cette fiche ne remplace ni une revue de durcissement ni un essai de reprise.

## Sources

- [Kubernetes — Installing kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
- [Kubernetes — Creating a cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
- [Kubernetes — Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)
- [Kubernetes — Ports and Protocols](https://kubernetes.io/docs/reference/networking/ports-and-protocols/)
- [Kubernetes — Operating etcd clusters](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
- [Kubernetes — Upgrading kubeadm clusters](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)

# Fiche_Simple_-_VM_Debian_13_Kubeadm_Installer_Runtime.md

- **Environnement** : tous les nœuds Debian 13, runtime containerd
- **OS / Version** : Debian 13; containerd des dépôts approuvés
- **Catégorie** : Kubernetes / runtime conteneur
- **Tags** : `debian13`, `kubeadm`, `containerd`, `cgroup`, `runtime`

---

## Problème précis à résoudre

Préparer containerd et aligner le pilote cgroup avec kubelet avant l'installation du cluster.

## 1. Hors-Production (Lab / Test / POC)

1. Activer le routage IPv4 :
   ```bash
   cat <<'CONF' | sudo tee /etc/sysctl.d/k8s.conf
   net.ipv4.ip_forward = 1
   CONF
   sudo sysctl --system
   sysctl net.ipv4.ip_forward
   ```
   👉 Explication : requis par certains réseaux de cluster; doit afficher `1`.

2. Installer containerd :
   ```bash
   apt-cache policy containerd
   sudo apt-get update
   sudo apt-get install -y containerd
   ```
   👉 Explication : contrôler la version candidate avant installation.

3. Générer la configuration par défaut et aligner le pilote cgroup :
   ```bash
   sudo mkdir -p /etc/containerd
   containerd config default | sudo tee /etc/containerd/config.toml >/dev/null
   sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
   grep SystemdCgroup /etc/containerd/config.toml
   ```
   👉 Explication : kubelet et runtime doivent utiliser le même pilote (`systemd`); confirmer avec la page officielle Container Runtimes de la version retenue.

4. Redémarrer et contrôler :
   ```bash
   sudo systemctl restart containerd
   sudo systemctl --no-pager status containerd
   ```
   👉 Explication : doit être `active (running)`.

## 2. Production — Contrôles

Valider la version CRI, le cgroup v2, les réglages systemd et la compatibilité avec la version mineure Kubernetes retenue.

## 3. Production — Sécurité

- Ne pas exposer l'API CRI ou le socket containerd au réseau.
- Ne pas remplacer une configuration existante sans sauvegarde.
- Ne pas ajouter Docker Engine comme substitut CRI sans installer et valider `cri-dockerd`.
- Appliquer le runtime de manière identique et contrôlée à tous les nœuds.

## Validation et retour arrière

- **Validation** : runtime actif sur chaque nœud, cgroup conforme et absence d'erreur CRI.
- **Retour arrière** : restaurer la configuration précédente, redémarrer containerd et vérifier les workloads existants.

## Si le problème n'est pas résolu

- [Kubernetes — runtimes de conteneurs](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)
- [containerd — documentation](https://containerd.io/docs/)
- [Guide complet kubeadm Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/89_Deploiement_Cluster_Kubernetes_kubeadm_Debian_13.md#3-preparer-chaque-noeud-et-installer-le-runtime)

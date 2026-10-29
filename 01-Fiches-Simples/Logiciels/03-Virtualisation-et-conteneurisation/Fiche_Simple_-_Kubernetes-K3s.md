# 📄 Kubernetes / K3s

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : K3s installé par le script officiel, canal stable en lab ; version à figer en production et à vérifier sur la version déployée (`k3s --version`)
- **Catégorie** : Virtualisation et conteneurisation
- **Tags** : `[debian-12]`, `[k3s]`, `[kubernetes]`, `[conteneurs]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer un cluster K3s à un seul nœud serveur sur Debian 12, vérifier que l'API répond et que les pods démarrent, puis le durcir (kubeconfig restreint, pare-feu limité, chiffrement des secrets, namespace isolé). Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Prérequis et désactivation du swap :
```bash
sudo apt update
sudo apt install -y curl ca-certificates
sudo swapoff -a
sudo sed -i '/\sswap\s/s/^/#/' /etc/fstab
swapon --show
```
👉 Explication : Installe `curl` et les certificats nécessaires au script d'installation. `swapoff -a` coupe le swap immédiatement, la commande `sed` commente la ligne swap de `/etc/fstab` pour qu'il reste coupé après redémarrage. `swapon --show` ne doit rien afficher.

2. Installation du serveur K3s :
```bash
curl -sfL https://get.k3s.io -o /tmp/k3s-install.sh
less /tmp/k3s-install.sh
sudo sh /tmp/k3s-install.sh
```
👉 Explication : Télécharge le script officiel, le fait lire (`less`) avant de l’exécuter. Il installe le binaire `k3s`, le lien `kubectl`, le service `k3s` et démarre un serveur à un nœud. Ce script exécute du code distant : acceptable en lab, à remplacer par une version figée en production.

3. Contrôle du service et du nœud :
```bash
sudo systemctl status k3s --no-pager
sudo k3s kubectl get nodes -o wide
```
👉 Explication : `Active: active (running)` est attendu pour le service. Le nœud doit passer à `Ready` après une à deux minutes.

4. Kubeconfig pour l'utilisateur courant :
```bash
mkdir -p ~/.kube
sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
sudo chown "$(id -u):$(id -g)" ~/.kube/config
kubectl get pods -A
```
👉 Explication : K3s écrit son kubeconfig dans `/etc/rancher/k3s/k3s.yaml`. Une copie dans `~/.kube/config` permet d'utiliser `kubectl` sans `sudo`. Ce fichier contient des identifiants administrateur : lab uniquement.

5. Déploiement d'un service de test :
```bash
kubectl create deployment web-test --image=docker.io/library/nginx:1.27
kubectl expose deployment web-test --port=80 --type=NodePort
kubectl rollout status deployment/web-test
kubectl get deployment,pods,svc
```
👉 Explication : Crée un déploiement nginx, l'expose sur un port NodePort, attend la fin du déploiement puis liste les ressources. Nettoyage : `kubectl delete service,deployment web-test`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installation avec options de durcissement :
```bash
curl -sfL https://get.k3s.io -o /tmp/k3s-install.sh
sudo INSTALL_K3S_CHANNEL=stable INSTALL_K3S_EXEC="server --write-kubeconfig-mode 600 --disable traefik --tls-san k3s-srv01.tssr.lan --secrets-encryption" sh /tmp/k3s-install.sh
```
👉 Explication : `--write-kubeconfig-mode 600` limite le kubeconfig à root, `--disable traefik` retire l'Ingress installé par défaut si un autre contrôleur est retenu, `--tls-san` ajoute le nom DNS au certificat de l'API, `--secrets-encryption` chiffre les secrets au repos. Point à vérifier : le canal `stable` change avec le temps ; figer la version avec `INSTALL_K3S_VERSION` pour la mise en production. Sur un serveur déjà installé en lab, désinstaller d'abord avec `sudo /usr/local/bin/k3s-uninstall.sh`.

2. Pare-feu limité aux administrateurs et aux nœuds :
```bash
sudo apt install -y ufw
sudo ufw allow from 10.10.20.5 to any port 22 proto tcp
sudo ufw allow from 10.10.20.0/24 to any port 6443 proto tcp
sudo ufw allow from 10.10.20.0/24 to any port 10250 proto tcp
sudo ufw default deny incoming
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : SSH est autorisé en premier pour éviter de couper l'accès. L'API (6443) et le kubelet (10250) ne sont ouverts qu'au réseau d'administration `10.10.20.0/24`. Point à vérifier : sur un nœud unique, le port 8472/udp (VXLAN) n'est pas nécessaire ; sur un cluster multi-nœuds, il doit être ouvert entre nœuds seulement. ufw ne filtre pas tous les flux des pods : valider par un test depuis un poste autorisé et un poste refusé.

3. Kubeconfig restreint et contrôle des accès :
```bash
mkdir -p ~/.kube
sudo install -m 600 -o "$(id -u)" -g "$(id -g)" /etc/rancher/k3s/k3s.yaml ~/.kube/config
kubectl get nodes
```
👉 Explication : Copie le kubeconfig avec les droits 600 et le propriétaire de l'administrateur. Ne jamais diffuser ce fichier hors des postes d'administration.

4. Namespace applicatif avec profil de sécurité restreint :
```bash
kubectl create namespace applis
kubectl label namespace applis pod-security.kubernetes.io/enforce=restricted
kubectl get namespace applis --show-labels
```
👉 Explication : Crée un namespace dédié. Le label `enforce=restricted` (Pod Security Admission) refuse les pods privilégiés ou qui demandent l'élévation de droits.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérification du chiffrement des secrets :
```bash
sudo k3s secrets-encrypt status
```
👉 Explication : Affiche si le chiffrement des secrets est actif et l'état de la clé. Point à vérifier : la rotation de clé se fait avec `secrets-encrypt rotate-keys`, à valider sur la version déployée.

2. Sauvegarde de l'état du cluster :
```bash
sudo k3s etcd-snapshot save --name snap-srv01-$(date +%F)
sudo k3s etcd-snapshot ls
```
👉 Explication : Crée un instantané du datastore. Point à vérifier : la commande exige un etcd embarqué (serveur initialisé avec `--cluster-init`) ; avec le backend SQLite par défaut elle n'est pas disponible. Les snapshots sont stockés dans `/var/lib/rancher/k3s/server/db/snapshots/`.

3. Protection des instantanés, qui contiennent des secrets :
```bash
sudo chmod 600 /var/lib/rancher/k3s/server/db/snapshots/snap-srv01-*
sudo ls -l /var/lib/rancher/k3s/server/db/snapshots/
```
👉 Explication : Restreint la lecture à root. Copier ensuite les instantanés hors du serveur, dans un stockage chiffré.

4. Contrôle du journal du service :
```bash
sudo journalctl -u k3s -n 50 --no-pager
```
👉 Explication : Affiche les 50 dernières lignes du journal de K3s. Les erreurs d'authentification et les refus de requête sont à remonter au responsable sécurité.

---

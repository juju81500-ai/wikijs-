# Fiche_Simple_-_VM_Debian_13_Kubeadm_Installer_Paquets.md

- **Environnement** : nœuds Debian 13, dépôt officiel Kubernetes de la mineure choisie
- **OS / Version** : Debian 13; kubelet, kubeadm, kubectl de même version mineure
- **Catégorie** : Kubernetes / installation des outils

---

## Problème précis à résoudre

Installer les paquets Kubernetes depuis le dépôt correspondant à la mineure sélectionnée.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis (remplacer `v1.37` par la mineure choisie après lecture de sa documentation) :
   ```bash
   sudo apt-get update
   sudo apt-get install -y apt-transport-https ca-certificates curl gpg
   sudo mkdir -p -m 755 /etc/apt/keyrings
   ```
   👉 Explication : outils et répertoire des clés.

2. Ajouter la clé et le dépôt de la mineure choisie :
   ```bash
   curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.37/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.37/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
   ```
   👉 Explication : un dépôt par version mineure; l'ancien `apt.kubernetes.io` est obsolète.

3. Installer et verrouiller :
   ```bash
   sudo apt-get update
   sudo apt-get install -y kubelet kubeadm kubectl
   sudo apt-mark hold kubelet kubeadm kubectl
   sudo systemctl enable --now kubelet
   ```
   👉 Explication : le verrouillage évite une mise à niveau accidentelle; elle suit une procédure dédiée.

4. Vérifier :
   ```bash
   kubeadm version -o short
   kubectl version --client
   ```
   👉 Explication : la version doit être celle de la mineure choisie.

## 2. Production — Contrôles

Planifier la mise à niveau une mineure à la fois, vérifier les notes de version et tester la procédure sur un cluster de préproduction.

## 3. Production — Sécurité

- Ne pas désactiver la validation APT ou importer une clé non vérifiée.
- Ne pas mélanger les versions mineures des composants sans support documenté.
- Ne pas mettre à niveau automatiquement kubelet/kubeadm/kubectl hors fenêtre prévue.
- Limiter l'accès aux sources APT et vérifier les candidats avant installation.

## Validation et retour arrière

- **Validation** : dépôt, versions et état hold des trois paquets sont cohérents sur tous les nœuds.
- **Retour arrière** : installer seulement une version précédente encore approuvée et compatible; ne pas rétrograder un cluster sans procédure officielle.

## Si le problème n'est pas résolu

- [Kubernetes — installer kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)
- [Kubernetes — versions et mises à niveau](https://kubernetes.io/releases/version-skew-policy/)
- [Guide complet kubeadm Debian 13](/02-fiches-completes/debian/13/installation-deploiement/89-deploiement-cluster-kubernetes-kubeadm-debian-13#4-installer-kubeadm-kubelet-et-kubectl)
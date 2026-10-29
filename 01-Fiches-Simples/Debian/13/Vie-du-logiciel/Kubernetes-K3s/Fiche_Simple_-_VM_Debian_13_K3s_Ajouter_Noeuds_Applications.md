# Fiche_Simple_-_VM_Debian_13_K3s_Ajouter_Noeuds_Applications.md

- **Environnement** : cluster K3s pilote; nœuds et workloads autorisés
- **OS / Version** : Debian 13; version K3s maintenue et cohérente entre nœuds
- **Catégorie** : Kubernetes / K3s / extension du cluster
- **Tags** : `debian13`, `k3s`, `kubernetes`, `agents`, `workloads`

---

## Problème précis à résoudre

Joindre des nœuds au cluster et déployer une première application sans exposer de secrets ni perturber de workloads existants.

## 1. Hors-Production (Lab / Test / POC)

1. Sur le serveur, lire le token de jointure et le conserver dans un coffre :
   ```bash
   sudo cat /var/lib/rancher/k3s/server/node-token
   ```
   👉 Explication : ce token permet de rejoindre le cluster; ne pas l'enregistrer dans un ticket ni un dépôt.

2. Sur l'agent, installer la même version que le serveur :
   ```bash
   curl -fsSL https://get.k3s.io -o /tmp/k3s-install.sh
   read -rs K3S_TOKEN
   sudo INSTALL_K3S_VERSION="v1.XX.Y+k3s1" K3S_URL="https://SERVEUR:6443" K3S_TOKEN="$K3S_TOKEN" sh /tmp/k3s-install.sh
   unset K3S_TOKEN
   ```
   👉 Explication : `read -rs` évite d'inscrire le token dans l'historique; remplacer `SERVEUR` et la version par les valeurs retenues.

3. Vérifier l'état du nœud :
   ```bash
   sudo k3s kubectl get nodes -o wide
   ```
   👉 Explication : le nouvel agent doit passer à `Ready`.

4. Déployer une application de test dans un namespace dédié :
   ```bash
   sudo k3s kubectl create namespace test-pilote
   sudo k3s kubectl -n test-pilote create deployment demo --image=nginx:stable
   sudo k3s kubectl -n test-pilote set resources deployment demo --requests=cpu=50m,memory=64Mi --limits=cpu=200m,memory=128Mi
   sudo k3s kubectl -n test-pilote rollout status deployment demo
   ```
   👉 Explication : un namespace isolé et des limites évitent d'impacter d'autres charges.

5. Valider DNS et service, puis nettoyer :
   ```bash
   sudo k3s kubectl -n test-pilote expose deployment demo --port=80
   sudo k3s kubectl -n test-pilote run dnstest --rm -it --image=busybox:stable --restart=Never -- nslookup demo
   sudo k3s kubectl delete namespace test-pilote
   ```
   👉 Explication : la résolution du service `demo` doit réussir; la suppression du namespace retire toutes les ressources de test.

## 2. Production — Contrôles

- Enregistrer l'identité, le rôle, la version et le propriétaire de chaque nœud.
- Vérifier l'état du cluster et les ressources avant chaque ajout ou déploiement.
- Tester les manifests et changements sur un namespace ou environnement pilote.
- Définir les contrôles d'accès, les limites de ressources et le cycle de vie des données persistantes.

## 3. Production — Sécurité

- Stocker les tokens et secrets dans un coffre approuvé; renouveler ou révoquer les accès selon la procédure.
- Appliquer RBAC minimal et limiter la création de workloads privilégiés.
- N'exposer un service qu'après validation du filtrage réseau, du TLS et de son propriétaire.
- Ne pas placer les secrets en clair dans les manifests versionnés.

## Validation et retour arrière

- **Validation** : nœud `Ready`, composants sains, application répondant sur le chemin approuvé et journaux sans erreur critique.
- **Retour arrière** : retirer le workload pilote selon son manifeste; préserver volumes et données avant suppression d'un nœud ou namespace.

## Si le problème n'est pas résolu

- [K3s — accès au cluster](https://docs.k3s.io/cluster-access)
- [Kubernetes — documentation des workloads](https://kubernetes.io/docs/concepts/workloads/)
- [Guide complet K3s Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/14_Orchestration_Cluster_K3s_Kubernetes_Debian_13.md#3-ajouter-des-noeuds-et-applications)

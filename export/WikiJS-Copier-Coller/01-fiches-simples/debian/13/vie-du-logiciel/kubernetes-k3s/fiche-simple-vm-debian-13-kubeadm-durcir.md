# Fiche_Simple_-_VM_Debian_13_Kubeadm_Durcir.md

- **Environnement** : cluster Kubernetes pilote kubeadm, revue d'accès et des flux
- **OS / Version** : Debian 13; Kubernetes kubeadm
- **Catégorie** : Kubernetes / sécurité et exploitation

---

## Problème précis à résoudre

Vérifier les contrôles d'accès, réseau, secrets et certificats avant toute utilisation opérationnelle du cluster.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'expiration des certificats :
   ```bash
   sudo kubeadm certs check-expiration
   ```
   👉 Explication : planifier la rotation avant l'échéance.

2. Contrôler les droits RBAC et l'exposition :
   ```bash
   kubectl get clusterrolebindings -o wide | grep -i cluster-admin
   kubectl get svc -A | grep -E 'NodePort|LoadBalancer'
   ```
   👉 Explication : `cluster-admin` limité aux administrateurs; ne pas exposer `NodePort` ou l'API à des réseaux non prévus.

3. Vérifier les politiques réseau et l'accès à l'API :
   ```bash
   kubectl get networkpolicy -A
   sudo ss -ltnp | grep 6443
   ```
   👉 Explication : restreindre 6443 aux réseaux d'administration via le pare-feu; appliquer des NetworkPolicy par défaut.

4. Rechercher des secrets hors dépôt : ne stocker aucun secret en clair dans les manifests.
   👉 Explication : utiliser un coffre ou un chiffrement des secrets au repos.

## 2. Production — Contrôles

Faire valider la revue de sécurité, audit RBAC, journalisation, rotation des certificats, gestion des secrets, segmentation, réponse à incident et propriétaires.

## 3. Production — Sécurité

- Ne pas partager `admin.conf`; traiter toute copie comme un accès cluster privilégié.
- Ne pas publier l'API, les ports de nœuds ou dashboards sans filtrage et authentification approuvés.
- Appliquer le moindre privilège et des politiques d'admission/réseau adaptées.
- Ne pas considérer les contrôles de cette fiche comme un audit de durcissement complet.

## Validation et retour arrière

- **Validation** : accès API limités, RBAC relu, politiques réseau actives, secrets protégés et certificats suivis.
- **Retour arrière** : tester les changements RBAC/réseau sur un pilote et conserver un accès de secours contrôlé.

## Si le problème n'est pas résolu

- [Kubernetes — sécuriser un cluster](https://kubernetes.io/docs/tasks/administer-cluster/securing-a-cluster/)
- [Kubernetes — RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Guide complet kubeadm Debian 13](/02-fiches-completes/debian/13/installation-deploiement/89-deploiement-cluster-kubernetes-kubeadm-debian-13#9-limites-de-securite-et-dexploitation)
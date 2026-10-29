# Fiche_Simple_-_VM_Debian_13_K3s_Securiser_Surveiller.md

- **Environnement** : cluster K3s administré et autorisé
- **OS / Version** : Debian 13; version K3s maintenue
- **Catégorie** : Kubernetes / K3s / sécurité et supervision
- **Tags** : `debian13`, `k3s`, `kubernetes`, `securite`, `supervision`

---

## Problème précis à résoudre

Réduire l'exposition du plan de contrôle et détecter les défaillances, dérives de capacité et erreurs des workloads.

## 1. Hors-Production (Lab / Test / POC)

1. Lister l'exposition réseau de l'API et du kubelet :
   ```bash
   sudo ss -tlnp | grep -E ':(6443|10250)\b'
   sudo nft list ruleset | grep -E '6443|10250' || echo "aucune règle dédiée"
   ```
   👉 Explication : l'API doit être limitée aux réseaux d'administration par pare-feu; ajouter une règle si aucune n'existe.

2. Vérifier les droits des comptes :
   ```bash
   sudo k3s kubectl get clusterrolebindings -o wide | grep -v 'system:'
   sudo k3s kubectl auth can-i --list --as=system:serviceaccount:default:default
   ```
   👉 Explication : on repère les liaisons d'administration et on vérifie qu'un compte applicatif n'a pas de droits excessifs.

3. Rechercher les conteneurs privilégiés :
   ```bash
   sudo k3s kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{" "}{.spec.containers[*].securityContext.privileged}{"\n"}{end}' | grep true || echo "aucun conteneur privilégié"
   ```
   👉 Explication : tout pod listé doit être justifié ou corrigé.

4. Contrôler l'état du cluster :
   ```bash
   sudo k3s kubectl get nodes
   sudo k3s kubectl get events -A --sort-by=.lastTimestamp | tail -20
   sudo k3s kubectl top nodes
   sudo journalctl -u k3s -n 50 --no-pager
   ```
   👉 Explication : `top` nécessite metrics-server (fourni par défaut avec K3s); les événements récents révèlent les erreurs.

5. Vérifier l'expiration des certificats :
   ```bash
   sudo k3s certificate check --output table 2>/dev/null || sudo ls -l /var/lib/rancher/k3s/server/tls/
   ```
   👉 Explication : planifier une rotation avant échéance; la commande dépend de la version K3s.

## 2. Production — Contrôles

- Revoir périodiquement les comptes, rôles, certificats, règles réseau et composants exposés.
- Surveiller disponibilité de l'API, état des nœuds, saturation, stockage et sauvegardes.
- Centraliser les journaux avec une rétention documentée et des accès restreints.
- Tester les mises à jour de sécurité et vérifier l'état après chaque changement.

## 3. Production — Sécurité

- Ne pas exposer l'API Kubernetes ou les dashboards publiquement sans architecture d'accès contrôlée.
- Appliquer le guide de durcissement K3s et le moindre privilège aux utilisateurs et workloads.
- Refuser les conteneurs privilégiés et les montages d'hôte non justifiés.
- Masquer les tokens, kubeconfigs et données d'identification dans les alertes et journaux.

## Validation et retour arrière

- **Validation** : seuls les réseaux et rôles approuvés accèdent aux fonctions prévues; les alertes pilotes remontent.
- **Retour arrière** : modifier les politiques progressivement et conserver l'accès de secours documenté avant de restreindre le plan de contrôle.

## Si le problème n'est pas résolu

- [K3s — guide de durcissement](https://docs.k3s.io/security/hardening-guide)
- [Kubernetes — bonnes pratiques de sécurité](https://kubernetes.io/docs/concepts/security/)
- [Guide complet K3s Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/14_Orchestration_Cluster_K3s_Kubernetes_Debian_13.md#4-securiser-et-surveiller)

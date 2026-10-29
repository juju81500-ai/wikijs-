# Fiche_Simple_-_VM_Debian_13_K3s_Maintenance_Reprise.md

- **Environnement** : cluster K3s avec sauvegardes et accès d'administration approuvés
- **OS / Version** : Debian 13; version K3s maintenue et documentée
- **Catégorie** : Kubernetes / K3s / maintenance et reprise
- **Tags** : `debian13`, `k3s`, `kubernetes`, `maintenance`, `reprise`

---

## Problème précis à résoudre

Mettre à jour ou restaurer K3s sans perdre le datastore, les secrets, les manifests ni les données persistantes des applications.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder le datastore (SQLite, nœud simple) et la configuration :
   ```bash
   sudo systemctl stop k3s
   sudo install -d -m 0700 /var/backups/k3s
   sudo tar -czf /var/backups/k3s/k3s-$(date +%F).tar.gz /var/lib/rancher/k3s/server/db /var/lib/rancher/k3s/server/token /etc/rancher/k3s
   sudo systemctl start k3s
   ```
   👉 Explication : arrêt bref pour une copie cohérente; avec etcd intégré, utiliser plutôt `sudo k3s etcd-snapshot save`.

2. Vérifier la sauvegarde :
   ```bash
   sudo tar -tzf /var/backups/k3s/k3s-$(date +%F).tar.gz | head
   sudo sha256sum /var/backups/k3s/k3s-$(date +%F).tar.gz
   ```
   👉 Explication : l'archive contient des secrets; la chiffrer et la copier hors machine.

3. Tester la restauration sur une VM isolée (jamais sur le datastore actif) :
   ```bash
   sudo systemctl stop k3s
   sudo tar -xzf /var/backups/k3s/k3s-AAAA-MM-JJ.tar.gz -C /
   sudo systemctl start k3s
   sudo k3s kubectl get nodes
   ```
   👉 Explication : remplacer la date de l'archive; les nœuds et workloads attendus doivent réapparaître.

4. Consulter les versions disponibles avant la mise à niveau :
   ```bash
   k3s --version
   curl -fsSL https://update.k3s.io/v1-release/channels/stable
   ```
   👉 Explication : lire les notes de version et valider la montée de version sur une copie.

5. Mettre à jour un nœud avec la version cible, puis valider :
   ```bash
   sudo INSTALL_K3S_VERSION="v1.XX.Y+k3s1" sh /tmp/k3s-install.sh
   sudo k3s kubectl get nodes
   sudo k3s kubectl get pods -A
   ```
   👉 Explication : mettre à jour un serveur à la fois, agents ensuite; passer au nœud suivant seulement quand tout est `Ready`.

## 2. Production — Contrôles

- Faire approuver le créneau et confirmer la dernière sauvegarde restaurable avant changement.
- Préparer les contrôles de santé, la capacité disponible et la procédure de retour arrière.
- Documenter versions source/cible, actions réalisées, temps d'arrêt et résultats des tests.
- Ne pas restaurer par-dessus un datastore actif sans procédure validée pour la version et la topologie.

## 3. Production — Sécurité

- Chiffrer et limiter l'accès aux sauvegardes, qui peuvent contenir secrets et identifiants.
- Ne jamais partager le token K3s ni les kubeconfigs dans un ticket ou dépôt non protégé.
- Préserver les données de diagnostic et sauvegardes avant toute action de désinstallation ou réinitialisation.
- Protéger les copies de test et détruire les secrets temporaires selon la politique locale.

## Validation et retour arrière

- **Validation** : datastore restaurable, nœuds `Ready`, composants système sains et workloads/données vérifiés.
- **Arrêt** : ne pas supprimer `/var/lib/rancher/k3s` ni réinitialiser les nœuds avant d'avoir préservé les données nécessaires.

## Si le problème n'est pas résolu

- [K3s — sauvegarde et restauration](https://docs.k3s.io/datastore/backup-restore)
- [K3s — mises à niveau manuelles](https://docs.k3s.io/upgrades/manual)
- [Guide complet K3s Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/14_Orchestration_Cluster_K3s_Kubernetes_Debian_13.md#5-maintenance-et-reprise)

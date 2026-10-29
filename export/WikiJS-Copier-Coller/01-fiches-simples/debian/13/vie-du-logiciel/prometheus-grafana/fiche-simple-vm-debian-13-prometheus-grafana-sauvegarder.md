# Fiche_Simple_-_VM_Debian_13_Prometheus_Grafana_Sauvegarder.md

- **Environnement** : serveur Prometheus/Grafana Debian 13 avant mise à niveau
- **OS / Version** : Debian 13; Prometheus TSDB et Grafana OSS
- **Catégorie** : supervision / sauvegarde et mise à jour

---

## Problème précis à résoudre

Préserver configuration, dashboards et données Prometheus de façon cohérente avant maintenance.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une sauvegarde de la configuration, des règles et des fichiers Grafana :
   ```bash
   sudo install -d -m 0700 /var/backups/prometheus-grafana
   sudo tar -czf /var/backups/prometheus-grafana/config-$(date +%F).tar.gz /etc/prometheus /etc/grafana /var/lib/grafana
   ```
   👉 Explication : l'archive peut contenir des secrets; le dossier est accessible à `root` seulement.

2. Sauvegarder le TSDB Prometheus de façon cohérente, service arrêté en laboratoire :
   ```bash
   sudo systemctl stop prometheus
   sudo tar -czf /var/backups/prometheus-grafana/tsdb-$(date +%F).tar.gz /var/lib/prometheus
   sudo systemctl start prometheus
   ```
   👉 Explication : une copie de répertoire actif sans arrêt risque d'être incohérente; en production, utiliser une méthode validée par l'équipe.

3. Copier les archives vers une cible indépendante et contrôler leur intégrité :
   ```bash
   sudo sha256sum /var/backups/prometheus-grafana/*.tar.gz
   ```
   👉 Explication : conserver les empreintes avec la copie hors machine, chiffrée et à accès restreint.

4. Avant mise à jour, lire les notes de version puis simuler :
   ```bash
   apt list --upgradable 2>/dev/null | grep -i grafana
   promtool check config /etc/prometheus/prometheus.yml
   ```
   👉 Explication : on identifie la mise à jour Grafana disponible et on confirme que la configuration reste valide.

5. Tester la restauration dans un environnement isolé :
   ```bash
   mkdir -p /tmp/restore-test
   sudo tar -xzf /var/backups/prometheus-grafana/config-$(date +%F).tar.gz -C /tmp/restore-test
   ls /tmp/restore-test/etc/prometheus
   ```
   👉 Explication : les fichiers doivent être lisibles; contrôler ensuite un dashboard et une règle sur l'instance de test.

## 2. Production — Contrôles

Définir RPO/RTO, fréquence, rétention, chiffrement, destination, propriétaire, procédure de restauration et test planifié.

## 3. Production — Sécurité

- Protéger les configurations et exports Grafana contenant tokens ou secrets de datasource.
- Ne pas considérer une copie à chaud du TSDB comme cohérente sans méthode validée.
- Ne pas remplacer l'unique copie de sauvegarde avant test de restauration.
- Tester une mise à niveau sur clone avant changement de version en production.

## Validation et retour arrière

- **Validation** : sauvegarde hors hôte, accès protégé et restauration testée; compatibilité upgrade vérifiée.
- **Retour arrière** : restaurer ensemble binaire, configuration et données compatibles conformément au plan validé.

## Si le problème n'est pas résolu

- [Prometheus — sauvegarde](https://prometheus.io/docs/prometheus/latest/querying/api/#snapshot)
- [Prometheus — administration](https://prometheus.io/docs/prometheus/latest/management_api/)
- [Grafana — sauvegarde](https://grafana.com/docs/grafana/latest/administration/back-up-grafana/)
- [Guide complet Prometheus/Grafana Debian 13](/02-fiches-completes/debian/13/installation-deploiement/45-deploiement-prometheus-grafana-debian-13#7-sauvegarde-et-mises-a-jour)
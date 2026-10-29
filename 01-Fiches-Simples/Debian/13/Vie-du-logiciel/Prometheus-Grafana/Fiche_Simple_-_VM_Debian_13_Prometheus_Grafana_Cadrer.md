# Fiche_Simple_-_VM_Debian_13_Prometheus_Grafana_Cadrer.md

- **Environnement** : VM Debian 13 dédiée; cibles de supervision explicitement autorisées
- **OS / Version** : Debian 13 Trixie; Prometheus 3.15.1 et Grafana OSS
- **Catégorie** : supervision / métrologie / cadrage
- **Tags** : `debian13`, `prometheus`, `grafana`, `cadrage`, `metrics`

---

## Problème précis à résoudre

Définir périmètre, rétention, cardinalité, seuils et responsabilités avant d'activer une collecte de métriques.

## 1. Hors-Production (Lab / Test / POC)

1. Énumérer les cibles autorisées et leurs propriétaires dans un tableau (hôte, port, propriétaire).
   👉 Explication : seules des cibles de test au départ.

2. Définir métriques, intervalle et rétention (valeurs consignées, exemple : intervalle 15 s, rétention 15 j) :
   ```bash
   echo "scrape_interval=15s retention=15d"
   ```
   👉 Explication : ces valeurs seront reprises dans `prometheus.yml` et l'option `--storage.tsdb.retention.time`.

3. Estimer le disque disponible et les ressources :
   ```bash
   nproc; free -h; df -h /var/lib
   ```
   👉 Explication : règle approximative : séries × échantillons/s × octets/échantillon (~1-2 octets) × rétention; surveiller la cardinalité.

4. Vérifier Node Exporter sur l'hôte attendu et le filtrage du port :
   ```bash
   systemctl is-active prometheus-node-exporter
   curl -s http://127.0.0.1:9100/metrics | head -3
   sudo ss -ltnp | grep 9100
   ```
   👉 Explication : le port 9100 ne doit être joignable que depuis Prometheus.

5. Consigner critères de validation, d'alerte et d'arrêt.
   👉 Explication : sans critère d'arrêt défini, le pilote ne peut pas être clos.

## 2. Production — Contrôles

Documenter propriétaires de cibles, astreinte, seuils, rétention, capacité, sauvegardes, règles de pare-feu, conformité des métriques et processus de mise à jour.

## 3. Production — Sécurité

- Ne pas collecter des hôtes ou adresses hors du périmètre autorisé.
- Ne pas collecter de labels contenant identifiants, secrets ou données personnelles.
- Limiter l'accès aux dashboards et endpoints; les métriques peuvent révéler topologie et capacité.
- Ne pas considérer Prometheus seul comme service d'alerting (Alertmanager non couvert).

## Validation et retour arrière

- **Validation** : liste de cibles, données, rétention, réseau et propriétaires approuvés.
- **Arrêt** : ne pas installer si les cibles ou données sensibles ne sont pas classifiées.

## Si le problème n'est pas résolu

- [Prometheus — configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)
- [Grafana — documentation](https://grafana.com/docs/grafana/latest/)
- [Guide complet Prometheus/Grafana Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/45_Deploiement_Prometheus_Grafana_Debian_13.md#1-definir-la-collecte)

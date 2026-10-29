# Fiche_Simple_-_VM_Debian_13_Prometheus_Grafana_Datasource.md

- **Environnement** : Grafana et Prometheus sur Debian 13, datasource locale
- **OS / Version** : Debian 13; Prometheus 3.15.1 et Grafana OSS
- **Catégorie** : supervision / datasource

---

## Problème précis à résoudre

Relier Grafana au Prometheus local et donner des droits adaptés aux utilisateurs.

## 1. Hors-Production (Lab / Test / POC)

1. Interface Grafana : ouvrir `http://127.0.0.1:3000` (ou l'URL du proxy), puis **Connections > Data sources > Add data source > Prometheus**.
   👉 Explication : on crée la source de données qui interroge Prometheus.

2. Renseigner **Prometheus server URL** : `http://127.0.0.1:9090`, puis cliquer sur **Save & test**.
   👉 Explication : le message « Successfully queried the Prometheus API » confirme la liaison; sinon vérifier le service et l'URL.

3. Vérifier l'accès côté serveur avant de continuer :
   ```bash
   curl -fsS http://127.0.0.1:9090/-/ready
   ```
   👉 Explication : la réponse doit indiquer que Prometheus est prêt.

4. Avant d'importer un dashboard, ouvrir **Dashboards > New > Import**, vérifier sa provenance, puis examiner les requêtes dans **Edit > Query**.
   👉 Explication : un modèle importé peut contenir des requêtes ou liens non prévus.

5. Attribuer un rôle limité : **Administration > Users and access > Users**, ouvrir l'utilisateur, puis choisir le rôle **Viewer**.
   👉 Explication : seuls les gestionnaires de dashboards ont besoin du rôle Editor/Admin.

6. Vérifier qu'aucun port n'est publié sur toutes les interfaces :
   ```bash
   sudo ss -tlnp | grep -E ':(9090|3000)\b'
   ```
   👉 Explication : `9090` doit être sur `127.0.0.1`; `3000` sur `127.0.0.1` si un proxy est utilisé.

## 2. Production — Contrôles

Définir comptes, rôles, dashboards propriétaires, rétention, partage externe, source d'identité et approbations des plugins.

## 3. Production — Sécurité

- Ne pas donner le rôle administrateur à tous les consommateurs de dashboards.
- Ne pas importer de tableaux de bord ou plugins sans revue de provenance.
- Les dashboards peuvent exposer noms d'hôtes, topologie et capacité; restreindre le partage.
- Ne pas exposer directement les interfaces Grafana ou Prometheus sans proxy et authentification approuvés.

## Validation et retour arrière

- **Validation** : datasource teste correctement, requêtes relues, droits limités et données attendues visibles.
- **Retour arrière** : supprimer uniquement la datasource ou le dashboard pilote identifié; exporter la configuration avant modification.

## Si le problème n'est pas résolu

- [Grafana — datasource Prometheus](https://grafana.com/docs/grafana/latest/datasources/prometheus/configure/)
- [Grafana — permissions](https://grafana.com/docs/grafana/latest/administration/user-management/manage-dashboard-permissions/)
- [Guide complet Prometheus/Grafana Debian 13](/02-fiches-completes/debian/13/installation-deploiement/45-deploiement-prometheus-grafana-debian-13#5-relier-grafana-a-prometheus)
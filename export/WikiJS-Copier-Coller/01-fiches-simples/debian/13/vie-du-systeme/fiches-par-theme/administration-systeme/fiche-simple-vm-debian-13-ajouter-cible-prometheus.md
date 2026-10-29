# 📄 Fiche_Simple_-_VM_Debian_13_Ajouter_Cible_Prometheus.md

- **Environnement** : Serveur Prometheus sur Debian 13
- **OS / Version** : Debian 13 Trixie, Prometheus 3.x
- **Catégorie** : Supervision / métriques

---

## 🎯 Problème précis à résoudre

Ajouter un exporteur à Prometheus sans exposer de métriques à des réseaux non autorisés.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier l'exporteur de la cible :
   ```bash
   curl -fsS http://IP_CIBLE:9100/metrics | head
   ```
   👉 Explication : remplacer par l'IP privée de la machine instrumentée; ne pas tester un hôte hors périmètre.

## ⚡ 2. Production — Façon Simplifiée

1. Sauvegarder la configuration Prometheus :
   ```bash
   sudo cp -a /etc/prometheus/prometheus.yml "/etc/prometheus/prometheus.yml.bak.$(date +%F-%H%M)"
   ```
   👉 Explication : point de retour arrière.

2. Ajouter un job dédié dans `/etc/prometheus/prometheus.yml` (`sudoedit`), sous `scrape_configs:` :
   ```yaml
     - job_name: "serveurs-linux"
       static_configs:
         - targets: ["IP_CIBLE:9100"]
           labels:
             environment: "production"
   ```
   👉 Explication : remplacer `IP_CIBLE`; garder des labels stables et à faible cardinalité.

3. Vérifier la syntaxe puis recharger :
   ```bash
   sudo promtool check config /etc/prometheus/prometheus.yml
   sudo systemctl reload prometheus
   ```
   👉 Explication : ne recharger que si le contrôle réussit; vérifier ensuite **Status > Targets** (`UP`).

## 🔒 3. Production — Façon Sécurisée

- Restreindre TCP/9100 sur l'hôte cible au seul serveur Prometheus; utiliser l'adresse privée et les règles firewall persistantes.
- Ne pas publier `/metrics` sur Internet ni sur un réseau utilisateur non maîtrisé.
- Utiliser TLS/authentification ou un proxy contrôlé si les métriques traversent une frontière réseau de confiance.
- Garder des noms de jobs et labels stables; éviter les labels de haute cardinalité comme UUID ou valeurs libres.

## ✅ Validation et retour arrière

- **Précontrôles** : exporteur actif, cible autorisée et sauvegarde du YAML.
- **Validation** : ouvrir **Status > Targets**, confirmer `UP`, puis vérifier `up{job="serveurs-linux"}`.
- **Retour arrière** : retirer le job ajouté, vérifier avec `promtool`, puis recharger Prometheus.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : [[Debian13_Prometheus_Cible_Down]]
- [Documentation officielle Prometheus — Node Exporter](https://prometheus.io/docs/guides/node-exporter/)
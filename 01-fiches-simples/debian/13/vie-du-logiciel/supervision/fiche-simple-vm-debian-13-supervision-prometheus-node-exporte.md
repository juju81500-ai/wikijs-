# 📄 VM_Debian_13_Supervision_Installation-Prometheus-Node-Exporter.md

- **Environnement** : VM (Debian 13 Trixie)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Supervision & Métriques / Prometheus Node Exporter
- **Tags** : `[debian13]`, `[prometheus]`, `[node-exporter]`, `[metrics]`, `[supervision]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer et configurer l'agent de collecte de métriques système Prometheus Node Exporter sur Debian 13 (Trixie), créer un compte système dédié sans privilèges, et sécuriser le métrique HTTP d'exposition (port 9100).

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide de prometheus-node-exporter depuis les dépôts Debian :
   `apt-get update && apt-get install -y prometheus-node-exporter`
   👉 Explication : Télécharge et installe le binaire d'exposition des métriques système du projet Debian.

2. Vérification immédiate du point de collecte HTTP local :
   `curl -s http://localhost:9100/metrics | head -n 15`
   👉 Explication : Interroge le serveur HTTP de Node Exporter et affiche les premières lignes de métriques au format Prometheus.

3. Vérification de l'état du service systemd :
   `systemctl status prometheus-node-exporter`
   👉 Explication : Contrôle le statut de fonctionnement du démon de métriques.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installer le paquet Debian, qui fournit normalement son propre compte de service et son unité systemd. Vérifier avant toute création de compte manuelle :
   ```bash
   systemctl cat prometheus-node-exporter
   getent passwd prometheus
   ```
   👉 Explication : Ne pas créer un second compte concurrent ; si l'agent est installé depuis un binaire tiers, suivre les instructions de ce paquet.

2. Configurer `/etc/default/prometheus-node-exporter` pour écouter sur l'IP privée assignée à la VM :
   ```text
   ARGS="--web.listen-address=192.0.2.10:9100"
   ```
   Remplacer l'adresse d'exemple par l'adresse de l'interface de supervision.

3. Activation et démarrage du service au boot :
   `systemctl enable --now prometheus-node-exporter`
   👉 Explication : S'assure que la collecte de métriques démarre automatiquement au lancement du système.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Si le transport TLS est nécessaire de bout en bout, créer un fichier web config et le passer explicitement à Node Exporter via `ARGS` :
   tls_server_config:
     cert_file: /etc/ssl/certs/node-exporter.crt
     key_file: /etc/ssl/private/node-exporter.key
   basic_auth_users:
     prometheus: <HASH_BCRYPT>
   👉 Explication : Ce fichier n'est pris en compte qu'avec `--web.config.file=/etc/prometheus/node-exporter-web.yml`. Créer le hash selon la documentation Prometheus, protéger la clé privée et configurer le même compte côté serveur Prometheus.

2. Après vérification du service utilisateur et des chemins, configurer dans `/etc/default/prometheus-node-exporter` :
   `ARGS="--web.listen-address=192.0.2.10:9100 --web.config.file=/etc/prometheus/node-exporter-web.yml"`
   puis recharger systemd si une surcharge d'unité a été modifiée et redémarrer l'exporter.

3. Surcharge des directives de sécurité systemd (ProtectSystem / PrivateTmp) :
   `echo -e "[Service]\nProtectSystem=strict\nProtectHome=true\nPrivateTmp=true\nNoNewPrivileges=true" > /etc/systemd/system/prometheus-node-exporter.service.d/hardening.conf && systemctl daemon-reload && systemctl restart prometheus-node-exporter`
   👉 Explication : Verrouille le service en lecture seule sur le reste du système de fichiers et isole ses répertoires temporaires.

4. Autoriser TCP/9100 uniquement depuis l'adresse du serveur Prometheus dans le pare-feu persistant géré par l'hôte. Valider et appliquer la règle par ce gestionnaire ; ne pas utiliser `nft add rule` seul comme règle de production.
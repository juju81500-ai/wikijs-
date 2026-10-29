---
title: "Déployer Prometheus 3.15.1 et Grafana sur Debian 13"
description: "Fiche simple : [cadrer la collecte](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Prometheus-Grafana/FicheSimple-VMDebian13PrometheusGrafanaCadrer.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "prometheus", "grafana", "node-exporter", "monitoring", "metrics"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer Prometheus 3.15.1 et Grafana sur Debian 13

- **OS / Version** : Debian 13 Trixie; Prometheus 3.15.1; Grafana OSS dépôt stable
- **Type de fiche** : Installation/Déploiement
- **Environnement** : VM Linux dédiée avec exporteurs sur des hôtes autorisés
- **Machine ciblée** : Serveur de métriques central
- **Catégorie** : Supervision / métrologie
- **Tags** : `debian13`, `prometheus`, `grafana`, `node-exporter`, `monitoring`, `metrics`

## 1. Définir la collecte

Fiche simple : [cadrer la collecte](/01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-cadrer).

Lister hôtes, métriques, intervalles, rétention, seuils et responsable d'astreinte. Dimensionner CPU/RAM/disque selon séries, cardinalité et rétention. Utiliser une liste explicite de cibles; ne pas collecter des adresses hors du périmètre autorisé.

Ce guide installe Prometheus et Grafana sur Debian 13. Il suppose que Node Exporter est déjà disponible sur l'hôte local (la fiche simple existante le configure). Pour alertes et notifications, déployer Alertmanager selon un guide séparé.

## 2. Installer Prometheus 3.15.1

Fiche simple : [installer Prometheus](/01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-installer-prometheus).

Créer l'utilisateur de service et les répertoires :

```bash
sudo useradd --system --no-create-home --shell /usr/sbin/nologin prometheus
sudo install -d -o prometheus -g prometheus -m 0750 /etc/prometheus /var/lib/prometheus
```

Télécharger la version officielle Linux AMD64 et vérifier son checksum :

```bash
cd /tmp
curl -fLO https://github.com/prometheus/prometheus/releases/download/v3.15.1/prometheus-3.15.1.linux-amd64.tar.gz
echo '6a726885328ad9efebbf36e876ce2fb6225468a71fd1e7ce3ba666d5f4d97a84  prometheus-3.15.1.linux-amd64.tar.gz' | sha256sum -c -
tar -xzf prometheus-3.15.1.linux-amd64.tar.gz
sudo install -o root -g root -m 0755 prometheus-3.15.1.linux-amd64/prometheus /usr/local/bin/prometheus
sudo install -o root -g root -m 0755 prometheus-3.15.1.linux-amd64/promtool /usr/local/bin/promtool
sudo cp -a prometheus-3.15.1.linux-amd64/consoles prometheus-3.15.1.linux-amd64/console_libraries /etc/prometheus/
sudo chown -R root:prometheus /etc/prometheus
sudo chown prometheus:prometheus /var/lib/prometheus
```

## 3. Configurer Prometheus

Fiche simple : [configurer Prometheus et son service](/01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-config-service).

Créer `/etc/prometheus/prometheus.yml` :

```yaml
global:
  scrape_interval: 30s
  evaluation_interval: 30s

scrape_configs:
  - job_name: prometheus
    static_configs:
      - targets: ["127.0.0.1:9090"]
  - job_name: node
    static_configs:
      - targets: ["127.0.0.1:9100"]
```

Protéger puis valider le fichier :

```bash
sudo chown root:prometheus /etc/prometheus/prometheus.yml
sudo chmod 0640 /etc/prometheus/prometheus.yml
sudo promtool check config /etc/prometheus/prometheus.yml
```

Créer `/etc/systemd/system/prometheus.service` :

```ini
[Unit]
Description=Prometheus monitoring server
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus --config.file=/etc/prometheus/prometheus.yml --storage.tsdb.path=/var/lib/prometheus --storage.tsdb.retention.time=15d --web.listen-address=127.0.0.1:9090 --web.external-url=https://metrics.example.net/
ExecReload=/bin/kill -HUP $MAINPID
Restart=on-failure
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=/var/lib/prometheus
PrivateTmp=true

[Install]
WantedBy=multi-user.target
```

Adapter `--web.external-url` au nom public réel. Prometheus n'applique pas d'authentification intégrée : le bind loopback le garde inaccessible du réseau. Pour un accès distant, utiliser un proxy authentifié/TLS contrôlé.

## 4. Installer Grafana OSS

Fiche simple : [installer Grafana](/01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-installer-grafana).

Ajouter le dépôt APT officiel Grafana, puis installer le paquet OSS :

```bash
sudo apt install -y apt-transport-https wget gnupg
sudo install -d -m 0755 /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/grafana.asc https://apt.grafana.com/gpg-full.key
sudo chmod 0644 /etc/apt/keyrings/grafana.asc
echo "deb [signed-by=/etc/apt/keyrings/grafana.asc] https://apt.grafana.com stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
sudo apt update
sudo apt install grafana
```

Si l'accès passe par un reverse proxy, configurer `http_addr = 127.0.0.1` dans `/etc/grafana/grafana.ini`, publier Grafana via HTTPS et activer SSO/MFA. Puis :

```bash
sudo systemctl enable --now grafana-server
sudo systemctl --no-pager status grafana-server
```

## 5. Relier Grafana à Prometheus

Fiche simple : [configurer la datasource](/01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-datasource).

Dans Grafana, ajouter la datasource **Prometheus** avec URL `http://127.0.0.1:9090`, puis **Save & test**. Créer un dashboard après contrôle des requêtes et de la source des modèles importés. Donner un rôle lecture seule aux utilisateurs qui ne gèrent pas les dashboards.

Ne pas publier directement les ports 9090 ou 3000 sur toutes les interfaces. N'autoriser les exporteurs que depuis le serveur Prometheus ou une passerelle de collecte approuvée.

## 6. Recette

Fiche simple : [valider la supervision](/01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-recette).

```bash
sudo systemctl --no-pager status prometheus grafana-server
curl -fsS http://127.0.0.1:9090/-/ready
curl -fsS http://127.0.0.1:9090/api/v1/targets
```

Vérifier que `prometheus` et `node` sont `UP`, puis afficher CPU, mémoire, disque et fuseau horaire dans Grafana.

## 7. Sauvegarde et mises à jour

Fiche simple : [sauvegarder et mettre à jour](/01-fiches-simples/debian/13/vie-du-logiciel/prometheus-grafana/fiche-simple-vm-debian-13-prometheus-grafana-sauvegarder).

Sauvegarder `/etc/prometheus`, `/etc/grafana`, dashboards/règles et `/var/lib/prometheus` via une méthode cohérente documentée; ne pas copier les fichiers TSDB actifs avec une simple archive. Avant upgrade, vérifier les notes de version et tester la migration sur une copie de la configuration et des données.

## Sources

- [Prometheus — Installation](https://prometheus.io/docs/prometheus/latest/installation/)
- [Prometheus — Version 3.15.1](https://github.com/prometheus/prometheus/releases/tag/v3.15.1)
- [Prometheus — Node Exporter](https://prometheus.io/docs/guides/node-exporter/)
- [Grafana — Installer sur Debian/Ubuntu](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/)
- [Grafana — Configurer la datasource Prometheus](https://grafana.com/docs/grafana/latest/datasources/prometheus/configure/)
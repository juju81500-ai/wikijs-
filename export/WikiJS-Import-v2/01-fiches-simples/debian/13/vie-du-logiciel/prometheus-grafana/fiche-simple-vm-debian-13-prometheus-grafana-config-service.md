---
title: "Fiche Simple - VM Debian 13 Prometheus Grafana Config Service"
description: "Configurer des cibles explicites, valider la syntaxe et lancer Prometheus lié à loopback."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "prometheus", "promtool", "systemd", "retention"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Prometheus_Grafana_Config_Service.md

- **Environnement** : serveur Prometheus Debian 13; Node Exporter local ou cibles approuvées
- **OS / Version** : Debian 13; Prometheus 3.15.1
- **Catégorie** : supervision / configuration de collecte
- **Tags** : `debian13`, `prometheus`, `promtool`, `systemd`, `retention`

---

## Problème précis à résoudre

Configurer des cibles explicites, valider la syntaxe et lancer Prometheus lié à loopback.

## 1. Hors-Production (Lab / Test / POC)

1. Créer `/etc/prometheus/prometheus.yml` avec uniquement les cibles autorisées :
   ```bash
   sudo tee /etc/prometheus/prometheus.yml >/dev/null <<'EOF'
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
   EOF
   ```
   👉 Explication : seules les cibles locales du pilote sont déclarées; ajouter les autres hôtes un par un après validation.

2. Protéger puis valider le fichier :
   ```bash
   sudo chown root:prometheus /etc/prometheus/prometheus.yml
   sudo chmod 0640 /etc/prometheus/prometheus.yml
   sudo promtool check config /etc/prometheus/prometheus.yml
   ```
   👉 Explication : `promtool` doit répondre `SUCCESS`; le compte de service lit le fichier sans pouvoir l'écrire.

3. Créer l'unité systemd non privilégiée :
   ```bash
   sudo tee /etc/systemd/system/prometheus.service >/dev/null <<'EOF'
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
   EOF
   ```
   👉 Explication : écriture limitée à `/var/lib/prometheus`, rétention de 15 jours, écoute sur loopback. Remplacer `metrics.example.net` par le nom public réel.

4. Démarrer et contrôler le service :
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable --now prometheus
   sudo systemctl --no-pager status prometheus
   sudo ss -tlnp | grep 9090
   sudo journalctl -u prometheus -n 30 --no-pager
   ```
   👉 Explication : l'écoute doit être sur `127.0.0.1:9090` et les journaux sans erreur de configuration.

## 2. Production — Contrôles

Faire relire les cibles, intervalles, labels, rétention, external URL, limites disque et changements de configuration.

## 3. Production — Sécurité

- Prometheus n'applique pas d'authentification intégrée; garder son interface sur loopback ou derrière un proxy authentifié/TLS.
- Ne pas collecter des endpoints non autorisés.
- Ne pas rendre les fichiers de configuration inscriptibles par le compte de service.
- Ne pas exposer le port 9090 sur toutes les interfaces.

## Validation et retour arrière

- **Validation** : `promtool check config` réussit, service systemd actif et port 9090 lié à loopback.
- **Retour arrière** : restaurer la configuration antérieure, revalider avec promtool puis recharger/redémarrer.

## Si le problème n'est pas résolu

- [Prometheus — configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)
- [Prometheus — sécurité](https://prometheus.io/docs/operating/security/)
- [Guide complet Prometheus/Grafana Debian 13](/02-fiches-completes/debian/13/installation-deploiement/45-deploiement-prometheus-grafana-debian-13#3-configurer-prometheus)
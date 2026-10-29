---
title: "Fiche Simple - VM Debian 13 Prometheus Grafana Installer Grafana"
description: "Installer Grafana OSS depuis le dépôt officiel et préparer un accès local derrière un frontal approuvé."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "grafana", "apt", "installation", "tls"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Prometheus_Grafana_Installer_Grafana.md

- **Environnement** : Debian 13; dépôt APT officiel Grafana
- **OS / Version** : Debian 13; Grafana OSS
- **Catégorie** : supervision / tableaux de bord
- **Tags** : `debian13`, `grafana`, `apt`, `installation`, `tls`

---

## Problème précis à résoudre

Installer Grafana OSS depuis le dépôt officiel et préparer un accès local derrière un frontal approuvé.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis et télécharger la clé officielle :
   ```bash
   sudo apt install -y apt-transport-https wget gnupg
   sudo install -d -m 0755 /etc/apt/keyrings
   sudo wget -O /etc/apt/keyrings/grafana.asc https://apt.grafana.com/gpg-full.key
   sudo chmod 0644 /etc/apt/keyrings/grafana.asc
   ```
   👉 Explication : la clé est stockée dans un trousseau dédié et ne sera valable que pour ce dépôt.

2. Déclarer le dépôt `stable` avec `signed-by` et vérifier le candidat :
   ```bash
   echo "deb [signed-by=/etc/apt/keyrings/grafana.asc] https://apt.grafana.com stable main" | sudo tee /etc/apt/sources.list.d/grafana.list
   sudo apt update
   apt-cache policy grafana
   ```
   👉 Explication : `apt-cache policy` doit montrer `apt.grafana.com` comme source du paquet.

3. Installer Grafana OSS :
   ```bash
   sudo apt install grafana
   ```
   👉 Explication : installe Grafana OSS et son unité systemd `grafana-server`.

4. Limiter l'écoute à loopback si un reverse proxy est prévu, dans `/etc/grafana/grafana.ini`, section `[server]` :
   ```ini
   http_addr = 127.0.0.1
   ```
   👉 Explication : Grafana n'est plus joignable directement depuis le réseau; seul le proxy HTTPS le publie.

5. Activer le service et le contrôler :
   ```bash
   sudo systemctl enable --now grafana-server
   sudo systemctl --no-pager status grafana-server
   sudo journalctl -u grafana-server -n 30 --no-pager
   ```
   👉 Explication : le service doit être `active (running)` sans erreur dans les journaux.

## 2. Production — Contrôles

Documenter version, dépôt, source d'authentification, propriétaire des dashboards, sauvegarde, mises à jour et accès utilisateurs.

## 3. Production — Sécurité

- Ne pas désactiver la validation APT ni installer depuis un miroir non approuvé.
- Ne pas exposer TCP/3000 directement au réseau utilisateur ou à Internet.
- Configurer TLS et SSO/MFA selon la politique avant ouverture.
- Changer les identifiants initiaux et utiliser des comptes nominatifs.

## Validation et retour arrière

- **Validation** : origine du paquet vérifiée, service actif et écoute limitée à l'interface attendue.
- **Retour arrière** : conserver la configuration précédente; ne pas purger les données/dashboard sans sauvegarde vérifiée.

## Si le problème n'est pas résolu

- [Grafana — installer sur Debian/Ubuntu](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/)
- [Grafana — configuration](https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/)
- [Guide complet Prometheus/Grafana Debian 13](/02-fiches-completes/debian/13/installation-deploiement/45-deploiement-prometheus-grafana-debian-13#4-installer-grafana-oss)
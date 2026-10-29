---
title: "Fiche Simple - VM Ubuntu 24.04 Supervision Zabbix Agent2"
description: "Installer Zabbix Agent 2 sur Ubuntu Server 24.04 LTS depuis le dépôt officiel, le relier à un serveur Zabbix précis, limiter les connexions entrantes et vérifier que l'hôte remonte ses métriques."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[zabbix]", "[zabbix-agent2]", "[monitoring]", "[ufw]", "[port-10050]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Supervision_Zabbix_Agent2

- **Environnement** : VM Ubuntu Server supervisée par un serveur Zabbix existant
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat) - Zabbix Agent 2 depuis le dépôt officiel Zabbix 7.0 LTS
- **Catégorie** : Supervision / Agent de métriques et d'inventaire
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[zabbix]`, `[zabbix-agent2]`, `[monitoring]`, `[ufw]`, `[port-10050]`

## 🎯 Problème précis à résoudre
Installer Zabbix Agent 2 sur Ubuntu Server 24.04 LTS depuis le dépôt officiel, le relier à un serveur Zabbix précis, limiter les connexions entrantes et vérifier que l'hôte remonte ses métriques.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Ajouter le dépôt officiel Zabbix 7.0 LTS pour Ubuntu 24.04 :
   ```bash
   cd /tmp
   wget https://repo.zabbix.com/zabbix/7.0/ubuntu/pool/main/z/zabbix-release/zabbix-release_latest_7.0+ubuntu24.04_all.deb
   sudo dpkg -i zabbix-release_latest_7.0+ubuntu24.04_all.deb
   sudo apt update
   ```
   👉 *Explication : Le paquet `zabbix-release` ajoute la source APT et la clé de signature. Le nom du fichier `.deb` change selon la version publiée ; vérifier l'URL sur repo.zabbix.com.*
2. Installer l'agent et tester une clé locale sans réseau :
   ```bash
   sudo apt install -y zabbix-agent2
   sudo zabbix_agent2 -t system.uptime
   ```
   👉 *Explication : L'option `-t` exécute une clé de contrôle en local et affiche la valeur, sans démarrer le service.*

## ⚡ 2. Production — Façon Simplifiée
1. Renseigner le serveur Zabbix et le nom de l'hôte dans la configuration :
   ```bash
   sudo cp -a /etc/zabbix/zabbix_agent2.conf /etc/zabbix/zabbix_agent2.conf.bak
   sudo sed -i 's/^Server=.*/Server=<ip_serveur_zabbix>/' /etc/zabbix/zabbix_agent2.conf
   sudo sed -i 's/^ServerActive=.*/ServerActive=<ip_serveur_zabbix>/' /etc/zabbix/zabbix_agent2.conf
   sudo sed -i 's/^Hostname=.*/Hostname=<nom_du_serveur>/' /etc/zabbix/zabbix_agent2.conf
   ```
   👉 *Explication : `Server` autorise les requêtes passives, `ServerActive` définit l'envoi actif, et `Hostname` doit correspondre exactement au nom déclaré dans l'interface Zabbix.*
2. Ouvrir le port 10050 uniquement pour le serveur Zabbix, puis démarrer l'agent :
   ```bash
   sudo ufw allow from <ip_serveur_zabbix> to any port 10050 proto tcp
   sudo systemctl enable --now zabbix-agent2
   systemctl status zabbix-agent2 --no-pager
   ```
   👉 *Explication : Le port 10050 ne doit jamais être ouvert à tout le réseau. La règle UFW précise limite l'accès à l'IP du serveur Zabbix.*

## 🔒 3. Production — Façon Sécurisée
1. Vérifier la liste blanche des serveurs autorisés et les permissions du fichier de configuration :
   ```bash
   grep -E '^(Server|ServerActive|Hostname)=' /etc/zabbix/zabbix_agent2.conf
   ls -l /etc/zabbix/zabbix_agent2.conf
   ```
   👉 *Explication : Le fichier peut contenir des secrets TLS/PSK ; il doit appartenir à `root` et ne pas être lisible par tous selon la politique du site.*
2. Tester la connexion depuis le serveur Zabbix avec `zabbix_get` (paquet `zabbix-get`) :
   ```bash
   zabbix_get -s <ip_de_cette_vm> -p 10050 -k agent.ping
   ```
   👉 *Explication : La réponse `1` confirme que l'agent accepte les requêtes du serveur. Toute autre IP doit recevoir un refus.*

## ✅ Validation et retour arrière
- Dans l'interface Zabbix, l'hôte doit passer au statut disponible (ZBX vert) après quelques minutes.
- Consulter les erreurs avec `sudo journalctl -u zabbix-agent2 --since today --no-pager`.
- Retour arrière : `sudo systemctl disable --now zabbix-agent2`, `sudo ufw delete allow from <ip_serveur_zabbix> to any port 10050 proto tcp`, puis `sudo apt purge -y zabbix-agent2`.
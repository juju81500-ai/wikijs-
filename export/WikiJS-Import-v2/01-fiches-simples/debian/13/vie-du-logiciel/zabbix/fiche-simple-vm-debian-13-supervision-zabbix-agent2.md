---
title: "Fiche Simple - VM Debian 13 Supervision Zabbix Agent2"
description: "Installer l'agent Zabbix 2 sur Debian 13 à partir des dépôts Debian, le relier au serveur Zabbix, et vérifier la communication sur le port 10050 sans autoriser l'exécution de commandes à distance."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[debian13]", "[debian]", "[zabbix]", "[zabbix-agent2]", "[supervision]", "[monitoring]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Debian_13_Supervision_Zabbix_Agent2

- **Environnement** : VM ou serveur Debian 13 supervisé par un serveur Zabbix
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Supervision / Agent Zabbix
- **Tags** : `[debian13]`, `[debian]`, `[zabbix]`, `[zabbix-agent2]`, `[supervision]`, `[monitoring]`

## 🎯 Problème précis à résoudre
Installer l'agent Zabbix 2 sur Debian 13 à partir des dépôts Debian, le relier au serveur Zabbix, et vérifier la communication sur le port 10050 sans autoriser l'exécution de commandes à distance.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer l'agent et vérifier la version disponible :
   ```bash
   sudo apt-get update
   sudo apt-get install -y zabbix-agent2
   zabbix_agent2 -V
   ```
   👉 Explication : Le paquet `zabbix-agent2` est fourni par les dépôts Debian 13. Pour une version plus récente que celle de Debian, déclarer le dépôt Zabbix officiel dans `/etc/apt/sources.list.d/` au format deb822 (fichier `.sources`), jamais dans `sources.list`.

2. Renseigner l'adresse du serveur et le nom de l'hôte dans la configuration :
   ```bash
   sudo sed -i 's/^#\? *Server=.*/Server=<ip_zabbix_server>/' /etc/zabbix/zabbix_agent2.conf
   sudo sed -i 's/^#\? *ServerActive=.*/ServerActive=<ip_zabbix_server>/' /etc/zabbix/zabbix_agent2.conf
   sudo sed -i 's/^#\? *Hostname=.*/Hostname=<nom_du_serveur>/' /etc/zabbix/zabbix_agent2.conf
   grep -E "^(Server|ServerActive|Hostname)=" /etc/zabbix/zabbix_agent2.conf
   ```
   👉 Explication : `Server` autorise les requêtes passives du serveur, `ServerActive` gère les contrôles actifs initiés par l'agent, et `Hostname` doit correspondre exactement au nom de l'hôte déclaré dans l'interface Zabbix.

3. Redémarrer l'agent et tester une clé localement :
   ```bash
   sudo systemctl restart zabbix-agent2
   sudo zabbix_agent2 -t agent.ping
   ```
   👉 Explication : `zabbix_agent2 -t` exécute la clé sans passer par le réseau. Le résultat attendu est `agent.ping [s|1]`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activer le démarrage automatique et contrôler l'état du service :
   ```bash
   sudo systemctl enable --now zabbix-agent2
   systemctl status zabbix-agent2 --no-pager
   ```
   👉 Explication : Le service `zabbix-agent2` doit être `active (running)` et démarrer avec la machine.

2. Depuis le serveur Zabbix ou un poste de supervision, tester la réponse de l'agent sur le port 10050 :
   ```bash
   zabbix_get -s <ip_serveur> -p 10050 -k agent.ping
   ```
   👉 Explication : Le binaire `zabbix_get` est fourni par le paquet `zabbix-get` (à installer sur le poste de supervision). La réponse `1` confirme que l'agent est joignable.

3. Déclarer l'hôte dans l'interface Zabbix avec le même `Hostname` et l'adresse de l'agent, puis vérifier que les métriques remontent (disponibilité `ZBX` au vert).

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier que les commandes à distance sont désactivées et qu'aucune clé dangereuse n'est autorisée :
   ```bash
   grep -E "^(EnableRemoteCommands|DenyKey|AllowKey)" /etc/zabbix/zabbix_agent2.conf
   ```
   👉 Explication : `EnableRemoteCommands=0` doit être le réglage effectif, pour empêcher le serveur Zabbix d'exécuter des commandes shell sur la machine. Ajouter `DenyKey=system.run[*]` si la valeur n'est pas présente.

2. Limiter le port 10050 au seul serveur Zabbix dans le pare-feu hôte (voir la fiche nftables de Debian 13) :
   ```bash
   sudo nft list ruleset | grep 10050
   ```
   👉 Explication : Le port 10050 ne doit accepter que l'adresse de `<ip_zabbix_server>`. Un agent ouvert à tout le réseau expose les métriques de la machine.

3. Contrôler les journaux de l'agent pour repérer les refus de connexion ou les erreurs de configuration :
   ```bash
   sudo journalctl -u zabbix-agent2 --since today --no-pager | tail -n 30
   ```
   👉 Explication : Un message `Cannot accept incoming connection` révèle une adresse `Server=` incorrecte ou un pare-feu qui bloque le serveur.
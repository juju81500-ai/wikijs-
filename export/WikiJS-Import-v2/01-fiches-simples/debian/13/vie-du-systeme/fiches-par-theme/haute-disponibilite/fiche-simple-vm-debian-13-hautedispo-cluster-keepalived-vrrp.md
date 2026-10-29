---
title: "VM_Debian_13_HauteDispo_Cluster-Keepalived-VRRP"
description: "Mettre en place une adresse IP virtuelle flottante (VIP) partagée entre deux nœuds Debian 13 (Trixie) à l'aide du protocole VRRP avec keepalived, assurer le basculement automatique en cas de panne et sécuriser les échanges d'état."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian13]", "[keepalived]", "[vrrp]", "[ha]", "[vip]", "[high-availability]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_13_HauteDispo_Cluster-Keepalived-VRRP.md

- **Environnement** : VM (Debian 13 Trixie / Cluster HA)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Haute Disponibilité / Virtual IP (VRRP)
- **Tags** : `[debian13]`, `[keepalived]`, `[vrrp]`, `[ha]`, `[vip]`, `[high-availability]`, `[hardening]`

## 🎯 Problème précis à résoudre
Mettre en place une adresse IP virtuelle flottante (VIP) partagée entre deux nœuds Debian 13 (Trixie) à l'aide du protocole VRRP avec `keepalived`, assurer le basculement automatique en cas de panne et sécuriser les échanges d'état.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide de keepalived sur les deux nœuds :
   `apt-get update && apt-get install -y keepalived`
   👉 Explication : Télécharge et installe le démon de gestion du protocole VRRP et de vérification d'état.

2. Vérification de la détection de la carte réseau :
   `ip -br addr`
   👉 Explication : Identifie le nom précis de l'interface réseau maître (ex: `eth0`).

3. Démarrage du service keepalived :
   `systemctl start keepalived`
   👉 Explication : Lance le processus de négociation VRRP.

---

## ⚡ 2. Production — Façon Simplifiée
1. Configuration du Nœud Maître (MASTER) dans `/etc/keepalived/keepalived.conf` :
   vrrp_instance VI_1 {
       state MASTER
       interface eth0
       virtual_router_id 51
       priority 101
       advert_int 1
       virtual_ipaddress {
           192.168.1.200/24 dev eth0
       }
   }
   👉 Explication : Définit ce serveur comme nœud prioritaire (`priority 101`) portant l'adresse IP flottante `192.168.1.200`.

2. Configuration du Nœud de Secours (BACKUP) dans `/etc/keepalived/keepalived.conf` :
   vrrp_instance VI_1 {
       state BACKUP
       interface eth0
       virtual_router_id 51
       priority 100
       advert_int 1
       virtual_ipaddress {
           192.168.1.200/24 dev eth0
       }
   }
   👉 Explication : Définit le second nœud comme serveur passif de secours (`priority 100`) prêt à reprendre la VIP.

3. Démarrage et activation au boot sur les deux nœuds :
   `systemctl enable --now keepalived`
   👉 Explication : Lance le service et monte l'adresse IP flottante `192.168.1.200` sur le nœud MASTER.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Ajout d'un script de contrôle de santé de service (Healthcheck Script) dans la configuration VRRP :
   vrrp_script check_haproxy {
       script "/usr/bin/killall -0 haproxy"
       interval 2
       weight 2
   }
   👉 Explication : Surveille en continu la disponibilité du service applicatif et réduit la priorité VRRP en cas de défaillance.

2. Garder les fichiers de configuration lisibles uniquement par root :
   `sudo chown root:root /etc/keepalived/keepalived.conf && sudo chmod 600 /etc/keepalived/keepalived.conf`
   👉 Explication : Les mots de passe VRRP ne chiffrent pas le protocole et ne doivent pas être considérés comme une protection contre l'écoute.

3. Autoriser le protocole IP 112 uniquement entre les deux pairs dans le pare-feu persistant géré par le serveur. Valider la règle depuis la console avant application ; ne pas utiliser `nft add rule` seul comme règle permanente.
---
title: "LXC_Alpine_3.19_Reseau_Fixer-IP-OpenRC"
description: "Fixer une adresse IP statique permanente, configurer le résolveur DNS et sécuriser la pile réseau sur un conteneur LXC Alpine Linux 3.19 sous OpenRC."
published: true
date: 2026-10-29T20:22:41Z
tags: ["[alpine3.19]", "[alpine]", "[reseau]", "[ip-statique]", "[openrc]", "[apk]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:41Z
dateModified: 2026-10-29T20:22:41Z
---

# 📄 LXC_Alpine_3.19_Reseau_Fixer-IP-OpenRC.md

- **Environnement** : LXC (Proxmox VE / PXC)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine
- **Catégorie** : Réseau
- **Tags** : `[alpine3.19]`, `[alpine]`, `[reseau]`, `[ip-statique]`, `[openrc]`, `[apk]`, `[hardening]`

## 🎯 Problème précis à résoudre
Fixer une adresse IP statique permanente, configurer le résolveur DNS et sécuriser la pile réseau sur un conteneur LXC Alpine Linux 3.19 sous OpenRC.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Assignation temporaire de l'adresse IP en mémoire :
   `ip addr add 192.168.1.60/24 dev eth0`
   👉 Explication : Applique immédiatement l'adresse IP 192.168.1.60 sur l'interface eth0 sans persistance au redémarrage.

2. Ajout de la route par défaut temporaire :
   `ip route add default via 192.168.1.1 dev eth0`
   👉 Explication : Définit la passerelle de sortie pour le trafic sortant.

3. Test immédiat de joignabilité :
   `ping -c 3 192.168.1.1`
   👉 Explication : Valide la communication de bas niveau avec la passerelle du laboratoire.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sur l'hôte Proxmox, relever la configuration du CT :
   ```bash
   pct config CTID
   ```
   👉 Explication : Dans un LXC Proxmox, l'adresse, la passerelle et le DNS sont généralement gérés par l'hôte, pas par `/etc/network/interfaces` dans Alpine.

2. Depuis l'interface Proxmox, modifier l'IPv4/IPv6, la passerelle et le DNS dans la configuration réseau du CT. Utiliser une adresse libre du bon bridge/VLAN et appliquer avec une console de secours disponible.

3. Dans le CT, vérifier l'adresse, la route et les paramètres DNS fournis :
   ```sh
   ip addr
   ip route
   cat /etc/resolv.conf
   ```
   👉 Explication : Ne pas éditer les fichiers réseau internes si Proxmox les régénère.

---

## 🔒 3. Production — Façon Sécurisée

1. Réserver l'adresse dans le plan IP ou DHCP et conserver Proxmox comme source unique de configuration.
2. Définir les règles de filtrage au niveau Proxmox/routeur selon les flux requis. Ne pas activer Awall/iptables dans le CT sans vérifier les capacités et la politique de l'hôte.
3. Ne pas désactiver IPv6 globalement ni rendre `/etc/resolv.conf` immuable. Si IPv6 est interdit par la politique, le désactiver au niveau réseau approprié et vérifier que DNS, routage et supervision restent opérationnels.
4. Tester SSH et les services depuis un second terminal et garder la console Proxmox accessible. En cas de perte d'accès, corriger la configuration réseau du CT depuis l'hôte.
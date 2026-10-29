---
title: "VM_Debian_12_Reseau_Fixer-IP-Statique"
description: "Fixer une adresse IP statique permanente, configurer le résolveur DNS et sécuriser la pile réseau sur une machine virtuelle Debian 12."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian12]", "[debian-family]", "[reseau]", "[ip-statique]", "[systemd-networkd]", "[nftables]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_12_Reseau_Fixer-IP-Statique.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Réseau
- **Tags** : `[debian12]`, `[debian-family]`, `[reseau]`, `[ip-statique]`, `[systemd-networkd]`, `[nftables]`, `[hardening]`

## 🎯 Problème précis à résoudre
Fixer une adresse IP statique permanente, configurer le résolveur DNS et sécuriser la pile réseau sur une machine virtuelle Debian 12.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Assignation temporaire de l'IP en mémoire :
   `ip addr add 192.168.1.50/24 dev eth0`
   👉 Explication : Applique immédiatement l'adresse IP 192.168.1.50 sur l'interface eth0 de manière volatile.
2. Ajout de la route par défaut temporaire :
   `ip route add default via 192.168.1.1 dev eth0`
   👉 Explication : Définit la passerelle de sortie temporaire.
3. Test de connectivité :
   `ping -c 3 192.168.1.1`
   👉 Explication : Vérifie la joignabilité de la passerelle.

---

## ⚡ 2. Production — Façon Simplifiée
1. Édition de la configuration réseau :
   `nano /etc/network/interfaces`
2. Bloc de configuration :
   iface eth0 inet static
     address 192.168.1.50/24
     gateway 192.168.1.1
   dns-nameservers 192.168.1.10
   👉 Explication : Fixe l'IP de manière persistante au redémarrage.
3. Application du réseau :
   `systemctl restart networking`
   👉 Explication : Recharge la pile réseau classique.

---

## 🔒 3. Production — Façon Sécurisée

1. Utiliser un seul gestionnaire réseau. Avant d'éditer, contrôler l'interface et les services actifs :
   ```bash
   ip -br addr
   systemctl is-active networking systemd-networkd NetworkManager
   ```
   👉 Explication : Ne pas activer `systemd-networkd` en parallèle d'ifupdown. Une bascule de gestionnaire se planifie avec console de secours.

2. Sauvegarder `/etc/network/interfaces`, conserver le DNS interne approuvé (exemple `192.168.1.10`) et adapter la configuration à l'interface réelle. Ne pas remplacer un fichier par un `echo` ni supprimer les autres déclarations.

3. Appliquer le changement pendant une fenêtre avec accès console. Tester l'adresse, la route, la résolution DNS et une nouvelle connexion avant de fermer l'accès de secours.

4. Le pare-feu doit être configuré par son propriétaire persistant (`nftables`, firewalld ou hôte Proxmox). Ne pas utiliser `nft add rule` comme configuration finale et ne pas figer `/etc/resolv.conf` : ce fichier peut être généré par le gestionnaire DNS.
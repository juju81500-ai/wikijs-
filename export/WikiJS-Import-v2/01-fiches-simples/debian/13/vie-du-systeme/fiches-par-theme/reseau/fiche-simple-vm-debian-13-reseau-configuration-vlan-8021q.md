---
title: "VM_Debian_13_Reseau_Configuration-VLAN-8021q"
description: "Configurer un trunk VLAN 802.1Q (ex: VLAN 10 Administration) sur une interface réseau physique sous Debian 13 avec systemd-networkd."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian13]", "[vlan]", "[systemd-networkd]", "[8021q]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_13_Reseau_Configuration-VLAN-8021q.md

- **Environnement** : VM (Debian 13)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Réseau / VLAN 802.1Q
- **Tags** : `[debian13]`, `[vlan]`, `[systemd-networkd]`, `[8021q]`, `[hardening]`

## 🎯 Problème précis à résoudre
Configurer un trunk VLAN 802.1Q (ex: VLAN 10 Administration) sur une interface réseau physique sous Debian 13 avec `systemd-networkd`.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Chargement du module noyau et création dynamique de la sous-interface VLAN :
   `modprobe 8021q && ip link add link eth0 name eth0.10 type vlan id 10`
   👉 Explication : Instancie immédiatement l'interface virtuelle pour le VLAN 10 sur la carte eth0.

2. Assignation d'adresse et activation du lien :
   `ip addr add 10.10.0.50/24 dev eth0.10 && ip link set dev eth0.10 up`
   👉 Explication : Attribue une adresse IP de test et monte l'interface VLAN.

3. Test de communication sur le sous-réseau VLAN :
   `ping -c 2 10.10.0.1`
   👉 Explication : Vérifie la joignabilité de la passerelle du VLAN 10.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarder la configuration réseau existante et créer `/etc/systemd/network/10-vlan10.netdev` avec un éditeur :
   ```ini
   [NetDev]
   Name=eth0.10
   Kind=vlan

   [VLAN]
   Id=10
   ```
   👉 Explication : Déclare le périphérique virtuel VLAN 10 auprès de systemd.

2. Ajouter `VLAN=eth0.10` dans la section `[Network]` du fichier `.network` qui gère déjà l'interface physique. Ne pas remplacer un fichier existant : il peut porter l'adresse de gestion et la route par défaut.

3. Créer `/etc/systemd/network/20-vlan10.network` avec l'adresse et la passerelle validées pour le VLAN :
   ```ini
   [Match]
   Name=eth0.10

   [Network]
   Address=10.10.0.50/24
   Gateway=10.10.0.1
   ```
   👉 Explication : Configure l'adresse IP statique et la passerelle du VLAN.

4. Depuis une console ou avec accès de secours, valider la configuration puis reconfigurer le lien :
   ```bash
   sudo networkctl reload
   sudo networkctl reconfigure eth0
   networkctl status eth0.10
   ```
   👉 Explication : Un redémarrage du gestionnaire réseau peut couper la session distante ; vérifier le VLAN depuis le réseau avant de quitter la console.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Ne modifier ICMP Redirects que si le rôle de routage et la politique réseau l'exigent ; ne pas utiliser la clé sysctl `net.ipv4.conf.eth0/10`, qui ne correspond pas à un chemin sysctl valide.

2. Verrouillage des permissions sur les fichiers de configuration réseau :
   `chmod 600 /etc/systemd/network/*.netdev /etc/systemd/network/*.network`
   👉 Explication : Empêche la lecture de la topologie réseau par des utilisateurs non privilégies.

3. Appliquer le filtrage inter-VLAN sur le pare-feu persistant propriétaire du trafic (hôte, routeur ou pare-feu local). Autoriser les seuls flux nécessaires et valider avant application ; une règle `nft add rule` ajoutée à chaud n'est pas persistante.
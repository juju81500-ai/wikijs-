---
title: "Fiche Simple - VM Rocky 9 WireGuard Configurer"
description: "Configurer une interface serveur et un premier pair avec adressage approuvé."
published: true
date: 2026-10-29T21:01:00Z
tags: ["wireguard", "rocky9", "vie-du-logiciel", "configurer"]
editor: markdown
dateCreated: 2026-10-29T21:01:00Z
dateModified: 2026-10-29T21:01:00Z
---

# Fiche_Simple_-_VM_Rocky_9_WireGuard_Configurer

- **Environnement** : VM Rocky Linux 9 dédiée à un serveur WireGuard natif
- **OS / Version** : Rocky Linux 9; wireguard-tools issu d'EPEL, module noyau à vérifier sur l'hôte
- **Catégorie** : WireGuard natif / configurer
- **Tags** : `wireguard`, `rocky9`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Configurer une interface serveur et un premier pair avec adressage approuvé.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire privé et générer la clé serveur sans l'afficher :
   ```bash
   sudo install -d -o root -g root -m 0700 /etc/wireguard
   sudo sh -c "umask 077; wg genkey > /etc/wireguard/server.key; wg pubkey < /etc/wireguard/server.key > /etc/wireguard/server.pub"
   sudo cat /etc/wireguard/server.pub
   ```
   👉 Explication : Seule la clé publique peut être communiquée; server.key reste privée.

2. Créer /etc/wireguard/wg0.conf avec sudoedit /etc/wireguard/wg0.conf :
   ```ini
   [Interface]
   Address = VPN_SERVER_CIDR
   ListenPort = VPN_UDP_PORT
   PrivateKey = CONTENU_DE_SERVER_KEY

   [Peer]
   PublicKey = CLIENT_PUBLIC_KEY
   AllowedIPs = CLIENT_VPN_ADDRESS/32
   ```
   👉 Explication : Remplacer VPN_SERVER_CIDR, VPN_UDP_PORT, CLIENT_PUBLIC_KEY et CLIENT_VPN_ADDRESS par le plan validé; coller CONTENU_DE_SERVER_KEY depuis le fichier server.key directement dans l'éditeur, sans l'écrire ailleurs.

3. Protéger la configuration :
   ```bash
   sudo chown root:root /etc/wireguard/wg0.conf /etc/wireguard/server.key
   sudo chmod 600 /etc/wireguard/wg0.conf /etc/wireguard/server.key
   ```
   👉 Explication : wg0.conf contient la clé privée : lecture root uniquement.

## 2. Production — Contrôles

Vérifier l'unicité des AllowedIPs; un /32 par pair client.

## 3. Production — Sécurité

- Ne pas utiliser 0.0.0.0/0 sans architecture full-tunnel validée; ne pas activer le routage IP implicitement.

## Validation et retour arrière

- **Validation** : Configuration prête, secrets protégés, interface non encore démarrée.
- **Retour arrière** : Supprimer /etc/wireguard/wg0.conf et les fichiers de clés créés.

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-securiser)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard — démarrage rapide](https://www.wireguard.com/quickstart/)
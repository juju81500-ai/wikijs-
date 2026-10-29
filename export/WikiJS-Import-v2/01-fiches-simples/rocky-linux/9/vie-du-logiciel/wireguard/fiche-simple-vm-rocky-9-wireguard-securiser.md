---
title: "Fiche Simple - VM Rocky 9 WireGuard Securiser"
description: "Réduire l'exposition du serveur WireGuard."
published: true
date: 2026-10-29T21:01:00Z
tags: ["wireguard", "rocky9", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T21:01:00Z
dateModified: 2026-10-29T21:01:00Z
---

# Fiche_Simple_-_VM_Rocky_9_WireGuard_Securiser

- **Environnement** : VM Rocky Linux 9 dédiée à un serveur WireGuard natif
- **OS / Version** : Rocky Linux 9; wireguard-tools issu d'EPEL, module noyau à vérifier sur l'hôte
- **Catégorie** : WireGuard natif / sécuriser
- **Tags** : `wireguard`, `rocky9`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Réduire l'exposition du serveur WireGuard.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir seulement le port UDP VPN (firewalld) :
   ```bash
   sudo firewall-cmd --permanent --add-port=VPN_UDP_PORT/udp
   sudo firewall-cmd --reload
   sudo firewall-cmd --list-all
   ```
   👉 Explication : VPN_UDP_PORT est à remplacer par le port UDP retenu. N'ajouter --add-masquerade que si le plan réseau impose du NAT.

2. Activer le routage uniquement si le serveur doit joindre un réseau interne :
   ```bash
   echo 'net.ipv4.ip_forward=1' | sudo tee /etc/sysctl.d/99-wireguard.conf
   sudo sysctl --system
   ```
   👉 Explication : Ajouter ensuite des règles de pare-feu limitant les destinations autorisées; ne pas router sans plan approuvé.

3. Contrôler les droits :
   ```bash
   sudo ls -l /etc/wireguard
   ```
   👉 Explication : server.key et wg0.conf doivent être en 0600, propriétaire root.

## 2. Production — Contrôles

Restreindre SSH au réseau d'administration; prévoir la rotation des clés d'un pair compromis (retrait du bloc Peer puis rechargement).

## 3. Production — Sécurité

- Retirer tout pair perdu ou sorti immédiatement : c'est la seule révocation possible.

## Validation et retour arrière

- **Validation** : Seul le port UDP VPN est ouvert; droits conformes.
- **Retour arrière** : sudo firewall-cmd --permanent --remove-port=VPN_UDP_PORT/udp && sudo firewall-cmd --reload

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-valider)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard — démarrage rapide](https://www.wireguard.com/quickstart/)
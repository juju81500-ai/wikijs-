---
title: "Fiche Simple - VM Debian 13 WireGuard Configurer"
description: "Configurer une interface serveur et un pair client unique avec adressage approuvé."
published: true
date: 2026-10-29T20:35:43Z
tags: ["wireguard", "debian13", "vie-du-logiciel", "configurer"]
editor: markdown
dateCreated: 2026-10-29T20:35:43Z
dateModified: 2026-10-29T20:35:43Z
---

# Fiche_Simple_-_VM_Debian_13_WireGuard_Configurer

- **Environnement** : VM Debian 13 dédiée à WireGuard natif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : WireGuard natif / configurer
- **Tags** : `wireguard`, `debian13`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Configurer une interface serveur et un pair client unique avec adressage approuvé.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire privé et générer la clé serveur sans l’afficher :
   ```bash
   sudo install -d -o root -g root -m 0700 /etc/wireguard
   sudo sh -c "umask 077; wg genkey > /etc/wireguard/server.key; wg pubkey < /etc/wireguard/server.key > /etc/wireguard/server.pub"
   sudo cat /etc/wireguard/server.pub
   ```
   👉 Explication : Seule la clé publique peut être copiée vers l’équipe cliente; ne jamais afficher ni transmettre server.key.

2. Créer `/etc/wireguard/wg0.conf` :
   ```bash
   sudoedit /etc/wireguard/wg0.conf
   ```
   Exemple à adapter :
   ```ini
   [Interface]
   Address = VPN_SERVER_CIDR
   ListenPort = VPN_UDP_PORT
   PrivateKey = SERVER_PRIVATE_KEY_CONTENT

   [Peer]
   PublicKey = CLIENT_PUBLIC_KEY
   AllowedIPs = CLIENT_VPN_ADDRESS/32
   ```
   👉 Explication : Remplacer les valeurs en capitales par les adresses et clés propres au déploiement; utiliser la clé serveur conservée en mode privé.

3. Protéger la configuration :
   ```bash
   sudo chown root:root /etc/wireguard/wg0.conf /etc/wireguard/server.key
   sudo chmod 600 /etc/wireguard/wg0.conf /etc/wireguard/server.key
   ```
   👉 Explication : Le fichier de configuration contient la clé privée et reste lisible par root uniquement.

## 2. Production — Contrôles

Vérifier unicité des AllowedIPs et cohérence des routes; un /32 par pair est recommandé pour un client individuel.

## 3. Production — Sécurité

- Ne pas utiliser 0.0.0.0/0 sans architecture full-tunnel validée; ne pas activer implicitement le transfert IP.

## Validation et retour arrière

- **Validation** : Configuration préparée, secrets protégés et règles réseau non encore modifiées.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [WireGuard natif — documentation officielle](https://www.wireguard.com/quickstart/)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-securiser)
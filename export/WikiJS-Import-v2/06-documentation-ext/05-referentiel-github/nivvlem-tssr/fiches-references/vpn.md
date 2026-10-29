---
title: "VPN (OpenVPN / WireGuard)"
description: "Un VPN (Virtual Private Network) permet de créer un tunnel sécurisé entre deux réseaux ou entre un client et un serveur distant, en chiffrant le trafic. Deux solutions très répandues sont :"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# VPN (OpenVPN / WireGuard)

## 📌 Présentation

Un VPN (Virtual Private Network) permet de créer un tunnel sécurisé entre deux réseaux ou entre un client et un serveur distant, en chiffrant le trafic. Deux solutions très répandues sont :
- **OpenVPN** : basé sur SSL/TLS, très configurable
- **WireGuard** : plus récent, rapide, et au code plus léger

---

## 🔧 Configuration OpenVPN (serveur Linux)

1. **Installation** :

```bash
sudo apt update && sudo apt install openvpn easy-rsa
```

2. **Préparation des certificats** avec Easy-RSA :

```bash
make-cadir ~/openvpn-ca
cd ~/openvpn-ca
./easyrsa init-pki
./easyrsa build-ca
./easyrsa gen-req server nopass
./easyrsa sign-req server server
```

3. **Configuration du serveur** : `/etc/openvpn/server.conf`

```ini
port 1194
dev tun
proto udp
server 10.8.0.0 255.255.255.0
ca ca.crt
cert server.crt
key server.key
dh dh.pem
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 1.1.1.1"
keepalive 10 120
```

4. **Lancement du service** :

```bash
sudo systemctl start openvpn@server
```

---

## ⚙️ Configuration client OpenVPN (fichier `.ovpn`)
```ini
client
dev tun
proto udp
remote mon-serveur.domaine.fr 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
cert client.crt
key client.key
remote-cert-tls server
```

---

## 🔧 Configuration WireGuard

1. **Installation** :

```bash
sudo apt install wireguard
```

2. **Génération des clés** :

```bash
wg genkey | tee privatekey | wg pubkey > publickey
```

3. **Fichier de configuration serveur** : `/etc/wireguard/wg0.conf`

```ini
[Interface]
PrivateKey = <clé privée serveur>
Address = 10.0.0.1/24
ListenPort = 51820

[Peer]
PublicKey = <clé publique client>
AllowedIPs = 10.0.0.2/32
```

4. **Client WireGuard** (exemple Windows/macOS/Android)
```ini
[Interface]
PrivateKey = <clé privée client>
Address = 10.0.0.2/24
DNS = 1.1.1.1

[Peer]
PublicKey = <clé publique serveur>
Endpoint = mon-serveur.domaine.fr:51820
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
```

---

## 🔎 Cas d’usage courant

- Connexion sécurisée à un réseau d’entreprise à distance
- Accès aux ressources internes (NAS, serveur, imprimantes)
- Création d’un pont sécurisé entre deux sites (site-to-site)

---

## ⚠️ Erreurs fréquentes

- Clés ou certificats mal générés ou mal placés
- Port VPN bloqué par le pare-feu (ex : 1194 UDP ou 51820 UDP)
- Adresse IP déjà utilisée dans la plage VPN
- Mauvaise redirection NAT sur le routeur
- Problème de MTU causant des lenteurs ou coupures

---

## ✅ Bonnes pratiques

- Toujours sécuriser les clés et certificats générés
- Utiliser des noms explicites pour les fichiers (client1.ovpn, srv.key…)
- Activer des logs pour diagnostiquer les connexions VPN
- Tester en local avant de déployer en production
- Prévoir une révocation des certificats ou clés (OpenVPN via CRL)

---

## 📚 Ressources complémentaires

- [Documentation OpenVPN](https://openvpn.net/community-resources/how-to/)
- [Documentation WireGuard](https://www.wireguard.com/quickstart/)
- `man openvpn`, `man wg`, `man wg-quick`
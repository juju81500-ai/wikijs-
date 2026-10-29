---
title: "pfSense (pare-feu et routeur open source)"
description: "pfSense est une distribution basée sur FreeBSD utilisée comme pare-feu, routeur et passerelle réseau. Elle est administrable via une interface web très complète et permet de gérer des VLAN, VPN, règles de filtrage, redirections de ports, DHCP, DNS, QoS, et bien plus."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# pfSense (pare-feu et routeur open source)

## 📌 Présentation

**pfSense** est une distribution basée sur FreeBSD utilisée comme pare-feu, routeur et passerelle réseau. Elle est administrable via une interface web très complète et permet de gérer des VLAN, VPN, règles de filtrage, redirections de ports, DHCP, DNS, QoS, et bien plus.

Très utilisée en entreprise, en collectivité ou en environnement éducatif, elle permet de remplacer des solutions propriétaires coûteuses (type Fortinet, Cisco ASA…)

---

## 🧱 Fonctionnalités clés

| Fonction | Description |
|----------|-------------|
| **Firewall stateful** | Règles par interface, protocole, port, utilisateur |
| **NAT / Port Forward** | Traduction d’adresse et redirections |
| **VPN** | OpenVPN, IPsec, WireGuard |
| **DHCP / DNS** | Serveur intégré avec options avancées |
| **VLAN** | Séparation logique de réseaux sur une même interface physique |
| **Captive Portal** | Authentification avant accès réseau (Wi-Fi invité…) |
| **HA / CARP** | Haute disponibilité entre deux pfSense |

---

## ⚙️ Configuration initiale (via console ou WebGUI)

1. **Attribuer une IP LAN (ex : 192.168.1.1)**
2. **Accéder à l’interface web** : `https://192.168.1.1` (admin/pfsense)
3. **Suivre l’assistant de configuration initiale**

---

## 🧰 Tâches courantes
### 🔐 Ajouter une règle de firewall

- **Menu** : Firewall > Rules > [Interface]
- Ajouter une règle (ex : autoriser HTTP ou SSH)

### 🌐 Redirection de port (NAT)

- **Menu** : Firewall > NAT > Port Forward
- Ex : rediriger port 80 externe vers un serveur LAN en 192.168.1.10:80

### 🎯 Réservation DHCP

- **Menu** : Services > DHCP Server > [LAN]
- Ajouter une réservation pour une IP fixe à une MAC adresse

### 🔒 Mise en place d’un VPN (OpenVPN)

- Assistant : VPN > OpenVPN > Wizard
- Générer CA, serveur VPN, exporter le client

---

## 🔎 Cas d’usage courant

- Sécuriser l’accès Internet d’un réseau local (filtrage, logs, QoS)
- Accès distant sécurisé via OpenVPN (télétravail)
- Interconnexion de sites via IPsec ou WireGuard
- Portail captif pour invités (Wi-Fi public)

---

## ⚠️ Erreurs fréquentes

- Oublier une règle `Allow All` en sortie → blocage inattendu
- Redirection NAT sans règle associée → trafic bloqué
- Réseaux VLAN mal configurés côté switch / pfSense → pas de connectivité
- Mauvais ordre des règles → la première qui matche s’applique !

---

## ✅ Bonnes pratiques

- **Créer des alias** (groupes IP, ports) pour simplifier la gestion
- **Documenter toutes les règles** avec des descriptions claires
- **Sauvegarder la configuration** régulièrement (Diagnostics > Backup)
- **Tester dans une VM avant mise en production** (lab virtualisé)
- Appliquer le **principe de moindre privilège** pour les règles firewall

---

## 📚 Ressources complémentaires

- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
- [Forum Netgate](https://forum.netgate.com/)
- [YouTube – Netgate tutorials](https://www.youtube.com/c/NetgateOfficial)
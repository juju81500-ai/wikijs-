---
title: "Routage et traduction d’adresses (Linux / Debian)"
description: "Le routage permet à une machine de communiquer avec une autre située sur un réseau logique différent."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Routage et traduction d’adresses (Linux / Debian)

## 📡 Définition du routage

Le **routage** permet à une machine de **communiquer avec une autre située sur un réseau logique différent**.

- L'hôte détermine si l'adresse de destination est dans le même réseau → sinon, il utilise sa **passerelle**.
- Le routeur (passerelle) examine la **table de routage** et redirige les paquets vers la bonne interface.

> 📌 Chaque hôte doit avoir une **route par défaut** et les routeurs doivent connaître tous les réseaux à atteindre.

---

## 🛠️ Configuration du routage sous Linux

### 🔹 Affichage et ajout de routes

```bash
ip route show                            # Affiche la table de routage
ip route add 192.168.2.0/24 via 192.168.1.1 dev ens33
```

### 🔹 Suppression ou modification

```bash
ip route del 192.168.2.0/24
ip route change default via 192.168.1.254
```

---

## 💾 Persistance des routes

Les routes configurées via `ip` sont **temporaires**. Pour les rendre persistantes :

- Ajout dans le fichier `/etc/network/interfaces`

```bash
auto ens33
iface ens33 inet static
  address 192.168.1.2
  netmask 255.255.255.0
  gateway 192.168.1.1
  post-up ip route add 192.168.2.0/24 via 192.168.1.254
```

> ✅ L’utilisation de `post-up` permet d’exécuter des commandes à l’activation de l’interface.

---

## 🔁 Activer le routage IP

Par défaut, Linux **ne route pas les paquets**. Il faut :

### 🔹 Modifier le fichier `/etc/sysctl.conf`

```bash
net.ipv4.ip_forward = 1
```

### 🔹 Appliquer la modification

```bash
sysctl -p
```

### 🔹 Vérifier l’activation

```bash
cat /proc/sys/net/ipv4/ip_forward   # 1 = activé, 0 = désactivé
```

---

## 🌐 Traduction d’adresses – NAT (SNAT / DNAT)

Le routage seul ne suffit pas dans certains cas :

- Réseaux **non routables sur Internet** (ex : 192.168.X.X)
- Besoin de rediriger le trafic à travers un **pare-feu / routeur NAT**

### 🔹 SNAT (Source NAT)

- Remplace l’IP **source** d’un paquet pour permettre sa sortie vers un autre réseau (ex : vers Internet)

### 🔹 DNAT (Destination NAT)

- Remplace l’IP **destination** d’un paquet pour rediriger le trafic vers une IP interne (ex : accès public à un serveur interne)

---

## 🔥 Outils de mise en œuvre du NAT

### 🔹 iptables

```bash
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
```

### 🔹 Shorewall

- Framework simplifiant la configuration d’iptables via des fichiers de règles déclaratifs

### 🔹 pfSense

- Outil graphique complet intégré dans la maquette ENI
- Permet le SNAT/DNAT par configuration Web, très lisible et efficace

---

## ✅ À retenir pour les révisions

- Le routage nécessite une **table de routes complète** côté routeurs
- Il faut **activer le routage IP** dans `/etc/sysctl.conf`
- Le **NAT** est indispensable pour l’accès Internet depuis un réseau privé
- **SNAT** : sortie vers l’extérieur ; **DNAT** : redirection de trafic entrant
- Utilise `ip route`, `iptables` ou **pfSense** pour configurer le tout

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Documenter la topologie des réseaux|Facilite les configurations statiques et les tests|
|Activer le routage **uniquement si nécessaire**|Évite les fuites de paquets sur des équipements non dédiés|
|Préférer la persistance des routes via `/etc/network/interfaces`|Plus fiable que les scripts init manuels|
|Tester avec `traceroute` et `ping`|Vérifie le bon passage des paquets à chaque étape|
|Utiliser pfSense en environnement d’apprentissage|Simplifie et sécurise la mise en œuvre du NAT|
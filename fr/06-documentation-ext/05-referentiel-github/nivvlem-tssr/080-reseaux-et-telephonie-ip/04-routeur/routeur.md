---
title: "Le routeur – Configuration, routage, inter-VLAN"
description: "- Structure et fonctionnement très proches du switch :"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Le routeur – Configuration, routage, inter-VLAN
## 🛠️ Configuration de base d’un routeur

- Structure et fonctionnement très proches du switch :
    - Même modes (utilisateur, privilégié, global)
    - Mêmes lignes de configuration (`console`, `vty`)
    - Mêmes mémoires : ROM, Flash, RAM, NVRAM

### Configuration d’une interface IP

```shell
Router(config)# interface g0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# description Lien vers LAN1
```

---

## 🧭 Routage statique

### Principe

- L’hôte consulte sa **passerelle par défaut** si le destinataire n’est pas sur le même réseau logique.
- Chaque routeur examine sa **table de routage** pour transmettre le paquet au prochain saut (next hop).
- **TTL** décrémenté à chaque saut : si = 0 → paquet abandonné.

### Création d’une route statique

```shell
Router(config)# ip route 192.168.10.0 255.255.255.0 10.0.0.254
```

### Route par défaut

```shell
Router(config)# ip route 0.0.0.0 0.0.0.0 192.168.1.1
```

---

## 📋 Table de routage

|Élément|Description|
|---|---|
|`C`|Route connectée directement|
|`L`|Adresse locale (interface elle-même)|
|`S`|Route statique|
|`R`|RIP (routing protocol)|

- **Distance administrative** (DA) : confiance accordée à la source (plus petite = plus fiable)
- **Métrique** : critère pour choisir entre plusieurs routes (nombre de sauts, bande passante, etc.)

### Valeurs de DA usuelles

|Protocole|DA|
|---|---|
|Connexion directe|0|
|Route statique|1|
|EIGRP interne|90|
|OSPF|110|
|RIP|120|

---

## 🔀 Routage inter-VLAN – Router-on-a-Stick

### Principe

- Utilise **une seule interface physique** avec **plusieurs sous-interfaces logiques**, une par VLAN
- Chaque sous-interface est taguée avec un VLAN (`dot1q`) et reçoit une IP de passerelle

### Configuration

```shell
interface g0/0.10
 encapsulation dot1q 10
 ip address 192.168.10.1 255.255.255.0
!
interface g0/0.20
 encapsulation dot1q 20
 ip address 192.168.20.1 255.255.255.0
!
interface g0/0.99
 encapsulation dot1q 99 native
 ip address 192.168.99.1 255.255.255.0
```

> Le trunk sur le switch doit correspondre à cette configuration (mêmes VLANs autorisés)

---

## 🌐 Protocole RIP (Routing Information Protocol)

### Caractéristiques

- Protocole de **routage dynamique** standard (RIPv2)
- IGP / Distance vector
- Distance administrative : 120
- Métrique : nombre de sauts (max 15)

### Configuration

```shell
Router(config)# router rip
Router(config-router)# version 2
Router(config-router)# network 10.0.0.0
Router(config-router)# network 192.168.1.0
```

### Multidiffusion RIP v2

- Envoi toutes les 30 secondes en **multicast** : 224.0.0.9
- RIP v1 utilisait le **broadcast** : 255.255.255.255

---

## ✅ À retenir pour les révisions

- Le routage statique est **manuel**, sûr mais rigide
- La **distance administrative** classe les sources de routage par fiabilité
- Le **Router-on-a-Stick** permet le **routage inter-VLAN avec une seule interface physique**
- **RIP v2** permet un routage dynamique simple pour les topologies modestes

---

## 📌 Bonnes pratiques professionnelles

- Toujours **décrire les interfaces** (`description`) pour le support
- Utiliser `show ip route` et `show running-config` pour diagnostiquer
- Limiter RIP à des **labos ou réseaux simples**, préférer OSPF/EIGRP en prod
- Éviter d’utiliser `RIP v1` (non sécurisé, sans support CIDR ni VLSM)
- **Documenter le plan de routage** (routes, sous-réseaux, interconnexions)
- Vérifier la correspondance **trunk ↔ sous-interfaces VLAN** pour le router-on-a-stick
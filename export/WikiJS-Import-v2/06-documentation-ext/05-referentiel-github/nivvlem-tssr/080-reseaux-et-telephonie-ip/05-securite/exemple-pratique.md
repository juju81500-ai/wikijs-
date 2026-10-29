---
title: "TP – ACL standard, étendues et NAT (statique, dynamique, PAT)"
description: "Mettre en pratique les concepts fondamentaux de sécurité réseau via la configuration d’ACL IPv4 (standard et étendues), la sécurisation des accès VTY, ainsi que l’implémentation des différentes formes de NAT sur routeur Cisco."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – ACL standard, étendues et NAT (statique, dynamique, PAT)

## 🧠 Objectif

Mettre en pratique les concepts fondamentaux de sécurité réseau via la **configuration d’ACL IPv4** (standard et étendues), la **sécurisation des accès VTY**, ainsi que l’implémentation des différentes formes de **NAT** sur routeur Cisco.

---

## 🧾 Contexte

Les TPs incluent :

- ACL standard numérotées et nommées
- ACL étendues (numérotées et nommées)
- Application d’ACL aux interfaces et lignes VTY
- Filtrage par protocole et plage d’adresses (wildcard masks)
- NAT statique (1:1), dynamique (pool) et PAT (NAT overload)

---

## 🔧 ACL IPv4 standard numérotée (R2, R3)

```shell
access-list 1 deny 192.168.11.0 0.0.0.255
access-list 1 permit any
interface g0/0
 ip access-group 1 out
```

```shell
access-list 1 deny 192.168.10.0 0.0.0.255
access-list 1 permit any
interface g0/0
 ip access-group 1 out
```

## 🔧 ACL IPv4 standard nommée (R1)

```shell
ip access-list standard File_Server_Restrictions
 permit host 192.168.20.4
 permit host 192.168.100.100
 deny any
interface f0/1
 ip access-group File_Server_Restrictions out
```

---

## 🎯 ACL IPv4 étendue – filtrage par protocole et port

### Numérotée (100)

```shell
access-list 100 permit tcp 172.22.34.64 0.0.0.31 host 172.22.34.62 eq ftp
access-list 100 permit icmp 172.22.34.64 0.0.0.31 host 172.22.34.62
interface g0/0
 ip access-group 100 in
```

### Nommée (HTTP_ONLY)

```shell
ip access-list extended HTTP_ONLY
 permit tcp 172.22.34.96 0.0.0.15 host 172.22.34.62 eq www
 permit icmp 172.22.34.96 0.0.0.15 host 172.22.34.62
interface g0/1
 ip access-group HTTP_ONLY in
```

---

## 🔒 Sécurisation accès VTY avec ACL

```shell
access-list 5 permit 192.168.1.10
line vty 0 4
 access-class 5 in
```

---

## 🌐 NAT statique (1:1)

```shell
ip nat inside source static 172.16.16.1 64.100.50.1
interface g0/0
 ip nat inside
interface s0/0/0
 ip nat outside
```

## 🔁 NAT dynamique (avec pool)

```shell
access-list 1 permit 172.16.0.0 0.0.255.255
ip nat pool ANY_POOL 209.165.200.229 209.165.200.230 netmask 255.255.255.252
ip nat inside source list 1 pool ANY_POOL
```

## 🔄 NAT avec PAT (overload)

```shell
ip nat pool R2POOL 209.165.202.129 209.165.202.129 netmask 255.255.255.252
ip nat inside source list R2NAT pool R2POOL overload
ip access-list standard R2NAT
 permit 192.168.10.0 0.0.0.255
 permit 192.168.20.0 0.0.0.255
 permit 192.168.30.0 0.0.0.255
ip nat inside source static 192.168.20.254 209.165.202.130
```

---

## ✅ À retenir pour les révisions

- Les **ACL standard** filtrent uniquement l’**IP source** ; les **étendues** permettent de filtrer aussi les **protocoles et ports**.
- L’ordre des lignes ACL est **critique** (filtrage séquentiel).
- Chaque ACL possède un **deny implicite** en fin de liste.
- La **NAT statique** est utilisée pour les services internes à exposer ; la **NAT dynamique** pour plusieurs clients internes ; la **PAT** pour l’accès Internet avec une IP publique partagée.

---

## 📌 Bonnes pratiques professionnelles

- Appliquer la **PSSI** : filtrage par défaut, ACLs testées, logging activé si possible
- Documenter les **objets ACL** : noms explicites, commentaires `remark`
- Toujours appliquer les ACLs au plus près de la **source (étendue)** ou de la **destination (standard)**
- Sur les ACLs d’accès VTY, restreindre aux **IP de gestion connues**
- Sur la NAT : bien **identifier les interfaces** inside / outside et tester les **traductions** (`show ip nat translations`)
---
title: "La sécurité – Hygiène informatique, PSSI, ACL, NAT"
description: "- L’ANSSI : autorité française en cybersécurité"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# La sécurité – Hygiène informatique, PSSI, ACL, NAT
## 🛡️ Hygiène informatique

### Définitions clés

- L’**ANSSI** : autorité française en cybersécurité
- **CyberEdu** : programme pédagogique ANSSI (modules accessibles en ligne)

### Bonnes pratiques (source ANSSI – 42 mesures)

- Définir les **besoins de sécurité** selon les enjeux économiques et métiers
- Appliquer une stratégie **par paliers**, du minimum au niveau optimal
- Utiliser une **charte informatique** pour encadrer les usages
- Maintenir les systèmes à jour et suivre une **politique de gestion des droits**

---

## 📋 Politique de sécurité (PSSI)

### Rôle

- Pilier de la stratégie SSI de l’entreprise
- Rédigée par la DSI, validée par la direction, gérée par le **RSSI**

### Composants typiques

- Définition du **besoin de sécurité**
- Déclinaison en politiques opérationnelles : filtrage pare-feu, règles d’accès, PDU, etc.
- Structure-type pour les **règles de flux** réseau :
    - Flux entrants / sortants
    - Protection pare-feu
    - Flux métiers autorisés
    - Flux parasites bloqués (non journalisés)
    - **Règle de refus implicite** : tout ce qui n’est pas autorisé est interdit

---

## 🧾 Convention de nommage

|Approche|Exemple|
|---|---|
|**Fonctionnelle**|`srv_dns-interne`, `tcp_appli1`|
|**Technique**|`tcp_21000`, `srv_appollo`|

> Utiliser une convention claire pour tout objet de configuration (règles ACL, objets pare-feu, VLAN, etc.)

---

## 🔐 Listes de contrôle d’accès (ACL)

### Objectifs

- Filtrer le trafic réseau
- Protéger les équipements et services sensibles
- Limiter le trafic indésirable ou superflu

### Types

|Type|Fonction|
|---|---|
|**Standard**|Filtrage couche 3 – adresse source uniquement|
|**Étendue**|Filtrage couche 3 & 4 – adresses + protocoles + ports|

### Emplacement

- ACL **standard** : proche de la **destination**
- ACL **étendues** : proche de la **source**

### Syntaxe – Exemple standard numérotée

```shell
access-list 10 permit 192.168.1.0 0.0.0.255
access-list 10 deny any
```

### Syntaxe – Exemple nommée étendue

```shell
ip access-list extended WEB-FILTER
 permit tcp 192.168.10.0 0.0.0.255 any eq 80
 deny ip any any
```

---

## 🎛️ Application des ACL

### Sur interfaces

```shell
interface g0/0
 ip access-group 10 in
```

### Sur lignes VTY

```shell
access-list 5 permit 192.168.1.10
line vty 0 4
 access-class 5 in
```

> À retenir : les **ACL ne filtrent pas le trafic généré par le routeur lui-même**

---

## 🎭 Masques génériques (wildcard masks)

|Élément|Valeur|
|---|---|
|Masque 255.255.255.0|Wildcard 0.0.0.255|
|Masque 255.255.255.192 (/26)|Wildcard 0.0.0.63|

### Mots-clés utiles

- `host` → 0.0.0.0 (exact match)
- `any` → 255.255.255.255 (toutes adresses)

---

## 📌 Bonnes pratiques ACL

- Écrire la politique à appliquer **avant** de créer l’ACL
- Documenter avec `remark`
- Tester l’ACL sur un **environnement de préproduction**
- Ne pas oublier : ACL = **filtrage séquentiel**, l’ordre compte
- **Implicit deny** à la fin : tout ce qui n’est pas autorisé est refusé

---

## 🌍 NAT (Network Address Translation)

### Objectif

- Traduire des adresses **privées internes** vers des adresses **publiques externes**

### Types de NAT

|Type|Description|
|---|---|
|**Statique**|Une IP privée ↔ une IP publique (1:1)|
|**Dynamique**|Plage d’IP privées vers une plage d’IP publiques|
|**PAT (NAT overload)**|Plusieurs IP privées vers **une seule IP publique**, via ports TCP/UDP|

### Cas d’usage

- Accès Internet pour un LAN privé (PAT)
- Publication d’un serveur interne avec une IP publique (statique)

---

## ✅ À retenir pour les révisions

- L’**hygiène informatique** est la base de toute stratégie de sécurité SI
- Une **PSSI claire** guide les actions techniques (ACL, NAT, filtrage)
- Les **ACL filtrent le trafic** en fonction de critères IP/protocole/port
- La **NAT/PAT** masque les IP internes et optimise l’usage des IP publiques

---

## 📌 Bonnes pratiques professionnelles

- Appliquer une **PSSI alignée avec les enjeux métier et légaux** (RGPD, etc.)
- Définir une **convention de nommage** cohérente et documentée
- Appliquer les ACL avec méthode : ordonnancement, test, commentaire
- Utiliser les **wildcards** correctement pour contrôler les plages IP
- Sécuriser les accès **VTY/SSH** avec ACL spécifiques
- Définir des règles NAT claires pour éviter les conflits de translation
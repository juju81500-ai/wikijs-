---
title: "Connecter les collaborateurs entre sites"
description: "Le VPN IPSec (Internet Protocol Security) est une méthode permettant de sécuriser les communications sur Internet."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Connecter les collaborateurs entre sites
## 📃 Introduction au VPN IPSec

Le **VPN IPSec** (_Internet Protocol Security_) est une méthode permettant de sécuriser les communications sur Internet.

### Spécificités :

- Utilise **2 tunnels distincts** complémentaires :
    1. **Tunnel IKE** (Internet Key Exchange)
    2. **Tunnel IPSec** (transport des données)

---

## 🔢 Tunnel IKE (Phase 1)

**Rôle :** échange des paramètres de sécurité.

Fonctions :

- Négociation des **algorithmes de chiffrement**
- Méthodes d'**authentification**
- Génération des **clés de session**

---

## 🔢 Tunnel IPSec (Phase 2)

**Rôle :** transfert sécurisé des données.

Fonctions :

- **Chiffrement** des données en transit
- **Authentification** de la source
- **Intégrité** des données (protection contre l'altération)

---

## 🔧 Configuration VPN site-à-site (pfSense)

### Phase 1 (IKE)

- Création du **Tunnel IKE**
- Négociation des paramètres de sécurité (algos, clés, authentification)

### Phase 2 (IPSec)

- Création du **Tunnel IPSec**
- Définition des **réseaux source et destination**

### Règles de pare-feu

- Autoriser les flux IPSec
- Configurer les accès inter-sites via la carte virtuelle IPSec

### Déploiement sur plusieurs routeurs

- Même procédure à appliquer sur le routeur distant
- Vérification via l'interface de supervision IPSec (vue d'ensemble)

---

## ✅ À retenir pour les révisions

- Le VPN **site à site IPsec** relie deux réseaux **LAN** distants de manière sécurisée
- **Phase 1 IKE** → négociation des paramètres de sécurité et authentification des routeurs
- **Phase 2 IPsec** → chiffrement et authentification des données entre les LANs
- La configuration se fait en **mode site à site** → chaque routeur connaît les réseaux autorisés du site distant
- Les **règles firewall IPsec** doivent contrôler précisément les flux autorisés entre les sites
- La supervision des **connexions IPsec** est indispensable → surveillance des logs et de l’état des tunnels
- Les algorithmes de chiffrement doivent être **modernes et robustes** (éviter les suites faibles)
- Attention à bien appairer les **paramètres Phase 1 / Phase 2** sur les deux extrémités du tunnel

---

## 📌 Bonnes pratiques professionnelles

- Utiliser des **algorithmes de chiffrement modernes**
- Documenter les **paramètres des tunnels**
- Restreindre les flux inter-sites à ce qui est nécessaire
- Surveiller régulièrement les **connexions IPSec**
- Mettre à jour les firmwares des routeurs/pfSense

---

## ⚠️ Pièges à éviter

- Mauvais appairage des paramètres entre sites (IKE / IPSec)
- Oublier de restreindre les flux inter-sites
- Laisser des tunnels IPSec inactifs en place
- Négliger la **surveillance des logs** IPSec

---

## ✅ Commandes utiles (diagnostic IPSec)

### pfSense

```bash
# Vérifier les connexions IPSec actives
swanctl --list-sas

# Vérifier les configurations chargées
swanctl --list-conns

# Logs IPSec
cat /var/log/ipsec.log
```
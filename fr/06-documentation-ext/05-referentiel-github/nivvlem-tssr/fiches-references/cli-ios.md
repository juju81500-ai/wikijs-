---
title: "CLI Cisco (IOS - Internetwork Operating System)"
description: "La CLI Cisco est une interface en ligne de commande utilisée sur les équipements réseau Cisco (routeurs, switches, pare-feux). Elle repose sur une structure hiérarchique par modes (user, privileged, configuration…) permettant une administration fine des équipements."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# CLI Cisco (IOS - Internetwork Operating System)

## 📌 Présentation

La CLI Cisco est une interface en ligne de commande utilisée sur les équipements réseau Cisco (routeurs, switches, pare-feux). Elle repose sur une structure hiérarchique par modes (user, privileged, configuration…) permettant une administration fine des équipements.

---

## 🧱 Hiérarchie des modes

| Mode | Invite | Accès |
|------|--------|-------|
| User EXEC | `>` | Consultation de base (ping, show) |
| Privileged EXEC | `#` | Commandes avancées (debug, copy, reload) |
| Global Configuration | `(config)#` | Configuration globale |
| Interface Configuration | `(config-if)#` | Configuration des interfaces |
| Line Configuration | `(config-line)#` | Configuration des lignes (console, VTY SSH) |

---

## 🔐 Accès au routeur

```plaintext
Router> enable              # Passe en mode privilégié
Router# configure terminal  # Passe en mode configuration globale
Router(config)#             # Invite de configuration globale
```

---

## 🧰 Commandes essentielles

### 🔎 Diagnostic / supervision

| Commande | Description |
|----------|-------------|
| `show running-config` | Affiche la configuration en cours |
| `show startup-config` | Affiche la configuration sauvegardée |
| `show interfaces` | Statut et détails des interfaces |
| `show ip interface brief` | Résumé IP des interfaces |
| `show version` | Informations matérielles et logicielles |
| `ping [IP]` | Test de connectivité |
| `traceroute [IP]` | Trajet réseau jusqu’à une IP |

### 🔧 Configuration de base

```plaintext
Router(config)# hostname R1
R1(config)# enable secret monmotdepasse
R1(config)# line vty 0 4
R1(config-line)# password cisco
R1(config-line)# login
```

### 🌐 Configuration IP d'une interface

```plaintext
R1(config)# interface GigabitEthernet0/0
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# no shutdown
```

### 💾 Sauvegarde et restauration

| Commande | Description |
|----------|-------------|
| `copy running-config startup-config` | Sauvegarder la config active |
| `copy startup-config running-config` | Restaurer la config sauvegardée |

---

## 🔎 Cas d’usage courant

- Configuration d’un routeur ou switch en ligne de commande
- Mise en place d’un plan d’adressage et configuration IP
- Dépannage réseau sur site via console ou SSH
- Contrôle d’accès, VLAN, routage, NAT, ACL…

---

## ⚠️ Erreurs fréquentes

- Oublier de faire `no shutdown` sur une interface activée
- Ne pas sauvegarder la configuration (`copy run start`) → perte au redémarrage
- Oublier d’attribuer un mot de passe sur les lignes VTY → accès SSH refusé
- Configurer une IP dans le mauvais masque ou sur la mauvaise interface

---

## ✅ Bonnes pratiques

- Sauvegarder la configuration après chaque modification importante
- Utiliser des noms d’hôtes explicites (`SW-Paris`, `RTR-DC1`, etc.)
- Désactiver les ports inutilisés (`shutdown` sur interface vide)
- Sécuriser les accès (mot de passe enable secret, SSH, ACL…)
- Documenter la topologie et la configuration réseau
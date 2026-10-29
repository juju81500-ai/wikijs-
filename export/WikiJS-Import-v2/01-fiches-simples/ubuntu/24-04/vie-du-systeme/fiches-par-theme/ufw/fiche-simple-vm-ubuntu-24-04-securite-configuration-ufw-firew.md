---
title: "VM_Ubuntu_24.04_Securite_Configuration-UFW-Firewall"
description: "Configurer et activer le pare-feu simplifié UFW (Uncomplicated Firewall) sous Ubuntu Server 24.04 LTS, appliquer une politique de sécurité fermée par défaut et filtrer les accès SSH et HTTP/HTTPS."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[ubuntu-24.04]", "[ufw]", "[pare-feu]", "[security]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Ubuntu_24.04_Securite_Configuration-UFW-Firewall.md

- **Environnement** : VM (Ubuntu Server 24.04 LTS)
- **OS / Version** : Ubuntu 24.04 LTS - Famille Debian / Ubuntu
- **Catégorie** : Sécurité & Pare-feu Local (UFW)
- **Tags** : `[ubuntu-24.04]`, `[ufw]`, `[pare-feu]`, `[security]`, `[hardening]`

## 🎯 Problème précis à résoudre
Configurer et activer le pare-feu simplifié UFW (Uncomplicated Firewall) sous Ubuntu Server 24.04 LTS, appliquer une politique de sécurité fermée par défaut et filtrer les accès SSH et HTTP/HTTPS.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérification du statut initial d'UFW :
   `ufw status verbose`
   👉 Explication : Indique si le pare-feu local UFW est actif ou inactif.
2. Autorisation rapide du trafic SSH entrant :
   `ufw allow ssh`
   👉 Explication : Ajoute une règle autorisant le port 22/TCP pour ne pas perdre la main lors de l'activation.

---

## ⚡ 2. Production — Façon Simplifiée
1. Application de la politique par défaut Zero-Trust (Bloquer l'entrant, autoriser le sortant) :
   `ufw default deny incoming && ufw default allow outgoing`
   👉 Explication : Ferme tous les ports entrants non explicitement autorisés.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction de l'accès SSH à la seule IP du bastion d'administration :
   `ufw allow from 192.168.1.10 to any port 22 proto tcp comment 'SSH Bastion Admin'`
   👉 Explication : Bloque l'accès SSH pour tous les autres équipements du réseau local.
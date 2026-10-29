---
title: "Fiche Simple - LXC Alpine Diagnostic Isoler Couche"
description: "Localiser si la panne provient du lien, de l'IP, de la route, du DNS, du port ou du service applicatif."
published: true
date: 2026-10-29T20:14:10Z
tags: ["alpine", "lxc", "diagnostic", "dns", "route", "service"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_LXC_Alpine_Diagnostic_Isoler_Couche.md

- **Environnement** : CT Alpine sur un réseau autorisé, tests limités aux destinations prévues
- **OS / Version** : branche Alpine maintenue
- **Catégorie** : diagnostic / isolation réseau
- **Tags** : `alpine`, `lxc`, `diagnostic`, `dns`, `route`, `service`

---

## Problème précis à résoudre

Localiser si la panne provient du lien, de l'IP, de la route, du DNS, du port ou du service applicatif.

## 1. Hors-Production (Lab / Test / POC)

1. Lien, bridge, VLAN :
   ```sh
   ip -br link
   ```
   👉 Explication : l'interface doit être `UP`; côté hôte, `ip -br link show type bridge` doit montrer le bridge et le VLAN doit être permis sur le switch.

2. IP et route :
   ```sh
   ip -br addr
   ip route
   ```
   👉 Explication : l'adresse/préfixe attendus et une route par défaut doivent exister.

3. Passerelle :
   ```sh
   ping -c 3 IP_PASSERELLE
   ```
   👉 Explication : un ping bloqué ne prouve pas une panne.

4. DNS :
   ```sh
   ping -c 2 IP_DESTINATION
   nslookup NOM_CIBLE
   ```
   👉 Explication : si l'IP répond mais pas le nom, le problème est le DNS (`/etc/resolv.conf`).

5. Port et service :
   ```sh
   ss -lntup
   rc-service SERVICE status
   ```
   👉 Explication : si `ss` ou `nslookup` manque, installer le paquet (`apk add iproute2 bind-tools`) lors d'une maintenance approuvée.

## 2. Production — Contrôles

Enregistrer le résultat de chaque couche, la destination précise et l'heure pour éviter les conclusions basées sur un seul test.

## 3. Production — Sécurité

- N'effectuer les tests que vers les systèmes autorisés et sur les ports nécessaires.
- Ne pas installer des outils réseau en production sans changement approuvé.
- Ne pas interpréter une réponse ICMP absente comme preuve unique d'indisponibilité.
- Ne pas lancer de scan large de réseau dans le cadre d'un diagnostic local.

## Validation et retour arrière

- **Validation** : couche fautive identifiée avec au moins un contrôle adapté et reproductible.
- **Arrêt** : si les outils manquent, utiliser les outils BusyBox disponibles ou demander l'approbation d'installation.

## Si le problème n'est pas résolu

- [Alpine Linux — documentation réseau](https://docs.alpinelinux.org/)
- [Proxmox VE — documentation](https://pve.proxmox.com/pve-docs/)
- [Guide complet de diagnostic LXC Alpine](/02-fiches-completes/alpine/toutes-versions/diagnostic/17-diagnostic-lxc-alpine-reseau-services#3-isoler-la-couche-en-panne)
---
title: "VM_Debian_12_Securite_NFTables-Pare-Feu"
description: "Mettre en place un pare-feu hôte persistant sur Debian 12 avec nftables : politique par défaut drop sur l'entrée, ouverture limitée aux flux nécessaires et SSH restreint au réseau d'administration."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian12]", "[debian-family]", "[nftables]", "[firewall]", "[systemd]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_12_Securite_NFTables-Pare-Feu.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Sécurité & Réseau / Pare-feu hôte
- **Tags** : `[debian12]`, `[debian-family]`, `[nftables]`, `[firewall]`, `[systemd]`, `[hardening]`

## 🎯 Problème précis à résoudre
Mettre en place un pare-feu hôte persistant sur Debian 12 avec `nftables` : politique par défaut `drop` sur l'entrée, ouverture limitée aux flux nécessaires et SSH restreint au réseau d'administration.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de nftables :
   `sudo apt-get update && sudo apt-get install -y nftables`
   👉 Explication : Installe l'outil `nft` et l'unité systemd `nftables.service` qui charge `/etc/nftables.conf` au démarrage.
2. Consultation du jeu de règles actuel :
   `sudo nft list ruleset`
   👉 Explication : Affiche les tables et chaînes actives ; vide sur une installation neuve, ce qui signifie aucun filtrage.
3. Contrôle de la syntaxe après écriture de la configuration :
   `sudo nft -c -f /etc/nftables.conf`
   👉 Explication : Vérifie le fichier sans appliquer les règles (option `-c`, check).

---

## ⚡ 2. Production — Façon Simplifiée
1. Rédaction de la configuration persistante :
   `sudoedit /etc/nftables.conf`
   👉 Explication : Contenu minimal à reprendre : `flush ruleset` puis `table inet filter { chain input { type filter hook input priority 0; policy drop; ct state established,related accept; iif lo accept; meta l4proto { icmp, ipv6-icmp } accept; ip saddr <reseau_admin> tcp dport 22 accept; } }`.
2. Activation et démarrage au boot :
   `sudo systemctl enable --now nftables`
   👉 Explication : Charge immédiatement les règles et les réapplique à chaque démarrage.

---

## 🔒 3. Production — Façon Sécurisée (Politique restrictive & Contrôle)
1. Ouverture de services métier par adresse source :
   `sudoedit /etc/nftables.conf`
   👉 Explication : Ajouter uniquement les ports nécessaires, par exemple `ip saddr <reseau_applicatif> tcp dport 443 accept`. Chaque règle doit correspondre à un port recensé dans la fiche serveur.
2. Application contrôlée de la nouvelle configuration :
   `sudo nft -c -f /etc/nftables.conf && sudo systemctl restart nftables`
   👉 Explication : Valide la syntaxe puis redémarre le service seulement si le test réussit. Garder une session console ouverte pendant l'opération.
3. Vérification des règles chargées et des ports en écoute :
   `sudo nft list ruleset && sudo ss -tulnp`
   👉 Explication : Croise les règles actives avec les services réellement à l'écoute pour repérer toute exposition non prévue.
---
title: "Politique nftables stricte pour une VM Debian 13"
description: "Ce document est un profil strict complémentaire de la fiche [pare-feu nftables Debian 13](./FicheSimple-VMDebian13SecuriteNFTablesFirewall.md). Ne choisir qu'une seule configuration comme source persistante ; ne pas charger les deux l'une après l'autre."
published: true
date: 2026-10-29T20:22:42Z
tags: ["debian13", "nftables", "firewall", "zero-trust", "hardening"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Politique nftables stricte pour une VM Debian 13

- **Environnement** : VM Debian 13 dédiée
- **Catégorie** : Sécurité / Pare-feu
- **Tags** : `debian13`, `nftables`, `firewall`, `zero-trust`, `hardening`

## Objectif

Ce document est un profil strict complémentaire de la fiche [pare-feu nftables Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/fiches-par-theme/nftables/fiche-simple-vm-debian-13-securite-nftables-firewall). Ne choisir qu'une seule configuration comme source persistante ; ne pas charger les deux l'une après l'autre.

## 🧪 1. Préparer l'accès

Avant de filtrer, confirmer l'adresse du poste d'administration, le port réel de SSH, les services publiés, IPv4/IPv6 et la console hyperviseur. Garder une session de secours ouverte.

```bash
sudo nft list ruleset
sudo ss -lntup
sudo ip route
```
   👉 Explication : affiche les règles, ports en écoute et routes actuels avant de bloquer quoi que ce soit.

Ne pas appliquer cette procédure sur un hôte Docker/Podman, un nœud Proxmox ou un serveur dont un autre gestionnaire administre le ruleset.

## ⚡ 2. Écrire une politique explicite

Utiliser `/etc/nftables.conf` comme configuration persistante. L'exemple ci-dessous n'autorise SSH que depuis un réseau d'administration fictif ; remplacer `192.0.2.0/24` et le port par les valeurs validées, ou retirer les services non hébergés.

```nft
#!/usr/sbin/nft -f
flush ruleset
table inet filter {
   chain input {
      type filter hook input priority filter; policy drop;
      iifname "lo" accept
      ct state invalid drop
      ct state established,related accept
      ip protocol icmp accept
      meta l4proto ipv6-icmp accept
      ip saddr 192.0.2.0/24 tcp dport 22 accept
      tcp dport { 80, 443 } accept
   }
   chain forward { type filter hook forward priority filter; policy drop; }
   chain output { type filter hook output priority filter; policy accept; }
}
```
   👉 Explication : fichier `/etc/nftables.conf` : politique `drop` en entrée avec autorisations explicites; adapter interfaces et ports.

`flush ruleset` supprime les règles déjà chargées : ne l'utiliser que si cette VM est dédiée et que le fichier est propriétaire de tout le filtrage.

## 🔒 3. Valider et appliquer

```bash
sudo nft -c -f /etc/nftables.conf
sudo nft -f /etc/nftables.conf
sudo systemctl enable --now nftables
sudo nft list ruleset
```
   👉 Explication : vérifie la syntaxe (`-c`), applique, active au démarrage et affiche le résultat; garder la console ouverte.

Tester une nouvelle connexion SSH et chacun des services attendus depuis un second terminal. Garder la console et la session initiale ouvertes jusqu'à réussite. En cas d'échec, restaurer le fichier précédent depuis la console, le valider puis le recharger.

Ne pas ajouter un limiteur de débit SSH improvisé : une règle de débit mal conçue peut bloquer des connexions légitimes et n'est pas un remplacement de l'authentification forte.
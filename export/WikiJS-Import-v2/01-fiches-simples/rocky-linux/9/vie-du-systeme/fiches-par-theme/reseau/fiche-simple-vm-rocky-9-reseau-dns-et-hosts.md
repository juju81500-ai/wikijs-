---
title: "Fiche Simple - VM Rocky 9 Reseau DNS Et Hosts"
description: "Configurer les serveurs DNS et le domaine de recherche d'une connexion NetworkManager sous Rocky Linux 9, puis fixer la résolution locale dans /etc/hosts, sans que le DHCP écrase les réglages."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[rocky9]", "[rhel9]", "[dns]", "[networkmanager]", "[hosts]", "[resolv]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Rocky_9_Reseau_DNS_Et_Hosts.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec NetworkManager
- **Catégorie** : Réseau / Résolution de noms
- **Tags** : `[rocky9]`, `[rhel9]`, `[dns]`, `[networkmanager]`, `[hosts]`, `[resolv]`

## 🎯 Problème précis à résoudre
Configurer les serveurs DNS et le domaine de recherche d'une connexion NetworkManager sous Rocky Linux 9, puis fixer la résolution locale dans `/etc/hosts`, sans que le DHCP écrase les réglages.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les connexions et lire les DNS configurés sur le profil :
   ```bash
   nmcli connection show
   nmcli -f ipv4.dns,ipv4.dns-search connection show "<nom_connexion>"
   ```
   👉 Explication : Le premier affiche les profils NetworkManager (par exemple `enp1s0`). Le second donne les serveurs DNS et le domaine de recherche enregistrés dans le profil.

2. Tester la résolution d'un nom interne :
   ```bash
   getent ahosts <nom_du_serveur>.<domaine>
   ```
   👉 Explication : `getent` suit l'ordre défini dans `/etc/nsswitch.conf`. Il fonctionne sans installer `bind-utils`, contrairement à `dig`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Définir les DNS internes et le domaine de recherche, puis réactiver la connexion :
   ```bash
   sudo nmcli connection modify "<nom_connexion>" ipv4.dns "<dns_primaire>,<dns_secondaire>" ipv4.dns-search "<domaine>"
   sudo nmcli connection up "<nom_connexion>"
   ```
   👉 Explication : `ipv4.dns` accepte une liste séparée par des virgules. NetworkManager régénère `/etc/resolv.conf`. Une connexion SSH passant par cette interface peut être coupée brièvement lors du `up`.

2. Ajouter la ligne de la machine dans `/etc/hosts` :
   ```bash
   sudo vi /etc/hosts
   getent hosts <nom_du_serveur>
   ```
   👉 Explication : Ajouter `<ip_du_serveur> <nom_du_serveur>.<domaine> <nom_du_serveur>`. Le fichier est lu avant le DNS si `/etc/nsswitch.conf` contient `hosts: files dns`.

3. Vérifier l'ordre de résolution et le résolveur actif :
   ```bash
   grep '^hosts' /etc/nsswitch.conf
   cat /etc/resolv.conf
   ```
   👉 Explication : Sous Rocky Linux 9, `/etc/resolv.conf` est géré par NetworkManager. Ne pas l'éditer à la main, car la modification est écrasée au prochain changement réseau.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Ignorer les DNS fournis par le DHCP pour que seuls les résolveurs internes restent actifs :
   ```bash
   sudo nmcli connection modify "<nom_connexion>" ipv4.ignore-auto-dns yes
   sudo nmcli connection up "<nom_connexion>"
   ```
   👉 Explication : Empêche l'ajout de résolveurs non maîtrisés, par exemple un DNS public, par le serveur DHCP.

2. Vérifier qu'aucun résolveur public n'est présent :
   ```bash
   nmcli -f IP4.DNS device show <interface>
   grep '^nameserver' /etc/resolv.conf
   ```
   👉 Explication : Seuls les résolveurs internes doivent apparaître. Un résolveur public contourne la journalisation DNS interne.

3. Vérifier qu'une connexion sans DNS interne ne retombe pas sur un résolveur externe :
   ```bash
   sudo nmcli -f ipv4.ignore-auto-dns,ipv4.dns connection show "<nom_connexion>"
   ```
   👉 Explication : `ipv4.ignore-auto-dns` doit valoir `yes` et `ipv4.dns` ne doit contenir que les serveurs internes validés.
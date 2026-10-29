---
title: "Fiche Simple - VM Ubuntu 24.04 Systeme Hostname FQDN"
description: "Définir le nom d'hôte statique et le FQDN d'un serveur Ubuntu 24.04 LTS, vérifier leur résolution locale et éviter qu'une réécriture de /etc/hosts par cloud-init ne les annule."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[hostname]", "[fqdn]", "[hostnamectl]", "[etc-hosts]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Systeme_Hostname_FQDN

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat)
- **Catégorie** : Système / Identité de la machine
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[hostname]`, `[fqdn]`, `[hostnamectl]`, `[etc-hosts]`

## 🎯 Problème précis à résoudre
Définir le nom d'hôte statique et le FQDN d'un serveur Ubuntu 24.04 LTS, vérifier leur résolution locale et éviter qu'une réécriture de `/etc/hosts` par cloud-init ne les annule.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Afficher l'identité actuelle de la machine :
   ```bash
   hostnamectl status
   hostname -f
   ```
   👉 *Explication : `hostnamectl` affiche le nom statique, le nom transitoire et l'identifiant de la machine ; `hostname -f` affiche le FQDN résolu.*
2. Définir le nom d'hôte statique (nom court, sans domaine) :
   ```bash
   sudo hostnamectl set-hostname <nom_du_serveur>
   ```
   👉 *Explication : Écrit le nom dans `/etc/hostname` et l'applique immédiatement, sans redémarrage.*

## ⚡ 2. Production — Façon Simplifiée
1. Ajouter l'entrée locale du FQDN dans `/etc/hosts` :
   ```bash
   sudo cp -a /etc/hosts /etc/hosts.bak
   sudo nano /etc/hosts
   ```
   Remplacer `nano` par `vim` si besoin, puis ajouter la ligne suivante :
   ```text
   127.0.1.1 <nom_du_serveur>.<domaine> <nom_du_serveur>
   ```
   👉 *Explication : Ubuntu utilise `127.0.1.1` comme adresse locale du nom d'hôte ; la ligne doit contenir le FQDN puis le nom court.*
2. Vérifier la cohérence du nom et du domaine :
   ```bash
   hostname
   hostname -f
   hostname -d
   getent hosts $(hostname -f)
   ```
   👉 *Explication : `hostname -d` doit afficher `<domaine>` ; `getent hosts` doit renvoyer la ligne de `/etc/hosts` ou l'adresse IP du DNS.*

## 🔒 3. Production — Façon Sécurisée
1. Si le serveur est déployé depuis une image cloud, empêcher cloud-init de réécrire `/etc/hosts` :
   ```bash
   sudo tee /etc/cloud/cloud.cfg.d/99-hosts-local.cfg >/dev/null <<'EOF'
   manage_etc_hosts: false
   preserve_hostname: true
   EOF
   ```
   👉 *Explication : Sans cette option, cloud-init peut restaurer un ancien nom d'hôte au redémarrage. Le fichier doit être créé avant le prochain démarrage.*
2. Vérifier que le nom n'est pas altéré après redémarrage :
   ```bash
   sudo cloud-init status --long
   hostnamectl status --static
   ```
   👉 *Explication : Le nom statique doit rester `<nom_du_serveur>` après redémarrage. La commande `cloud-init status` n'existe que sur les installations avec cloud-init.*

## ✅ Validation et retour arrière
- Confirmer que `hostname -f` renvoie `<nom_du_serveur>.<domaine>` depuis une nouvelle session SSH.
- En cas d'erreur, restaurer `/etc/hosts` avec `sudo cp -a /etc/hosts.bak /etc/hosts` et rétablir l'ancien nom avec `sudo hostnamectl set-hostname <ancien_nom>`.
---
title: "Fiche Simple - VM Ubuntu 24.04 Securite Sysctl Noyau"
description: "Appliquer un jeu de paramètres sysctl de durcissement au noyau et à la pile réseau d'Ubuntu Server 24.04 LTS, dans un fichier dédié de /etc/sysctl.d/, sans écraser la configuration fournie par le système."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[sysctl]", "[kernel]", "[tcp-syncookies]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Sysctl_Noyau

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat, noyau 6.8 par défaut)
- **Catégorie** : Sécurité / Durcissement du noyau et de la pile réseau
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[sysctl]`, `[kernel]`, `[tcp-syncookies]`, `[hardening]`

## 🎯 Problème précis à résoudre
Appliquer un jeu de paramètres `sysctl` de durcissement au noyau et à la pile réseau d'Ubuntu Server 24.04 LTS, dans un fichier dédié de `/etc/sysctl.d/`, sans écraser la configuration fournie par le système.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever les valeurs actuelles des paramètres ciblés :
   ```bash
   sysctl net.ipv4.tcp_syncookies net.ipv4.conf.all.accept_redirects kernel.dmesg_restrict kernel.kptr_restrict
   ```
   👉 *Explication : Permet de comparer l'état avant et après application.*
2. Tester une valeur sans la rendre permanente :
   ```bash
   sudo sysctl -w net.ipv4.conf.all.accept_redirects=0
   ```
   👉 *Explication : `sysctl -w` modifie le noyau en mémoire ; la valeur est perdue au redémarrage.*

## ⚡ 2. Production — Façon Simplifiée
1. Créer un fichier dédié, avec un numéro élevé pour qu'il soit lu en dernier :
   ```bash
   sudo install -o root -g root -m 0644 /dev/null /etc/sysctl.d/99-durcissement.conf
   sudo tee /etc/sysctl.d/99-durcissement.conf >/dev/null <<'EOF'
   net.ipv4.tcp_syncookies = 1
   net.ipv4.conf.all.accept_redirects = 0
   net.ipv4.conf.default.accept_redirects = 0
   net.ipv4.conf.all.send_redirects = 0
   net.ipv4.conf.all.accept_source_route = 0
   net.ipv4.conf.all.rp_filter = 1
   net.ipv4.icmp_echo_ignore_broadcasts = 1
   fs.protected_hardlinks = 1
   fs.protected_symlinks = 1
   kernel.dmesg_restrict = 1
   kernel.kptr_restrict = 2
   kernel.randomize_va_space = 2
   EOF
   ```
   👉 *Explication : Ces valeurs désactivent les redirections ICMP et le routage par la source, activent les SYN cookies contre le SYN flood et restreignent l'accès aux journaux du noyau et aux adresses mémoire.*
2. Appliquer tous les fichiers `sysctl.d` et vérifier :
   ```bash
   sudo sysctl --system
   sysctl net.ipv4.tcp_syncookies kernel.kptr_restrict
   ```
   👉 *Explication : `sysctl --system` relit `/etc/sysctl.conf` et `/etc/sysctl.d/*.conf` dans l'ordre alphabétique.*

## 🔒 3. Production — Façon Sécurisée
1. Vérifier qu'aucun paramètre de routage n'est requis avant de durcir davantage :
   ```bash
   sysctl net.ipv4.ip_forward
   ```
   👉 *Explication : Un serveur qui route, héberge Docker ou Kubernetes doit garder `net.ipv4.ip_forward = 1`. Ne jamais ajouter `ip_forward = 0` sur ces hôtes sans vérification.*
2. Contrôler qu'aucun autre fichier ne réécrit les mêmes clés :
   ```bash
   sudo grep -R -E 'accept_redirects|tcp_syncookies|kptr_restrict' /etc/sysctl.conf /etc/sysctl.d/
   ```
   👉 *Explication : Un fichier lu après `99-durcissement.conf` pourrait annuler la valeur appliquée ; les conflits doivent être corrigés à la source.*

## ✅ Validation et retour arrière
- Confirmer après redémarrage que `sysctl kernel.kptr_restrict` renvoie `2`.
- Retour arrière : `sudo rm /etc/sysctl.d/99-durcissement.conf` puis `sudo sysctl --system`. Les valeurs par défaut reviennent après relecture des fichiers restants.
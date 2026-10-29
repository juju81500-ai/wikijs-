---
title: "Fiche Simple - VM Alpine 3.19 Vie Systeme 34 Durcissement Du Noyau Et"
description: "Appliquer des réglages sysctl de sécurité."
published: true
date: 2026-10-29T20:22:10Z
tags: ["alpine319", "vie-du-systeme", "cycle-de-vie", "etape-34"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_34_Durcissement_Du_Noyau_Et

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 34 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-34`

---

## Problème précis à résoudre

Appliquer des réglages sysctl de sécurité.

## 1. Hors-Production (Lab / Test / POC)

1. Écrire un fichier de paramètres :
   ```sh
   doas sh -c 'cat > /etc/sysctl.d/90-hardening.conf <<EOF
   net.ipv4.conf.all.rp_filter = 1
   net.ipv4.conf.all.accept_redirects = 0
   net.ipv4.conf.all.send_redirects = 0
   net.ipv4.tcp_syncookies = 1
   kernel.kptr_restrict = 2
   kernel.dmesg_restrict = 1
   EOF'
   ```
   👉 Explication : filtre les routes anormales, refuse les redirections ICMP, protège contre le SYN flood et masque les adresses du noyau.

2. Appliquer le fichier :
   ```sh
   doas sysctl -p /etc/sysctl.d/90-hardening.conf
   ```
   👉 Explication : charge les valeurs sans redémarrer.

3. Vérifier l'application au démarrage :
   ```sh
   rc-status boot | grep sysctl
   sysctl net.ipv4.tcp_syncookies
   ```
   👉 Explication : le service `sysctl` du niveau `boot` relit le dossier à chaque démarrage.

## 2. Production — Contrôles

Tester les services après changement.

## 3. Production — Sécurité

Ne pas désactiver `rp_filter` sur un routeur à chemins asymétriques sans analyse.

## Validation et retour arrière

- **Validation** : `sysctl` retourne les valeurs durcies.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)
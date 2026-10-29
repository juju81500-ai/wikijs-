---
title: "Fiche Simple - LXC Alpine Proxmox Premier Demarrage"
description: "Vérifier le démarrage et initialiser l'identité, les paquets et les services du CT Alpine avant d'y déployer un rôle applicatif."
published: true
date: 2026-10-29T20:14:10Z
tags: ["alpine", "proxmox", "lxc", "openrc", "apk"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_LXC_Alpine_Proxmox_Premier_Demarrage.md

- **Environnement** : nouveau CT Alpine sur Proxmox VE, accès par console
- **OS / Version** : branche Alpine maintenue retenue pour le service
- **Catégorie** : virtualisation / configuration initiale
- **Tags** : `alpine`, `proxmox`, `lxc`, `openrc`, `apk`

---

## Problème précis à résoudre

Vérifier le démarrage et initialiser l'identité, les paquets et les services du CT Alpine avant d'y déployer un rôle applicatif.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer le CT : **CT > Start** (ou en ligne de commande) :
   ```bash
   pct start CTID
   pct enter CTID
   ```
   👉 Explication : `pct enter` ouvre un shell dans le conteneur.

2. Contrôler l'état initial :
   ```sh
   cat /etc/alpine-release
   ip -br addr
   ip route
   cat /etc/resolv.conf
   rc-status
   ```
   👉 Explication : adresse, passerelle et DNS doivent correspondre au plan.

3. Mettre à jour :
   ```sh
   apk update
   apk upgrade
   ```
   👉 Explication : selon la politique de correctifs du site.

4. Créer un compte nominatif non-root et configurer `doas` :
   ```sh
   apk add doas
   adduser utilisateur
   adduser utilisateur wheel
   echo 'permit persist :wheel' > /etc/doas.d/wheel.conf
   ```
   👉 Explication : remplacer `utilisateur`; installer ensuite seulement les paquets du rôle.

## 2. Production — Contrôles

Vérifier version, dépôts APK, comptes, synchronisation horaire, résolution DNS, services et accès d'administration avant le déploiement applicatif.

## 3. Production — Sécurité

- Ne pas travailler durablement sous root pour l'administration quotidienne.
- Ne pas mélanger dépôts de branches Alpine différentes.
- Ne pas activer des services inutiles au démarrage.
- Ne pas stocker de secret dans l'historique shell ou des fichiers accessibles à tous.

## Validation et retour arrière

- **Validation** : compte admin testé, paquets à jour, réseau et OpenRC conformes au besoin.
- **Retour arrière** : conserver console Proxmox; restaurer la configuration précédente si une mise à jour ou configuration casse l'accès.

## Si le problème n'est pas résolu

- [Alpine Linux — documentation](https://docs.alpinelinux.org/)
- [Alpine Linux — apk](https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper)
- [Guide complet LXC Alpine sur Proxmox](/02-fiches-completes/alpine/toutes-versions/installation-deploiement/16-installation-lxc-alpine-proxmox#4-premier-demarrage-et-configuration)
---
title: "Fiche Simple - VM Debian 13 Samba AD DC Preparer Debian"
description: "Configurer l'hôte et installer les paquets du rôle AD DC."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "samba", "active-directory", "lab", "apt", "kerberos"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Preparer_Debian.md

- **Environnement** : VM Debian 13 de laboratoire, contrôleur de domaine Samba AD DC (DNS SAMBA_INTERNAL)
- **OS / Version** : Debian 13 Trixie; Samba 4.22 (dépôts Debian)
- **Catégorie** : annuaire / préparation
- **Tags** : `debian13`, `samba`, `active-directory`, `lab`, `apt`, `kerberos`

---

## Problème précis à résoudre

Configurer l'hôte et installer les paquets du rôle AD DC.

## 1. Hors-Production (Lab / Test / POC)

1. Éditer `/etc/hosts` pour qu'il contienne (adresse et nom d'exemple à remplacer) :
   ```text
   127.0.0.1 localhost
   192.0.2.10 dc1.ad.lab.test dc1
   ```
   👉 Explication : associe le FQDN du DC à son adresse statique, jamais à `127.0.1.1`.

2. Exécuter :
   ```bash
   hostnamectl
   timedatectl status
   ip -br address
   ```
   👉 Explication : vérifie le nom, la synchronisation NTP et l'adresse statique.

3. Exécuter :
   ```bash
   sudo apt update
   apt-cache policy samba-ad-dc
   sudo apt install samba-ad-dc samba-common-bin krb5-user dnsutils smbclient acl attr
   ```
   👉 Explication : installe le rôle AD DC et ses outils après avoir vérifié la version Debian proposée.

4. Exécuter :
   ```bash
   systemctl list-unit-files 'smbd*' 'nmbd*' 'winbind*' 'samba*'
   ```
   👉 Explication : liste les unités; arrêter et désactiver `smbd`, `nmbd`, `winbind` séparés s'ils existent, mais jamais `samba-ad-dc`.

## 2. Production — Contrôles

Ne pas ajouter de dépôt tiers Samba; suivre le manuel Debian de la version installée.

## 3. Production — Sécurité

- Pas de dépôt tiers au hasard.
- Ne pas laisser des services Samba autonomes concurrencer le daemon AD DC.

## Validation et retour arrière

- **Validation** : le nom, l'heure et l'IP sont corrects et les paquets sont installés.
- **Retour arrière** : `sudo apt remove` des paquets installés ou restauration de la VM de lab.

## Si le problème n'est pas résolu

- [Debian 13 — samba-ad-dc(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html)
- [Debian 13 — samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html)
- [Guide complet Déployer un contrôleur de domaine Samba AD DC sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/65-deploiement-samba-ad-dc-debian-13#2-preparer-debian)
---
title: "Fiche Simple - VM Debian 13 Suricata IDS Installer"
description: "Installer Suricata 8.0.7 et suricata-update depuis trixie-backports."
published: true
date: 2026-10-29T20:14:10Z
tags: ["suricata", "debian13", "backports", "apt"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Suricata_IDS_Installer.md

- **Environnement** : VM Debian 13 avec trixie-backports activé
- **OS / Version** : Debian 13 Trixie; Suricata 8.0.7 et suricata-update (Debian Backports)
- **Catégorie** : detection reseau / installation
- **Tags** : `suricata`, `debian13`, `backports`, `apt`

---

## Problème précis à résoudre

Installer Suricata 8.0.7 et suricata-update depuis trixie-backports.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les versions candidates :
   ```bash
   sudo apt update
   apt-cache policy suricata suricata-update
   ```
   👉 Explication : attendu : Suricata `1:8.0.7-1~bpo13+1` et suricata-update `1.3.8-1~bpo13+1` depuis Backports; sinon relever les versions réelles.

2. Installer depuis Backports :
   ```bash
   sudo apt install -t trixie-backports suricata suricata-update jq
   ```
   👉 Explication : `-t trixie-backports` impose une paire cohérente; `jq` servira à lire `eve.json`.

3. Contrôler l'installation :
   ```bash
   suricata --build-info
   suricata-update -V
   systemctl cat suricata.service
   ```
   👉 Explication : on lit l'unité systemd du paquet pour comprendre ses arguments avant toute modification.

## 2. Production — Contrôles

Documenter les versions, suivre les mises à jour de Backports et tester chaque mise à jour sur un pilote.

## 3. Production — Sécurité

- Ne pas remplacer l'unité du paquet par un exemple d'une autre distribution.
- Pas de compilation manuelle ni de mélange de fichiers de configuration.

## Validation et retour arrière

- **Validation** : `suricata --build-info` répond avec la version 8.0.7.
- **Retour arrière** : `sudo apt remove suricata suricata-update` (la configuration reste dans `/etc/suricata`).

## Si le problème n'est pas résolu

- [Suricata — installation Debian](https://docs.suricata.io/en/latest/install/debian.html)
- [Debian Backports — page de manuel suricata](https://manpages.debian.org/trixie-backports/suricata/suricata.1.en.html)
- [Guide complet Suricata Debian 13](/02-fiches-completes/debian/13/installation-deploiement/71-deploiement-suricata-8-debian-13-backports#2-verifier-la-version-candidate-et-installer)
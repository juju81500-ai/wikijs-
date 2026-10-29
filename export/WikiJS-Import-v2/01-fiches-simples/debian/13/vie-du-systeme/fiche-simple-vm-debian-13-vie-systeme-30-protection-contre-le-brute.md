---
title: "Fiche Simple - VM Debian 13 Vie Systeme 30 Protection Contre Le Brute"
description: "Bloquer les tentatives répétées."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian13", "vie-du-systeme", "cycle-de-vie", "etape-30"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

---

## Problème précis à résoudre

Bloquer les tentatives répétées.

## 1. Hors-Production (Lab / Test / POC)

1. Installer fail2ban :
   ```bash
   sudo apt install fail2ban
   sudo tee /etc/fail2ban/jail.local >/dev/null <<'EOT'
   [sshd]
   enabled = true
   maxretry = 5
   bantime = 1h
   EOT
   ```
   👉 Explication : active la prison SSH.

2. Activer et contrôler :
   ```bash
   sudo systemctl enable --now fail2ban
   sudo fail2ban-client status sshd
   ```
   👉 Explication : affiche les IP bannies.

## 2. Production — Contrôles

Ajouter le réseau d'administration à `ignoreip`.

## 3. Production — Sécurité

Surveiller les faux positifs.

## Validation et retour arrière

- **Validation** : `fail2ban-client status sshd` répond.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Debian 13 Securite Fail2ban](</01-fiches-simples/debian/13/vie-du-logiciel/fail2ban/fiche-simple-vm-debian-13-securite-fail2ban>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)
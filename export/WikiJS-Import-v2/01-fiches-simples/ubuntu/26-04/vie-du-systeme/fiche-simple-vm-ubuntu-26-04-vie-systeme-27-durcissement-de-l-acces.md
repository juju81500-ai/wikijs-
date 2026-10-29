---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 27 Durcissement De L Acces"
description: "Sécuriser sshd."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-27"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-27`

---

## Problème précis à résoudre

Sécuriser sshd.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un fichier de surcharge (nom en `20-` pour passer avant `50-cloud-init.conf`) :
   ```bash
   sudo tee /etc/ssh/sshd_config.d/20-durcissement.conf >/dev/null <<'EOT'
   PermitRootLogin no
   PasswordAuthentication no
   MaxAuthTries 3
   EOT
   ```
   👉 Explication : interdit root et les mots de passe; pour `sshd`, la première valeur lue gagne, donc un fichier `50-cloud-init.conf` qui autorise les mots de passe ne l'emporte pas.

2. Tester puis recharger sans fermer la session actuelle :
   ```bash
   sudo sshd -t
   sudo systemctl reload ssh
   sudo sshd -T | grep -E 'permitrootlogin|passwordauthentication'
   ```
   👉 Explication : contrôle la syntaxe et la configuration effective; si le port d'écoute change, la socket `ssh.socket` doit être mise à jour (`sudo systemctl daemon-reload && sudo systemctl restart ssh.socket`).

## 2. Production — Contrôles

Limiter par `AllowGroups` et par pare-feu au réseau d'administration.

## 3. Production — Sécurité

Garder une session ouverte jusqu'au test réussi d'une seconde connexion.

## Validation et retour arrière

- **Validation** : `sshd -T` montre `no` pour les deux options.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)
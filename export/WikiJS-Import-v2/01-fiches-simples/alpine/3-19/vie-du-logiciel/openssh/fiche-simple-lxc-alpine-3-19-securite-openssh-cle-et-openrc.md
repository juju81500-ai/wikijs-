---
title: "Fiche Simple - LXC Alpine 3.19 Securite OpenSSH Cle Et OpenRC"
description: "Installer le serveur OpenSSH dans un conteneur Alpine, vérifier un accès par clé Ed25519, puis réduire l'authentification distante sans perdre l'accès d'administration."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[alpine3.19]", "[alpine]", "[openssh]", "[ssh]", "[openrc]", "[ed25519]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Securite_OpenSSH_Cle_Et_OpenRC.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 avec OpenRC (version legacy)
- **Catégorie** : Installation / Sécurité / SSH
- **Tags** : `[alpine3.19]`, `[alpine]`, `[openssh]`, `[ssh]`, `[openrc]`, `[ed25519]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer le serveur OpenSSH dans un conteneur Alpine, vérifier un accès par clé Ed25519, puis réduire l'authentification distante sans perdre l'accès d'administration.

> Alpine 3.19 est une version ancienne : vérifier sa prise en charge et migrer vers une branche maintenue avant tout usage en production.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer OpenSSH et démarrer son service OpenRC :
   ```sh
   apk add openssh
   rc-update add sshd default
   rc-service sshd start
   rc-service sshd status
   ```
2. Depuis le poste client, créer une clé si nécessaire et la copier au compte cible :
   ```sh
   ssh-keygen -t ed25519
   ssh-copy-id -i ~/.ssh/id_ed25519.pub <utilisateur>@<ip-du-ct>
   ```
   👉 *Explication : la clé privée reste sur le poste client; seule la clé publique est installée sur Alpine.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier la clé depuis une nouvelle session SSH avant toute modification de l'authentification :
   ```sh
   ssh -i ~/.ssh/id_ed25519 <utilisateur>@<ip-du-ct>
   ```
2. Sauvegarder puis éditer `/etc/ssh/sshd_config`. Définir les directives suivantes, sans dupliquer les entrées existantes :
   ```text
   PubkeyAuthentication yes
   PermitRootLogin no
   PasswordAuthentication no
   ```
3. Vérifier la syntaxe et redémarrer le service :
   ```sh
   sshd -t
   rc-service sshd restart
   ```
   👉 *Explication : ne désactiver l'authentification par mot de passe qu'après avoir testé la clé dans une seconde session.*

## 🔒 3. Production — Façon Sécurisée
1. Garder la console Proxmox ouverte; le réseau et les capacités disponibles dans un LXC dépendent aussi de l'hôte.
2. Utiliser un compte nominatif non-root, une clé protégée par phrase secrète et une règle de pare-feu limitée aux sources d'administration.
3. Ne pas exposer SSH sur Internet sans filtrage, supervision et procédure d'accès de secours.

## ✅ Validation et retour arrière
- Tester une nouvelle connexion par clé, puis confirmer qu'une connexion root directe est refusée.
- En cas d'échec, restaurer `/etc/ssh/sshd_config` depuis la console et redémarrer `sshd`.
- Vérifier le port d'écoute et les journaux disponibles avant de fermer la session de secours.
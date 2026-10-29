---
title: "Fiche Simple - VM Alpine 3.19 Vie Systeme 27 Durcissement De L Acces"
description: "Limiter la surface d'attaque de sshd."
published: true
date: 2026-10-29T20:22:10Z
tags: ["alpine319", "vie-du-systeme", "cycle-de-vie", "etape-27"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Alpine_3.19_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : VM Alpine Linux 3.19 (serveur)
- **OS / Version** : Alpine Linux 3.19; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `alpine319`, `vie-du-systeme`, `cycle-de-vie`, `etape-27`

---

## Problème précis à résoudre

Limiter la surface d'attaque de `sshd`.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder puis modifier la configuration :
   ```sh
   doas cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
   doas sed -i -e 's/^#\?PermitRootLogin.*/PermitRootLogin no/' -e 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' -e 's/^#\?MaxAuthTries.*/MaxAuthTries 3/' /etc/ssh/sshd_config
   echo 'AllowUsers ADMIN' | doas tee -a /etc/ssh/sshd_config
   ```
   👉 Explication : refuse `root` et les mots de passe, limite les essais, n'autorise que ADMIN; placer `AllowUsers` hors d'un bloc `Match`.

2. Tester la syntaxe puis recharger :
   ```sh
   doas sshd -t
   doas rc-service sshd restart
   ```
   👉 Explication : `sshd -t` vérifie la syntaxe; garder la session ouverte pendant le test.

3. Tester depuis un second terminal :
   ```sh
   ssh ADMIN@ADRESSE_IP
   ```
   👉 Explication : la connexion par clé doit passer.

## 2. Production — Contrôles

Documenter l'exception si un accès par mot de passe reste nécessaire.

## 3. Production — Sécurité

Ne jamais couper la session de secours avant d'avoir validé la nouvelle.

## Validation et retour arrière

- **Validation** : `sshd -T | grep -E 'permitrootlogin|passwordauthentication'` affiche `no`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : LXC Alpine 3.19 Securite OpenSSH Cle Et OpenRC](</01-fiches-simples/alpine/3-19/vie-du-logiciel/openssh/fiche-simple-lxc-alpine-3-19-securite-openssh-cle-et-openrc>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Alpine Linux 3.19](/01-fiches-simples/alpine/3-19/vie-du-systeme/sommaire-vie-du-systeme-alpine-3-19)
- [Documentation officielle](https://docs.alpinelinux.org/)
---
title: "Fiche Simple - LXC Alpine 3.19 Systeme Creer Compte Admin Doas"
description: "Créer un compte d'administration non-root sur Alpine Linux et lui accorder une élévation contrôlée avec doas, sans installer ni configurer sudo."
published: true
date: 2026-10-29T20:22:41Z
tags: ["[alpine3.19]", "[alpine]", "[lxc]", "[comptes]", "[doas]", "[openrc]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:41Z
dateModified: 2026-10-29T20:22:41Z
---

# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Creer_Compte_Admin_Doas.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - OpenRC
- **Catégorie** : Création de compte / Sécurité
- **Tags** : `[alpine3.19]`, `[alpine]`, `[lxc]`, `[comptes]`, `[doas]`, `[openrc]`, `[hardening]`

## 🎯 Problème précis à résoudre
Créer un compte d'administration non-root sur Alpine Linux et lui accorder une élévation contrôlée avec `doas`, sans installer ni configurer `sudo`.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer `doas` et créer le compte de test :
   ```sh
   apk add doas
   adduser testadmin
   adduser testadmin wheel
   ```
   👉 *Explication : `adduser` demande un mot de passe interactif; le second appel ajoute le compte au groupe d'administration `wheel`.*
2. Créer une règle limitée aux membres de `wheel` :
   ```sh
   install -d -o root -g root -m 0755 /etc/doas.d
   printf '%s\n' 'permit persist :wheel' > /etc/doas.d/10-wheel.conf
   chown root:root /etc/doas.d/10-wheel.conf
   chmod 0400 /etc/doas.d/10-wheel.conf
   ```
   👉 *Explication : `persist` évite de redemander le mot de passe pendant un court délai; il ne supprime pas l'authentification.*

## ⚡ 2. Production — Façon Simplifiée
1. Installer le paquet, créer un compte nominatif et l'ajouter à `wheel` :
   ```sh
   apk add doas
   adduser adminops
   adduser adminops wheel
   ```
2. Écrire la règle `doas` avec des permissions appartenant à root :
   ```sh
   install -d -o root -g root -m 0755 /etc/doas.d
   printf '%s\n' 'permit persist :wheel' > /etc/doas.d/10-wheel.conf
   chown root:root /etc/doas.d/10-wheel.conf
   chmod 0400 /etc/doas.d/10-wheel.conf
   ```
3. Ouvrir une nouvelle session sous `adminops` et tester une commande autorisée :
   ```sh
   doas id
   ```
   👉 *Explication : La commande doit demander l'authentification puis afficher `uid=0(root)`.*

## 🔒 3. Production — Façon Sécurisée
1. Créer un compte nominatif par administrateur; ne pas partager le compte `root` ni le mot de passe du compte d'administration.
2. Ne pas utiliser `permit nopass` et ne pas accorder une règle générale à des utilisateurs non administrateurs.
3. Dans un conteneur LXC, retenir que `doas` élève les privilèges dans le conteneur, pas sur l'hôte Proxmox. Conserver un accès console de l'hôte pour le dépannage.

## ✅ Validation et retour arrière
- Vérifier l'appartenance avec `id adminops`, puis tester `doas id` depuis une session distincte.
- En cas d'échec, contrôler la syntaxe et les droits de `/etc/doas.d/10-wheel.conf`.
- Pour retirer l'accès, exécuter `deluser adminops wheel` et supprimer la règle uniquement si elle n'est pas utilisée par d'autres comptes.

## 🔗 Si le problème n'est pas résolu
- Consulter la fiche Alpine dédiée à la gestion des services OpenRC et vérifier les journaux du système.
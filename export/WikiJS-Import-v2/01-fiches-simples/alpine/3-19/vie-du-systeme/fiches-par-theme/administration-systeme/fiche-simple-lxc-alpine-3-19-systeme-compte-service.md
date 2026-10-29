---
title: "Fiche Simple - LXC Alpine 3.19 Systeme Compte Service"
description: "Créer un compte système dédié, sans shell de connexion ni mot de passe, pour exécuter un service applicatif sous Alpine Linux, afin d'isoler ce service du compte administrateur et du compte root."
published: true
date: 2026-10-29T20:22:41Z
tags: ["[alpine3.19]", "[alpine]", "[lxc]", "[comptes]", "[service-account]", "[openrc]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:41Z
dateModified: 2026-10-29T20:22:41Z
---

# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Compte_Service.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Système & Services / Comptes de service
- **Tags** : `[alpine3.19]`, `[alpine]`, `[lxc]`, `[comptes]`, `[service-account]`, `[openrc]`, `[hardening]`

## 🎯 Problème précis à résoudre
Créer un compte système dédié, sans shell de connexion ni mot de passe, pour exécuter un service applicatif sous Alpine Linux, afin d'isoler ce service du compte administrateur et du compte `root`.

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Créer le groupe et le compte système (BusyBox `adduser`) :
   ```sh
   addgroup -S <service_groupe>
   adduser -S -D -H -h /var/lib/<service_nom> -s /sbin/nologin -G <service_groupe> <service_nom>
   ```
   👉 Explication : `-S` crée un compte système (UID bas), `-D` ne définit pas de mot de passe, `-H` ne crée pas le répertoire personnel, `-s /sbin/nologin` interdit la connexion interactive.

2. Créer le répertoire de données du service :
   ```sh
   install -d -o <service_nom> -g <service_groupe> -m 0750 /var/lib/<service_nom>
   ```
   👉 Explication : Seul le compte du service et son groupe peuvent lire ou écrire dans ce répertoire.

3. Vérifier l'identité et le shell du compte :
   ```sh
   id <service_nom>
   getent passwd <service_nom>
   ```
   👉 Explication : La sortie doit montrer le groupe `<service_groupe>` et le shell `/sbin/nologin`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Verrouiller le mot de passe du compte de service :
   ```sh
   passwd -l <service_nom>
   ```
   👉 Explication : Le verrouillage interdit toute authentification par mot de passe sur ce compte, même si un mot de passe lui était attribué par erreur.

2. Faire tourner le démon sous ce compte dans le script OpenRC du service (`/etc/init.d/<nom_du_service>`) :
   ```sh
   command_user="<service_nom>:<service_groupe>"
   ```
   👉 Explication : OpenRC démarre le processus avec ce compte au lieu de `root`. Redémarrer le service ensuite avec `rc-service <nom_du_service> restart`.

3. Vérifier l'utilisateur effectif du processus :
   ```sh
   ps -o user,comm | grep <nom_du_binaire>
   ```
   👉 Explication : La colonne `USER` doit afficher `<service_nom>` et non `root`.

---

## 🔒 3. Production — Façon Sécurisée
1. Restreindre les fichiers de configuration du service au compte `root` et au groupe du service :
   ```sh
   chown -R root:<service_groupe> /etc/<nom_du_service>
   chmod -R 0640 /etc/<nom_du_service>
   ```
   👉 Explication : Le service peut lire sa configuration sans pouvoir la modifier. Ne pas appliquer ces commandes à `/etc/init.d/`, dont les permissions sont gérées par les paquets.

2. Ne jamais utiliser le compte de service pour une session d'administration ni lui accorder une entrée dans `doas` ou `/etc/sudoers`, et documenter le compte dans l'inventaire (étape 49 du cycle de vie).
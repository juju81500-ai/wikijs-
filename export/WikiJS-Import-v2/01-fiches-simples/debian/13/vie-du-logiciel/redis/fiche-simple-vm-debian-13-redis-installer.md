---
title: "Fiche Simple - VM Debian 13 Redis Installer"
description: "Installer Redis depuis le dépôt Debian et vérifier le service."
published: true
date: 2026-10-29T20:37:00Z
tags: ["debian13", "redis", "installation"]
editor: markdown
dateCreated: 2026-10-29T20:37:00Z
dateModified: 2026-10-29T20:37:00Z
---

# Fiche_Simple_-_VM_Debian_13_Redis_Installer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Redis des dépôts Debian
- **Catégorie** : base clé-valeur / Redis / Installer
- **Tags** : `debian13`, `redis`, `installation`

---

## Problème précis à résoudre

Installer Redis depuis le dépôt Debian et vérifier le service.

## 1. Hors-Production (Lab / Test / POC)

1. Relever la version candidate :
   ```bash
   sudo apt update
   apt-cache policy redis-server
   ```
   👉 Explication : consigner version et origine.

2. Installer :
   ```bash
   sudo apt install -y redis-server redis-tools
   ```
   👉 Explication : installe le serveur, `redis-cli` et l'unité systemd.

3. Activer et vérifier :
   ```bash
   sudo systemctl enable --now redis-server
   systemctl status redis-server --no-pager
   redis-server --version
   ```
   👉 Explication : service actif.

4. Tester localement :
   ```bash
   redis-cli ping
   ```
   👉 Explication : la réponse attendue est `PONG`.

## 2. Production — Contrôles

Consigner la version et la cadence de mise à jour de sécurité.

## 3. Production — Sécurité

- Dépôt Debian officiel uniquement.
- Ne pas ouvrir le port 6379.
- Ne pas lancer Redis en `root`.

## Validation et retour arrière

- **Validation** : `redis-cli ping` répond `PONG`.
- **Retour arrière** : `sudo apt purge redis-server redis-tools` après sauvegarde de `/var/lib/redis`.

## Si le problème n'est pas résolu

- [Redis — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-prerequis-limites)
- [Redis — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-configurer)
- [Redis — Sécuriser (ACL, TLS, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-securiser)
- [Redis — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-valider)
- [Redis — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-sauvegarder-restaurer)
- [Redis — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/redis/fiche-simple-vm-debian-13-redis-mettre-a-jour)
- [Redis — documentation officielle](https://redis.io/docs/latest/)
- [Redis — sécurité](https://redis.io/docs/latest/operate/oss_and_stack/management/security/)
- [Installation Redis avec NetBox (fiche du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-netbox-installer-postgresql-redis)
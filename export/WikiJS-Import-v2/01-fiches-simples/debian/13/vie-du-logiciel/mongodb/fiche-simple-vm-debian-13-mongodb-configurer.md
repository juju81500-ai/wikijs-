---
title: "Fiche Simple - VM Debian 13 MongoDB Configurer"
description: "Configurer /etc/mongod.conf (écoute, stockage, journalisation) et vérifier le démarrage."
published: true
date: 2026-10-29T20:37:00Z
tags: ["debian13", "mongodb", "configuration"]
editor: markdown
dateCreated: 2026-10-29T20:37:00Z
dateModified: 2026-10-29T20:37:00Z
---

# Fiche_Simple_-_VM_Debian_13_MongoDB_Configurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MongoDB Community (dépôt officiel)
- **Catégorie** : base de données / MongoDB / Configurer
- **Tags** : `debian13`, `mongodb`, `configuration`

---

## Problème précis à résoudre

Configurer `/etc/mongod.conf` (écoute, stockage, journalisation) et vérifier le démarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration :
   ```bash
   sudo cp -a /etc/mongod.conf /etc/mongod.conf.orig
   ```
   👉 Explication : point de retour.

2. Contrôler les sections principales :
   ```bash
   sudo grep -nE 'dbPath|bindIp|port|path|authorization' /etc/mongod.conf
   ```
   👉 Explication : vérifier `storage.dbPath`, `net.bindIp: 127.0.0.1`, `systemLog.path`.

3. Appliquer un changement et redémarrer :
   ```bash
   sudo systemctl restart mongod
   sudo journalctl -u mongod -n 20 --no-pager
   ```
   👉 Explication : aucune erreur au démarrage.

4. Tester la connexion locale :
   ```bash
   mongosh --eval 'db.runCommand({ ping: 1 })'
   ```
   👉 Explication : `ok: 1` attendu.

## 2. Production — Contrôles

Configuration versionnée et relue ; limites système (`ulimit`) et THP contrôlés.

## 3. Production — Sécurité

- `bindIp` limité à loopback tant que la sécurité n'est pas appliquée.
- Droits `mongodb:mongodb` sur `dbPath`.
- Aucun secret dans `mongod.conf`.

## Validation et retour arrière

- **Validation** : `ping` renvoie `ok: 1`.
- **Retour arrière** : restaurer `/etc/mongod.conf.orig` et redémarrer.

## Si le problème n'est pas résolu

- [MongoDB — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-prerequis-limites)
- [MongoDB — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-installer)
- [MongoDB — Sécuriser (authentification, TLS, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-securiser)
- [MongoDB — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-valider)
- [MongoDB — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-sauvegarder-restaurer)
- [MongoDB — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-mettre-a-jour)
- [MongoDB — installation sous Debian](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
- [MongoDB — sécurité](https://www.mongodb.com/docs/manual/security/)
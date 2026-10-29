---
title: "Fiche Simple - VM Debian 13 MongoDB Valider"
description: "Prouver que MongoDB est opérationnel, authentifié et chiffré."
published: true
date: 2026-10-29T20:37:00Z
tags: ["debian13", "mongodb", "recette"]
editor: markdown
dateCreated: 2026-10-29T20:37:00Z
dateModified: 2026-10-29T20:37:00Z
---

# Fiche_Simple_-_VM_Debian_13_MongoDB_Valider

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MongoDB Community (dépôt officiel)
- **Catégorie** : base de données / MongoDB / Valider (recette)
- **Tags** : `debian13`, `mongodb`, `recette`

---

## Problème précis à résoudre

Prouver que MongoDB est opérationnel, authentifié et chiffré.

## 1. Hors-Production (Lab / Test / POC)

1. État du service et écoute :
   ```bash
   systemctl is-active mongod
   sudo ss -tlnp | grep mongod
   ```
   👉 Explication : écoute sur les adresses prévues seulement.

2. Refus sans authentification :
   ```bash
   mongosh --eval 'db.getSiblingDB("admin").getUsers()'
   ```
   👉 Explication : la commande doit retourner `Unauthorized`.

3. Connexion authentifiée avec TLS :
   ```bash
   mongosh 'mongodb://ADMIN_DB@NOM_SERVEUR:27017/admin?tls=true&tlsCAFile=/chemin/CA.crt' --eval 'db.runCommand({ping:1})'
   ```
   👉 Explication : le mot de passe est demandé ; remplacer `ADMIN_DB`, `NOM_SERVEUR`, le chemin de l'AC (à remplacer).

4. Écriture de test :
   ```bash
   mongosh 'mongodb://APPUSER@NOM_SERVEUR:27017/APPDB?tls=true&tlsCAFile=/chemin/CA.crt' --eval 'db.recette.insertOne({ok:1}); db.recette.drop()'
   ```
   👉 Explication : valide droits et écriture ; collection supprimée.

## 2. Production — Contrôles

Consigner la recette ; superviser disponibilité, connexions, espace disque, journal.

## 3. Production — Sécurité

- Supprimer les données de test.
- Aucun compte de recette conservé.
- Surveiller `/var/log/mongodb/mongod.log`.

## Validation et retour arrière

- **Validation** : tous les contrôles réussis.
- **Retour arrière** : revenir à la configuration sauvegardée.

## Si le problème n'est pas résolu

- [MongoDB — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-prerequis-limites)
- [MongoDB — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-installer)
- [MongoDB — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-configurer)
- [MongoDB — Sécuriser (authentification, TLS, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-securiser)
- [MongoDB — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-sauvegarder-restaurer)
- [MongoDB — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-mettre-a-jour)
- [MongoDB — installation sous Debian](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
- [MongoDB — sécurité](https://www.mongodb.com/docs/manual/security/)
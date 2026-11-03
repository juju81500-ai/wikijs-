---
title: "Fiche Simple - VM Debian 13 MongoDB Sauvegarder Restaurer"
description: "Sauvegarder MongoDB avec mongodump et restaurer avec mongorestore sur un serveur de test."
published: true
date: 2026-11-03T14:22:28Z
tags: ["debian13", "mongodb", "sauvegarde"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Fiche_Simple_-_VM_Debian_13_MongoDB_Sauvegarder_Restaurer

- **Environnement** : [[Glossary:VM]] Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MongoDB Community (dépôt officiel)
- **Catégorie** : base de données / MongoDB / Sauvegarder et restaurer
- **Tags** : `debian13`, `mongodb`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder MongoDB avec `mongodump` et restaurer avec `mongorestore` sur un serveur de test.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder dans une archive compressée :
   ```bash
   sudo install -d -m 0700 /var/backups/mongodb
   mongodump --uri='mongodb://ADMIN_DB@NOM_SERVEUR:27017/?authSource=admin&tls=true&tlsCAFile=/chemin/CA.crt' --gzip --archive=/var/backups/mongodb/all-$(date +%F).archive.gz
   ```
   👉 Explication : le mot de passe est demandé ; remplacer les valeurs (à remplacer). Pour de gros volumes ou des jeux répliqués, privilégier les instantanés de volume.

2. Contrôler l'archive :
   ```bash
   ls -lh /var/backups/mongodb/
   sha256sum /var/backups/mongodb/all-$(date +%F).archive.gz
   ```
   👉 Explication : noter l'empreinte pour contrôler la copie externe.

3. Restaurer sur un serveur de test :
   ```bash
   mongorestore --uri='mongodb://ADMIN_DB@NOM_SERVEUR_TEST:27017/?authSource=admin&tls=true&tlsCAFile=/chemin/CA.crt' --gzip --archive=/var/backups/mongodb/all-DATE.archive.gz
   ```
   👉 Explication : remplacer `NOM_SERVEUR_TEST` et `DATE` (à remplacer) ; jamais sur la production sans validation.

4. Vérifier :
   ```bash
   mongosh --eval 'db.adminCommand({listDatabases:1}).databases.map(d=>d.name)'
   ```
   👉 Explication : les bases attendues sont présentes.

## 2. Production — Contrôles

Sauvegarde planifiée et chiffrée, copie hors site, test de restauration régulier.

## 3. Production — Sécurité

- Chiffrer les copies.
- Dossier en `0700`.
- Ne pas stocker sur le même disque.

## Validation et retour arrière

- **Validation** : restauration testée sur un serveur distinct.
- **Retour arrière** : reprendre la sauvegarde précédente.

## Si le problème n'est pas résolu

- [MongoDB — Prérequis et limites](/fr/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-prerequis-limites)
- [MongoDB — Installer](/fr/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-installer)
- [MongoDB — Configurer](/fr/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-configurer)
- [MongoDB — Sécuriser (authentification, TLS, pare-feu)](/fr/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-securiser)
- [MongoDB — Valider (recette)](/fr/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-valider)
- [MongoDB — Mise à jour et retour arrière](/fr/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-mettre-a-jour)
- [MongoDB — installation sous Debian](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
- [MongoDB — sécurité](https://www.mongodb.com/docs/manual/security/)
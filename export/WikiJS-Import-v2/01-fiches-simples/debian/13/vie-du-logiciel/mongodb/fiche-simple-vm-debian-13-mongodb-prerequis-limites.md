---
title: "Fiche Simple - VM Debian 13 MongoDB Prerequis Limites"
description: "Vérifier qu'un MongoDB Community peut être installé sur Debian 13 et cadrer les limites."
published: true
date: 2026-10-29T20:37:00Z
tags: ["debian13", "mongodb", "prerequis"]
editor: markdown
dateCreated: 2026-10-29T20:37:00Z
dateModified: 2026-10-29T20:37:00Z
---

# Fiche_Simple_-_VM_Debian_13_MongoDB_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MongoDB Community (dépôt officiel)
- **Catégorie** : base de données / MongoDB / Prérequis et limites
- **Tags** : `debian13`, `mongodb`, `prerequis`

---

## Problème précis à résoudre

Vérifier qu'un MongoDB Community peut être installé sur Debian 13 et cadrer les limites.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS, le processeur et l'espace disque :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   grep -m1 -o -w avx /proc/cpuinfo || echo 'AVX absent'
   df -h /var/lib /var/backups
   ```
   👉 Explication : MongoDB 5.0 et plus exige un processeur avec AVX ; prévoir de l'espace pour données, journal et sauvegardes (XFS recommandé par l'éditeur).

2. Vérifier le support de Debian 13 :
   👉 Explication : MongoDB Community est distribué par son propre dépôt APT : vérifier dans la matrice de compatibilité de la version visée que Debian 13 est prise en charge ; à défaut utiliser une distribution listée ou un conteneur officiel.

3. Contrôler le port :
   ```bash
   sudo ss -tlnp | grep -E ':27017\b' || echo 'port 27017 libre'
   ```
   👉 Explication : aucun autre mongod ne doit écouter.

## 2. Production — Contrôles

Consigner version, volumétrie, clients, responsable, RPO/RTO.

## 3. Production — Sécurité

- Pas d'exposition réseau avant la fiche Sécuriser.
- Limites : instance unique ; replica set et sharding hors périmètre.
- Ne pas utiliser un MongoDB sans authentification.

## Validation et retour arrière

- **Validation** : support de la version et matériel vérifiés.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [MongoDB — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-installer)
- [MongoDB — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-configurer)
- [MongoDB — Sécuriser (authentification, TLS, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-securiser)
- [MongoDB — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-valider)
- [MongoDB — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-sauvegarder-restaurer)
- [MongoDB — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/mongodb/fiche-simple-vm-debian-13-mongodb-mettre-a-jour)
- [MongoDB — installation sous Debian](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-debian/)
- [MongoDB — sécurité](https://www.mongodb.com/docs/manual/security/)
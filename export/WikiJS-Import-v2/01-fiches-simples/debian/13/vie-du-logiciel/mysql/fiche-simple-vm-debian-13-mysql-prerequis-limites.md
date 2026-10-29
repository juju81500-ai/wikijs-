---
title: "Fiche Simple - VM Debian 13 MySQL Prerequis Limites"
description: "Vérifier qu'un MySQL Community peut être installé sur Debian 13 et connaître les limites avant de commencer."
published: true
date: 2026-10-29T20:37:00Z
tags: ["debian13", "mysql", "prerequis"]
editor: markdown
dateCreated: 2026-10-29T20:37:00Z
dateModified: 2026-10-29T20:37:00Z
---

# Fiche_Simple_-_VM_Debian_13_MySQL_Prerequis_Limites

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MySQL Community (dépôt officiel Oracle)
- **Catégorie** : base de données / MySQL / Prérequis et limites
- **Tags** : `debian13`, `mysql`, `prerequis`

---

## Problème précis à résoudre

Vérifier qu'un MySQL Community peut être installé sur Debian 13 et connaître les limites avant de commencer.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS et l'espace disque :
   ```bash
   cat /etc/os-release | grep PRETTY_NAME
   df -h /var/lib /var/backups
   ```
   👉 Explication : prévoir de l'espace pour les données, journaux binaires et sauvegardes.

2. Détecter un MariaDB déjà installé :
   ```bash
   dpkg -l | grep -E 'mariadb|mysql' || echo 'aucun serveur installé'
   sudo ss -tlnp | grep -E ':3306\b' || echo 'port 3306 libre'
   ```
   👉 Explication : MariaDB et MySQL ne cohabitent pas sur les mêmes paquets ni le même port.

3. Vérifier la prise en charge de Debian 13 par le dépôt Oracle :
   👉 Explication : Debian 13 ne distribue pas MySQL : il faut le dépôt APT officiel MySQL (paquet `mysql-apt-config`). Vérifier sur la page de téléchargement que Debian 13 est prise en charge pour la version visée (8.4 LTS) ; sinon utiliser MariaDB, une VM Ubuntu LTS ou un conteneur officiel.

## 2. Production — Contrôles

Consigner la raison du choix MySQL (compatibilité applicative), la version LTS, la volumétrie, les clients, le responsable.

## 3. Production — Sécurité

- Ne pas mélanger paquets Debian MariaDB et paquets MySQL Oracle.
- Pas d'exposition réseau avant la fiche Sécuriser.
- Limites : serveur unique ; réplication, InnoDB Cluster hors périmètre.

## Validation et retour arrière

- **Validation** : OS confirmé, port libre, prise en charge de la version vérifiée.
- **Retour arrière** : aucune modification effectuée.

## Si le problème n'est pas résolu

- [MySQL — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-installer)
- [MySQL — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-configurer)
- [MySQL — Sécuriser (TLS, comptes, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-securiser)
- [MySQL — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-valider)
- [MySQL — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-sauvegarder-restaurer)
- [MySQL — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/mysql/fiche-simple-vm-debian-13-mysql-mettre-a-jour)
- [MySQL — documentation officielle](https://dev.mysql.com/doc/)
- [Alternative MariaDB (fiches du pack)](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-prerequis-limites)
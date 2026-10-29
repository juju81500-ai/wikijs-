---
title: "Fiche Simple - VM Debian 12 Zabbix Preparer Base"
description: "Créer la base Zabbix et importer une seule fois le schéma correspondant à la version installée."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "zabbix", "mariadb", "database", "schema"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_Zabbix_Preparer_Base.md

- **Environnement** : MariaDB local dédié au serveur Zabbix Debian 12
- **OS / Version** : Debian 12 Bookworm; MariaDB maintenu et schéma Zabbix 7.0 LTS
- **Catégorie** : supervision / base de données
- **Tags** : `debian12`, `zabbix`, `mariadb`, `database`, `schema`

---

## Problème précis à résoudre

Créer la base Zabbix et importer une seule fois le schéma correspondant à la version installée.

## 1. Hors-Production (Lab / Test / POC)

1. Installer et sécuriser MariaDB :
   ```bash
   sudo apt install mariadb-server
   sudo mariadb-secure-installation
   ```
   👉 Explication : répondre aux questions pour supprimer comptes anonymes et base de test.

2. Créer le schéma et l'utilisateur dédiés (le secret est saisi, jamais écrit en clair dans l'historique) :
   ```bash
   read -rsp "Mot de passe base zabbix : " ZPW; echo
   sudo mariadb -e "CREATE DATABASE zabbix CHARACTER SET utf8mb4 COLLATE utf8mb4_bin; CREATE USER 'zabbix'@'localhost' IDENTIFIED BY '${ZPW}'; GRANT ALL PRIVILEGES ON zabbix.* TO 'zabbix'@'localhost'; SET GLOBAL log_bin_trust_function_creators = 1;"
   unset ZPW
   ```
   👉 Explication : jeu de caractères recommandé par Zabbix; ranger le secret dans le coffre.

3. Vérifier que les paquets fournissent le schéma :
   ```bash
   sudo apt install zabbix-sql-scripts
   dpkg -L zabbix-sql-scripts | grep 'server.sql.gz'
   ```
   👉 Explication : confirme le chemin du script d'import.

4. Confirmer que la base est vide, puis importer une seule fois (sauvegarde faite avant) :
   ```bash
   sudo mariadb -e 'USE zabbix; SHOW TABLES;'
   zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | sudo mariadb --default-character-set=utf8mb4 zabbix
   sudo mariadb -e 'SET GLOBAL log_bin_trust_function_creators = 0;'
   ```
   👉 Explication : l'import peut être long; ne pas relancer à l'aveugle s'il est interrompu.

## 2. Production — Contrôles

Valider la version du schéma, la base cible, les droits du compte, le stockage, l'export pré-import et la procédure de restauration.

## 3. Production — Sécurité

- Ne pas importer dans une base existante sans inventaire et sauvegarde.
- Ne pas relancer un import interrompu à l'aveugle.
- Ne pas exposer MariaDB sur un réseau non requis.
- Ne pas placer le mot de passe dans une commande, un fichier partagé ou le wiki.

## Validation et retour arrière

- **Validation** : schéma correspondant à la version Zabbix installé et accès local du compte dédié confirmé.
- **Retour arrière** : conserver le journal d'import; restaurer l'export cohérent plutôt que multiplier les imports.

## Si le problème n'est pas résolu

- [Zabbix — création et configuration de la base](https://www.zabbix.com/documentation/7.0/en/manual/appendix/install/db_scripts)
- [MariaDB — documentation](https://mariadb.com/kb/en/documentation/)
- [Guide complet Zabbix Debian 12](/02-fiches-completes/debian/12/installation-deploiement/04-supervision-centralisee-zabbix-70-lts-debian-12)
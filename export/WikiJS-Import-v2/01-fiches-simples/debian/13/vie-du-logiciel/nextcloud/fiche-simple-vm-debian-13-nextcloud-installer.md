---
title: "Fiche Simple - VM Debian 13 Nextcloud Installer"
description: "Installer Nextcloud (archive officielle vérifiée) avec Apache, PHP et MariaDB sur Debian 13."
published: true
date: 2026-10-29T20:37:37Z
tags: ["debian13", "nextcloud", "cloud", "apache", "php", "installer"]
editor: markdown
dateCreated: 2026-10-29T20:37:37Z
dateModified: 2026-10-29T20:37:37Z
---

# Fiche_Simple_-_VM_Debian_13_Nextcloud_Installer

- **Environnement** : VM Debian 13; Nextcloud (archive officielle), Apache, PHP 8.4 et MariaDB
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Nextcloud — Installer
- **Tags** : `debian13`, `nextcloud`, `cloud`, `apache`, `php`, `installer`

---

## Problème précis à résoudre

Installer Nextcloud (archive officielle vérifiée) avec Apache, PHP et MariaDB sur Debian 13.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo apt update
   sudo apt install -y apache2 mariadb-server libapache2-mod-php php php-gd php-mysql php-curl php-mbstring php-intl php-gmp php-bcmath php-xml php-zip php-apcu php-imagick bzip2 curl
   ```
   👉 Explication : modules PHP exigés par Nextcloud ; la liste exacte est à comparer à la documentation de la version installée.

2. Créer la base et l'utilisateur (mot de passe saisi, non écrit en dur) :
   ```bash
   read -rsp 'Mot de passe base Nextcloud : ' NC_DB_PASS; echo
   sudo mariadb <<SQL
   CREATE DATABASE nextcloud CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
   CREATE USER 'nextcloud'@'localhost' IDENTIFIED BY '${NC_DB_PASS}';
   GRANT ALL PRIVILEGES ON nextcloud.* TO 'nextcloud'@'localhost';
   FLUSH PRIVILEGES;
   SQL
   ```
   👉 Explication : le mot de passe est demandé au clavier. Voir les fiches MariaDB du pack pour la sécurisation initiale (`mariadb-secure-installation`).

3. Télécharger l'archive et son empreinte, puis vérifier :
   ```bash
   cd /tmp
   curl -fLO https://download.nextcloud.com/server/releases/latest.tar.bz2
   curl -fLO https://download.nextcloud.com/server/releases/latest.tar.bz2.sha256
   sha256sum -c latest.tar.bz2.sha256
   ```
   👉 Explication : `latest` suit la dernière version stable ; pour figer une version utiliser `nextcloud-VERSION.tar.bz2` (à remplacer). Une signature GPG (`.asc`) est aussi publiée : la vérifier en production.

4. Déployer dans la racine web :
   ```bash
   sudo tar -xjf /tmp/latest.tar.bz2 -C /var/www
   sudo chown -R www-data:www-data /var/www/nextcloud /srv/nextcloud-data
   ```
   👉 Explication : l'archive contient le dossier `nextcloud/`.

5. Installer via `occ` (mot de passe administrateur saisi) :
   ```bash
   read -rsp 'Mot de passe admin Nextcloud : ' NC_ADMIN_PASS; echo
   cd /var/www/nextcloud
   sudo -u www-data php occ maintenance:install --database mysql --database-name nextcloud --database-user nextcloud --database-pass "$NC_DB_PASS" --admin-user ADMIN_NC --admin-pass "$NC_ADMIN_PASS" --data-dir /srv/nextcloud-data
   unset NC_DB_PASS NC_ADMIN_PASS
   ```
   👉 Explication : `ADMIN_NC` est à remplacer. Les mots de passe transitent brièvement dans la liste des processus : pour un serveur multi-utilisateurs, préférer l'assistant web.

## 2. Production — Contrôles

Vérifier que la version installée correspond à celle visée (`occ status`), que l'archive a été contrôlée, que les droits sont limités à www-data et que Apache est actif.

## 3. Production — Sécurité

- Historique shell : ne jamais écrire de mot de passe en clair ; effacer les variables après usage.
- Supprimer `/tmp/latest.tar.bz2*` après déploiement.
- Ne pas exposer l'instance avant la fiche Sécuriser.

## Validation et retour arrière

- **Validation** : `sudo -u www-data php /var/www/nextcloud/occ status` indique `installed: true`.
- **Retour arrière** : supprimer `/var/www/nextcloud`, `DROP DATABASE nextcloud;` et l'utilisateur SQL, ou restaurer le snapshot.

## Si le problème n'est pas résolu

- [Nextcloud — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-prerequis-limites)
- [Nextcloud — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-configurer)
- [MariaDB — Sécuriser](/01-fiches-simples/debian/13/vie-du-logiciel/mariadb/fiche-simple-vm-debian-13-mariadb-securiser)
- [Nextcloud — manuel d'administration](https://docs.nextcloud.com/server/latest/admin_manual/)
- [Nextcloud — prérequis système](https://docs.nextcloud.com/server/latest/admin_manual/installation/system_requirements.html)
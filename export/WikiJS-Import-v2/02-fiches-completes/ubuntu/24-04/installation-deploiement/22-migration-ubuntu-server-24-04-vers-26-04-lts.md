---
title: "Migrer Ubuntu Server 24.04 vers 26.04 LTS"
description: "Fiche simple : [évaluer la migration](../../../../01-Fiches-Simples/Ubuntu/24.04/Vie-du-systeme/Fiches-par-theme/Migration-26.04/FicheSimple-VMUbuntu24.04Migration26.04Evaluer.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu24.04", "ubuntu26.04", "noble", "resolute", "migration", "apt", "production"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Migrer Ubuntu Server 24.04 vers 26.04 LTS

- **Type de fiche** : Autres — migration de version
- **Environnement** : VM ou serveur Ubuntu Server LTS
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble) vers Ubuntu Server 26.04 LTS (Resolute)
- **Rôle** : Préparer, exécuter et valider une mise à niveau majeure
- **Tags** : `ubuntu24.04`, `ubuntu26.04`, `noble`, `resolute`, `migration`, `apt`, `production`

## 1. Évaluer la migration

Fiche simple : [évaluer la migration](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiches-par-theme/migration-26-04/fiche-simple-vm-ubuntu-24-04-migration-26-04-evaluer).

Lire les notes officielles 26.04 pour le chemin LTS exact, les intervening releases et les applications installées. Ubuntu 26.04 change les versions de PHP, PostgreSQL, OpenSSH, systemd, Netplan, APT et plusieurs services; une mise à niveau de l'OS ne garantit pas la compatibilité des applications.

## 2. Inventorier et sauvegarder

Fiche simple : [inventorier et sauvegarder](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiches-par-theme/migration-26-04/fiche-simple-vm-ubuntu-24-04-migration-26-04-inventorier-sauvegarder).

```bash
cat /etc/os-release
apt list --upgradable
apt-mark showhold
sudo dpkg --audit
systemctl --failed
df -h / /boot /var
```

Inventorier dépôts externes/PPAs, services, extensions, clés SSH, montages, tâches planifiées et fichiers de configuration. Faire une sauvegarde complète vers une cible distincte et restaurer une copie dans une VM isolée avant l'intervention réelle.

## 3. Tester l'impact des changements de base

Fiche simple : [tester l'impact des changements de base](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiches-par-theme/migration-26-04/fiche-simple-vm-ubuntu-24-04-migration-26-04-impact-changements).

- **PHP 8.3 → 8.5 :** vérifier l'application et extensions natives; préparer la migration du code.
- **PostgreSQL 16 → 18 :** utiliser un chemin de migration de cluster supporté; sauvegarder/dumper la base; ne pas réutiliser directement l'ancien répertoire de données.
- **MySQL 8.0 → 8.4 :** vérifier l'authentification; `mysql_native_password` est désactivé par défaut dans la nouvelle version.
- **Chrony :** nouvelle installation et migration adoptent Chrony comme service horaire par défaut; éviter les sources en double.
- **systemd 259 :** cgroup v1 est supprimé; les scripts SysV sont à migrer vers des unités natives.
- **APT 3 :** `apt-key` est supprimé; adapter dépôts tiers et scripts de gestion de clés.
- **Dracut :** vérifier les hooks et procédures initramfs personnalisés.
- **OpenLDAP/Samba/Dovecot :** consulter les notes spécifiques si ces services sont installés.

## 4. Préparer Noble

Fiche simple : [préparer Noble](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiches-par-theme/migration-26-04/fiche-simple-vm-ubuntu-24-04-migration-26-04-preparer-noble).

1. Installer toutes les mises à jour disponibles de Noble et redémarrer si nécessaire.
2. Corriger `dpkg --audit`, dépôts externes non compatibles, paquets retenus et espace insuffisant.
3. Vérifier cloud-init/Netplan, DNS, accès console et session SSH de secours.
4. Pour une base MariaDB ou PostgreSQL, confirmer sauvegarde cohérente et procédure de mise à niveau du moteur séparée.

## 5. Exécuter l'upgrade

Fiche simple : [exécuter l'upgrade](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiches-par-theme/migration-26-04/fiche-simple-vm-ubuntu-24-04-migration-26-04-upgrade).

En fenêtre de maintenance avec console ou accès hors bande :

```bash
sudo apt update
sudo apt full-upgrade
sudo do-release-upgrade -c
```

Quand l'outil propose la version LTS prise en charge :

```bash
sudo do-release-upgrade
```

Lire chaque proposition de suppression, remplacement de configuration et redémarrage de service. Ne pas forcer une suite APT `resolute` dans les sources pendant qu'un upgrade est interrompu.

## 6. Valider après redémarrage

Fiche simple : [valider après redémarrage](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiches-par-theme/migration-26-04/fiche-simple-vm-ubuntu-24-04-migration-26-04-valider).

```bash
cat /etc/os-release
uname -r
systemctl --failed
ip -br address
ip route
resolvectl status
apt list --upgradable
```

Contrôler services, tâches, certificats, dépôts, pare-feu, sauvegarde et supervision. Tester chaque parcours applicatif depuis un client.

## 7. Revenir en arrière

Fiche simple : [revenir en arrière](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/fiches-par-theme/migration-26-04/fiche-simple-vm-ubuntu-24-04-migration-26-04-retour-arriere).

Une mise à niveau Debian/Ubuntu n'a pas de downgrade APT pris en charge. En cas d'échec, isoler la VM et restaurer la sauvegarde/snapshot validé; restaurer aussi les bases dans un état compatible avec les binaires retenus.

## Sources

- [Ubuntu 26.04 LTS — résumé des changements](https://documentation.ubuntu.com/release-notes/26.04/summary-for-lts-users/)
- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/)
- [Ubuntu 24.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
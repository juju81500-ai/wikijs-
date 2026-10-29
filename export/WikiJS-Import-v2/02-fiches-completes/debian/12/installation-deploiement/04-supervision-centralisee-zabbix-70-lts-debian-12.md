---
title: "Serveur Zabbix 7.0 LTS sur Debian 12"
description: "Fiche simple : [concevoir et préparer Zabbix](../../../../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Zabbix/FicheSimple-VMDebian12ZabbixConcevoirPreparer.md)."
published: true
date: 2026-10-29T19:55:10Z
tags: ["zabbix", "7.0-lts", "debian12", "supervision", "mariadb"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Serveur Zabbix 7.0 LTS sur Debian 12

- **Environnement** : VM de supervision dédiée
- **Rôles** : Serveur, frontend Web et base locale ; agents ou proxies séparés selon le réseau
- **Tags** : `zabbix`, `7.0-lts`, `debian12`, `supervision`, `mariadb`

## 1. Conception et prérequis

Fiche simple : [concevoir et préparer Zabbix](/01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-concevoir-preparer).

Dimensionner la base selon le nombre d'hôtes, d'items et la durée de conservation. Réserver DNS/IP, TLS, stockage, sauvegarde de la base et accès réseau des agents. Utiliser le dépôt officiel Zabbix correspondant exactement à Debian 12 et à la branche 7.0 LTS ; ne pas mélanger paquets Debian et dépôt d'une autre distribution.

```bash
sudo apt update
apt-cache policy zabbix-server-mysql zabbix-frontend-php
```

## 2. Base de données

Fiche simple : [préparer la base Zabbix](/01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-preparer-base).

Installer MariaDB depuis les dépôts maintenus, sécuriser son installation et créer un schéma dédié avec le jeu de caractères recommandé par la version de Zabbix. Stocker le secret dans un coffre et restreindre le compte au serveur local.

Avant import, vérifier que les paquets Zabbix fournissent le schéma attendu :

```bash
dpkg -L zabbix-sql-scripts | grep 'server.sql.gz'
```

Importer le schéma une seule fois après avoir confirmé que la base est vide et que la sauvegarde existe. L'import initial peut être long ; ne pas relancer à l'aveugle s'il est interrompu.

## 3. Installer serveur et interface

Fiche simple : [installer et configurer serveur et frontend](/01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-installer-configurer).

Installer le serveur MySQL, le frontend PHP, les scripts SQL et l'agent depuis le dépôt Zabbix validé. Configurer `DBName`, `DBUser` et `DBPassword` dans `/etc/zabbix/zabbix_server.conf` sans committer le secret. Régler le fuseau horaire et le serveur Web avec le frontend fourni par le paquet.

```bash
sudo apt install zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent
sudo zabbix_server -V
```

Adapter le paquet du serveur Web si le déploiement utilise Nginx au lieu d'Apache. Démarrer les services après configuration et valider leurs journaux.

## 4. Tests de bout en bout

Fiche simple : [valider l'installation](/01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-valider-installation).

- Terminer l'assistant Web via HTTPS et changer les identifiants par défaut.
- Vérifier l'état du serveur, de l'agent local, la réception de données et le déclenchement d'une alerte de test.
- Autoriser uniquement les flux nécessaires entre agents/proxies et serveur ; ne pas ouvrir le port serveur à tout Internet.
- Vérifier l'heure, la taille de la base, les partitions et les alertes de capacité.

```bash
systemctl --no-pager status zabbix-server zabbix-agent
sudo journalctl -u zabbix-server --since '-15 minutes' --no-pager
```

## 5. Sauvegarde et mises à jour

Fiche simple : [sauvegarder et mettre à jour](/01-fiches-simples/debian/12/vie-du-logiciel/zabbix/fiche-simple-vm-debian-12-zabbix-sauvegarder-mettre-a-jour).

Sauvegarder la base et `/etc/zabbix` de façon cohérente, tester une restauration isolée et documenter la rétention. Avant une mise à jour majeure, suivre la matrice officielle et sauvegarder ; en cas d'échec, restaurer ensemble base et configuration à un point cohérent.
---
title: "VM_Debian_12_Supervision_Installation-Zabbix-Serveur"
description: "Installer le serveur de supervision central Zabbix Server avec base de données MariaDB et frontend Web Apache sur Debian 12 à partir des dépôts officiels, et sécuriser l'accès à la console web et à la base de données."
published: true
date: 2026-10-29T19:55:10Z
tags: ["[debian12]", "[zabbix-server]", "[mariadb]", "[apache2]", "[supervision]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# 📄 VM_Debian_12_Supervision_Installation-Zabbix-Serveur.md

- **Environnement** : VM (Debian 12 Bookworm)
- **OS / Version** : Debian 12 - Famille Debian
- **Catégorie** : Supervision / Zabbix Server
- **Tags** : `[debian12]`, `[zabbix-server]`, `[mariadb]`, `[apache2]`, `[supervision]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer le serveur de supervision central Zabbix Server avec base de données MariaDB et frontend Web Apache sur Debian 12 à partir des dépôts officiels, et sécuriser l'accès à la console web et à la base de données.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet de dépôt officiel Zabbix :
   Télécharger le paquet de dépôt correspondant à Debian 12 depuis la source officielle Zabbix, vérifier son intégrité, puis installer et actualiser les index APT.
   👉 Explication : Active les canaux de paquets officiels maintenus par l'éditeur Zabbix.
2. Installation des composants serveur, web et base de données :
   `apt-get install -y zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf mariadb-server`
   👉 Explication : Installe le moteur central Zabbix, le serveur MariaDB et les fichiers d'interface Apache/PHP.
3. Initialisation du schéma de la base de données :
   `zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mariadb -u zabbix -p zabbix`
   👉 Explication : Injecte les tables et la structure initiale de la base de données de supervision.

---

## ⚡ 2. Production — Façon Simplifiée
1. Modifier `/etc/zabbix/zabbix_server.conf` après sauvegarde et définir `DBPassword` avec le secret réellement créé pour Zabbix dans MariaDB. Ne pas inclure ce secret dans une commande, un dépôt ou cette fiche.
   👉 Explication : Le service doit utiliser un compte MariaDB limité à sa base.
2. Démarrage et activation des services au boot :
   `systemctl restart zabbix-server zabbix-agent apache2 mariadb && systemctl enable zabbix-server zabbix-agent apache2 mariadb`
   👉 Explication : Lance l'ensemble des démons de la pile de supervision et garantit leur persistance.
3. Validation du statut du serveur :
   `systemctl status zabbix-server`
   👉 Explication : Vérifie le bon fonctionnement du processus démon.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Activer HTTPS uniquement après configuration d'un certificat valide dans le virtual host Apache, puis tester le site via HTTPS. `a2enmod ssl headers` seul n'installe pas de certificat et ne configure pas TLS.
2. Surcharge des directives de sécurité PHP dans la configuration Zabbix :
   `echo 'php_flag session.cookie_secure on' >> /etc/zabbix/apache.conf && systemctl reload apache2`
   👉 Explication : Force l'isolation des cookies de session HTTP pour parer le vol de jetons.
3. Autoriser TCP/10051 uniquement aux proxies/agents actifs prévus dans le pare-feu persistant géré par l'hôte. Valider et appliquer la règle par ce gestionnaire ; ne pas utiliser une règle nftables runtime comme configuration finale.